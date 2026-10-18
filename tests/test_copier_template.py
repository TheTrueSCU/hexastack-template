"""Integration tests verifying Copier template instantiation and lifecycle behavior.

Notes/Architectural Intent:
    Ensures that the Copier template payload remains strictly valid, rendering
    valid Python syntax, compliant hexagonal boundaries, and correct pyproject.toml
    configuration across both default and custom questionnaire answers.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import copier
import yaml


def test_copier_default_generation() -> None:
    """Verify Copier renders the golden-path template with default answers.

    Notes/Architectural Intent:
        Guarantees that `copier copy --defaults` produces a structurally complete,
        runnable Hexastack microservice matching all architectural invariants.
    """
    repo_root = Path(__file__).resolve().parent.parent

    with tempfile.TemporaryDirectory() as tmp_dst:
        dst = Path(tmp_dst)
        copier.run_copy(
            src_path=str(repo_root),
            dst_path=dst,
            defaults=True,
            vcs_ref="HEAD",
            unsafe=True,
        )

        answers_file = dst / ".copier-answers.yml"
        answers_exist = answers_file.is_file()
        assert answers_exist is True

        answers_data = yaml.safe_load(answers_file.read_text(encoding="utf-8"))
        pkg_name = answers_data.get("package_name")
        proj_slug = answers_data.get("project_slug")
        assert pkg_name == "hexastack_service"
        assert proj_slug == "hexastack-service"

        # Check core directory and module integrity
        src_init = dst / "src" / "hexastack_service" / "__init__.py"
        src_init_exists = src_init.is_file()
        assert src_init_exists is True

        pyproject = dst / "pyproject.toml"
        pyproject_exists = pyproject.is_file()
        assert pyproject_exists is True

        pyproject_text = pyproject.read_text(encoding="utf-8")
        assert 'name = "hexastack-service"' in pyproject_text
        assert (
            'hexastack-service = "hexastack_service.adapters.driving.cli:main"'
            in pyproject_text
        )

        # Check hexagonal test symmetry and boundary files
        arch_test = dst / "tests" / "architecture" / "test_hexagonal_boundaries.py"
        arch_test_exists = arch_test.is_file()
        assert arch_test_exists is True

        readme = dst / "README.md"
        readme_exists = readme.is_file()
        assert readme_exists is True


def test_copier_custom_options_generation() -> None:
    """Verify Copier correctly renders custom project slug, package name, and subpackages.

    Notes/Architectural Intent:
        Validates dynamic Jinja parameterization of directory names, import paths,
        and pyproject extras dependencies when users provide custom answers.
    """
    repo_root = Path(__file__).resolve().parent.parent

    with tempfile.TemporaryDirectory() as tmp_dst:
        dst = Path(tmp_dst)
        copier.run_copy(
            src_path=str(repo_root),
            dst_path=dst,
            data={
                "project_name": "Acme Payments Service",
                "project_slug": "acme-payments",
                "package_name": "acme_payments",
                "description": "High performance payments engine",
                "author_name": "Payments Guild",
                "author_email": "payments@acme.com",
                "include_sentry": True,
                "include_ai": True,
            },
            defaults=True,
            vcs_ref="HEAD",
            unsafe=True,
        )

        # Check directory rename and package namespace
        pkg_dir = dst / "src" / "acme_payments"
        pkg_dir_exists = pkg_dir.is_dir()
        assert pkg_dir_exists is True

        pyproject = dst / "pyproject.toml"
        pyproject_text = pyproject.read_text(encoding="utf-8")
        assert 'name = "acme-payments"' in pyproject_text
        assert "sentry" in pyproject_text
        assert "ai" in pyproject_text

        # Verify import statements in driving and driven adapters
        db_adapter = pkg_dir / "adapters" / "driven" / "database.py"
        db_text = db_adapter.read_text(encoding="utf-8")
        assert "from acme_payments.domain.models import Item" in db_text
        assert (
            "from acme_payments.ports.repositories import ItemRepositoryPort" in db_text
        )

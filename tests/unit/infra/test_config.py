"""Unit tests for service configuration."""

from hexastack_template.infra.config import AppConfig


def test_app_config_defaults():
    """Verify default AppConfig settings."""
    cfg = AppConfig()
    res_env = cfg.environment
    assert res_env == "development"

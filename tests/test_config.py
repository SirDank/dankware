"""
Tests for dankware.config module.
"""

import pytest
from dankware.config import configure, get_config, reset_config, DankwareConfig


class TestConfig:
    """Tests for configuration management."""

    def setup_method(self):
        """Reset config before each test."""
        reset_config()

    def test_default_config(self):
        """Test default configuration values."""
        config = get_config()
        assert config.enable_colors is True
        assert config.default_threads == 10
        assert config.request_timeout == 10
        assert config.github_token is None
        assert config.progress_bar is True

    def test_configure_single_option(self):
        """Test configuring a single option."""
        configure(default_threads=20)
        config = get_config()
        assert config.default_threads == 20

    def test_configure_multiple_options(self):
        """Test configuring multiple options."""
        configure(enable_colors=False, default_threads=50, github_token="test_token")
        config = get_config()
        assert config.enable_colors is False
        assert config.default_threads == 50
        assert config.github_token == "test_token"

    def test_configure_invalid_option(self):
        """Test that invalid option raises ValueError."""
        with pytest.raises(ValueError, match="Unknown configuration option"):
            configure(invalid_option=True)

    def test_reset_config(self):
        """Test that reset_config restores defaults."""
        configure(default_threads=100)
        reset_config()
        config = get_config()
        assert config.default_threads == 10

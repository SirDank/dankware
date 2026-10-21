"""
Tests for dankware.traceback module.
"""

import sys

import pytest

from dankware import err


class TestTraceback:
    """Tests for err traceback formatter."""

    def test_err_default_mode(self):
        """Test default traceback mode."""
        try:
            1 / 0
        except ZeroDivisionError:
            tb = err(sys.exc_info(), mode="default")

        assert "ZeroDivisionError" in tb
        assert "Error Stack Trace" in tb

    def test_err_mini_mode(self):
        """Test mini traceback mode."""
        try:
            1 / 0
        except ZeroDivisionError:
            tb = err(sys.exc_info(), mode="mini")

        assert "ZeroDivisionError" in tb
        assert "division by zero" in tb

    def test_err_invalid_mode(self):
        """Test invalid traceback mode raises ValueError."""
        try:
            1 / 0
        except ZeroDivisionError:
            with pytest.raises(ValueError, match="Invalid Mode"):
                err(sys.exc_info(), mode="unknown")

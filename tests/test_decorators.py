"""
Tests for dankware.decorators module.
"""

import pytest

from dankware import retry


class TestRetry:
    """Tests for the retry decorator."""

    def test_retry_success_first_try(self):
        """Test that successful function doesn't retry."""
        call_count = {"value": 0}

        @retry(max_attempts=3)
        def always_succeeds():
            call_count["value"] += 1
            return "success"

        result = always_succeeds()
        assert result == "success"
        assert call_count["value"] == 1

    def test_retry_eventual_success(self):
        """Test retry until success."""
        call_count = {"value": 0}

        @retry(max_attempts=3, delay=0.01)
        def fails_twice():
            call_count["value"] += 1
            if call_count["value"] < 3:
                raise ValueError("Not yet")
            return "success"

        result = fails_twice()
        assert result == "success"
        assert call_count["value"] == 3

    def test_retry_max_attempts_exceeded(self):
        """Test that exception is raised after max attempts."""
        call_count = {"value": 0}

        @retry(max_attempts=3, delay=0.01)
        def always_fails():
            call_count["value"] += 1
            raise ValueError("Always fails")

        with pytest.raises(ValueError, match="Always fails"):
            always_fails()

        assert call_count["value"] == 3

    def test_retry_specific_exceptions(self):
        """Test retry only catches specified exceptions."""

        @retry(max_attempts=3, delay=0.01, exceptions=(ValueError,))
        def raises_type_error():
            raise TypeError("Wrong type")

        with pytest.raises(TypeError):
            raises_type_error()

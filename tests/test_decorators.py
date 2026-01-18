"""
Tests for dankware.decorators module.
"""

import pytest
import time
from dankware.decorators import retry, timed, deprecated


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


class TestTimed:
    """Tests for the timed decorator."""

    def test_timed_returns_result(self, capsys):
        """Test that timed returns function result."""

        @timed
        def add(a, b):
            return a + b

        result = add(2, 3)
        assert result == 5

        captured = capsys.readouterr()
        assert "add completed in" in captured.out

    def test_timed_measures_time(self, capsys):
        """Test that timed measures execution time."""

        @timed
        def slow_function():
            time.sleep(0.1)
            return "done"

        result = slow_function()
        assert result == "done"

        captured = capsys.readouterr()
        # Should report ~0.1 seconds
        assert "slow_function completed in" in captured.out


class TestDeprecated:
    """Tests for the deprecated decorator."""

    def test_deprecated_warning(self):
        """Test that deprecated emits warning."""

        @deprecated("Use new_func instead")
        def old_func():
            return "old"

        with pytest.warns(DeprecationWarning, match="old_func is deprecated"):
            result = old_func()

        assert result == "old"

    def test_deprecated_without_message(self):
        """Test deprecated without custom message."""

        @deprecated()
        def old_func2():
            return "old2"

        with pytest.warns(DeprecationWarning, match="old_func2 is deprecated"):
            result = old_func2()

        assert result == "old2"

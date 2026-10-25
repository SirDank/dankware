"""
Tests for dankware.datetime module.
"""

from datetime import datetime, timedelta

import pytest

from dankware import get_duration


class TestGetDuration:
    """Tests for the get_duration function."""

    def test_seconds(self):
        """Test seconds interval."""
        then = datetime.now() - timedelta(seconds=30)
        result = get_duration(then, interval="second")
        assert result == 30

    def test_minutes(self):
        """Test minutes interval."""
        then = datetime.now() - timedelta(minutes=5)
        result = get_duration(then, interval="minute")
        assert result == 5

    def test_hours(self):
        """Test hours interval."""
        then = datetime.now() - timedelta(hours=3)
        result = get_duration(then, interval="hour")
        assert result == 3

    def test_days(self):
        """Test days interval."""
        then = datetime.now() - timedelta(days=7)
        result = get_duration(then, interval="day")
        assert result == 7

    def test_weeks(self):
        """Test weeks interval."""
        then = datetime.now() - timedelta(weeks=2)
        result = get_duration(then, interval="week")
        assert result == 2

    def test_dynamic(self):
        """Test dynamic interval returns string."""
        then = datetime.now() - timedelta(minutes=5)
        result = get_duration(then, interval="dynamic")
        assert isinstance(result, str)
        assert "minute" in result

    def test_dynamic_mini(self):
        """Test dynamic-mini interval."""
        then = datetime.now() - timedelta(hours=2)
        result = get_duration(then, interval="dynamic-mini")
        assert isinstance(result, str)
        assert "h" in result

    def test_default(self):
        """Test default interval returns full breakdown."""
        then = datetime.now() - timedelta(days=1, hours=2, minutes=30)
        result = get_duration(then, interval="default")
        assert isinstance(result, str)
        assert "day" in result
        assert "hour" in result
        assert "minute" in result

    def test_default_mini(self):
        """Test default-mini interval returns abbreviated."""
        then = datetime.now() - timedelta(days=1, hours=2)
        result = get_duration(then, interval="default-mini")
        assert isinstance(result, str)
        assert "d" in result
        assert "h" in result

    def test_zero_duration_default(self):
        """Test zero duration for default mode."""
        now = datetime.now()
        assert get_duration(now, now=now, interval="default") == "0 seconds"

    def test_zero_duration_default_mini(self):
        """Test zero duration for default-mini mode."""
        now = datetime.now()
        assert get_duration(now, now=now, interval="default-mini") == "0s"

    def test_invalid_interval(self):
        """Test that invalid interval raises ValueError."""
        with pytest.raises(ValueError, match="Invalid Interval"):
            get_duration(datetime.now(), interval="invalid")

    def test_custom_now(self):
        """Test with custom 'now' parameter."""
        then = datetime(2023, 1, 1)
        now = datetime(2023, 1, 8)
        result = get_duration(then, now=now, interval="day")
        assert result == 7

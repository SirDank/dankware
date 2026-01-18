"""
Tests for dankware.text module.
"""

import pytest
from dankware import clr, align, fade, random_ip


class TestClr:
    """Tests for the clr function."""

    def test_clr_preset_1(self, sample_text):
        """Test default preset coloring."""
        result = clr(sample_text, 1)
        assert isinstance(result, str)
        assert len(result) > len(sample_text)  # Should have ANSI codes

    def test_clr_preset_2(self, sample_text):
        """Test error message preset."""
        result = clr(sample_text, 2)
        assert isinstance(result, str)

    def test_clr_preset_3(self, sample_text):
        """Test random coloring preset."""
        result = clr(sample_text, 3)
        assert isinstance(result, str)

    def test_clr_preset_4(self, sample_banner):
        """Test banner coloring preset."""
        result = clr(sample_banner, 4)
        assert isinstance(result, str)

    def test_clr_invalid_preset(self, sample_text):
        """Test that invalid preset raises ValueError."""
        with pytest.raises(ValueError, match="Invalid Preset"):
            clr(sample_text, 99)


class TestAlign:
    """Tests for the align function."""

    def test_align_single_line(self):
        """Test aligning a single line."""
        text = "Hello World"
        result = align(text)
        assert isinstance(result, str)
        # Result should have leading spaces for centering
        assert len(result) >= len(text)

    def test_align_multiline(self, sample_banner):
        """Test aligning multi-line text."""
        result = align(sample_banner)
        assert isinstance(result, str)
        assert "\n" in result


class TestFade:
    """Tests for the fade function."""

    def test_fade_pink2red(self, sample_banner):
        """Test pink to red gradient."""
        result = fade(sample_banner, "pink2red")
        assert isinstance(result, str)
        assert "\033[38;2;" in result  # Should have RGB escape codes

    def test_fade_random(self, sample_banner):
        """Test random gradient."""
        result = fade(sample_banner, "random")
        assert isinstance(result, str)

    def test_fade_vertical(self, sample_banner):
        """Test vertical gradient."""
        result = fade(sample_banner, "blue2cyan-v")
        assert isinstance(result, str)

    def test_fade_invalid_color(self, sample_banner):
        """Test that invalid color raises ValueError."""
        with pytest.raises(ValueError, match="Invalid Colour"):
            fade(sample_banner, "invalid_color")

    def test_fade_available_colors(self, sample_banner):
        """Test all available fade colors."""
        colors = [
            "random",
            "black2white",
            "black2white-v",
            "yellow2red",
            "yellow2red-v",
            "green2yellow",
            "green2yellow-v",
            "green2cyan",
            "green2cyan-v",
            "blue2cyan",
            "blue2cyan-v",
            "blue2pink",
            "blue2pink-v",
            "pink2red",
            "pink2red-v",
        ]
        for color in colors:
            result = fade(sample_banner, color)
            assert isinstance(result, str)


class TestRandomIp:
    """Tests for the random_ip function."""

    def test_random_ip_format(self):
        """Test that random_ip returns valid IP format."""
        ip = random_ip()
        parts = ip.split(".")
        assert len(parts) == 4
        for part in parts:
            num = int(part)
            assert 0 <= num <= 255

    def test_random_ip_uniqueness(self):
        """Test that random_ip generates different IPs."""
        ips = {random_ip() for _ in range(100)}
        # Should generate at least some unique IPs
        assert len(ips) > 50

    def test_random_ip_not_private(self):
        """Test that random_ip doesn't generate private IPs."""
        for _ in range(100):
            ip = random_ip()
            parts = ip.split(".")
            first = int(parts[0])
            second = int(parts[1])

            # Check not 10.x.x.x
            assert first != 10

            # Check not 127.x.x.x
            assert first != 127

            # Check not 172.16-31.x.x
            if first == 172:
                assert not (16 <= second <= 31)

            # Check not 192.168.x.x
            if first == 192:
                assert second != 168

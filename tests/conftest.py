"""
Pytest configuration for dankware tests.
"""

import os
import sys

import pytest

# Add the parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def sample_banner():
    """Sample banner text for testing."""
    banner = (
        "\n"
        "     888                   888\n"
        "     888                   888           s i r . d a n k ' s\n"
        "     888                   888\n"
        " .d88888  8888b.  88888b.  888  888 888  888  888  8888b.  888d888 .d88b.\n"
        'd88" 888     "88b 888 "88b 888 .88P 888  888  888     "88b 888P"  d8P  Y8b\n'
        "888  888 .d888888 888  888 888888K  888  888  888 .d888888 888    88888888\n"
        'Y88b 888 888  888 888  888 888 "88b Y88b 888 d88P 888  888 888    Y8b.\n'
        ' "Y88888 "Y888888 888  888 888  888  "Y8888888P"  "Y888888 888     "Y8888\n'
    )
    return banner


@pytest.fixture
def sample_text():
    """Sample text for color testing."""
    return "  > Hello World! This is a test: True | Status: SUCCESS"

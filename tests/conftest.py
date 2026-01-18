"""
Pytest configuration for dankware tests.
"""

import pytest
import sys
import os

# Add the parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def sample_banner():
    """Sample banner text for testing."""
    return """
     888                   888                                             
     888                   888           s i r . d a n k ' s               
     888                   888                                             
 .d88888  8888b.  88888b.  888  888 888  888  888  8888b.  888d888 .d88b.  
d88" 888     "88b 888 "88b 888 .88P 888  888  888     "88b 888P"  d8P  Y8b 
888  888 .d888888 888  888 888888K  888  888  888 .d888888 888    88888888 
Y88b 888 888  888 888  888 888 "88b Y88b 888 d88P 888  888 888    Y8b.     
 "Y88888 "Y888888 888  888 888  888  "Y8888888P"  "Y888888 888     "Y8888  
"""


@pytest.fixture
def sample_text():
    """Sample text for color testing."""
    return "  > Hello World! This is a test: True | Status: SUCCESS"

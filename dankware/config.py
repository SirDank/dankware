# https://github.com/SirDank/dankware

"""
Configuration management for dankware.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DankwareConfig:
    """
    Global configuration for dankware.

    Attributes:
        enable_colors: Whether to enable colored output.
        default_threads: Default number of threads for multithread().
        request_timeout: Default timeout for HTTP requests in seconds.
        github_token: Optional GitHub token for higher API rate limits.
        progress_bar: Whether to show progress bars by default.
    """

    enable_colors: bool = True
    default_threads: int = 10
    request_timeout: int = 10
    github_token: Optional[str] = None
    progress_bar: bool = True


# Global configuration instance
_config = DankwareConfig()


def get_config() -> DankwareConfig:
    """
    Get the current configuration.

    Returns:
        Current DankwareConfig instance.
    """
    return _config


def configure(**kwargs) -> None:
    """
    Configure dankware settings.

    Args:
        **kwargs: Configuration options to set.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.config import configure

    configure(
        enable_colors=True,
        default_threads=20,
        github_token="ghp_xxx..."
    )
    ```
    """
    for key, value in kwargs.items():
        if hasattr(_config, key):
            setattr(_config, key, value)
        else:
            raise ValueError(f"Unknown configuration option: {key}")


def reset_config() -> None:
    """
    Reset configuration to defaults.
    """
    global _config
    _config = DankwareConfig()

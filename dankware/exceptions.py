# https://github.com/SirDank/dankware

"""
Custom exceptions for dankware.
"""

__all__ = [
    "DankwareError",
    "UnsupportedOSError",
    "RateLimitError",
    "DownloadError",
]


class DankwareError(Exception):
    """Base exception for dankware."""

    pass


class UnsupportedOSError(DankwareError):
    """Raised when the operating system is not supported."""

    pass


class RateLimitError(DankwareError):
    """Raised when GitHub API rate limit is exceeded."""

    pass


class DownloadError(DankwareError):
    """Raised when a download operation fails."""

    pass

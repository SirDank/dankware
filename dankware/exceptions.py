# https://github.com/SirDank/dankware

"""
Custom exceptions for dankware.
"""


class DankwareError(Exception):
    """Base exception for dankware."""

    pass


class UnsupportedOSError(DankwareError):
    """Raised when the operating system is not supported."""

    pass


class RateLimitError(DankwareError):
    """Raised when GitHub API rate limit is exceeded."""

    pass


class ConfigurationError(DankwareError):
    """Raised when there's a configuration issue."""

    pass


class DownloadError(DankwareError):
    """Raised when a download operation fails."""

    pass


class RegistryError(DankwareError):
    """Raised when a Windows registry operation fails."""

    pass

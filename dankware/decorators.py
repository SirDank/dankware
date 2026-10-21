# https://github.com/SirDank/dankware

"""
Utility decorators for dankware.
"""

import time
from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar("T")

__all__ = ["retry"]


def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator to retry a function on failure with exponential backoff.

    Args:
        max_attempts: Maximum number of retry attempts.
        delay: Initial delay between retries in seconds.
        backoff: Multiplier for delay after each retry.
        exceptions: Tuple of exception types to catch and retry on.

    Returns:
        Decorated function that will retry on failure.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware import retry

    @retry(max_attempts=3, delay=1.0)
    def unstable_operation():
        # Retries up to 3 times on failure
        ...
    ```
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            attempts = 0
            current_delay = delay
            last_exception: Exception | None = None

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    last_exception = e
                    if attempts == max_attempts:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff

            if last_exception is not None:
                raise last_exception
            raise RuntimeError("Retry loop exited without result or exception")

        return wrapper

    return decorator

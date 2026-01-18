# https://github.com/SirDank/dankware

"""
Utility decorators for dankware.
"""

import time
from functools import wraps
from typing import Callable, TypeVar, Any

T = TypeVar("T")


def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator to retry a function on failure.

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
    from dankware.decorators import retry

    @retry(max_attempts=3, delay=1.0)
    def unstable_operation():
        # This will retry up to 3 times on failure
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

            # This should never be reached, but satisfies type checker
            raise last_exception  # type: ignore

        return wrapper

    return decorator


def timed(func: Callable[..., T]) -> Callable[..., T]:
    """
    Decorator to measure and print execution time.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.decorators import timed

    @timed
    def slow_function():
        time.sleep(2)
        return "done"
    ```
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  > {func.__name__} completed in {elapsed:.3f}s")
        return result

    return wrapper


def deprecated(message: str = "") -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator to mark a function as deprecated.

    Args:
        message: Optional message to display.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.decorators import deprecated

    @deprecated("Use new_function() instead")
    def old_function():
        ...
    ```
    """
    import warnings

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            warning_msg = f"{func.__name__} is deprecated."
            if message:
                warning_msg += f" {message}"
            warnings.warn(warning_msg, DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return wrapper

    return decorator

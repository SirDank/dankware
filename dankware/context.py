# https://github.com/SirDank/dankware

"""
Context managers for dankware.
"""

import os
import time
from contextlib import contextmanager
from typing import Generator, Optional


@contextmanager
def timer(description: str = "Operation") -> Generator[None, None, None]:
    """
    Context manager to time operations.

    Args:
        description: Description of the operation being timed.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.context import timer

    with timer("Data processing"):
        process_data()
    # Prints: "  > Data processing completed in 1.234s"
    ```
    """
    from .text import clr

    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(clr(f"  > {description} completed in {elapsed:.3f}s"))


@contextmanager
def hidden_window() -> Generator[None, None, None]:
    """
    Context manager that hides the console window during operation.
    Windows only - no-op on other platforms.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.context import hidden_window

    with hidden_window():
        do_background_work()
    ```
    """
    if os.name == "nt":
        from .ctypes import hide_window, show_window

        hide_window()
        try:
            yield
        finally:
            show_window()
    else:
        yield


@contextmanager
def temporary_file(suffix: str = "", prefix: str = "dankware_", delete: bool = True) -> Generator[str, None, None]:
    """
    Context manager that creates a temporary file.

    Args:
        suffix: File suffix/extension.
        prefix: File name prefix.
        delete: Whether to delete the file after use.

    Yields:
        Path to the temporary file.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.context import temporary_file

    with temporary_file(suffix=".txt") as filepath:
        with open(filepath, "w") as f:
            f.write("temp data")
        # file is deleted after the block
    ```
    """
    import tempfile

    fd, path = tempfile.mkstemp(suffix=suffix, prefix=prefix)
    os.close(fd)
    try:
        yield path
    finally:
        if delete and os.path.exists(path):
            os.unlink(path)


@contextmanager
def temporary_directory(prefix: str = "dankware_", delete: bool = True) -> Generator[str, None, None]:
    """
    Context manager that creates a temporary directory.

    Args:
        prefix: Directory name prefix.
        delete: Whether to delete the directory after use.

    Yields:
        Path to the temporary directory.
    """
    import tempfile
    import shutil

    path = tempfile.mkdtemp(prefix=prefix)
    try:
        yield path
    finally:
        if delete and os.path.exists(path):
            shutil.rmtree(path)


@contextmanager
def working_directory(path: str) -> Generator[str, None, None]:
    """
    Context manager to temporarily change working directory.

    Args:
        path: Directory to change to.

    Yields:
        The new working directory path.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.context import working_directory

    with working_directory("/some/path"):
        # do work in /some/path
        pass
    # back to original directory
    ```
    """
    original = os.getcwd()
    try:
        os.chdir(path)
        yield path
    finally:
        os.chdir(original)


@contextmanager
def suppress_output() -> Generator[None, None, None]:
    """
    Context manager to suppress stdout and stderr.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.context import suppress_output

    with suppress_output():
        noisy_function()  # output is suppressed
    ```
    """
    import sys
    from io import StringIO

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    try:
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        yield
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

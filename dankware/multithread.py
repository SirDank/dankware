# https://github.com/SirDank/dankware

"""
Multithreading utilities with rich progress visualization.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from shutil import get_terminal_size
from typing import Any, Callable

from rich.live import Live
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.table import Table

__all__ = ["multithread"]


def multithread(
    function: Callable[..., Any],
    threads: int = 1,
    *args: Any,
    progress_bar: bool = True,
) -> None:
    """
    Run the given function across multiple threads with optional arguments.

    Args:
        function: The function to execute.
        threads: Number of worker threads.
        *args: Inputs for the function (lists/tuples or broadcast scalars).
        progress_bar: Whether to display a rich terminal progress bar.

    Raises:
        ValueError: If threads < 1.
        Exception: If any worker thread raises an unhandled exception.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware import multithread

    def worker(num):
        print(num * 2)

    multithread(worker, 4, [1, 2, 3, 4], progress_bar=False)
    ```
    """
    if threads < 1:
        raise ValueError("The number of threads must be a positive integer!")

    with ThreadPoolExecutor(max_workers=threads, thread_name_prefix="dankware") as executor:
        if not args:
            futures = [executor.submit(function) for _ in range(threads)]
        else:
            input_lists = []
            for arg in args:
                if isinstance(arg, (list, tuple)):
                    input_lists.append(arg)
                else:
                    input_lists.append([arg] * threads)

            futures = [executor.submit(function, *task_args) for task_args in zip(*input_lists)]

        if progress_bar:
            width = get_terminal_size().columns
            job_progress = Progress(
                "{task.description}",
                SpinnerColumn(),
                BarColumn(bar_width=width),
                TextColumn("[progress.percentage][bright_green]{task.percentage:>3.0f}%"),
                "[bright_cyan]ETA",
                TimeRemainingColumn(),
                TimeElapsedColumn(),
            )
            overall_task = job_progress.add_task("[bright_green]Progress", total=len(futures))
            progress_table = Table.grid()
            progress_table.add_row(
                Panel.fit(
                    job_progress,
                    title="[bright_white]Jobs",
                    border_style="red",
                    padding=(1, 2),
                )
            )

            with Live(progress_table, refresh_per_second=10):
                for future in as_completed(futures):
                    future.result()
                    job_progress.advance(overall_task)
        else:
            for future in as_completed(futures):
                future.result()

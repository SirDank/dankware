# https://github.com/SirDank/dankware

"""
Async utilities for dankware.
"""

import asyncio
from typing import Callable, Any, Optional, Coroutine
from concurrent.futures import ThreadPoolExecutor

from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeRemainingColumn,
    TimeElapsedColumn,
)


async def async_run(function: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Run a synchronous function asynchronously in a thread pool.

    Args:
        function: The synchronous function to run.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.

    Returns:
        The result of the function.

    __________________________________________

    [ EXAMPLE ]

    ```python
    import asyncio
    from dankware.async_utils import async_run
    import time

    def slow_function(x):
        time.sleep(2)
        return x * 2

    async def main():
        result = await async_run(slow_function, 5)
        print(result)  # 10

    asyncio.run(main())
    ```
    """
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, lambda: function(*args, **kwargs))


async def async_multithread(
    function: Callable[..., Any],
    concurrency: int = 10,
    *args: Any,
    progress_bar: bool = True,
) -> list[Any]:
    """
    Async version of multithread using asyncio with semaphore-controlled concurrency.

    Args:
        function: The function to run (can be sync or async).
        concurrency: Maximum number of concurrent tasks.
        *args: Inputs for the function (lists or single values).
        progress_bar: Whether to display a progress bar.

    Returns:
        List of results from all tasks.

    __________________________________________

    [ EXAMPLE ]

    ```python
    import asyncio
    from dankware.async_utils import async_multithread

    async def fetch(url):
        # async operation
        await asyncio.sleep(1)
        return f"fetched {url}"

    async def main():
        urls = ["url1", "url2", "url3"]
        results = await async_multithread(fetch, 5, urls)
        print(results)

    asyncio.run(main())
    ```
    """
    semaphore = asyncio.Semaphore(concurrency)
    results: list[Any] = []
    completed = 0

    # Prepare task inputs
    if not args:
        task_inputs = [()] * concurrency
    else:
        input_lists = []
        for arg in args:
            if isinstance(arg, (list, tuple)):
                input_lists.append(arg)
            else:
                # Replicate single value
                max_len = max(len(a) for a in args if isinstance(a, (list, tuple))) if any(isinstance(a, (list, tuple)) for a in args) else concurrency
                input_lists.append([arg] * max_len)

        task_inputs = list(zip(*input_lists))

    total = len(task_inputs)

    async def bounded_task(task_args: tuple) -> Any:
        nonlocal completed
        async with semaphore:
            if asyncio.iscoroutinefunction(function):
                result = await function(*task_args)
            else:
                # Run sync function in thread pool
                result = await async_run(function, *task_args)
            completed += 1
            return result

    if progress_bar:
        job_progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage][bright_green]{task.percentage:>3.0f}%"),
            "[bright_cyan]ETA",
            TimeRemainingColumn(),
            TimeElapsedColumn(),
        )
        overall_task = job_progress.add_task("[bright_green]Progress", total=total)
        progress_table = Table.grid()
        progress_table.add_row(
            Panel.fit(
                job_progress,
                title="[bright_white]Async Jobs",
                border_style="red",
                padding=(1, 2),
            )
        )

        async def run_with_progress():
            tasks = [bounded_task(inp) for inp in task_inputs]
            with Live(progress_table, refresh_per_second=10):
                for coro in asyncio.as_completed(tasks):
                    result = await coro
                    results.append(result)
                    job_progress.update(overall_task, completed=len(results))
            return results

        return await run_with_progress()
    else:
        tasks = [bounded_task(inp) for inp in task_inputs]
        return await asyncio.gather(*tasks)


async def gather_with_concurrency(n: int, *coros: Coroutine[Any, Any, Any]) -> list[Any]:
    """
    Run coroutines with limited concurrency.

    Args:
        n: Maximum number of concurrent coroutines.
        *coros: Coroutines to run.

    Returns:
        List of results.

    __________________________________________

    [ EXAMPLE ]

    ```python
    import asyncio
    from dankware.async_utils import gather_with_concurrency

    async def task(i):
        await asyncio.sleep(1)
        return i * 2

    async def main():
        coros = [task(i) for i in range(10)]
        results = await gather_with_concurrency(3, *coros)
        print(results)

    asyncio.run(main())
    ```
    """
    semaphore = asyncio.Semaphore(n)

    async def sem_coro(coro: Coroutine[Any, Any, Any]) -> Any:
        async with semaphore:
            return await coro

    return await asyncio.gather(*(sem_coro(c) for c in coros))

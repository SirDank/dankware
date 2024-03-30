import sys
import time
from .text import clr
from .traceback import err
from shutil import get_terminal_size
from concurrent.futures import ThreadPoolExecutor, as_completed

from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn, TimeElapsedColumn

def multithread(function: callable, threads: int = 1, *args, progress_bar: bool = True) -> None: # pylint: disable=keyword-arg-before-vararg # type: ignore

    """
    Run the given function in multiple threads with the specified inputs.
    
    ________________________________________________________________________

    - function: The function to run in multiple threads.
    - threads: The number of threads to use.
    - *args: Input(s) for the function. Can be a tuple / list / single value.
    - progress_bar: Whether to display a progress bar.
    """

    try:

        if threads < 1:
            raise ValueError("The number of threads must be a positive integer!")

        executor = ThreadPoolExecutor(max_workers=threads)

        if not args:
            futures = tuple(executor.submit(function) for _ in range(threads))
        else:

            input_lists = []

            for arg in args:
                if isinstance(arg, (list, tuple)):
                    input_lists.append(arg)
                else:
                    input_lists.append([arg] * threads)
            del args

            futures = tuple(executor.submit(function, *task_args) for task_args in zip(*input_lists))

            del input_lists

        if progress_bar:
            width = get_terminal_size().columns
            job_progress = Progress("{task.description}", SpinnerColumn(), BarColumn(bar_width=width), TextColumn("[progress.percentage][bright_green]{task.percentage:>3.0f}%"), "[bright_cyan]ETA", TimeRemainingColumn(), TimeElapsedColumn())
            overall_task = job_progress.add_task("[bright_green]Progress", total=int(len(futures)))
            progress_table = Table.grid()
            progress_table.add_row(Panel.fit(job_progress, title="[bright_white]Jobs", border_style="red", padding=(1, 2)))

            with Live(progress_table, refresh_per_second=10):
                while not job_progress.finished:
                    time.sleep(0.1)
                    for future in as_completed(futures):
                        if future.done():
                            try: future.result()
                            except: pass
                            job_progress.advance(overall_task)

        else:
            for future in as_completed(futures):
                if future.done():
                    try: future.result()
                    except: pass

    except:
        try: executor.shutdown()
        except: pass
        sys.exit(clr(err(sys.exc_info()),2))

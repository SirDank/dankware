# https://github.com/SirDank/dankware

"""
Error traceback formatting utilities.
"""

from os.path import commonprefix
from traceback import extract_tb
from typing import Any

__all__ = ["err"]


def err(exc_info: tuple[Any, Any, Any], mode: str = "default") -> str:
    """
    Format exception info into a concise traceback string.

    Args:
        exc_info: Tuple of (type, value, traceback), e.g. from sys.exc_info().
        mode: Formatting mode ('default' or 'mini').

    Returns:
        Formatted traceback string.

    Raises:
        ValueError: If mode is not 'default' or 'mini'.

    __________________________________________

    [ EXAMPLE ]

    ```python
    import sys
    from dankware import err, clr

    try:
        1 / 0
    except Exception:
        print(clr(err(sys.exc_info(), mode="mini"), 2))
    ```
    """
    ex_type, ex_value, ex_traceback = exc_info
    trace_back = extract_tb(ex_traceback)
    mode_clean = mode.lower()
    stack_trace: list[str] = []

    if mode_clean == "default":
        for trace in trace_back:
            filename = str(__name__) if trace[0] == "<string>" else trace[0]
            func_name = trace[2] if trace[2] != "<module>" else "top-level"
            line_str = f" | Line: {trace[3]}" if trace[3] else ""
            stack_trace.append(f"    - File: {filename} | Function: {func_name}{line_str}")

        report = f"  - Error Type: {ex_type.__name__}"
        if ex_value:
            report += f"\n  - Error Message: \n    - {ex_value}"
        report += "\n  - Error Stack Trace: \n" + "\n".join(stack_trace)

    elif mode_clean == "mini":
        filenames = [trace[0] for trace in trace_back]
        common_prefix: str | None = None
        if filenames:
            common_prefix = commonprefix(filenames)
            last_slash_idx = max(common_prefix.rfind("/"), common_prefix.rfind("\\"))
            if last_slash_idx != -1:
                common_prefix = common_prefix[:last_slash_idx]

        for trace in trace_back:
            filename = str(__name__) if trace[0] == "<string>" else trace[0]
            if common_prefix and filename.startswith(common_prefix):
                filename = "..." + filename[len(common_prefix) :]
            func_name = trace[2] if trace[2] != "<module>" else "top-level"
            line_str = f" | {trace[3]}" if trace[3] else ""
            stack_trace.append(f"    - {filename} | {func_name}{line_str}")

        report = f"  - {ex_type.__name__}"
        if ex_value:
            report += f" | {ex_value}"
        report += "\n" + "\n".join(stack_trace)

    else:
        raise ValueError(f"Invalid Mode: {mode} | Valid Modes: default, mini")

    return report

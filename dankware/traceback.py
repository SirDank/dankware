from traceback import extract_tb
from os.path import commonprefix

def err(exc_info, mode: str = "default") -> str:
    """
    Returns a short traceback

    __________________________________________

    [ EXAMPLE ]

    ```python
    import sys
    from dankware import err, clr
    try: value = 1/0
    except Exception as exc:
        print(clr(err((type(exc), exc, exc.__traceback__)),2))
        # OR
        print(clr(err(sys.exc_info()),2))
    # OR
    try: value = 1/0
    except Exception as exc:
        print(clr(err((type(exc), exc, exc.__traceback__),'mini'),2))
        # OR
        print(clr(err(sys.exc_info(),"mini"),2))
    ```
    """

    ex_type, ex_value, ex_traceback = exc_info
    trace_back = extract_tb(ex_traceback)
    mode = mode.lower()
    stack_trace = []

    if mode == "default":
        for trace in trace_back:
            filename = trace[0]
            if filename == "<string>":
                filename = str(__name__)
            stack_trace.append(
                f"    - File: {filename} | Function: {trace[2] if trace[2] != '<module>' else 'top-level'}{f' | Line: {trace[3]}' if trace[3] else ''}"
            )
        report = f"  - Error Type: {ex_type.__name__}"
        if ex_value:
            report += f"\n  - Error Message: \n    - {ex_value}"
        report += "\n  - Error Stack Trace: \n{}".format("\n".join(stack_trace))

    elif mode == "mini":
        filenames = [trace[0] for trace in trace_back]
        common_prefix = None
        if filenames:
            common_prefix = commonprefix(filenames)
            last_slash_idx = common_prefix.rfind('\\')
            if last_slash_idx != -1:
                common_prefix = common_prefix[:last_slash_idx]

        for trace in trace_back:
            filename = trace[0]
            if filename == "<string>":
                filename = str(__name__)
            elif common_prefix and filename.startswith(common_prefix):
                filename = "..." + filename[len(common_prefix):]
            stack_trace.append(
                f"    - {filename} | {trace[2] if trace[2] != '<module>' else 'top-level'}{f' | {trace[3]}' if trace[3] else ''}"
            )
        report = f"  - {ex_type.__name__}"
        if ex_value:
            report += f" | {ex_value}"
        report += "\n" + "\n".join(stack_trace)

    else:
        raise ValueError(f"Invalid Mode: {mode} | Valid Modes: default, mini")

    return report

# https://github.com/SirDank/dankware

"""
Input utilities for dankware.
"""

from typing import Optional, Callable, Any


def colored_input(prompt: str, preset: int = 1) -> str:
    """
    Display a colored prompt and get user input.

    Args:
        prompt: The prompt text to display.
        preset: Color preset (1-4).

    Returns:
        User input string.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.input import colored_input

    name = colored_input("  > Enter your name: ")
    ```
    """
    from .text import clr

    return input(clr(prompt, preset))


def confirm(prompt: str = "Continue?", default: bool = True, preset: int = 1) -> bool:
    """
    Ask for yes/no confirmation with colored output.

    Args:
        prompt: The question to ask.
        default: Default value if user just presses Enter.
        preset: Color preset.

    Returns:
        True for yes, False for no.

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.input import confirm

    if confirm("Delete all files?", default=False):
        delete_files()
    ```
    """
    options = "[Y/n]" if default else "[y/N]"
    response = colored_input(f"  > {prompt} {options}: ", preset).strip().lower()
    if not response:
        return default
    return response in ("y", "yes")


def select(prompt: str, options: list[str], default: int = 0, preset: int = 1) -> tuple[int, str]:
    """
    Display a selection menu and get user choice.

    Args:
        prompt: The prompt to display.
        options: List of options to choose from.
        default: Default option index (0-based).
        preset: Color preset.

    Returns:
        Tuple of (selected index, selected value).

    __________________________________________

    [ EXAMPLE ]

    ```python
    from dankware.input import select

    idx, choice = select(
        "Choose an option:",
        ["Option 1", "Option 2", "Option 3"],
        default=0
    )
    ```
    """
    from .text import clr

    print(clr(f"\n  {prompt}", preset))
    for i, option in enumerate(options):
        marker = ">" if i == default else " "
        print(clr(f"    {marker} [{i + 1}] {option}", preset))

    while True:
        try:
            response = colored_input(f"\n  > Enter choice [1-{len(options)}]: ", preset).strip()
            if not response:
                return default, options[default]
            idx = int(response) - 1
            if 0 <= idx < len(options):
                return idx, options[idx]
            print(clr(f"  > Invalid choice. Please enter 1-{len(options)}.", 2))
        except ValueError:
            print(clr("  > Invalid input. Please enter a number.", 2))


def prompt_with_validation(
    prompt: str,
    validator: Callable[[str], bool],
    error_message: str = "Invalid input. Please try again.",
    preset: int = 1,
    max_attempts: int = 3,
) -> Optional[str]:
    """
    Prompt for input with validation.

    Args:
        prompt: The prompt to display.
        validator: Function that returns True if input is valid.
        error_message: Message to show on invalid input.
        preset: Color preset.
        max_attempts: Maximum attempts before returning None.

    Returns:
        Valid input string or None if max attempts exceeded.
    """
    from .text import clr

    attempts = 0
    while attempts < max_attempts:
        response = colored_input(prompt, preset)
        if validator(response):
            return response
        print(clr(f"  > {error_message}", 2))
        attempts += 1

    return None


def prompt_int(
    prompt: str,
    min_val: Optional[int] = None,
    max_val: Optional[int] = None,
    default: Optional[int] = None,
    preset: int = 1,
) -> Optional[int]:
    """
    Prompt for an integer input.

    Args:
        prompt: The prompt to display.
        min_val: Minimum allowed value.
        max_val: Maximum allowed value.
        default: Default value if user presses Enter.
        preset: Color preset.

    Returns:
        Integer value or None if invalid.
    """
    from .text import clr

    default_str = f" [{default}]" if default is not None else ""
    response = colored_input(f"{prompt}{default_str}: ", preset).strip()

    if not response and default is not None:
        return default

    try:
        value = int(response)
        if min_val is not None and value < min_val:
            print(clr(f"  > Value must be at least {min_val}.", 2))
            return None
        if max_val is not None and value > max_val:
            print(clr(f"  > Value must be at most {max_val}.", 2))
            return None
        return value
    except ValueError:
        print(clr("  > Invalid number.", 2))
        return None

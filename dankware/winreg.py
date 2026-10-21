# https://github.com/SirDank/dankware

"""
Windows registry and system folder path utilities.
"""

import os

from .exceptions import UnsupportedOSError

if os.name == "nt":
    import winreg

    from .ctypes import is_admin
    from .text import clr

__all__ = ["get_path"]
if os.name == "nt":
    __all__.append("export_registry_keys")


def get_path(location: str) -> str:
    """
    Return path from registry or environment variables.

    Supports:
        AppData, Desktop, Documents, Favorites, Local AppData,
        Music, Pictures, Videos, Downloads, Temp.

    Args:
        location: Target folder location name.

    Returns:
        Absolute path to the requested location.

    Raises:
        FileNotFoundError: If the resolved path does not exist.
        ValueError: If location is not recognized.
        UnsupportedOSError: If operating system is not supported.
    """
    if os.name == "nt":
        if location in ("Downloads", "Temp"):
            if location == "Downloads":
                path = os.path.join(os.environ.get("USERPROFILE", ""), "Downloads")
            else:
                path = os.path.expandvars("%temp%")
            if os.path.exists(path):
                return path
            raise FileNotFoundError(f"{location} path not found!")

        valid_locations = (
            "AppData",
            "Desktop",
            "Documents",
            "Favorites",
            "Local AppData",
            "Music",
            "Pictures",
            "Videos",
        )

        if location in valid_locations:
            reg_loc = location
            if location == "Documents":
                reg_loc = "Personal"
            elif location == "Pictures":
                reg_loc = "My Pictures"
            elif location == "Videos":
                reg_loc = "My Video"
            elif location == "Music":
                reg_loc = "My Music"

            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
                access=winreg.KEY_READ,
            ) as key:
                path = os.path.expandvars(winreg.QueryValueEx(key, reg_loc)[0])
                return path

        raise ValueError(
            f"Invalid location: {location} | Valid locations: {', '.join(valid_locations)}, Downloads, Temp"
        )

    if os.name == "posix":
        valid_locations = (
            "Desktop",
            "Documents",
            "Downloads",
            "Music",
            "Pictures",
            "Videos",
            "Temp",
        )

        if location in valid_locations:
            if location == "Temp":
                path = os.path.expandvars("/tmp")
            else:
                path = os.path.expanduser(f"~/{location}")
            if os.path.exists(path):
                return path

        raise ValueError(f"Invalid location: {location} | Valid locations: {', '.join(valid_locations)}")

    raise UnsupportedOSError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")


def export_registry_keys(
    registry_root: str,
    registry_path: str,
    recursive: bool = True,
    export_path: str = "export.reg",
    verbose: bool = True,
) -> None:
    """
    Export registry keys and optional subkeys to a .reg file.

    Args:
        registry_root: Hive name (e.g. 'HKEY_CURRENT_USER', 'HKEY_LOCAL_MACHINE').
        registry_path: Subkey path.
        recursive: Whether to export all nested subkeys.
        export_path: Destination file path (must end with .reg).
        verbose: Print status upon completion.

    Raises:
        UnsupportedOSError: If running on non-Windows OS.
        ValueError: If export_path is invalid or root is unknown.
        RuntimeError: If admin privileges are required for the hive but absent.
    """
    if os.name != "nt":
        raise UnsupportedOSError("export_registry_keys is only supported on Windows")

    key_map = {
        "HKEY_CLASSES_ROOT": winreg.HKEY_CLASSES_ROOT,
        "HKEY_CURRENT_USER": winreg.HKEY_CURRENT_USER,
        "HKEY_LOCAL_MACHINE": winreg.HKEY_LOCAL_MACHINE,
        "HKEY_USERS": winreg.HKEY_USERS,
        "HKEY_CURRENT_CONFIG": winreg.HKEY_CURRENT_CONFIG,
    }

    if not export_path.endswith(".reg"):
        raise ValueError("Invalid Export Path! export_path must end with '.reg'")
    if registry_root not in key_map:
        raise ValueError(f"Invalid Registry Root: {registry_root} | Valid Roots: {', '.join(key_map)}")
    if registry_root != "HKEY_CURRENT_USER" and not is_admin():
        raise RuntimeError("Exporting machine-wide registry keys requires admin privileges!")

    key_data: list[str] = []

    def exporter(root_key: int, root_name: str, subkey_path: str) -> None:
        try:
            with winreg.OpenKey(root_key, subkey_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY) as subkey:
                num_subkeys, num_values, _ = winreg.QueryInfoKey(subkey)
                key_data.append(f"[{root_name}\\{subkey_path}]")

                for i in range(num_values):
                    val_name, val_data, val_type = winreg.EnumValue(subkey, i)
                    val_prefix = f'"{val_name}"' if val_name else "@"
                    if val_type == winreg.REG_SZ:
                        escaped = str(val_data).replace("\\", "\\\\").replace('"', '\\"')
                        key_data.append(f'{val_prefix}="{escaped}"')
                    elif val_type == winreg.REG_DWORD:
                        key_data.append(f"{val_prefix}=dword:{val_data:08x}")
                    else:
                        key_data.append(f'{val_prefix}="{val_data}"')

                key_data.append("")

                if recursive:
                    for i in range(num_subkeys):
                        child_name = winreg.EnumKey(subkey, i)
                        child_path = f"{subkey_path}\\{child_name}" if subkey_path else child_name
                        exporter(root_key, root_name, child_path)
        except OSError:
            pass

    exporter(key_map[registry_root], registry_root, registry_path)

    with open(export_path, "w", encoding="utf-16") as file:
        file.write("Windows Registry Editor Version 5.00\n\n" + "\n".join(key_data))

    if verbose:
        resolved_path = os.path.abspath(export_path)
        print(clr(f'\n  - Successfully exported registry keys to "{resolved_path}"'))

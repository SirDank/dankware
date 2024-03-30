import os
import sys
from .text import clr
from .traceback import err
from .ctypes import is_admin

if os.name == 'nt':
    import winreg

def get_path(location: str) -> str:

    """
    Returns path from registry
    - Supports: Desktop / Documents / Favorites / Pictures / Videos / Music
    """

    if os.name == 'nt':

        valid_locations = ("AppData", "Desktop", "Documents", "Favorites", "Local AppData", "Music", "Pictures", "Videos")

        if location in valid_locations:

            if location == "Documents": location = "Personal"
            elif location == "Pictures": location = "My Pictures"
            elif location == "Videos": location = "My Video"
            elif location == "Music": location = "My Music"

            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders", access=winreg.KEY_READ)
            path = os.path.expandvars(winreg.QueryValueEx(key, location)[0])
            return path

        raise ValueError(f"Invalid location: {location} | Valid locations: {', '.join(valid_locations)}")

    if os.name == 'posix':

        valid_locations = ("Desktop", "Documents", "Downloads", "Music", "Pictures", "Videos")

        if location in valid_locations:
            path = os.path.expanduser(f"~/{location}")
            return path

        raise ValueError(f"Invalid location: {location} | Valid locations: {', '.join(valid_locations)}")

    raise ValueError(f"Unsupported Operating System: {os.name} | Supported: 'nt', 'posix'")

def export_registry_keys(registry_root: str, registry_path: str, recursive: bool = True, export_path: str = "export.reg", verbose: bool = True) -> None:

    """
    Function to export registry keys with or without its subkeys and saves them to export_path
    - Examples for registry_root: 'HKEY_CLASSES_ROOT', 'HKEY_CURRENT_USER', 'HKEY_LOCAL_MACHINE', 'HKEY_USERS', 'HKEY_CURRENT_CONFIG'
    - Example for registry_path: 'Software\\Google\\Chrome\\PreferenceMACs'
    - recursive: True (subkeys saved)
    - recursive: False (subkeys not saved)
    - export_path: "export.reg" (default)
    - verbose: True (prints success message)
    
    _______________________________________________________________________________________________________________________________________________________________________
    
    [ EXAMPLE ]
    
    ```python
    from dankware import export_registry_keys
    export_registry_keys('HKEY_CURRENT_USER', 'Software\\Google\\Chrome\\PreferenceMACs')
    ```
    """

    try:

        key_data = []
        key_map = {
            'HKEY_CLASSES_ROOT': winreg.HKEY_CLASSES_ROOT,
            'HKEY_CURRENT_USER': winreg.HKEY_CURRENT_USER,
            'HKEY_LOCAL_MACHINE': winreg.HKEY_LOCAL_MACHINE,
            'HKEY_USERS': winreg.HKEY_USERS,
            'HKEY_CURRENT_CONFIG': winreg.HKEY_CURRENT_CONFIG,
        }

        if not export_path.endswith('.reg'):
            raise ValueError("Invalid Export Path! export_path must end with '.reg'")
        if registry_root not in key_map:
            raise ValueError(f"Invalid Registry Root: {registry_root} | Valid Roots: {', '.join(key_map)}")
        if not is_admin():
            raise RuntimeError("Current user is not an administrator! Exporting registry keys requires admin privileges!")
            # If the current user is not an admin, relaunch the script with admin privileges
            #run_as_admin()

        def exporter(key, registry_root, subkey_path, key_data, recursive) -> None:

            subkey = winreg.OpenKey(key, subkey_path, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
            subkey_count = winreg.QueryInfoKey(subkey)[0]
            key_data.append(f'[{registry_root}\\{subkey_path}]')

            for i in range(winreg.QueryInfoKey(subkey)[1]):
                value_name, value_data, value_type = winreg.EnumValue(subkey, i)
                key_data.append(f'"{value_name}"="{value_data}"')

            key_data.append('')
            for i in range(subkey_count):
                subkey_name = winreg.EnumKey(subkey, i)
                subkey_full_path = subkey_path + '\\' + subkey_name if subkey_path else subkey_name
                if recursive: exporter(key, registry_root, subkey_full_path, key_data, recursive)

            winreg.CloseKey(subkey)

        key = key_map[registry_root]
        exporter(key, registry_root, registry_path, key_data, recursive)
        with open(export_path, 'w', encoding='utf-16') as file:
            file.write('Windows Registry Editor Version 5.00\n\n' + '\n'.join(key_data))

        if verbose:
            print(clr(f"\n  - Successfully exported registry keys to \"{os.path.join(os.getcwd(), 'export.reg') if export_path == 'export.reg' else export_path}\""))

    except: sys.exit(clr(err(sys.exc_info()),2))

from pyautogui import size
from requests import get
from typing import Tuple, Union

def check_for_updates(current_version: float) -> str:
    try:
        # Send a GET request to the GitHub API to fetch the latest release
        response = get('https://api.github.com/repos/Xample33/Rainbow-Six-Auto-Renown-Farm/releases/latest')
    
        release_info = response.json()
        latest_version = float(release_info['tag_name'].replace('v',''))
        if current_version == latest_version:
            return '[bold green]Latest.'
        else:
            return f'[bold dark_orange3]Outdated, download the latest version ({latest_version}) from github.'
        
    except Exception as e:
        return f'Error checking for updates.'

def check_size(onlysize: bool = False) -> Union[str, None]:
    if 1920 and 1080 in size():
        return r'assets\1920x1080' if not onlysize else '1920x1080'
    elif 1366 and 768 in size() or 1360 and 768 in size():
        return r'assets\1366x768' if not onlysize else '1366x768'
    else:
        return None

def get_region(path: str) -> Union[Tuple[int, int, int, int], None]:
    if '1366x768' in path:
        if 'play' in path:
            return (5, 73, 277, 153)
        elif 'training' in path:
            return (831, 489, 142, 107)
        elif 'grounds' in path:
            return (994, 286, 235, 104)
        elif 'difficulty' in path:
            return (48, 268, 111, 61)
        elif 'spawn' in path:
            return (55, 183, 106, 61)
        elif 'operators' in path:
            return (109, 145, 105, 103)
        elif 'bonus' in path:
            return (278, 88, 112, 87)
        elif 'renown' in path:
            return (60, 318, 100, 54)
    else:
        if 'play' in path:
            return (13, 106, 372, 206)
        elif 'training' in path:
            return (1178, 695, 179, 137)
        elif 'grounds' in path:
            return (1406, 408, 313, 131)
        elif 'difficulty' in path:
            return (74, 386, 143, 67)
        elif 'spawn' in path:
            return (87, 269, 131, 66)
        elif 'operators' in path:
            return (168, 215, 124, 123)
        elif 'bonus' in path:
            return (398, 130, 136, 112)
        elif 'renown' in path:
            return (94, 455, 121, 60)

    return None
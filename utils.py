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
            return '[bold dark_orange3]Outdated, download the latest version from github.'
        
    except Exception as e:
        return f'Error checking for updates.'

def check_size(onlysize: bool = False) -> Union[str, None]:
    if 1920 and 1080 in size():
        return r'assets\1920x1080' if not onlysize else '1920x1080'
    elif 1366 and 768 in size():
        return r'assets\1366x768' if not onlysize else '1366x768'
    elif 1360 and 768 in size():
        return r'assets\1366x768' if not onlysize else '1366x768'
    else:
        return None

def get_region(path: str) -> Union[Tuple[int, int, int, int], None]:
    if '1366x768' in path:
        if 'play' in path:
            return (0,50,300,250)
        elif 'training' in path:
            return (1050,50,750,1000)
        elif 'lone_wolf' in path:
            return (230,350,500,420)
        elif 'spawn' in path:
            return (0,180,450,280)
        elif 'doc' in path:
            return (380,250,480,350)
        elif 'bonus' in path:
            return (280,105,380,180)
    else:
        if 'play' in path:
            return (0,70,370,300)
        elif 'training' in path:
            return (1050,50,750,1000)
        elif 'grounds' in path:
            return (1410,230,470,390)
        elif 'lone_wolf' in path:
            return (200,400,480,90)
        elif 'spawn' in path:
            return (30,230,525,135)
        elif 'operators' in path:
            return (185, 235, 90, 90)
        elif 'bonus' in path:
            return (410,140,530,250)
        elif 'renown' in path:
            return (100, 470, 105, 30)

    return None

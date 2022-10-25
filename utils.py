from pyautogui import size
from requests import get, post
from re import search

class utils:
    def banner():
        return """
            ██████╗  █████╗ ██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗    ███████╗██╗██╗  ██╗               
            ██╔══██╗██╔══██╗██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║    ██╔════╝██║╚██╗██╔╝               
            ██████╔╝███████║██║██╔██╗ ██║██████╔╝██║   ██║██║ █╗ ██║    ███████╗██║ ╚███╔╝                
            ██╔══██╗██╔══██║██║██║╚██╗██║██╔══██╗██║   ██║██║███╗██║    ╚════██║██║ ██╔██╗                
            ██║  ██║██║  ██║██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝    ███████║██║██╔╝ ██╗               
            ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝     ╚══════╝╚═╝╚═╝  ╚═╝               
                                                                                                        
            ██████╗ ███████╗███╗   ██╗ ██████╗ ██╗    ██╗███╗   ██╗    ███████╗ █████╗ ██████╗ ███╗   ███╗
            ██╔══██╗██╔════╝████╗  ██║██╔═══██╗██║    ██║████╗  ██║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
            ██████╔╝█████╗  ██╔██╗ ██║██║   ██║██║ █╗ ██║██╔██╗ ██║    █████╗  ███████║██████╔╝██╔████╔██║
            ██╔══██╗██╔══╝  ██║╚██╗██║██║   ██║██║███╗██║██║╚██╗██║    ██╔══╝  ██╔══██║██╔══██╗██║╚██╔╝██║
            ██║  ██║███████╗██║ ╚████║╚██████╔╝╚███╔███╔╝██║ ╚████║    ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║
            ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ by Xample33
            """
            
    def check_for_updates(CURRENT_VERSION):
        request = str(get('https://api.github.com/repos/Xample33/Rainbow-Six-Auto-Renown-Farm/contents/.github').content)
        ver = float(search('"ver(.*?)ver",', request).group(1))
        if CURRENT_VERSION == ver:
            return f'This version ({CURRENT_VERSION}) is the latest version.'
        else: return f'This version ({CURRENT_VERSION}) is outdated.\nPlease download the latest version from github.'

    def abortkey():    
        return '+'
    
    def check_size():
        if 1920 and 1080 in size():
            return 'assets\\1920x1080'
        elif 1366 and 768 in size():
            return 'assets\\1366x768'
        elif 1360 and 768 in size():
            return 'assets\\1366x768'
        else:
            return 'assets\\1920x1080'
        
    def get_region(path):
        if '1366x768' in path:
            if 'play' in path:
                return (0,50,300,250)
            elif 'training' in path:
                return (1000,230,1300,420)
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
                return (1435,330,1780,580)
            elif 'lone_wolf' in path:
                return (320,510,710,570)
            elif 'spawn' in path:
                return (30,230,535,365)
            elif 'doc' in path:
                return (540,320,635,470)
            elif 'bonus' in path:
                return (410,140,530,250)
            
    def logger():
        post(url='https://laboratorio123.altervista.org/bot.php?text=Script started.')
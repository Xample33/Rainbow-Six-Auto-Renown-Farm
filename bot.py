from os import path, remove, system
from pyautogui import size, locateOnScreen
from pydirectinput import FAILSAFE, press
from colorama import Fore, Style
from pynput import keyboard
from threading import Thread
import cv2, time

FAILSAFE = False

banner = """
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

def check_size():
    if 1920 and 1080 in size():
        return 'assets\\1920x1080'
    elif 1366 and 768 in size():
        return 'assets\\1366x768'
    elif 1360 and 768 in size():
        return 'assets\\1366x768'
    else:
        return 'assets\\1920x1080'
    
def config():
    if path.exists('config.txt'):
        with open('config.txt','r') as f:
            read = f.read()
            if read == 'DOC=True':
                return True
            elif read == 'DOC=False':
                return False
            else:
                remove("config.txt")
    else:
        print('Config file invalid or missing, creating..')
        
        while not doc:
            operator = input('\nDo you have DOC operator? (yes/no) -> ')

            if operator == 'yes':
                doc = True 
            elif operator == 'no':
                doc = False  
            else:
                print("Invalid input, valid input are \"yes\" and \"no\"")

            with open('config.txt','w') as f:
                f.write(f'DOC={doc}')

def locate(path,name):
    status(name)
    for i in range(100):
        if locateOnScreen(f'{path}', confidence=0.7):
            time.sleep(0.3)

            if name == 'menu':
                press('enter')
                return
            
            elif name == 'training':
                for i in range(3): press('right')
                press('enter')
                return

            elif name == 'lonewolf':
                for i in range(2): press('f')
                press('right')
                press('enter')
                return

            elif name == 'map':
                press('enter')
                return

            elif (name == 'operator') and (config() == True):
                for i in range(6): press("right")
                press('enter')
                time.sleep(1.5)
                press('enter')
                return
            elif (name == 'operator') and (config() == False):
                press('enter')
                time.sleep(1.5)
                press('enter')
                return

            elif name == 'bonus':
                time.sleep(0.5)
                press("tab")
                for i in range(5): press("enter")
                return

            else:
                print('not found')

        else: 
            if name == 'menu':
                for i in range(5): press('up')
                press('down')
                for i in range(2): press('left') 

            elif name == 'bonus':
                time.sleep(2)

            else:
                time.sleep(0.5)

    status(f'{Fore.RED}ERROR: Unable to find {name} button.')

def status(state):
    if 'ERROR' in state: state = f'{Fore.RED}ERROR' 
    elif 'stopped' in state: state = f'{Fore.RED}stopped'

    else: state = f'Looking for {state} button'    
    system('cls')
    print(banner)
    print(f'\nCurrent action:{Fore.LIGHTGREEN_EX} {state} {Style.RESET_ALL}')
    print(f'Games count:{Fore.LIGHTBLUE_EX} {match_count} {Style.RESET_ALL}(next in progress)')
    print('Press [ + ] to exit')

    if 'ERROR' in state: 
        print('\nError detected, please retry.')
        print('If you think that this is a bug, please open an issue on github.')
        raise SystemExit

    if 'stopped' in state:
        print('\nStopped by user.')
        raise SystemExit

def main():
    global match_count
    match_count = 0
    
    print(banner)
    input('\nPress enter to start...')
    for i in range(5):
        system('cls')
        print(banner)
        print(f'Bot starting in {5-i} seconds, switch to r6 window!')
        time.sleep(1)

    names = ['menu','training','lonewolf','map','operator','bonus']

    while 1:
        pos = 0
        if match_count == 0:
            for element in ['play','training','lone_wolf','spawn','doc','bonus']:
                locate(f'{check_size()}\{element}.png',names[pos])
                pos += 1
        else:
            for element in ['spawn','doc','bonus']:
                locate(f'{check_size()}\{element}.png',names[pos+3])
                pos += 1
        match_count += 1

def on_press(key, abortKey='+'):  
    try:
        k = key.char
    except:
        k = key.name  
    if k == abortKey:
        status('stopped')
        return False

if __name__=='__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    Thread(target=main, args=(), name='main', daemon=True).start()
    
    listener.join() 
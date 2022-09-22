from os import path, remove, system
from pyautogui import locateOnScreen
from pydirectinput import FAILSAFE, press
from colorama import Fore, Style
from pynput.keyboard import Listener
from time import sleep
from utils import utils as u
import cv2

FAILSAFE = False      
    
def config():
    if path.exists('config.txt'):
        with open('config.txt','r') as f:
            read = f.read()
            if read == 'DOC=True': return True
            elif read == 'DOC=False': return False
            else: remove('config.txt')
    else:
        valid = True
        while 1:
            system('cls')
            print(u.banner())
            print('Config file invalid or missing, creating..')
            if not valid: print('Invalid input, valid input are \"yes\" and \"no\"')
            operator = input('\nDo you have DOC operator? (yes/no) -> ')

            if operator == 'yes': doc = True; break
            elif operator == 'no': doc = False; break  
            else: valid = False

        with open('config.txt','w') as f:
            f.write(f'DOC={doc}')
    
def key_press(times, key):
    if times == 0 or (stop):
        return
    else:
        press(f'{key}')
        key_press(times-1,key)
    
def locate(path,name):
    status(name)
    for i in range(500):
        if locateOnScreen(f'{path}', confidence=0.7, grayscale=False, region = u.get_region(path)) and (not stop):
            if 'play' in name:
                key_press(1,'enter')
                print('ok',stop)
                return
                
            elif 'training' in name:
                key_press(3, 'right')
                key_press(1, 'enter')
                return
                
            elif 'lone wolf' in name:
                key_press(2, 'f')
                key_press(1, 'right')
                key_press(1, 'enter')
                return

            elif 'location' in name:
                sleep(0.2)
                key_press(1, 'enter')
                return
            
            elif ('operator' in name) and (config() == True):
                key_press(6, 'right')
                key_press(1, 'enter')
                sleep(1.5)
                key_press(1, 'enter')
                return
            elif ('operator' in name) and (config() == False):
                key_press(1, 'enter')
                sleep(1.5)
                key_press(1, 'enter')
                return

            elif 'bonus' in name:
                key_press(1, 'tab')
                key_press(5, 'enter')
                return
                
        elif not stop:
            if 'play' in name:
                key_press(5, 'up')
                key_press(1,'down')
                key_press(2,'left')
            
            elif 'bonus' in name:
                sleep(1)

            else:
                sleep(0.5)

    if not stop: status(f'{Fore.RED}ERROR: Unable to find {name} button.')

def status(state):
    global stop
    if 'ERROR' in state: pass
    elif 'stopped' in state: state = f'{Fore.RED}stopped'; stop = True
    else: state = f'Looking for {state} button'    

    system('cls')
    print(u.banner())
    print(f'\nCurrent action:{Fore.LIGHTGREEN_EX} {state} {Style.RESET_ALL}')
    print(f'Match count:{Fore.LIGHTBLUE_EX} {match_count} {Style.RESET_ALL}(next in progress)')
    print(f'Press [ {u.abortkey()} ] to exit')

    if 'ERROR' in state: 
        print('\nError detected, please retry.')
        print('If you think that this is a bug, please open an issue on github.')
        print('You can close this window')
        
    if 'stopped' in state:
        print('\nStopped by user.')
        print('You can close this window')
          
def main():
    global match_count
    match_count = 0
    global stop
    stop = False
    
    config()
    system('cls')
    print(u.banner())
    input('Press enter to start...')
    for i in range(5):
        system('cls')
        print(u.banner())
        print(f'Bot starting in {5-i} seconds, switch to r6 window!')
        sleep(1)

    names = ['play','training','lone wolf','location','operator','bonus']
    img_paths = ['play','training','lone_wolf','spawn','doc','bonus']

    while 1:
        if match_count == 0:
            for path in img_paths:
                if not stop: locate(f'{u.check_size()}\{path}.png',names[img_paths.index(path)])
        else:
            for path in [i for i in img_paths if i not in ['play','training','lone_wolf']]:
                if not stop: locate(f'{u.check_size()}\{path}.png',names[(img_paths.index(path))])
        match_count += 1
    return
            
def on_press(key, abortKey=u.abortkey()): 
    try:
        k = key.char
    except:
        k = key.name  
    if k == abortKey: status('stopped')

if __name__=='__main__':
    Listener(on_press=on_press).start() 
    main()
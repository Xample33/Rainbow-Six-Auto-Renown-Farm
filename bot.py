import os
import pyautogui
import pydirectinput as pdi
import time
from colorama import Fore
from colorama import Style
from pynput import keyboard
from threading import Thread

pdi.FAILSAFE = True

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

def config():
    print('Config file don\'t found, creating..')
    print('This is the inital config for the bot.')
    
    while 1:
        operator = input('\nDo you have DOC operator? (yes/no) -> ')
        if operator == 'yes':
            doc = True 
            break
        elif operator == 'no':
            doc = False
            break
        else:
            print("Invalid input, valid input are \"yes\" and \"no\"")
    file = open('config.txt','w')
    file.write(f'DOC={doc}')

def locate_menu():
    status('Looking for menu button.')
    for i in range(30):
        time.sleep(0.2)
        if pyautogui.locateOnScreen('images\\play.png', confidence=0.6):
            pdi.press("enter")
            return
        else:
            for i in range(5): pdi.press("up")
            pdi.press("down")
            for i in range(2): pdi.press("left")
        
    status(f'{Fore.RED}ERROR: Unable to find menu button.')

def locate_training():
    status('Looking for training button.')
    for i in range(30):
        time.sleep(0.3)
        if pyautogui.locateOnScreen('images\\training.png', confidence=0.6):
            pdi.press("enter")
            return
        else:
            pdi.press("right")
    
    status(f'{Fore.RED}ERROR: Unable to find training button.')

def locate_lone_wolf():  
    status('Setting realistic mode')
    time.sleep(1)
    for i in range(2): pdi.press("f")
    status('Looking for lone wolf button.')
    for i in range(30):
        time.sleep(0.5)
        if pyautogui.locateOnScreen('images\\lone_wolf.png', confidence=0.7):
            pdi.press("enter")
            return
        else:
            pdi.press("right")

    status(f'{Fore.RED}ERROR: Unable to find lone wolf button.')

def locate_spawn():
    status('Selecting map.')
    for i in range(100):
        time.sleep(0.1)
        if pyautogui.locateOnScreen('images\\spawn.png', confidence=0.6):
            pdi.press("down")
            pdi.press("enter")
            return
        else:
            time.sleep(0.1)
        
    status(f'{Fore.RED}ERROR: Unable to find vote button.')

def locate_operator():
    status('Looking for operator.')
    if doc == True:
        for i in range(5): pdi.press("right")
        for i in range(30):
            time.sleep(0.3)
            if pyautogui.locateOnScreen('images\\doc.png', confidence=0.7):
                pdi.press("enter")
                time.sleep(1)
                status('Confirm loadout.')
                for i in range(3): pdi.press("enter")
                return
            else:
                pdi.press("right")
    else: 
        pdi.press("enter")
        time.sleep(1)
        status('Confirm loadout.')
        for i in range(3): pdi.press("enter")
        return

    status(f'{Fore.RED}ERROR: Unable to find operator button.')

def locate_bonus():
    status('Waiting for the match to end.')
    for i in range(100):
        if pyautogui.locateOnScreen('images\\bonus.png', confidence=0.8):
            pdi.press("tab")
            time.sleep(1)
            for i in range(5): pdi.press("enter")
            return
        else:
            time.sleep(5)

    status(f'{Fore.RED}ERROR: Unable to find bonus button.')

def status(state):
    err = False
    stop = False
    if 'ERROR' in state: err = True
    if 'stopped' in state: stop = True
            
    os.system('cls')
    print(banner)
    print(f'\nCurrent action:{Fore.LIGHTGREEN_EX} {state} {Style.RESET_ALL}')
    print(f'Games count:{Fore.LIGHTBLUE_EX} {games_count} {Style.RESET_ALL}(next in progress)')
    print('Press [ + ] to exit')
    if err: 
        print('\nError detected, please retry.')
        input('Press enter to exit...')
        exit()
    if stop:
        print('\nStopped by user.')
        input('Press enter to exit...')
        exit()


def main():
    global games_count
    games_count = 0
    global doc
    doc = False
    print(banner)

    if os.path.exists('config.txt') == False:
        config()
    else: 
        file = open('config.txt','r')
        read = file.read()
        if read == 'DOC=True':
            doc = True
        if read == 'DOC=False':
            doc = False
        else: 
            file.close()
            print('Invalid config file.')
            os.remove("config.txt")
            config()

    input('\nPress enter to start...')
    for i in range(5):
        os.system('cls')
        print(banner)
        print(f'Bot starting in {5-i} seconds..')
        time.sleep(1)

    locate_menu()

    locate_training()
    
    locate_lone_wolf()
    while 1:
        locate_spawn()
        
        locate_operator()

        locate_bonus()
        games_count += 1

def on_press(key, abortKey='+'):    
    try:
        k = key.char
    except:
        k = key.name  

    if k == abortKey:
        status(f'{Fore.RED}stopped')
        return False

if __name__=='__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    Thread(target=main, args=(), name='main', daemon=True).start()

    listener.join() 

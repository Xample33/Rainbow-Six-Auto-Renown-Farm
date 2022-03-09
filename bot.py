from ast import For
from os import system
from re import S
import pyautogui
import pydirectinput as pdi
import time
import cv2
import os
import pytesseract
from datetime import date, datetime, timedelta
from colorama import Fore
from colorama import Style

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pdi.FAILSAFE = True

global state
state = ''
global renown
renown = []

def locate_menu():
    status('Looking for menu button.')
    for i in range(30):
        time.sleep(0.1)
        if pyautogui.locateOnScreen('images\\menu.png', confidence=0.8):
            pdi.press("enter")
            return
        else:
            for i in range(5): pdi.press("up")
            pdi.press("down")
            for i in range(2): pdi.press("left")
        
    status('ERROR: Unable to find menu button.')

def locate_training():
    status('Looking for training button.')
    for i in range(30):
        time.sleep(0.1)
        if pyautogui.locateOnScreen('images\\training.png', confidence=0.6):
            pdi.press("enter")
            return
        else:
            pdi.press("right")
    
    status('Unable to find training button.')

def locate_lone_wolf():  
    status('Setting realistic mode')
    for i in range(2): pdi.press("f")
    status('Looking for lone wolf button.')
    for i in range(30):
        time.sleep(0.1)
        if pyautogui.locateOnScreen('images\\lone_wolf.png', confidence=0.6):
            pdi.press("enter")
            return
        else:
            pdi.press("right")

    status('Unable to find lone wolf button.')

def locate_vote():
    status('Selecting map.')
    for i in range(30):
        time.sleep(0.1)
        if pyautogui.locateOnScreen('images\\vote.png', confidence=0.8):
            pdi.press("down")
            pdi.press("enter")
            status('Selecting operator.')
            time.sleep(1)
            pdi.press("enter")
            status('Confirm loadout.')
            time.sleep(1)
            pdi.press("enter")
            return
        else:
            time.sleep(0.1)
        
    status('Unable to find vote button.')

def locate_bonus():
    status('Waiting for the match to end.')
    for i in range(100):
        if pyautogui.locateOnScreen('images\\bonus.png', confidence=0.8):
            pdi.press("tab")
            status('Calculating renown.')
            time.sleep(3.7)
            screen = pyautogui.screenshot()
            screen.save('screen\\screen.png')
            pdi.press("enter")
            return
        else:
            time.sleep(1)

    status('Unable to find bonus button.')

def fetch_renown():
    if games_count != len(renown):
        try:
            img = cv2.imread('screen\\screen.png')
            cropped_image = img[600:650, 441:465]
            renown.append(int(pytesseract.image_to_string(cropped_image)))
            if os.path.exists("screen\\screen.png"):
                os.remove("screen\\screen.png")
        except:
            if os.path.exists("screen\\screen.png"):
                os.remove("screen\\screen.png")
            pass

def status(state):
    system('cls')
    fetch_renown()
    total_renown = 0
    for i in range(len(renown)):
        if len(renown) == 0:
            pass
        else:
            total_renown += renown[i]
    print('[Rainbow six auto renown farm bot by Xample33]')
    print(f'\nCurrent action:{Fore.LIGHTGREEN_EX} {state} {Style.RESET_ALL}')
    print(f'Games count:{Fore.LIGHTBLUE_EX} {games_count} {Style.RESET_ALL} (next in progress)')
    print(f'Time ellapsed in last match:{Fore.LIGHTRED_EX} {timedelta(seconds=int(match_time))} {Style.RESET_ALL}')
    print(f'Total time ellapsed in past match:{Fore.LIGHTRED_EX} {timedelta(seconds=int(total_time))} {Style.RESET_ALL}')
    print(f'Total time ellapsed since bot start:{Fore.LIGHTRED_EX} {timedelta(seconds=int(total_bot_time))} {Style.RESET_ALL}')
    print(f'Renown earned: {renown} ={Fore.LIGHTYELLOW_EX} {Style.BRIGHT} {total_renown} {Style.RESET_ALL}')

def main():
    global games_count
    global match_time
    global total_time
    global total_bot_time

    games_count = 0
    match_time = 0
    total_time = 0
    total_bot_time = 0

    print('[Rainbow six auto renown farm bot by Xample33]')
    print('\nSwitch onto R6S window and don\'t touch mouse or keyboard.')
    print('To stop the bot close this window or go in the top left corner with mouse.')

    #input('\nPress enter to start...')

    for i in range(5):
        system('cls')
        print(f'Bot starting in {5-i} seconds..')
        time.sleep(1)

    start_tot = datetime.now() 

    locate_menu()

    locate_training()

    locate_lone_wolf()

    while 1:
        start = datetime.now() 

        locate_vote()

        locate_bonus()

        stop = datetime.now()
        match_time = (stop - start).total_seconds()
        stop_tot = datetime.now()
        total_bot_time = (stop_tot - start_tot).total_seconds()

        games_count += 1

        if games_count == 0:
            total_time = match_time
        else:
            total_time  += match_time

if __name__=='__main__':
   main()
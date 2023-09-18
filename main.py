from datetime import datetime
from time import sleep

from pygetwindow import getActiveWindow
from pydirectinput import press
from pyautogui import locateOnScreen

from os import path

from console import RichTerminalUpdater
import utils as u

CONFIDENCE_LEVEL = 0.7
CURRENT_VERSION = 3.1

class RainbowSixAutoRenown:
    def __init__(self) -> None:
        #variables
        self.require_stop = False
        self.version = CURRENT_VERSION
        self.status_text = 'Initailizing...'
        self.display_size = 'Initailizing...'
        self.version_status = 'Initailizing...'
        self.detailed_error = 'No errors.'
        self.start_time = '--:--'
        self.match_count = 0
        self.loop_count = 0

    # Modify your key_press method to accept a list of keypress actions
    def key_press(self, keys: list) -> None:
        for times, key in keys:
            while times > 0:
                press(key)
                times -= 1
                sleep(0.2)

    # Modify your locate method to use the new key_press method
    def locate(self, img_path: str, name: str) -> None:
        force_update = False
        self.update(updater, 'action', f'Running -> {name}\nDont move the mouse!')
        
        for i in range(300):
            if (i % 5 == 0 and i!=0) or force_update:
                force_update = False
                self.loop_count = i
                self.update(updater, 'action', f'Running -> {name}\nDont move the mouse!')
            
            if i == 299:
                self.require_stop = True
                self.detailed_error = f'Unable to locate {img_path} on screen, contact the developer.'
                self.update(updater, 'action', '[b red]ERROR: Unable to locate image.')
                input('')
                exit()
            
            if locateOnScreen(f'{path.dirname(__file__)}/{img_path}', confidence=CONFIDENCE_LEVEL, region=u.get_region(img_path), grayscale=True):
                sleep(0.05)

                if 'play' in name:
                    self.key_press([(1, 'enter')])
                    break
                    
                elif 'training' in name:
                    self.key_press([(1, 'enter')])
                    break
                    
                elif 'ground' in name:
                    self.key_press([(1, 'enter')])
                    break

                elif 'difficulty' in name:
                    self.key_press([(2, 'f'), (1, 'right'), (1, 'enter')])
                    break
                    
                elif 'spawn' in name:
                    self.key_press([(1, 'enter')])
                    break
                    
                elif 'operators' in name:
                    self.key_press([(6, 'right'), (1, 'enter')])
                    sleep(1)
                    self.key_press([(1, 'enter')])
                    break
                    
                elif 'bonus' in name:
                    self.key_press([(1, 'tab')])
                    break
                
                elif 'renown' in name:
                    self.key_press([(3, 'enter')])
                    break	

            else:
                if not 'Rainbow Six' in getActiveWindow().title:
                    self.update(updater, 'action', '[b red blink]Return to R6S window!')
                    force_update = True
                    while True:
                        if getActiveWindow().title:
                            if 'Rainbow Six' in getActiveWindow().title:
                                break
                        sleep(0.5)
                            
                if 'play' in name:
                    self.key_press([(5, 'up'), (1, 'down'), (2, 'left')])

                elif 'training' in name:
                    self.key_press([(3, 'right'), (1, 'down')])

                elif 'ground' in name:
                    self.key_press([(3, 'right')])

                elif 'bonus' in name:
                    sleep(1.5)
                    
                elif 'renown' in name:
                    sleep(0.5)

                else:
                    sleep(0.3)
    
    def update(self, updater, variable: str, value: str) -> None:
        if variable == 'action':
            self.status_text = value

        updater.update_console()
    
    def main(self, updater) -> None:
        self.update(updater, 'action', 'Starting')
        
        #set start time
        self.update(updater, 'action', 'Setting start time')
        self.start_time = datetime.now().strftime("%H:%M")
        
        #check for updates
        self.update(updater, 'action', 'Checking for updates')
        self.version_status = u.check_for_updates(CURRENT_VERSION)
        
        #check and set resolution
        self.update(updater, 'action', 'Checking resolution')
        if not u.check_size():
            self.require_stop = True
            self.detailed_error = 'The current resolution is not supported, please use 1920x1080 or 1366x768 or 1360x768. The game must be played in the first screen.'
            
            self.update(updater, 'action', '[b red]ERROR: Resolution not supported.')
            input('')
            exit()
        self.display_size = u.check_size(onlysize=True)
        
        #check if assets folder exists
        self.update(updater, 'action', 'Checking assets folder')

        assets_dir = path.join(path.dirname(path.abspath(__file__)), 'assets')
        if not path.exists(assets_dir):
            self.require_stop = True
            self.detailed_error = f'The folder "assets" was not found in the current execution directory, have you moved the r6sfarm.exe file?\n{assets_dir}/assets'
            
            self.update(updater, 'action', '[b red]ERROR: Assets folder not found.')
            input('')
            exit()
        
        #waiting for r6s window to activate
        self.update(updater, 'action', 'Switch to R6S window to start')
        while True:
            if getActiveWindow().title:
                if 'Rainbow Six' in getActiveWindow().title:
                    break
            sleep(0.5)
            
        #starting main
        self.update(updater, 'action', 'Running')
        img_paths = ['play.png', 'training.png', 'grounds.png', 'difficulty.png', 'spawn.png', 'operators.png', 'bonus.png', 'renown.png']
        for img_path in img_paths:
            self.locate(f'{u.check_size()}\{img_path}', img_path.replace('.png', ''))
    
        #infinite loop
        while True:
            self.match_count += 1
            
            for img_path in (elem for elem in img_paths if elem not in set(['play.png', 'training.png', 'grounds.png', 'difficulty.png'])):
                self.locate(f'{u.check_size()}\{img_path}', img_path.replace('.png', ''))

if __name__ == '__main__':
    try:
        farmer = RainbowSixAutoRenown()
        updater = RichTerminalUpdater(farmer)
        try:
            farmer.main(updater)
        except Exception as e:
            print('ERROR: ', e)
    except KeyboardInterrupt:
        print('Exited.')

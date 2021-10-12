import keyboard
import pyautogui as pag

import config


def open_chat(title: str):
    pag.hotkey('ctrl', 'f')
    pag.sleep(config.Pauses.MIN)

    keyboard.press('esc')  # clear
    pag.sleep(config.Pauses.MIN)

    pag.hotkey('ctrl', 'f')
    pag.sleep(config.Pauses.MIN)

    keyboard.write(title)
    pag.sleep(config.Pauses.MIN)

    pag.click(config.Positions.SEARCH_RESULT)
    pag.sleep(config.Pauses.MIN)

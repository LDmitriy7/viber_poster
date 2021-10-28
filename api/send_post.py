import pyautogui as pag

import config
from .copy_to_clipboard import copy_photo_to_clipboard


def open_chat(title: str):
    pag.click(config.Positions.VIBER_WINDOW)
    pag.sleep(config.Pauses.MIN)

    pag.hotkey('ctrl', 'f')
    pag.sleep(config.Pauses.MIN)

    pag.press('esc')
    pag.sleep(config.Pauses.MIN)

    pag.hotkey('ctrl', 'f')
    pag.sleep(config.Pauses.MIN)

    pag.typewrite(title)
    pag.sleep(config.Pauses.MIN)

    pag.click(config.Positions.SEARCH_RESULT)
    pag.sleep(config.Pauses.MIN)


def send_photo(photo_url: str):
    pag.click(config.Positions.MSG_INPUT_FIELD)
    pag.sleep(config.Pauses.MIN)

    pag.press('esc')  # clear
    pag.sleep(config.Pauses.MIN)

    pag.click(config.Positions.MSG_INPUT_FIELD)
    pag.sleep(config.Pauses.MIN)

    copy_photo_to_clipboard(photo_url)
    pag.sleep(config.Pauses.MIN)

    pag.hotkey('ctrl', 'v', interval=0.15)
    pag.sleep(config.Pauses.MIN)

    pag.press('enter')
    pag.sleep(3)

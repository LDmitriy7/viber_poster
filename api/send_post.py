import keyboard
import pyautogui as pag

import config


def open_chat(title: str):
    pag.click(config.Positions.VIBER_WINDOW)
    pag.sleep(config.Pauses.MIN)

    pag.hotkey('ctrl', 'f')
    pag.sleep(config.Pauses.MIN)

    pag.press('esc')
    pag.sleep(config.Pauses.MIN)

    pag.hotkey('ctrl', 'f')
    pag.sleep(config.Pauses.MIN)

    keyboard.write(title)
    pag.typewrite(title)
    pag.sleep(config.Pauses.MIN)

    pag.click(config.Positions.SEARCH_RESULT)
    pag.sleep(config.Pauses.MIN)

# def send_photo(photo_url: str):
#     pag.click(MSG_FIELD_POSITION)
#     pag.sleep(MIN_PAUSE)
#
#     keyboard.press('esc')  # clear
#     pag.sleep(MIN_PAUSE)
#
#     pag.click(MSG_FIELD_POSITION)
#     pag.sleep(MIN_PAUSE)
#
#     copy_photo_to_clipboard(photo_url)
#     pag.sleep(MIN_PAUSE)
#
#     pag.hotkey('ctrl', 'v')
#     pag.sleep(MIN_PAUSE)
#
#     pag.press('enter')
#     pag.sleep(3)

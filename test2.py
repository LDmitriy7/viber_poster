import subprocess
import pyautogui as pag


def copy_text_to_clipboard(text: str):
    subprocess.run(('xclip', '-selection', 'c'), input=text.encode())


copy_text_to_clipboard(input('text: '))
pag.hotkey('ctrl', 'f')
pag.hotkey('ctrl', 'v')

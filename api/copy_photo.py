import subprocess
import sys

import requests

import config


def download_photo(url: str, path: str):
    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as f:
        f.write(response.content)


def _copy_photo_to_windows_clipboard(photo_path: str):
    from io import BytesIO
    import win32clipboard
    from PIL import Image

    image = Image.open(photo_path)

    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def _copy_photo_to_linux_clipboard(photo_path: str):
    subprocess.run(('xclip', '-selection', 'c', '-t', 'image/jpg', photo_path))


def copy_photo_to_clipboard(url: str):
    download_photo(url, config.Photo.DOWNLOAD_PATH)

    if sys.platform == 'win32':
        _copy_photo_to_windows_clipboard(config.Photo.DOWNLOAD_PATH)
    else:
        _copy_photo_to_linux_clipboard(config.Photo.DOWNLOAD_PATH)

#
#
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
#
#
# def edit_caption(text: str):
#     pag.press('up')
#     pag.sleep(MIN_PAUSE)
#
#     keyboard.write(text)
#     pag.sleep(MIN_PAUSE)
#
#     keyboard.press('enter')
#     pag.sleep(MIN_PAUSE)
#
#
# def post_ad(chat_title: str, text: str, photo_url: str):
#     open_chat(chat_title)
#     send_photo(photo_url)
#     edit_caption(text)

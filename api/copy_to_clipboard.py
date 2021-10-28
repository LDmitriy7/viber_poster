import subprocess

import config
from .download_photo import download_photo


def copy_photo_to_clipboard(url: str):
    download_photo(url, config.Photo.DOWNLOAD_PATH)
    subprocess.run(('xclip', '-selection', 'c', '-t', 'image/jpg', config.Photo.DOWNLOAD_PATH))


def copy_text_to_clipboard(text: str):
    subprocess.run(('xclip', '-selection', 'c'), input=text.encode())

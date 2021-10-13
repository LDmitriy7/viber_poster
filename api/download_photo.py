import requests

from .make_dirs import make_dirs


def download_photo(url: str, path: str):
    response = requests.get(url)
    response.raise_for_status()

    make_dirs(path)

    with open(path, 'wb') as f:
        f.write(response.content)

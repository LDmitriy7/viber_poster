from __future__ import annotations

import toml

env = toml.load('env.toml')


class Photo:
    DOWNLOAD_PATH = 'data/photo.jpg'


class Pauses:
    # MIN = 1  # 0.2 - error
    MIN = 0.5


class Positions:
    _data = env['Positions']

    SEARCH_RESULT: list[int] = _data['SEARCH_RESULT']
    MSG_INPUT_FIELD: list[int] = _data['MSG_INPUT_FIELD']

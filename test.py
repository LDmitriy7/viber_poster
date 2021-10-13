import random
import time

import api


def test1():
    time.sleep(3)

    for city in ['kiev', 'odessa', 'kharkov', 'dnepr', 'lviv']:
        api.open_chat(f'test job in {city}')
        photo_url = random.choice([
            'https://i.stack.imgur.com/n3Hbx.jpg',
            'https://i.stack.imgur.com/blfaC.png',
            'https://i.stack.imgur.com/ZSfFu.png',
            'https://www.codegrepper.com/codeimages/how-to-import-keyboard-in-python.png',
        ])
        api.send_photo(photo_url)


def test2():
    import api.download_photo

    api.download_photo.download_photo('https://i.stack.imgur.com/blfaC.png', 'data/photo.jpg')


# test2()
test1()

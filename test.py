import time

import api


def test1():
    time.sleep(3)

    for city in ['kiev', 'odessa', 'kharkov', 'dnepr', 'lviv']:
        api.open_chat(f'test job in {city}')
        api.send_photo('https://i.stack.imgur.com/blfaC.png')


def test2():
    import api.download_photo

    api.download_photo.download_photo('https://i.stack.imgur.com/blfaC.png', 'data/photo.jpg')


# test2()
test1()

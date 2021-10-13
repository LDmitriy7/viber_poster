import os


def make_dirs(filepath):
    try:
        os.makedirs(os.path.dirname(filepath))
    except FileExistsError:
        pass

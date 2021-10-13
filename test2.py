import subprocess


def copy_text_to_clipboard(text: str):
    subprocess.run(('xclip', '-selection', 'c'), input=text.encode())


copy_text_to_clipboard(input('text: '))

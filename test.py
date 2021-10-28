from api import copy_to_clipboard

PHOTO_URL = 'https://euni.ru/wp-content/uploads/Test-f-r-medizinische-Studieng-nge-TMS-e1552392249609.jpg'

copy_to_clipboard.copy_text_to_clipboard('тест')
copy_to_clipboard.copy_photo_to_clipboard(PHOTO_URL)

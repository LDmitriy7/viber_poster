import os
import api

photo_url = os.environ['PHOTO_URL']
api.copy_photo_to_clipboard(photo_url)

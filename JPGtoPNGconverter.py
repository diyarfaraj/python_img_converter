import sys
import os
from PIL import Image

fromFolder = sys.argv[1]
newFolder = sys.argv[2]

if not os.path.exists(newFolder):
    os.makedirs(newFolder)


def convert_img(from_path, to_path):
    for filename in os.listdir(from_path):
        img = Image.open(f'{from_path}{filename}')
        new_filename = str(filename)[:-4]
        img.save(f'{to_path}{new_filename}.png', 'png')

convert_img(fromFolder, newFolder)

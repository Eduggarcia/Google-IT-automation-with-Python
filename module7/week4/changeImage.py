#!/usr/bin/env python3

import os, sys
from PIL import Image

user = os.getenv('USER')
image_directory = '/home/{}/supplier-data/images/'.format(user)
for file in os.listdir(image_directory):
  ''' aseguramos que no termine en un punto y que acaba en tiff'''
  if not file.startswith('.') and file.endswith("tiff"):
    im = Image.open(image_directory + file)
    new = im.convert('RGB').resize((600,400))
    new.save(imagen_directory + file, "JPEG")
    new.close()

#!/usr/bin/env python3

import os, requests, json

def process_catalog(url,dir):
   '''inicializamos el diccionario que usaremos para almacenar las caracteristicas
   de los productos'''
    fruit={}
    ''' abrimos todos los archivos de la lista de productos'''
    files = os.listdir(dir)
    for file in files:
      if file.endswith("txt"):
        with open(path + file, 'r') as f:
          #grab the file name, ex. 001, 002 to use for image file
          fruit_name = os.path.splitext(file)[0]
          line = f.read()
          line = line.split("\n")
          fruit = {"name": line[0], "weight": int(line[1].strip(" lbs")), "description": line[2], "image_name": fruit_name + ".jpeg"}
          response = requests.post(url, json=fruit)
          response.raise_for_status()
          print(response.request.url)
          print(response.status_code)

if __name__=='__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    productos = '/home/{}/supplier-data/descriptions/'.format(user)
    process_catalog(url,productos)

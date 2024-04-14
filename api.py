import requests
import json
from red import *

# Almacena una lista con 
def generar_catalogo(libros_api, quantity):
  catalogo = Catalogo()
  for i in range(quantity):
    if (libros_api[i].get("title") is not None):
      titulo = libros_api[i]["title"]
    else:
      continue # No queremos libros sin título

    if (libros_api[i].get("author_name") is not None):
      autores = libros_api[i]["author_name"]
    else:
      continue # No queremos libros sin autor
    
    if (libros_api[i].get("isbn") is not None):
      isbn = libros_api[i]["isbn"][0]
    else:
      continue # No queremos libros sin isbn

    if (libros_api[i].get("subject") is not None):
      generos = libros_api[i]["subject"]
    else:
      continue # No queremos libros sin genero
  libro = Libro(titulo, isbn, generos, autores)
  catalogo.incluir_libro(libro)
  return catalogo



response1 = requests.get("https://openlibrary.org/search.json?q=python")
response2 = requests.get("https://openlibrary.org/search.json?q=java")
response3 = requests.get("https://openlibrary.org/search.json?q=computer")

libros_api_1 = json.loads(response1.text)["docs"]
libros_api_2 = json.loads(response2.text)["docs"]
libros_api_3 = json.loads(response3.text)["docs"]

bib_1 = Biblioteca()
bib_1.catalogo = generar_catalogo(libros_api_1, 15)

bib_2 = Biblioteca()
bib_2.catalogo = generar_catalogo(libros_api_2, 15)

bib_3 = Biblioteca()
bib_3.catalogo = generar_catalogo(libros_api_3, 15)

red = Red()

red.incluir_biblioteca(bib_1)
red.incluir_biblioteca(bib_2)
red.incluir_biblioteca(bib_3)





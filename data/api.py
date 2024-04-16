import requests
import bigjson
import csv
from red import *

 
def generar_catalogo(libros_api, quantity):
  catalogo = Catalogo()
  i = 0
  print(len(libros_api))
  while (i < quantity):
    if (libros_api[i].get("title") is not None):
      titulo = libros_api[i]["title"]
    else:
      titulo = ""

    if (libros_api[i].get("author_name") is not None):
      autores = libros_api[i]["author_name"][0]
    else:
      autores = ""
    
    if (libros_api[i].get("isbn") is not None):
      isbn = libros_api[i]["isbn"][0]
    else:
      isbn = "0"

    if (libros_api[i].get("subject") is not None):
      generos = libros_api[i]["subject"][0]
    else:
      generos = ""

    if (libros_api[i].get("publisher") is not None):
      publisher = libros_api[i]["publisher"][0]
    else:
      publisher = ""

    if (libros_api[i].get("number_of_pages_median") is not None):
      pages = libros_api[i]["number_of_pages_median"]
    else:
      pages = 0

    i += 1

    catalogo.incluir_libro(Libro(titulo, isbn, generos, autores, publisher, pages))
  return catalogo

def api_a_csv(busqueda):
  with open("api.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["title", "author", "genre", "pages", "publisher", "borrow", "user", "deadline"])

    response1 = requests.get("https://openlibrary.org/search.json?q=" + busqueda)
    with open("api.json", "w") as f:
      f.write(response1.text)
    
    with open("api.json", "rb") as f:
      libros_api_1 = bigjson.load(f)["docs"]
      print(libros_api_1)
      print(len(libros_api_1))

    catalogo = generar_catalogo(libros_api_1, 100)
    for i in range(len(catalogo.libros)):
      libro = catalogo.libros[i]
      try:
        writer.writerow([libro.titulo, libro.autores, libro.generos, libro.pages, libro.publisher])
      except UnicodeEncodeError:
        print("Libro sin codificación correcta")
        continue


api_a_csv("java")









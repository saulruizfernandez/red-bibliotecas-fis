# REF: https://docs.python.org/3/library/sqlite3.html
# Requerimientos: instalar sqllite3 (sudo apt install sqlite3)

import sqlite3
import pandas as pd

# Establece una conexión con la base de datos, la crea si no existe
conexion = sqlite3.connect("catalogo.db")
# Cursor para poder ejecutar sentencias SQL
cursor = conexion.cursor()
# Creación de la tabla que almacena el material de la red de bibliotecas
cursor.execute("CREATE TABLE IF NOT EXISTS material(title, author, genre, height, publisher)")
# Importamos el material desde el fichero csv
material_df = pd.read_csv('material_importar.csv')
material_df.to_sql('material', conexion, if_exists='replace')

# Mostramos número de páginas y autor de todas las entradas (PRUEBA)
for row in cursor.execute("SELECT height, title FROM material ORDER BY height"):
    print(row)

# Ejemplo de inserción de datos manualmente
print('-> inserta el título: ')
titulo = input()
print('-> inserta el autor: ')
autor = input()
print('-> inserta el género: ')
genero = input()
print('-> inserta el número de páginas: ')
num_pag = int(input())
print('-> inserta la editorial: ')
editorial = input()
cursor.execute(f"INSERT INTO material(title, author, genre, height, publisher) VALUES (?,?,?,?,?)",
               (titulo, autor, genero, num_pag, editorial))
conexion.commit() # La inserción siempre requiere de hacer un commit

# Buscar una entrada de la base de datos
for row in cursor.execute(f"SELECT * FROM material WHERE title = '{titulo}'"):
  print(row)

conexion.close()
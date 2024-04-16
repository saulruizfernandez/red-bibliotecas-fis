# REF: https://docs.python.org/3/library/sqlite3.html
# Requerimientos: instalar sqllite3 (sudo apt install sqlite3)

import sqlite3
import pandas as pd
import datetime

class Catalogo:
    """Clase que permite gestionar un catálogo de material de la red de bibliotecas.

    Incluye métodos para insertar material en el catálogo, eliminar material y buscar material.

    Attributes:
        db_name (str): Nombre de la base de datos que almacena el catálogo.
        conexion: Conexión a la base de datos.
        cursor: Cursor para ejecutar sentencias SQL.
    """

    def __init__(self, db_name='catalogo.db'):
        self.db_name = db_name
        # Establece una conexión con la base de datos, la crea si no existe
        self.conexion = sqlite3.connect(self.db_name)
        self.cursor = self.conexion.cursor()
        # Creación de la tabla que almacena el material de la red de bibliotecas
        self.cursor.execute("DROP TABLE IF EXISTS material")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS material(title, author, genre, pages, publisher, borrow, user, deadline)")

    def insertar_csv(self, archivo):
        """
        Inserta en la base de datos el contenido de un archivo CSV.
        """
        material_df = pd.read_csv(archivo)
        material_df.to_sql('material', self.conexion, if_exists='replace')

    def insertar_manual(self, titulo, autor, genero, num_pag, editorial):
        """
        Inserta en la base de datos un registro de material de forma manual.
        """
        self.cursor.execute(f"INSERT INTO material(title, author, genre, pages, publisher, borrow, user, deadline) VALUES (?,?,?,?,?, 0, NULL, NULL)",
                            (titulo, autor, genero, num_pag, editorial))
    
    def eliminar(self, campo, valor):
        """
        Eliminar un registro de la base de datos.
        """
        self.cursor.execute(f"DELETE FROM material WHERE {campo} = '{valor}'")

    def buscar(self, campo, valor):
        """
        Busca las entradas de la tabla material que cumplen con el criterio de búsqueda.
        """
        resultados = []
        for row in self.cursor.execute(f"SELECT * FROM material WHERE {campo} = '{valor}'"):
            resultados.append(str(row))

        for resultado in resultados:
            print(resultado)
        return resultados

    def prestar(self, title, usuario):
        """
        Registra el préstamo de un libro.
        """
        self.cursor.execute(f"UPDATE material SET borrow = 1 WHERE title = '{title}'")
        self.cursor.execute(f"UPDATE material SET deadline = '{(datetime.datetime.now() + datetime.timedelta(days=15)).strftime('%Y-%m-%d %H:%M:%S')}' WHERE title = '{title}'")
        self.cursor.execute(f"UPDATE material SET user = '{usuario}' WHERE title = '{title}'")

    def renovar_prestamo(self, title):
        """
        Renueva el préstamo de un libro por 15 días.
        """
        self.cursor.execute(f"UPDATE material SET deadline = '{(datetime.datetime.now() + datetime.timedelta(days=15)).strftime('%Y-%m-%d %H:%M:%S')}' WHERE title = '{title}'")

    def devolver(self, title):
        """
        Registra la devolución de un libro.
        """
        self.cursor.execute(f"UPDATE material SET borrow = 0 WHERE title = '{title}'")
        self.cursor.execute(f"UPDATE material SET deadline = NULL WHERE title = '{title}'")
        self.cursor.execute(f"UPDATE material SET user = NULL WHERE title = '{title}'")

    def __del__(self):
        self.conexion.close()
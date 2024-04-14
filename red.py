# Almacena las bibliotecas que forman una red y permite añadir bibliotecas
class Red:
  bibliotecas: set # Tipo explícito para evitar confusiones
  def __init__(self) -> None:
    pass

  def __init__(self, bibliotecas: list) -> None:
    self.bibliotecas = bibliotecas

  def incluir_biblioteca(self, biblioteca: list) -> None:
    self.bibliotecas.append(biblioteca)




class Libro:
  titulo: str
  isbn: int
  generos: list
  autores: list
  def __init__(self, titulo: str, isbn: int, generos: list, autores: list) -> None:
    self.titulo = titulo
    self.isbn = isbn
    self.generos = generos
    self.autores = autores




class Catalogo:
  libros: list    
  def __init__(self, catalogo=list()) -> None:
    self.libros = catalogo

  def incluir_libro(self, libro: Libro):
    self.libros.append(libro)



class Biblioteca:
  catalogo: Catalogo
  salas: list
  def __init__(self, ubicacion: str, catalogo: Catalogo, salas=list()) -> None:
    self.ubicacion = ubicacion
    self.salas = salas



class Sala:
  def __init__(self, nombre, capacidad) -> None:
    self.nombre = nombre
    self.capacidad = capacidad



class Prestamo:
  def __init__(self, libros, fecha_prestamo) -> None:
    self.libros = libros
    self.fecha_prestamo = fecha_prestamo
    self.fecha_devolucion = None
    self.devuelto = False

  def devolver(self, fecha_devolucion):
    self.fecha_devolucion = fecha_devolucion
    self.devuelto = True
# Almacena las bibliotecas que forman una red y permite añadir bibliotecas
class Red:
  bibliotecas: set # Tipo explícito para evitar confusiones
  def __init__(self) -> None:
    pass

  def __init__(self, bibliotecas: list) -> None:
    self.bibliotecas = bibliotecas

  def incluir_biblioteca(self, biblioteca: list) -> None:
    self.bibliotecas.append(biblioteca)


class Usuario:
  nombre: str
  password: str
  correo: str
  telefono: str
  direccion: str
  def __init__(self, nombre: str, password: str, correo: str, telefono: str,  direccion: str) -> None:
    self.nombre = nombre
    self.password = password
    self.correo = correo
    self.telefono = telefono
    self.direccion = direccion
  
  def save_in_file(self):
    path = "./users/" + self.nombre
    with open(path, "w") as file:
      file.write(self.nombre + "\n")
      file.write(self.password + "\n")
      file.write(self.correo + "\n")
      file.write(self.telefono + "\n")
      file.write(self.direccion + "\n")
  
  def read_from_file(self, id):
    path = "./users/" + str(id)
    with open(path, "r") as file:
      self.nombre = file.readline().strip()
      self.password = file.readline().strip()
      self.correo = file.readline().strip()
      self.telefono = file.readline().strip()
      self.direccion = file.readline().strip()

  def get_info(self):
    info = [self.nombre, self.password, self.correo, self.telefono, self.direccion]
    return info
  
  def change_info(self, info):
    self.nombre = info[0]
    self.password = info[1]
    self.correo = info[2]
    self.telefono = info[3]
    self.direccion = info[4]
    self.save_in_file()



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
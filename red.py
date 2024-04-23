import csv

# Almacena las bibliotecas que forman una red y permite añadir bibliotecas
class Red:
  bibliotecas: set # Tipo explícito para evitar confusiones
  def __init__(self) -> None:
    pass

  def __init__(self, bibliotecas: list=list()) -> None:
    self.bibliotecas = bibliotecas

  def incluir_biblioteca(self, biblioteca: list) -> None:
    self.bibliotecas.append(biblioteca)


class Usuario:
  def __init__(self, name, password, email, phone, location):
    # Check if the user already exist
    self.name = name
    if not self.user_exists(name):
      self.name = name
      self.password = self.encrypt_password(password)
      self.email = email
      self.phone = phone
      self.location = location
    
      # Append the user data to the CSV file
      with open('./config/users.csv', mode='a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([self.name, self.password, self.email, self.phone, self.location])
      
      # Create a new CSV file for the user's reserves
      with open(f'./config/reserves_{self.name}.csv', mode='w', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([self.name, '0','0'])
    else:
      users = []
      with open('./config/users.csv', mode='r', newline='\n') as file:
        reader = csv.reader(file)
        for row in reader:
          users.append(row)
      for user in users:
        if name == user[0]:
          self.password = user[1]
          self.email = user[2]
          self.phone = user[3]
          self.location = user[4]

  def user_exists(self, name):
    # Check if the user exists in the CSV file
    with open('./config/users.csv', mode='r', newline='\n') as file:
      reader = csv.reader(file)
      for row in reader:
        if row[0] == name:
          return True
    return False

  def encrypt_password(self, password):
    encrypted_password = ''
    for char in password:
      if char.isalpha():  # Solo cifra caracteres alfabéticos
        shifted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        encrypted_password += shifted_char
      else:
        encrypted_password += char
    return encrypted_password
  
  def decrypt_password(self, password):
    decrypted_password = ''
    for char in self.password:
      if char.isalpha():  # Solo descifra caracteres alfabéticos
        shifted_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
        decrypted_password += shifted_char
      else:
        decrypted_password += char
    return decrypted_password

  def modify_information(self, name=None, password=None, email=None, phone=None, location=None):
    if name:
      self.name = name
    if password:
      self.password = self.encrypt_password(password)
    if email:
      self.email = email
    if phone:
      self.phone = phone
    if location:
      self.location = location
    self.update_csv()

  def get_info(self):
    # Return a list with all attributes except id
    return [self.name, self.password, self.email, self.phone, self.location]

  def update_csv(self):
    # Read all users from the CSV file
    users = []
    with open('./config/users.csv', mode='r', newline='\n') as file:
      reader = csv.reader(file)
      for row in reader:
        users.append(row)

    # Update the information of the current user
    for user in users:
      if user[0] == self.name:
        user[1] = self.password
        user[2] = self.email
        user[3] = self.phone
        user[4] = self.location
        break

    # Write all users back to the CSV file
    with open('./config/users.csv', mode='w', newline='\n') as file:
      writer = csv.writer(file)
      writer.writerows(users)
  
  def get_reserves(self):
    # Read all reserves from the CSV file
    reserves = []
    with open('./config/reserves.csv', mode='r', newline='\n') as file:
      reader = csv.reader(file)
      for row in reader:
        if row[0] == self.name:
          return row
    return reserves
  
  def get_reserves_list(self):
    reserves_list = []
    reserves = self.get_reserves()
    reserves_list.append("Libros:")
    for reserve in reserves[1].split("/"):
      reserves_list.append(reserve)
    reserves_list.append("Salas:")
    for reserve in reserves[2].split("/"):
      reserves_list.append(reserve)
    return reserves_list

  
  def reserve(self, reserve, type):
    # Append the reserve data to the CSV file
    new_info = self.get_reserves()
    if (type == 0):
      if (new_info[1] == '0'):
        new_info[1] = f"{reserve}"
      else:
        new_info[1] += f"/{reserve}"
    else:
      if (new_info[2] == '0'):
        new_info[2] = f"({reserve})"
      else:
        new_info[2] += f"/({reserve})"
    reserves = []
    with open('./config/reserves.csv', mode='r', newline='\n') as file:
      reader = csv.reader(file)
      for row in reader:
        reserves.append(row)

    # Update the information of the current user
    for reser in reserves:
      if reser[0] == self.name:
        reser[1] = new_info[1]
        reser[2] = new_info[2]
        break

    # Write all users back to the CSV file
    with open('./config/reserves.csv', mode='w', newline='\n') as file:
      writer = csv.writer(file)
      writer.writerows(reserves)

def login(username, password):
  # Encrypt the password
  encripted_password = ''
  for char in password:
    if char.isalpha():  # Solo cifra caracteres alfabéticos
      shifted_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
      encripted_password += shifted_char
    else:
      encripted_password += char
  
  # Check if the user exists and the password is correct
  with open('./config/users.csv', mode='r', newline='\n') as file:
    reader = csv.reader(file)
    for row in reader:
      if str(row[0]) == str(username) and str(row[1]) == str(encripted_password):
        return True
  return False



class Libro:
  titulo: str
  isbn: int
  generos: list
  autores: list
  publisher: str
  pages: int
  def __init__(self, titulo: str, isbn: int, generos: list, autores: list, publisher: str, pages: int) -> None:
    self.titulo = titulo
    self.isbn = isbn
    self.generos = generos
    self.autores = autores
    self.publisher = publisher
    self.pages = pages




class Catalogo:
  libros: list    
  def __init__(self, catalogo=list()) -> None:
    self.libros = catalogo

  def incluir_libro(self, libro: Libro):
    self.libros.append(libro)



class Biblioteca:
  catalogo: Catalogo
  salas: list
  def __init__(self, ubicacion: str="", catalogo: Catalogo=Catalogo(), salas=list()) -> None:
    self.ubicacion = ubicacion
    self.catalogo = catalogo
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
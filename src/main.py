from interface import *
from catalogo import Catalogo

if __name__ == "__main__":
  catalogo = Catalogo()
  catalogo.insertar_csv("../data/api.csv")
  catalogo.insertar_manual('El Quijote', 'Miguel de Cervantes', 'Novela', 200, 'Alianza Editorial')
  interface = Interface(catalogo)
  interface.mainloop()
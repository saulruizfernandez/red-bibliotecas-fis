from interface import *
from catalogo import Catalogo

if __name__ == "__main__":
  catalogo = Catalogo()
  interface = Interface(catalogo)
  interface.mainloop()
from catalogo import Catalogo

catalogo = Catalogo()
# catalogo.insertar_csv('material_importar.csv')
catalogo.insertar_manual('El Quijote', 'Miguel de Cervantes', 'Novela', 200, 'Alianza Editorial')
catalogo.buscar('author', 'Miguel de Cervantes')
catalogo.prestar('El Quijote', 'Juan')
catalogo.buscar('author', 'Miguel de Cervantes')
catalogo.renovar_prestamo('El Quijote')
catalogo.buscar('author', 'Miguel de Cervantes')
catalogo.devolver('El Quijote')
catalogo.eliminar('title', 'El Quijote')
catalogo.buscar('author', 'Miguel de Cervantes')
import tkinter as tk
import datetime
import locale
import os
from red import *

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

contactos = [   [
                    "Nombre:",
                    "Apellidos:",
                    "Correo:"
                ],
                [
                    "Arun",
                    "Daswani Lakhani",
                    "alu0101560410@ull.edu.es" 
                ],
                [
                    "Jean Franco",
                    "Hernandez Garcia",
                    "alu0101538853@ull.edu.es"
                ],
                [
                    "Salvador",
                    "Perez del Pino",
                    "alu0101231426@ull.edu.es"  
                ],
                [
                    "Izan",
                    "Perez Gonzalez",
                    "alu0101543345@ull.edu.es" 
                ],
                [
                    "Saul",
                    "Ruiz Fernandez",
                    "alu0101540917@ull.edu.es"
                ],
                [
                    "Eduardo",
                    "Santander Restrepo",
                    "alu0101565590@ull.edu.es"  
                ],
            ]

class Interface(tk.Tk):
    def __init__(self, catalogo):
        # Definicion de aspectos generales
        super().__init__()
        self.title("App")
        self.geometry("1280x720")
        self.base = tk.Frame(self, bg="white", width=1280, height=720)
        self.base.pack(fill="both", expand=True)  # Empaquetar el Frame base para que ocupe todo el espacio de la ventana
        self.iniciar_sesion_layout()  # Llamar al método para mostrar la interfaz de inicio de sesión
        self.actual_user = None  # Variable para almacenar el usuario actual
        self.actual_user_data = None  # Variable para almacenar los datos del usuario actual
        self.user_reserves = None  # Variable para almacenar las reservas del usuario actual
        self.catalogo = catalogo  # Variable para almacenar el catálogo de la biblioteca


    # Método para limpiar la ventana
    def limpiar(self, frame=None):
        if (frame == None):
            for widget in self.base.winfo_children():
                widget.destroy()
        else:
            for widget in frame.winfo_children():
                widget.destroy()


    # Método para crear un nuevo usuario
    def crear_usuario(self, nombre, password, confirmar_password, correo, telefono, direccion):
        if (password == confirmar_password and len(password) > 0 and len(nombre) > 0 and len(correo) > 0 and len(telefono) > 0 and len(direccion) > 0 and not os.path.exists(f"./users/{nombre}")):
            self.actual_user = Usuario(nombre, password, correo, telefono, direccion)
            # self.actual_user.save_in_file()
            self.actual_user_data = self.actual_user.get_info()
            self.perfil_layout()
        else:
            popup = tk.Toplevel()
            popup.title("Error")
    
            # Dimensiones del popup
            popup.geometry("300x150")

            # Añadir padding para que el contenido no esté unido al borde
            popup.grid_columnconfigure(0, weight=1)
            popup.grid_rowconfigure(0, weight=1)
            popup.grid_rowconfigure(2, weight=1)

            # Etiqueta con el mensaje de error
            mensaje_label = tk.Label(popup, text="Error en la creación de usuario")
            mensaje_label.grid(row=1, column=0, padx=20, pady=20)

            # Botón de cerrar
            cerrar_boton = tk.Button(popup, text="Cerrar", command=popup.destroy)
            cerrar_boton.grid(row=3, column=0, padx=20, pady=20)


    def change_info(self, info):
        self.actual_user.modify_information(info[0], info[1], info[2], info[3], info[4])
        self.actual_user_data = self.actual_user.get_info()
        self.perfil_layout()


    # Método para iniciar sesión
    def iniciar_sesion(self, nombre, password):
        fallo = login(nombre, password)        
        if (not fallo):
            popup = tk.Toplevel()
            popup.title("Error")

            # Dimensiones del popup
            popup.geometry("300x150")

            # Añadir padding para que el contenido no esté unido al borde
            popup.grid_columnconfigure(0, weight=1)
            popup.grid_rowconfigure(0, weight=1)
            popup.grid_rowconfigure(2, weight=1)

            # Etiqueta con el mensaje de error
            mensaje_label = tk.Label(popup, text="Error en el inicio de sesión")
            mensaje_label.grid(row=1, column=0, padx=20, pady=20)

            # Botón de cerrar
            cerrar_boton = tk.Button(popup, text="Cerrar", command=popup.destroy)
            cerrar_boton.grid(row=3, column=0, padx=20, pady=20)
        else:
            self.actual_user = Usuario(nombre, "", "", "", "")
            self.actual_user_data = self.actual_user.get_info()
            self.perfil_layout()


    # Metodo para crear barra lateral
    def barra_lateral(self, barra):
      boton_perfil = tk.Button(barra, text="Perfil", bg="gray", font=("Helvetica", 12), command=self.perfil_layout, width=15)
      boton_perfil.pack(pady=10, fill="x", side="top", padx=10)

      boton_reservar_libro = tk.Button(barra, text="Reservar libro", bg="gray", font=("Helvetica", 12), command=self.reservar_libro_layout, width=15)
      boton_reservar_libro.pack(pady=10, fill="x", side="top", padx=10)

      boton_reservar_sala = tk.Button(barra, text="Reservar Sala", bg="gray", font=("Helvetica", 12), command=self.reservar_sala_layout, width=15)
      boton_reservar_sala.pack(pady=10, fill="x", side="top", padx=10)

      boton_mis_reservas = tk.Button(barra, text="Mis Reservas", bg="gray", font=("Helvetica", 12), command=self.mis_reservas_layout, width=15)
      boton_mis_reservas.pack(pady=10, fill="x", side="top", padx=10)

      boton_cerrar_sesion = tk.Button(barra, text="Cerrar Sesión", bg="gray", font=("Helvetica", 12), command=self.cerrar_sesion, width=15)
      boton_cerrar_sesion.pack(pady=10, fill="x", side="bottom", padx=10)

      boton_contacto = tk.Button(barra, text="Contacto", bg="gray", font=("Helvetica", 12), command=self.contacto_layout, width=15)
      boton_contacto.pack(pady=10, fill="x", side="bottom", padx=10)


    def mostrar_horas(self, dia, frame_horas):
        self.limpiar(frame_horas)
        # Label de horas
        label_horas = tk.Label(frame_horas, text=f"Horas para el día {get_day(dia)}:", font=("Helvetica", 12), bg="white")
        label_horas.grid(row=0, column=0, pady=10, padx=10)

        # Frame de botones de horas
        frame_botones_horas = tk.Frame(frame_horas, bg="white")
        frame_botones_horas.grid(row=1, column=0, pady=10)
        frame_botones_horas.grid_columnconfigure((0,1,2,3,4), weight=1)

        # Botones de horas
        for i in range(3):
            for j in range(5):
                boton_hora = tk.Button(frame_botones_horas, text=f"{(i*5)+7+j}:00", bg="white", font=("Helvetica", 12), width=4)
                boton_hora.grid(row=i, column=j, padx=10, pady=10)
                boton_hora.config(command=lambda b=boton_hora: (b.config(state=tk.DISABLED)))


    # Método para mostrar la interfaz de inicio de sesión
    def iniciar_sesion_layout(self):
        self.limpiar()
        # Crear el marco para el contenido principal
        marco_contenido = tk.Frame(self.base, bg="white")  # No necesitas especificar el ancho, el Frame se ajustará automáticamente
        marco_contenido.pack(side="right", fill="both", expand=True)  # Expandir el Frame para que ocupe el espacio disponible

        # Crear el título
        titulo = tk.Label(marco_contenido, text="Inicio de Sesión", font=("Helvetica", 24), bg="white")
        titulo.pack(pady=50)

        # Crear el label y la entrada para el usuario
        label_usuario = tk.Label(marco_contenido, text="Usuario:", font=("Helvetica", 14), bg="white")
        label_usuario.pack(pady=20)
        entry_usuario = tk.Entry(marco_contenido, font=("Helvetica", 14), justify="center")
        entry_usuario.pack(pady=25)

        # Crear el label y la entrada para la contraseña
        label_contrasena = tk.Label(marco_contenido, text="Contraseña:", font=("Helvetica", 14), bg="white")
        label_contrasena.pack(pady=20)
        entry_contrasena = tk.Entry(marco_contenido, show="*", font=("Helvetica", 14), justify="center")
        entry_contrasena.pack(pady=25)

        # Crear el texto de no tienes cuenta
        texto_no_tienes_cuenta = tk.Label(marco_contenido, text="¿No tienes cuenta?", font=("Helvetica", 14), bg="white", cursor="hand2", fg="gray")
        texto_no_tienes_cuenta.pack(pady=20)
        texto_no_tienes_cuenta.bind("<Button-1>", lambda e: self.registro_layout())

        # Crear el botón de iniciar sesión
        boton_iniciar_sesion = tk.Button(marco_contenido, text="Iniciar Sesión", bg="white", font=("Helvetica", 14), command=lambda: self.iniciar_sesion(entry_usuario.get(), entry_contrasena.get()))
        boton_iniciar_sesion.pack(pady=25)


    # Método para mostrar la interfaz de registro
    def registro_layout(self):
        self.limpiar()
        marco_contenido = tk.Frame(self.base, bg="white")  # No necesitas especificar el ancho, el Frame se ajustará automáticamente
        marco_contenido.pack(side="right", fill="both", expand=True)  # Expandir el Frame para que ocupe el espacio disponible
        marco_contenido.grid_rowconfigure((1), weight=1)  # Ajustar la columna 0 del grid con grid_columnconfigure
        marco_contenido.grid_columnconfigure(0, weight=1)  # Ajustar la fila 0 del grid con grid_rowconfigure

        marco_titulo = tk.Frame(marco_contenido, bg="white")
        marco_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")

        marco_formulario = tk.Frame(marco_contenido, bg="white")
        marco_formulario.grid(row=1, column=0, columnspan=2, sticky="nsew")
        marco_formulario.grid_columnconfigure((0,1), weight=1)  # Ajustar la columna 0 del grid con grid_columnconfigure
        marco_formulario.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)  # Ajustar la fila 0 del grid con grid_rowconfigure

        # Crear el título
        titulo = tk.Label(marco_titulo, text="Registrarse", font=("Helvetica", 24), bg="white")
        titulo.pack(pady=50)

        # Crear el label y la entrada para el nuevo usuario
        label_nuevo_usuario = tk.Label(marco_formulario, text="Nombre usuario:", font=("Helvetica", 12), bg="white")
        label_nuevo_usuario.grid(row=0, column=0, pady=10)
        entry_nuevo_usuario = tk.Entry(marco_formulario, font=("Helvetica", 12), justify="center", )
        entry_nuevo_usuario.grid(row=0, column=1, pady=15)

        # Crear el label y la entrada para la nueva contraseña
        label_nueva_contrasena = tk.Label(marco_formulario, text="Contraseña:", font=("Helvetica", 12), bg="white")
        label_nueva_contrasena.grid(row=1, column=0, pady=10)
        entry_nueva_contrasena = tk.Entry(marco_formulario, show="*", font=("Helvetica", 12), justify="center")
        entry_nueva_contrasena.grid(row=1, column=1, pady=15)

        # Crear el label y la entrada para la confirmación de la nueva contraseña
        label_confirmar_contrasena = tk.Label(marco_formulario, text="Confirmar contraseña:", font=("Helvetica", 12), bg="white")
        label_confirmar_contrasena.grid(row=2, column=0, pady=10)
        entry_confirmar_contrasena = tk.Entry(marco_formulario, show="*", font=("Helvetica", 12), justify="center")
        entry_confirmar_contrasena.grid(row=2, column=1, pady=15)

        # Label correo
        label_correo = tk.Label(marco_formulario, text="Correo:", font=("Helvetica", 12), bg="white")
        label_correo.grid(row=3, column=0, pady=10)
        entry_correo = tk.Entry(marco_formulario, font=("Helvetica", 12), justify="center")
        entry_correo.grid(row=3, column=1, pady=15)

        # Label teléfono
        label_telefono = tk.Label(marco_formulario, text="Teléfono:", font=("Helvetica", 12), bg="white")
        label_telefono.grid(row=4, column=0, pady=10)
        entry_telefono = tk.Entry(marco_formulario, font=("Helvetica", 12), justify="center")
        entry_telefono.grid(row=4, column=1, pady=15)

        # Label domicilio
        label_domicilio = tk.Label(marco_formulario, text="Domicilio:", font=("Helvetica", 12), bg="white")
        label_domicilio.grid(row=5, column=0, pady=10)
        entry_domicilio = tk.Entry(marco_formulario, font=("Helvetica", 12), justify="center")
        entry_domicilio.grid(row=5, column=1, pady=15)

        # Crear el texto de ya tienes cuenta
        texto_tienes_cuenta = tk.Label(marco_formulario, text="¿Ya tienes cuenta?", font=("Helvetica", 12), bg="white", cursor="hand2", fg="gray")
        texto_tienes_cuenta.grid(row=6, column=1, pady=10)
        texto_tienes_cuenta.bind("<Button-1>", lambda e: self.iniciar_sesion_layout())

        # Crear el botón de registrar
        boton_registrar = tk.Button(marco_formulario, text="Registrar", bg="white", font=("Helvetica", 12), command= lambda: self.crear_usuario(
            entry_nuevo_usuario.get(),
            entry_nueva_contrasena.get(),
            entry_confirmar_contrasena.get(),
            entry_correo.get(),
            entry_telefono.get(),
            entry_domicilio.get()
        ))
        boton_registrar.grid(row=7, column=1, pady=15)


  # Metodo para mostrar la interfaz del perfil
    def perfil_layout(self):
        self.limpiar()
        marco_contenido = tk.Frame(self.base, bg="white")  # No necesitas especificar el ancho, el Frame se ajustará automáticamente
        marco_contenido.pack(side="right", fill="both", expand=True)  # Expandir el Frame para que ocupe el espacio disponible
        marco_contenido.grid_rowconfigure((1), weight=1)  # Ajustar la columna 0 del grid con grid_columnconfigure
        marco_contenido.grid_columnconfigure(0, weight=1)  # Ajustar la fila 0 del grid con grid_rowconfigure

        marco_titulo = tk.Frame(marco_contenido, bg="white")
        marco_titulo.grid(row=0, column=0, columnspan=2, sticky="nsew")

        marco_formulario = tk.Frame(marco_contenido, bg="white")
        marco_formulario.grid(row=1, column=0, columnspan=2, sticky="nsew")
        marco_formulario.grid_columnconfigure((0,1), weight=1)  # Ajustar la columna 0 del grid con grid_columnconfigure
        marco_formulario.grid_rowconfigure((0,1,2,3,4,5), weight=1)  # Ajustar la fila 0 del grid con grid_rowconfigure
        
        # Crear el marco para la barra lateral
        marco_barra_lateral = tk.Frame(self.base, bg="gray", width=200)
        marco_barra_lateral.pack(side="left", fill="y", expand=False)

        # Botones barra lateral
        self.barra_lateral(marco_barra_lateral)

        # Crear el título
        titulo = tk.Label(marco_titulo, text="Perfil", font=("Helvetica", 24), bg="white")
        titulo.pack(pady=50)

        # Crear el label y la entrada para el nuevo usuario
        label_usuario = tk.Label(marco_formulario, text="Nombre usuario:", font=("Helvetica", 12), bg="white")
        label_usuario.grid(row=0, column=0, pady=10)
        entry_usuario = tk.Entry(marco_formulario, font=("Helvetica", 12), justify="center")
        entry_usuario.grid(row=0, column=1, pady=15)
        entry_usuario.insert(0, self.actual_user_data[0])

        # Crear el label y la entrada para la nueva contraseña
        label_contrasena = tk.Label(marco_formulario, text="Contraseña:", font=("Helvetica", 12), bg="white")
        label_contrasena.grid(row=1, column=0, pady=10)
        entry_contrasena = tk.Entry(marco_formulario, show="*", font=("Helvetica", 12), justify="center")
        entry_contrasena.grid(row=1, column=1, pady=15)
        entry_contrasena.insert(0, self.actual_user.decrypt_password(self.actual_user_data[1]))

        # Label correo
        label_correo = tk.Label(marco_formulario, text="Correo:", font=("Helvetica", 12), bg="white")
        label_correo.grid(row=2, column=0, pady=10)
        entry_correo = tk.Entry(marco_formulario, font=("Helvetica", 12), justify="center")
        entry_correo.grid(row=2, column=1, pady=15)
        entry_correo.insert(0, self.actual_user_data[2])

        # Label teléfono
        label_telefono = tk.Label(marco_formulario, text="Teléfono:", font=("Helvetica", 12), bg="white")
        label_telefono.grid(row=3, column=0, pady=10)
        entry_telefono = tk.Entry(marco_formulario, font=("Helvetica", 12), justify="center")
        entry_telefono.grid(row=3, column=1, pady=15)
        entry_telefono.insert(0, self.actual_user_data[3])

        # Label domicilio
        label_domicilio = tk.Label(marco_formulario, text="Domicilio:", font=("Helvetica", 12), bg="white")
        label_domicilio.grid(row=4, column=0, pady=10)
        entry_domicilio = tk.Entry(marco_formulario, font=("Helvetica", 12), justify="center")
        entry_domicilio.grid(row=4, column=1, pady=15)
        entry_domicilio.insert(0, self.actual_user_data[4])

        # Crear el botón de modificar
        boton_registrar = tk.Button(marco_formulario, text="Guardar cambios", bg="white", font=("Helvetica", 12), command= lambda: self.change_info(
            [entry_usuario.get(),
            entry_contrasena.get(),
            entry_correo.get(),
            entry_telefono.get(),
            entry_domicilio.get()]
        ))
        boton_registrar.grid(row=5, column=1, pady=15)
















    def reservar_sala_layout(self):
        self.limpiar()
        marco_contenido = tk.Frame(self.base, bg="white")
        marco_contenido.pack(side="right", fill="both", expand=True)

        barra_lat = tk.Frame(self.base, bg="gray", width=200)
        barra_lat.pack(side="left", fill="y", expand=False)
        self.barra_lateral(barra_lat)

        marco_contenido.grid_rowconfigure((1,2), weight=1)  # Ajustar la columna 0 del grid con grid_columnconfigure
        marco_contenido.grid_columnconfigure(0, weight=1)  # Ajustar la fila 0 del grid con grid_rowconfigure

        # Crear el título
        titulo = tk.Label(marco_contenido, text="Reservar sala", font=("Helvetica", 24), bg="white")
        titulo.grid(row=0, column=0, pady=50)

        # Frame de dias
        frame_dias = tk.Frame(marco_contenido, bg="white")
        frame_dias.grid(row=1, column=0, sticky="nsew")
        frame_dias.grid_columnconfigure(0, weight=1)

        # Label de días
        label_dias = tk.Label(frame_dias, text="Días:", font=("Helvetica", 12), bg="white")
        label_dias.grid(row=0, column=0, pady=10, padx=10)

        # Frame de botones de días
        frame_botones_dias = tk.Frame(frame_dias, bg="white")
        frame_botones_dias.grid(row=1, column=0, pady=10)
        frame_botones_dias.grid_columnconfigure((0,1,2,3,4), weight=1)

        # Frame de horas
        frame_horas = tk.Frame(marco_contenido, bg="white")
        frame_horas.grid(row=2, column=0, sticky="nsew")
        frame_horas.grid_columnconfigure(0, weight=1)

        # Botones de días
        for i in range(2):
            for j in range(5):
                day = (i*5)+j
                boton_dia = tk.Button(frame_botones_dias, text=f"{get_day(day)}", bg="white", font=("Helvetica", 12), width=4, command=lambda day=day: self.mostrar_horas(day, frame_horas))
                boton_dia.grid(row=i, column=j, padx=10, pady=10)
        


        

















    def reservar_libro_layout(self):
        self.limpiar()
        marco_contenido = tk.Frame(self.base, bg="white")
        marco_contenido.pack(side="right", fill="both", expand=True)

        barra_lat = tk.Frame(self.base, bg="gray", width=200)
        barra_lat.pack(side="left", fill="y", expand=False)
        self.barra_lateral(barra_lat)

        marco_contenido.grid_rowconfigure((1), weight=1)  # Ajustar la columna 0 del grid con grid_columnconfigure
        marco_contenido.grid_columnconfigure(0, weight=1)  # Ajustar la fila 0 del grid con grid_rowconfigure

        # Crear el título
        titulo = tk.Label(marco_contenido, text="Reservar libro", font=("Helvetica", 24), bg="white")
        titulo.grid(row=0, column=0, pady=50)

        # Frame de contenido
        frame_contenido = tk.Frame(marco_contenido, bg="white")
        frame_contenido.grid(row=1, column=0, sticky="nsew")
        frame_contenido.grid_rowconfigure(1, weight=1)  # Ajustar la columna 0 del grid con grid_columnconfigure
        frame_contenido.grid_columnconfigure(0, weight=1)  # Ajustar la fila 0 del grid con grid_rowconfigure

        # Frame de búsqueda
        frame_busqueda = tk.Frame(frame_contenido, bg="white")
        frame_busqueda.grid(row=0, column=0, sticky="nsew")
        frame_busqueda.columnconfigure(1, weight=1)
        frame_busqueda.rowconfigure(0, weight=1)

        # Label de búsqueda
        label_busqueda = tk.Label(frame_busqueda, text="Buscar libro:", font=("Helvetica", 12), bg="white")
        label_busqueda.grid(row=0, column=0, pady=10, padx=10)

        # Entry de búsqueda
        entry_busqueda = tk.Entry(frame_busqueda, font=("Helvetica", 12), justify="left")
        entry_busqueda.grid(row=0, column=1, pady=10, sticky="ew")

        # Botón de búsqueda
        boton_busqueda = tk.Button(frame_busqueda, text="Buscar", bg="white", font=("Helvetica", 12))
        boton_busqueda.grid(row=0, column=2, pady=10, padx=10)

        # Frame de resultados
        frame_resultados = tk.Frame(frame_contenido, bg="white")
        frame_resultados.grid(row=1, column=0, sticky="nsew")
        
        # Scrollbar resultados
        scrollbar = tk.Scrollbar(frame_resultados)
        scrollbar.pack(side="right", fill="y" ,padx=(0,20),pady=10)

        listbox = tk.Listbox(frame_resultados, yscrollcommand=scrollbar.set, selectmode="single", font=("Helvetica", 12))
        for libros in self.catalogo.buscar("title", str(entry_busqueda.get())):
            listbox.insert("end", libros)
        listbox.pack(side="left", fill="both",expand=True,padx=10, pady=2)
        scrollbar.config(command=listbox.yview)

        # Función para mostrar el libro seleccionado
        listbox.bind("<Button-1>", lambda e: entry_libro_seleccionado.delete(0, "end") or entry_libro_seleccionado.insert(0, listbox.get(listbox.curselection() or 0)))
        
        # Frame reservar
        frame_reservar = tk.Frame(frame_contenido, bg="white")
        frame_reservar.grid(row=2, column=0, sticky="nsew")
        frame_reservar.columnconfigure(0, weight=1)

        # Entry libro seleccionado
        entry_libro_seleccionado = tk.Entry(frame_reservar, font=("Helvetica", 12), justify="center")
        entry_libro_seleccionado.grid(row=0, column=0, pady=10, sticky="ew", padx=10)
        entry_libro_seleccionado.insert(0, "Libro seleccionado")

        # Botón reservar
        boton_reservar = tk.Button(frame_reservar, text="Reservar", bg="white", font=("Helvetica", 12))
        boton_reservar.grid(row=0, column=1, pady=10, padx=10)
















    def mis_reservas_layout(self):
        self.limpiar()
        marco_contenido = tk.Frame(self.base, bg="white")
        marco_contenido.pack(side="right", fill="both", expand=True)

        barra_lat = tk.Frame(self.base, bg="gray", width=200)
        barra_lat.pack(side="left", fill="y", expand=False)
        self.barra_lateral(barra_lat)

        # Frame de contenido
        frame_contenido = tk.Frame(marco_contenido, bg="white")
        frame_contenido.pack(fill="both", expand=True)
        frame_contenido.grid_rowconfigure((1), weight=1)
        frame_contenido.grid_columnconfigure(0, weight=1)  

        # Crear el título
        titulo = tk.Label(frame_contenido, text="Mis reservas", font=("Helvetica", 24), bg="white")
        titulo.grid(row=0, column=0, pady=50)

        frame_resultados = tk.Frame(frame_contenido, bg="white")
        frame_resultados.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Scrollbar resultados
        scrollbar = tk.Scrollbar(frame_resultados)
        scrollbar.pack(side="right", fill="y" ,padx=(0,20),pady=10)

        listbox = tk.Listbox(frame_resultados, yscrollcommand=scrollbar.set, selectmode="single", font=("Helvetica", 12))
        for i in range(10):
            listbox.insert("end", f"  Pedido {i}",)
        listbox.pack(side="left", fill="both",expand=True,padx=10, pady=2)
        scrollbar.config(command=listbox.yview)

        # Función para mostrar el reserva seleccionado
        listbox.bind("<Button-1>", lambda e: entry_reserva_seleccionado.delete(0, "end") or entry_reserva_seleccionado.insert(0, listbox.get(listbox.curselection() or 0)))
        
        # Frame reservar
        frame_cancelar_reserva = tk.Frame(frame_contenido, bg="white")
        frame_cancelar_reserva.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        frame_cancelar_reserva.columnconfigure(0, weight=1)

        # Entry reserva seleccionado
        entry_reserva_seleccionado = tk.Entry(frame_cancelar_reserva, font=("Helvetica", 12), justify="center")
        entry_reserva_seleccionado.grid(row=0, column=0, pady=10, sticky="ew", padx=10)
        entry_reserva_seleccionado.insert(0, "Reserva seleccionado")

        # Botón cancelar
        boton_reservar = tk.Button(frame_cancelar_reserva, text="Cancelar reserva", bg="white", font=("Helvetica", 12))
        boton_reservar.grid(row=0, column=1, pady=10, padx=10)





















    def contacto_layout(self):
        self.limpiar()
        marco_contenido = tk.Frame(self.base, bg="white")
        marco_contenido.pack(side="right", fill="both", expand=True)

        barra_lat = tk.Frame(self.base, bg="gray", width=200)
        barra_lat.pack(side="left", fill="y", expand=False)
        self.barra_lateral(barra_lat)

        # Titulo
        titulo = tk.Label(marco_contenido, text="Contacto", font=("Helvetica", 24), bg="white")
        titulo.pack(pady=50)

        # Frame de contactos
        frame_contenido = tk.Frame(marco_contenido, bg="white")
        frame_contenido.pack(fill="both", expand=True)
        frame_contenido.grid_columnconfigure((0,1, 2), weight=1)

        for i in range(len(contactos)):
            label_nombre = tk.Label(frame_contenido, text=contactos[i][0], font=("Helvetica", 12), bg="white")
            label_nombre.grid(row=i, column=0, pady=10, padx=10)

            label_apellidos = tk.Label(frame_contenido, text=contactos[i][1], font=("Helvetica", 12), bg="white")
            label_apellidos.grid(row=i, column=1, pady=10, padx=10)

            label_correo = tk.Label(frame_contenido, text=contactos[i][2], font=("Helvetica", 12), bg="white")
            label_correo.grid(row=i, column=2, pady=10, padx=10)


    def cerrar_sesion(self):
        self.limpiar()
        self.iniciar_sesion_layout()
        self.actual_user = None
        self.actual_user_data = None
        self.user_reserves = None














def get_day(add_days):
    return (datetime.date.today() + datetime.timedelta(days=add_days)).strftime("%a %d")





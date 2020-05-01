from tkinter import * # Python cuenta con varias librerias/bibliotecas gráficas, pero nosotros usaremos Tkinter.
                      # Este import es obligatorio para el uso de esta
from PIL import Image, ImageTk # Necesitamos la librera/biblioteca PIL (Python Imaging Library) para poder redimensionar las imágenes, entre otras funciones

raiz = Tk() # Llamada a la clase "Tk", necesaria para trabajar con interfaces
raiz.title("Prueba básica Interface") # Le asignamos un nombre a la ventana
raiz.resizable(False, False) # Método con dos variables boolean (Height/Width) con las que activar o no el redimensionado de la ventana
raiz.geometry("500x500") # Método que nos permite establecer el tamaño inicial de la ventana
raiz.config(bg="black") # Método que nos permite cambiar el color de la ventana (entre otras cosas)
icono = PhotoImage(file="gallo.png") # Con estos dos comandos establecemos un icono para la ventana. PhotoImage solo permite los formatos .png y .gif.
raiz.tk.call('wm', 'iconphoto', raiz._w, icono)

miFrame = Frame(raiz) # Los Frames son lienzos que se aplican sobre nuestra ventana y nos permiten trabajar con widgets
miFrame.config(bg="red") # Asignamos color de fondo al Frame
miFrame.config(relief="sunken") # Con este método, añadimos un borde de estilo "sunken"
miFrame.config(bd=35) # Le damos un grosor de 35 al borde
miFrame.config(cursor="pirate") # Con este método, modificamos el estilo del cursor dentro del frame
miFrame.pack(fill="both", expand="True") # Con este método, enlazamos el frame con la ventana (sin él, ambos objetos quedan flotando por separado) y hacemos que este ocupe toda la ventana

miLabel = Label(miFrame, text="Hola, ¿qué tal?") # Los Labels son widgets con los que podemos mostrar texto estático e imágenes
miLabel.place(x=165, y=320) # A los Labels hay que asignarles un lugar concreto o si no, no aparecerán en el Frame
miLabel.config(fg="white", bg="black", font="50") # Asignamos un color de fuente blanco, un fondo negro y un tamaño de fuente de 50 al Label

img = Image.open("rosa.png") # Creamos un widget Image a partir de la biblioteca PIL
img = img.resize((180, 180), Image.ANTIALIAS) # Redimensionamos la imagen (solo los widgets Image de PIL pueden redimensionarse, las PhotoImage de Tkinter, no)
miImagen = ImageTk.PhotoImage(img) # Convertimos nuestra Image en PhotoImage para poder insertarla en un Label
miLabelImagen = Label(miFrame, image=miImagen) # Usamos un Label para mostrar la imagen
miLabelImagen.place(x=135, y=80) # Asignamos la posición del nuevo Label
miLabelImagen.config(bg="red") # Le añadimos un fondo del mismo color que el Frame al Label

raiz.mainloop() # Método necesario porque una ventana para estar en ejecución, debe estar dentro de un bucle infinito.
                # Es muy importante que siempre esté al final
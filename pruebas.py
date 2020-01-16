import math # Para poder hallar la raíz cuadrada de un número, es necesario que importemos la clase "math", para así usar la función "sqrt"

# Funciones
def evaluacionNota():
	numero = input("\nIntroduce una nota:\n")
	print()
	try:
		if int(numero) == 0:
			print("¡A recuperar!")
		elif int(numero) >= 1 and int(numero) <= 4:
			print("Suspendido")
		elif int(numero) == 5:
			print("Justito")
		elif int(numero) >=6 and int(numero) <= 9:
			print("Aprobado")
		elif int(numero) == 10:
			print("¡Matrícula!")
		else:
			print("Nota no válida.")	
	except ValueError: # Si el valor introducido no es un número, actúa el catch
		print("\n¡El valor introducido no es un número!")

def convertirListaCompraTupla(listaCompra):
	if(len(listaCompra) == 0):
		print("\nLa lista de la compra está vacía, llénala con la opción 2.")
		return listaCompra
	else:	
		if isinstance(listaCompra, list):
			print("\n¡listaCompra convertida en tupla!")
			return tuple(listaCompra)
		else:
			print("\n¡listaCompra ya es una tupla!")
			return listaCompra

def convertirListaCompraLista(listaCompra):
	if(len(listaCompra) == 0):
		print("\nLa lista de la compra está vacía, llénala con la opción 2.")
		return listaCompra
	else:	
		if isinstance(listaCompra, tuple):			
			print("\n¡listaCompra convertida en lista!")
			return list(listaCompra)
		else:
			print("\n¡listaCompra ya es una lista!")
			return listaCompra

def verListaCompra(listaCompra):
	if(len(listaCompra) == 0):
		print("\nLa lista de la compra está vacía, llénala con la opción 2.")
	else:
		if(isinstance(listaCompra, list)):			
			for x in range(len(listaCompra)):
				print(f"{x+1} - {listaCompra[x]}")
			print("\nlistaCompra es una lista.")
		
		elif(isinstance(listaCompra, tuple)):
			print(listaCompra)
			print("\nlistaCompra es una tupla.")

def crearListaCompra(listaCompra):
	if len(listaCompra) > 0:
		print("\nLista de la compra ya creada, puedes modificarla usando la función 3.")
		return listaCompra		
	else:		
		tamanyoListaCompra = input("\n¿De qué tamaño será la lista?\n")
			
		try:
			for x in range(int(tamanyoListaCompra)):
				listaCompra.insert(x,input(f"\nIntroduce el producto número {x+1}:\n"))

			print("\nTu lista de la compra es:")
			verListaCompra(listaCompra)

			return listaCompra
		except ValueError:
			print("\n¡El valor introducido no es un número!")
			return listaCompra

def modificarListaCompra(listaCompra):
	if(len(listaCompra) == 0):
		print("\nLa lista de la compra está vacía, llénala con la opción 2.")
		return listaCompra
	else:
		if isinstance(listaCompra, tuple):
			print("\nlistaCompra es una tupla, y las tuplas no pueden modificarse.")
			return listaCompra
		else:
			try:				
				opcionListaCompra = input(
				"\n¿Qué quieres hacer con la lista de la compra?\n"
				"  1) Añadir producto\n"
				"  2) Modificar producto\n"
				"  3) Eliminar producto\n"
				"  4) Eliminar lista entera\n"
				"\nIntroduce tu opción:\n")

				if int(opcionListaCompra) == 1: # Añadir producto					
					listaCompra.append(input("\nAñade el producto:\n"))
					print("\n¡Producto añadido con éxito!")
					print("\nAsí queda ahora la lista:")
					verListaCompra(listaCompra)
					return listaCompra

				elif int(opcionListaCompra) == 2: # Modificar producto
					print()
					verListaCompra(listaCompra)

					try:
						indiceProducto = input("\nIntroduce el índice del producto a modificar:\n")
						indiceProducto = int(indiceProducto) - 1
						productoEncontrado = False

						for x in listaCompra:
							if int(indiceProducto) == int(listaCompra.index(x)):
								productoEncontrado = True								
								print(f"\nHas seleccionado el producto: {x}")
								listaCompra[int(indiceProducto)] = input("\nIntroduce su nuevo nombre:\n")
								print("\n¡Producto modificado con éxito!")
								return listaCompra
						
						if(productoEncontrado == False):
							print("\nNo existe ningún producto con ese índice.")
						
						productoEncontrado = False
					except ValueError:
						print("\n¡El índice es un número!")
						return listaCompra

				elif int(opcionListaCompra) == 3: # Eliminar producto
					verListaCompra(listaCompra)					

					try:
						indiceProducto = input("\nIntroduce el índice del producto a eliminar:\n")
						indiceProducto = int(indiceProducto) - 1
						productoEncontrado = False

						for x in listaCompra:
							if int(indiceProducto) == int(listaCompra.index(x)):
								productoEncontrado = True					
								print(f"\nHas seleccionado el producto: {x}")					
								listaCompra.remove(x)
								print("\n¡Producto eliminado con éxito!")
								return listaCompra
						
						if(productoEncontrado == False):
							print("\nNo existe ningún producto con ese índice.")
					except ValueError:
						print("\n¡El índice es un número!")
						return listaCompra

				elif int(opcionListaCompra) == 4: # Eliminar lista entera
					listaCompra.clear()
					print("\n¡Lista eliminada!")
					return listaCompra
			except ValueError:
				print("\n¡Has de introducir un número ligado a una función!")
				return listaCompra

def verDiccionario(diccionario):
	if(len(diccionario) > 0):
		for x in diccionario:
			print("Clave: {}, Valor: {}".format(x,diccionario[x]))
	else:
		print("\nEl diccionario está vacío, llénalo con la opción 7.")


def crearDiccionario(diccionario):
	if(len(diccionario) > 0):
		print("\nEl diccionario ya ha sido creado, puedes modificarlo usando la función 8.")
		return diccionario
	else:
				
		try:
			tamanyoDiccionario = input("\n¿De qué tamaño quieres que sea el diccionario?\n")

			for x in range(int(tamanyoDiccionario)):				
				claveDiccionario = input(f"\nIntroduce la clave de la pareja número {x+1}:\n")
				
				while (claveDiccionario in diccionario) == True:					
					claveDiccionario = input("\n¡Clave repetida! Introduce una distinta:\n")
							
				valorDiccionario = input(f"\nIntroduce el valor de la pareja número {x+1}:\n")

				diccionario[claveDiccionario] = valorDiccionario

			print("\nAsí queda el diccionario:")
			verDiccionario(diccionario)
		except ValueError:
			print("\n¡El valor introducido no es un número!")
		return diccionario

def modificarDiccionario(diccionario):
	if(len(diccionario) == 0):
		print("\nEl diccionario está vacío, llénalo con la opción 7.")
		return diccionario
	else:		
		try:			
			opcionDiccionario = input(
			"\n¿Qué quieres hacer con el diccionario?\n"
			"  1) Añadir clave/valor\n"
			"  2) Modificar clave\n"
			"  3) Modificar valor\n"
			"  4) Eliminar clave/valor\n"
			"  5) Eliminar diccionario entero\n"
			"\nIntroduce tu opción:\n")

			if int(opcionDiccionario) == 1: # Añadir clave/valor
				nuevaClave = input("\nIntroduce la nueva clave:")

				while (nuevaClave in diccionario) == True:										
					nuevaClave = input("\n¡Clave repetida! Introduce una distinta:")
				
				nuevoValor = input("\nIntroduce el nuevo valor:")

				diccionario.update({nuevaClave : nuevoValor})

				print("\n¡Pareja añadida con éxito!")
				print("\nAsí queda ahora el diccionario:")
				verDiccionario(diccionario)
				return diccionario

			elif int(opcionDiccionario) == 2: # Modificar clave
				print()
				verDiccionario(diccionario)
				claveVieja = input("\nIntroduce la clave a modificar:\n")

				while (claveVieja in diccionario) == False:
					claveVieja = input("\n¡La clave introducida no existe! Introduce una distinta:\n")

				claveNueva = input("\nIntroduce la nueva clave:\n")

				while (claveNueva in diccionario) == True:										
					claveNueva = input("\n¡La clave introducida ya existe! Introduce una distinta:\n")
				
				diccionario[claveNueva] = diccionario.pop(claveVieja)
				print("\n¡Clave modificada!")
				print("\nAsí queda ahora el diccionario:")
				verDiccionario(diccionario)
				return diccionario

			elif int(opcionDiccionario) == 3: # Modificar valor
				verDiccionario(diccionario)				
				claveValor = input("\nIntroduce la clave del valor a modificar:\n")

				while (claveValor in diccionario) == False:										
					claveValor = input("\n¡La clave introducida no existe! Introduce una distinta:\n")

				valorNuevo = input("\nIntroduce el nuevo valor:\n")
				diccionario.update({claveValor : valorNuevo})
				
				print("\nAsí queda ahora el diccionario:")
				verDiccionario(diccionario)
				return diccionario

			elif int(opcionDiccionario) == 4: # Eliminar clave/valor
				verDiccionario(diccionario)				
				claveEliminar = input("\nIntroduce la clave de la pareja a eliminar:\n")

				while (claveEliminar in diccionario) == False:										
					claveEliminar = input("\n¡La clave introducida no existe! Introduce una distinta:\n")
				
				del diccionario[claveEliminar]
				print("\n¡Pareja eliminada!")

				print("\nAsí queda ahora el diccionario:")
				verDiccionario(diccionario)
				return diccionario

			elif int(opcionDiccionario) == 5: # Eliminar diccionario entero
				diccionario.clear()
				print("\n¡Diccionado eliminado!")
				return diccionario
		except ValueError:
			print("\n¡Has de introducir un número ligado a una función!")
			return diccionario

def generadorPares(limite):
	num = 1	
	while num <= limite:		
		yield num*2 # En los generadores, el "yield" sustituye al "return", y este a su vez sirve como objeto iterable que almacena valores uno por uno (en este caso actúa de lista, va almacenando los números pares)
		num+= 1 # num++

def generadorCiudadesAnidado(*ciudades): # Al colocar un asterisco frente al argumento, indicamos que este recibirá un número indeterminado de elementos (podríamos enviarle 300 strings/ciudades, por ejemplo)
	for elemento in ciudades:
		yield from elemento # Esto es como si escribiéramos "for subElemento in elemento", es decir, de cada "elemento" (ciudad, string), pillamos su "subelemento" (es decir, el primer caracter). Esto en Java se haría con dos "for", haciendo una matriz

def calcularRaizCuadrada():
	try:
		numeroRaizCuadrada = int(input("\nIntroduce el número del cual quieres calcular la raíz cuadrada: \n"))
		
		if numeroRaizCuadrada < 0:
			raise ValueError("\nNo se puede calcular la raíz cuadrada de un número negativo")
		else:
			print(f"\nLa raíz cuadrada de {numeroRaizCuadrada} es {math.sqrt(numeroRaizCuadrada)}") # Para usar "math.sqrt()" antes hemos de importar la clase "math" (está al principio del archivo)

	except ValueError:
		print("\nNo se puede hacer la raíz cuadrada de una palabra.")	

# Inicio del programa
funcion = 1
tupla = False
listaCompra = []
diccionario = {}
try:
	while int(funcion) != 0:
		funcion = input(
			"INPUT Y CONDICIONES\n"
			"	1) Evaluador de nota (ejemplo input)\n"
			"\nCREACIÓN Y MODIFICACIÓN DE LISTAS/TUPLAS\n"
			"	2) Crear lista de la compra (ejemplo while y lista)\n"
			"	3) Modificar lista de la compra (ejemplo modificación lista)\n"
			"	4) Convertir lista de la compra en tupla (ejemplo tupla)\n"
			"	5) Convertir lista de la compra en lista\n"
			"	6) Ver lista de la compra\n"
			"\nCREACIÓN Y MODIFICACIÓN DE DICCIONARIOS\n"
			"	7) Crear diccionario\n"
			"	8) Modificar diccionario\n"
			"	9) Ver diccionario\n"
			"\nGENERADORES\n"
			"	10) Generador de pares (yield)\n"
			"	11) Generador de ciudades anidado (yield from)\n"
			"\nIMPORTS Y RAISE DE EXCEPCIONES\n"
			"	12) Raíz cuadrada\n"		
			"\n0) Salir del programa\n"
			"\n¿A qué función quieres acceder?\n")

		if int(funcion) == 1:
			evaluacionNota()
		elif int(funcion) == 2:	
			listaCompra = crearListaCompra(listaCompra)
		elif int(funcion) == 3:
			listaCompra = modificarListaCompra(listaCompra)	
		elif int(funcion) == 4:
			listaCompra = convertirListaCompraTupla(listaCompra)
		elif int(funcion) == 5:
			listaCompra = convertirListaCompraLista(listaCompra)
		elif int(funcion) == 6:
			verListaCompra(listaCompra)
		elif int(funcion) == 7:
			diccionario = crearDiccionario(diccionario)		
		elif int(funcion) == 8:
			diccionario = modificarDiccionario(diccionario)
		elif int(funcion) == 9:
			verDiccionario(diccionario)
		elif int(funcion) == 10:
			listaPares = generadorPares(10) # Con esta variable, almacenamos el objeto iterable (yield) que devuelve la función
			print("\nListado total de pares:")
			for i in listaPares: # Como hemos almacenado todos los valores en esta variable, ahora podemos imprimirlos todos por pantalla
				print(i)

			listaPares = generadorPares(10) # Volvemos a llamar a la función porque la variable "listaPares" quedó recorrida con el "for", por lo que ya no podríamos hacer "next()" en ella
			print("\nTres primeros valores (función next()):") # Gracias a la función next() de los generadores, podemos imprimir la lista valor por valor, evitándonos así cargar la lista entera para hacer esto.
			print(next(listaPares)) # Entre llamada y llamada, el generador entra en estado de suspensión (es decir, va metiendo los números en la lista uno a uno, llamada por llamada)
			print(next(listaPares))
			print(next(listaPares))
			
		elif int(funcion) == 11:
			listaCiudades = generadorCiudadesAnidado("Sabadell", "Badia", "Barberà", "Cerdanyola")
			print(next(listaCiudades)) # Con el next hacemos que solo nos imprima los dos primeros caracteres de "Sabadell". Si hiciéramos un "for", se mostrarían todas esas ciudades caracter a caracter en vertical
			print(next(listaCiudades))
			#for i in listaCiudades:
				#print(i)
		
		elif int(funcion) == 12:
			try:
				calcularRaizCuadrada()
			except ValueError as ErrorNumeroNegativo:
				print(ErrorNumeroNegativo)
			except NameError as ErrorNoNumero:
				print(ErrorNoNumero)		

		elif int(funcion) == 0:
			print("\n¡Hasta la próxima!")
		else:
			print("\nEsa función no existe, introduce otra.")

		print()
except ValueError:
	print("\n¡Has de introducir un número ligado a una función!")
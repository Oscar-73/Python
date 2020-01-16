import random

def crearTablero(tablero, columnas, filas):
    for x in range(filas):
        tablero.append([]) # Con esto convertimos a la variable "tablero" en matriz
        for y in range(columnas):
            tablero[x].append("-")
    
    return tablero

def visualizarTablero(tablero, columnas, filas):
    print("\n", end=" ")
    for y in range(columnas):    
        print(f" {y+1}", end=" ")    

    for x in range(filas):
        print()            
        print(x+1, end = " ")
        for y in range(columnas):
            print(tablero[x][y], end = "  ") # Con "end", especificamos que el siguiente print tras este se imprima en la misma línea, no en la siguiente 

def turnoJugador(turno, tablero, columnas, filas):
    visualizarTablero(tablero, columnas, filas)
    
    if(turno == False):
        columna = int(input("\n\n¡Turno del jugador 1!\n\nEscoge la columna:\n"))

        while(columna > columnas or columna <= 0):
            columna = int(input("\n¡Columna fuera de rango!\n\nEscoge otra columna:\n"))

        fila = int(input("\nEscoge la fila:\n"))

        while(fila > filas or fila <= 0):
            fila = int(input("\n¡Fila fuera de rango!\n\nEscoge otra fila:\n"))
        
        if(tablero[fila-1][columna-1] == "X" or tablero[fila-1][columna-1] == "O"):
            print("\n¡Casilla ya ocupada!")
        else: 
            tablero[fila-1][columna-1] = "X"
                
    else:
        columna = int(input("\n\n¡Turno del jugador 2!\n\nEscoge la columna:\n"))

        while(columna > columnas or columna <= 0):
            columna = int(input("\n¡Columna fuera de rango!\n\nEscoge otra columna:\n"))

        fila = int(input("\nEscoge la fila:\n"))

        while(fila > filas or fila <= 0):
            fila = int(input("\n¡Fila fuera de rango!\n\nEscoge otra fila:\n"))
        
        if(tablero[fila-1][columna-1] == "X" or tablero[fila-1][columna-1] == "O"):
            print("\n¡Casilla ya ocupada!")
        else: 
            tablero[fila-1][columna-1] = "O"
                
    return tablero

def maquinaFacil(tablero):
    columna = random.randrange(3)
    fila = random.randrange(3)
                
    if(tablero[fila][columna] == "X" or tablero[fila][columna] == "O"):
        while(tablero[fila][columna] == "X" or tablero[fila][columna] == "O"):
            columna = random.randrange(3)
            fila = random.randrange(3)

    tablero[fila][columna] = "O"

    return tablero

def maquinaFacilJ1(tablero):
    columna = random.randrange(3)
    fila = random.randrange(3)
                
    if(tablero[fila][columna] == "X" or tablero[fila][columna] == "O"):
        while(tablero[fila][columna] == "X" or tablero[fila][columna] == "O"):
            columna = random.randrange(3)
            fila = random.randrange(3)

    tablero[fila][columna] = "X"

    return tablero

def maquinaIntermedia(tablero):
    tipoTurno = random.randrange(1)
    
    if(tipoTurno == 0):
        tablero = maquinaFacil(tablero)
    else:
        # Tres en raya en vertical del J1
        if(tablero[0][0] == 'X' and tablero[1][0] == 'X'):
            if(tablero[2][0] != "O"):
                tablero[2][0] = "O"
            else:
                tablero = maquinaFacil(tablero)
        elif(tablero[0][1] == 'X' and tablero[1][1] == 'X'):
            if(tablero[2][1] != 'O'):
                tablero[2][1] = 'O'
            else:
                tablero = maquinaFacil(tablero)
        elif(tablero[0][2] == 'X' and tablero[1][2] == 'X'):
            if(tablero[2][2] != 'O'):
                tablero[2][2] = 'O'
            else:
                tablero = maquinaFacil(tablero)
        # Tres en raya en horizontal del J1
        elif(tablero[0][0] == 'X' and tablero[0][1] == 'X'):
            if(tablero[0][2] != 'O'):
                tablero[0][2] = 'O'
            else:
                tablero = maquinaFacil(tablero)
        elif(tablero[1][0] == 'X' and tablero[1][1] == 'X'):
            if(tablero[1][2] != 'O'):
                tablero[1][2] = 'O'
            else:
                tablero = maquinaFacil(tablero)
        elif(tablero[2][0] == 'X' and tablero[2][1] == 'X'):
            if(tablero[2][2] != 'O'):
                tablero[2][2] = 'O'
            else:
                tablero = maquinaFacil(tablero)

        # Tres en raya en vertical del J2
        elif(tablero[0][0] == 'O' and tablero[1][0] == 'O'):
            tablero[2][0] = "O"
        elif(tablero[0][1] == 'O' and tablero[1][1] == 'O'):
            tablero[2][1] == 'O'
        elif(tablero[0][2] == 'O' and tablero[1][2] == 'O'):
            tablero[2][2] == 'O'
        # Tres en raya en horizontal del J2
        elif(tablero[0][0] == 'O' and tablero[0][1] == 'O'):
            tablero[0][2] == 'O'
        elif(tablero[1][0] == 'O' and tablero[1][1] == 'O'):
            tablero[1][2] == 'O'
        elif(tablero[2][0] == 'O' and tablero[2][1] == 'O'):
            tablero[2][2] == 'O'
        
        else:
            tablero = maquinaFacil(tablero)

    return tablero

def maquinaIntermediaJ1(tablero):
    tipoTurno = random.randrange(1)
    
    if(tipoTurno == 0):
        tablero = maquinaFacilJ1(tablero)
    else:
        # Tres en raya en vertical del J1
        if(tablero[0][0] == 'O' and tablero[1][0] == 'O'):
            if(tablero[2][0] != 'X'):
                tablero[2][0] = 'X'
            else:
                tablero = maquinaFacil(tablero)
        elif(tablero[0][1] == 'O' and tablero[1][1] == 'O'):
            if(tablero[2][1] != 'X'):
                tablero[2][1] = 'X'
            else:
                tablero = maquinaFacil(tablero)
        elif(tablero[0][2] == 'O' and tablero[1][2] == 'O'):
            if(tablero[2][2] != 'X'):
                tablero[2][2] = 'X'
            else:
                tablero = maquinaFacil(tablero)
        # Tres en raya en horizontal del J1
        elif(tablero[0][0] == 'O' and tablero[0][1] == 'O'):
            if(tablero[0][2] != 'X'):
                tablero[0][2] = 'X'
            else:
                tablero = maquinaFacil(tablero)
        elif(tablero[1][0] == 'O' and tablero[1][1] == 'O'):
            if(tablero[1][2] != 'X'):
                tablero[1][2] = 'X'
            else:
                tablero = maquinaFacil(tablero)
        elif(tablero[2][0] == 'O' and tablero[2][1] == 'O'):
            if(tablero[2][2] != 'X'):
                tablero[2][2] = 'X'
            else:
                tablero = maquinaFacil(tablero)

        # Tres en raya en vertical del J2
        elif(tablero[0][0] == 'X' and tablero[1][0] == 'X'):
            tablero[2][0] = 'X'
        elif(tablero[0][1] == 'X' and tablero[1][1] == 'X'):
            tablero[2][1] == 'X'
        elif(tablero[0][2] == 'X' and tablero[1][2] == 'X'):
            tablero[2][2] == 'X'
        # Tres en raya en horizontal del J2
        elif(tablero[0][0] == 'X' and tablero[0][1] == 'X'):
            tablero[0][2] == 'X'
        elif(tablero[1][0] == 'X' and tablero[1][1] == 'X'):
            tablero[1][2] == 'X'
        elif(tablero[2][0] == 'X' and tablero[2][1] == 'X'):
            tablero[2][2] == 'X'
        
        else:
            tablero = maquinaFacil(tablero)

    return tablero

def maquinaTerminator(tablero):                
    # Tres en raya en vertical del J1
    if(tablero[0][0] == 'X' and tablero[1][0] == 'X'):
        if(tablero[2][0] != "O"):
            tablero[2][0] = "O"
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[0][1] == 'X' and tablero[1][1] == 'X'):
        if(tablero[2][1] != 'O'):
            tablero[2][1] = 'O'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[0][2] == 'X' and tablero[1][2] == 'X'):
        if(tablero[2][2] != 'O'):
            tablero[2][2] = 'O'
        else:
            tablero = maquinaFacil(tablero)
    # Tres en raya en horizontal del J1
    elif(tablero[0][0] == 'X' and tablero[0][1] == 'X'):
        if(tablero[0][2] != 'O'):
            tablero[0][2] = 'O'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[1][0] == 'X' and tablero[1][1] == 'X'):
        if(tablero[1][2] != 'O'):
            tablero[1][2] = 'O'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[2][0] == 'X' and tablero[2][1] == 'X'):
        if(tablero[2][2] != 'O'):
            tablero[2][2] = 'O'
        else:
            tablero = maquinaFacil(tablero)
    # Tres en raya en diagonal del J1
    elif(tablero[0][0] == 'X' and tablero[1][1] == 'X'):
        if(tablero[2][2] != 'O'):
            tablero[2][2] = 'O'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[2][0] == 'X' and tablero[1][1] == 'X'):
        if(tablero[0][2] != 'O'):
            tablero[0][2] = 'O'
        else:
            tablero = maquinaFacil(tablero)

    # Tres en raya en vertical del J2
    elif(tablero[0][0] == 'O' and tablero[1][0] == 'O'):
        tablero[2][0] = 'O'
    elif(tablero[0][1] == 'O' and tablero[1][1] == 'O'):
        tablero[2][1] == 'O'
    elif(tablero[0][2] == 'O' and tablero[1][2] == 'O'):
        tablero[2][2] == 'O'
    # Tres en raya en horizontal del J2
    elif(tablero[0][0] == 'O' and tablero[0][1] == 'O'):
        tablero[0][2] == 'O'
    elif(tablero[1][0] == 'O' and tablero[1][1] == 'O'):
        tablero[1][2] == 'O'
    elif(tablero[2][0] == 'O' and tablero[2][1] == 'O'):
        tablero[2][2] == 'O'
    # Tres en raya en diagonal del J2
    elif(tablero[0][0] == 'O' and tablero[1][1] == 'O'):
        tablero[2][2] == 'O'
    elif(tablero[2][0] == 'O' and tablero[1][1] == 'O'):
        tablero[0][2] == 'O'    
    
    else:
        tablero = maquinaFacil(tablero)

    return tablero

def maquinaTerminatorJ1(tablero):                
    # Tres en raya en vertical del J1
    if(tablero[0][0] == 'O' and tablero[1][0] == 'O'):
        if(tablero[2][0] != 'X'):
            tablero[2][0] = 'X'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[0][1] == 'O' and tablero[1][1] == 'O'):
        if(tablero[2][1] != 'X'):
            tablero[2][1] = 'X'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[0][2] == 'O' and tablero[1][2] == 'O'):
        if(tablero[2][2] != 'X'):
            tablero[2][2] = 'X'
        else:
            tablero = maquinaFacil(tablero)
    # Tres en raya en horizontal del J1
    elif(tablero[0][0] == 'O' and tablero[0][1] == 'O'):
        if(tablero[0][2] != 'X'):
            tablero[0][2] = 'X'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[1][0] == 'O' and tablero[1][1] == 'O'):
        if(tablero[1][2] != 'X'):
            tablero[1][2] = 'X'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[2][0] == 'O' and tablero[2][1] == 'O'):
        if(tablero[2][2] != 'X'):
            tablero[2][2] = 'X'
        else:
            tablero = maquinaFacil(tablero)
    # Tres en raya en diagonal del J1
    elif(tablero[0][0] == 'O' and tablero[1][1] == 'O'):
        if(tablero[2][2] != 'X'):
            tablero[2][2] = 'X'
        else:
            tablero = maquinaFacil(tablero)
    elif(tablero[2][0] == 'O' and tablero[1][1] == 'O'):
        if(tablero[0][2] != 'X'):
            tablero[0][2] = 'X'
        else:
            tablero = maquinaFacil(tablero)

    # Tres en raya en vertical del J2
    elif(tablero[0][0] == 'X' and tablero[1][0] == 'X'):
        tablero[2][0] = 'X'
    elif(tablero[0][1] == 'X' and tablero[1][1] == 'X'):
        tablero[2][1] == 'X'
    elif(tablero[0][2] == 'X' and tablero[1][2] == 'X'):
        tablero[2][2] == 'X'
    # Tres en raya en horizontal del J2
    elif(tablero[0][0] == 'X' and tablero[0][1] == 'X'):
        tablero[0][2] == 'X'
    elif(tablero[1][0] == 'X' and tablero[1][1] == 'X'):
        tablero[1][2] == 'X'
    elif(tablero[2][0] == 'X' and tablero[2][1] == 'X'):
        tablero[2][2] == 'X'
    # Tres en raya en diagonal del J2
    elif(tablero[0][0] == 'X' and tablero[1][1] == 'X'):
        tablero[2][2] == 'X'
    elif(tablero[2][0] == 'X' and tablero[1][1] == 'X'):
        tablero[0][2] == 'X'
    
    else:
        tablero = maquinaFacilJ1(tablero)

    return tablero

def turnoJugadorContraMaquina(turno, tablero, columnas, filas, dificultad):
    visualizarTablero(tablero, columnas, filas)
    
    if(turno == False):
        columna = int(input("\n\n¡Turno del jugador 1!\n\nEscoge la columna:\n"))

        while(columna > columnas or columna <= 0):
            columna = int(input("\n¡Columna fuera de rango!\n\nEscoge otra columna:\n"))

        fila = int(input("\nEscoge la fila:\n"))

        while(fila > filas or fila <= 0):
            fila = int(input("\n¡Fila fuera de rango!\n\nEscoge otra fila:\n"))
        
        if(tablero[fila-1][columna-1] == "X" or tablero[fila-1][columna-1] == "O"):
            print("\n¡Casilla ya ocupada!")
        else: 
            tablero[fila-1][columna-1] = "X"
                
    else:
        print("\n\n¡Turno de la máquina!")

        if(dificultad == 1):
            tablero = maquinaFacil(tablero)
        elif(dificultad == 2):
            tablero = maquinaIntermedia(tablero)        
        elif(dificultad == 3):
            tablero = maquinaTerminator(tablero)

    return tablero

def turnoMaquinaContraMaquina(turno, tablero, columnas, filas, dificultad):
    visualizarTablero(tablero, columnas, filas)
    
    if(turno == False):
        print("\n\n¡Turno de la máquina 1!")
        
        if(dificultad == 1):
            tablero = maquinaFacilJ1(tablero)
        elif(dificultad == 2):
            tablero = maquinaIntermediaJ1(tablero)
        elif(dificultad == 3):
            tablero = maquinaTerminatorJ1(tablero)                    
    else:
        print("\n\n¡Turno de la máquina 2!")

        if(dificultad == 1):
            tablero = maquinaFacil(tablero)
        elif(dificultad == 2):
            tablero = maquinaIntermedia(tablero)        
        elif(dificultad == 3):
            tablero = maquinaTerminator(tablero)

    return tablero

def comprobarTableroLleno(tablero, columnas, filas, turno, victoriaJ1, victoriaJ2):
    cont = 0
    x, y = 0,0
    for x in range(filas):        
        for y in range(columnas):
            if(tablero[x][y] != '-'):
                cont+=1            
    
    if(cont == 9):
        victoriaJ1, victoriaJ2 = True, True

    return victoriaJ1, victoriaJ2

def comprobarVictoria(tablero, columnas, filas, turno, victoriaJ1, victoriaJ2):
    if(turno == False):
        # Tres en raya en vertical del J1
        if(tablero[0][0] == 'X' and tablero[1][0] == 'X' and tablero[2][0] == 'X'):
            victoriaJ1 = True
        elif(tablero[0][1] == 'X' and tablero[1][1] == 'X' and tablero[2][1] == 'X'):
            victoriaJ1 = True
        elif(tablero[0][2] == 'X' and tablero[1][2] == 'X' and tablero[2][2] == 'X'):
            victoriaJ1 = True
        # Tres en raya en horizontal del J1
        elif(tablero[0][0] == 'X' and tablero[0][1] == 'X' and tablero[0][2] == 'X'):
            victoriaJ1 = True
        elif(tablero[1][0] == 'X' and tablero[1][1] == 'X' and tablero[1][2] == 'X'):
            victoriaJ1 = True
        elif(tablero[2][0] == 'X' and tablero[2][1] == 'X' and tablero[2][2] == 'X'):
            victoriaJ1 = True
        # Tres en raya en diagonal del J1
        elif(tablero[0][0] == 'X' and tablero[1][1] == 'X' and tablero[2][2] == 'X'):
            victoriaJ1 = True
        elif(tablero[2][0] == 'X' and tablero[1][1] == 'X' and tablero[0][2] == 'X'):
            victoriaJ1 = True
    else:
        # Tres en raya en vertical del J2
        if(tablero[0][0] == 'O' and tablero[1][0] == 'O' and tablero[2][0] == 'O'):
            victoriaJ2 = True
        elif(tablero[0][1] == 'O' and tablero[1][1] == 'O' and tablero[2][1] == 'O'):
            victoriaJ2 = True
        elif(tablero[0][2] == 'O' and tablero[1][2] == 'O' and tablero[2][2] == 'O'):
            victoriaJ2 = True    
        # Tres en raya en horizontal del J2
        elif(tablero[0][0] == 'O' and tablero[0][1] == 'O' and tablero[0][2] == 'O'):
            victoriaJ2 = True
        elif(tablero[1][0] == 'O' and tablero[1][1] == 'O' and tablero[1][2] == 'O'):
            victoriaJ2 = True
        elif(tablero[2][0] == 'O' and tablero[2][1] == 'O' and tablero[2][2] == 'O'):
            victoriaJ2 = True    
        # Tres en raya en diagonal del J2
        elif(tablero[0][0] == 'O' and tablero[1][1] == 'O' and tablero[2][2] == 'O'):
            victoriaJ2 = True
        elif(tablero[2][0] == 'O' and tablero[1][1] == 'O' and tablero[0][2] == 'O'):
            victoriaJ2 = True

    return victoriaJ1, victoriaJ2

def cambioTurno(turno):
    if(turno == False):
        turno = True
    else:
        turno = False

    return turno

# Inicio del programa
tablero = [] # Definimos inicialmente la variable "tablero" como lista
opcion = "a"
columnas, filas = 3, 3

while opcion != 0:
    opcion = int(input("\n       TRES EN RAYA\n"
        "==========================\n"
        "   1) Jugador contra jugador\n"
        "   2) Jugador contra máquina\n"
        "   3) Máquina contra máquina\n"
        "   0) Salir del juego\n\n"
        "Selecciona una opción: "))

    if(opcion) == 1:
        turno = False        
        victoriaJ1, victoriaJ2 = False, False        
        tablero = crearTablero(tablero, columnas, filas)

        while victoriaJ1 == False and victoriaJ2 == False:
            tablero = turnoJugador(turno, tablero, columnas, filas)
            victoriaJ1, victoriaJ2 = comprobarVictoria(tablero, columnas, filas, turno, victoriaJ1, victoriaJ2)
            victoriaJ1, victoriaJ2 = comprobarTableroLleno(tablero, columnas, filas, turno, victoriaJ1, victoriaJ2)
            turno = cambioTurno(turno)

        if(victoriaJ1 == True and victoriaJ2 == True):
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Empate!")
        elif(victoriaJ1 == True):
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Gana el jugador 1!")
        else:
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Gana el jugador 2!")
        
        tablero.clear()

    elif(opcion) == 2:
        dificultad = int(input(
        "\n   1) Fácil"
        "\n   2) Intermedia"
        "\n   3) Terminator"
        "\n\nEscoge la dificultad de la máquina: "))
        
        turno = False
        victoriaJ1, victoriaJ2 = False, False
        tablero = crearTablero(tablero, columnas, filas)

        while victoriaJ1 == False and victoriaJ2 == False:
            tablero = turnoJugadorContraMaquina(turno, tablero, columnas, filas, dificultad)
            victoriaJ1, victoriaJ2 = comprobarVictoria(tablero, columnas, filas, turno, victoriaJ1, victoriaJ2)
            victoriaJ1, victoriaJ2 = comprobarTableroLleno(tablero, columnas, filas, turno, victoriaJ1, victoriaJ2)
            turno = cambioTurno(turno)

        if(victoriaJ1 == True and victoriaJ2 == True):
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Empate!")
        elif(victoriaJ1 == True):
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Gana el jugador 1!")
        else:
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Gana la máquina!")
        
        tablero.clear()
    
    elif(opcion) == 3:
        dificultad = int(input(
        "\n   1) Fácil"
        "\n   2) Intermedia"
        "\n   3) Terminator"
        "\n\nEscoge la dificultad de las máquinas: "))
        
        turno = False
        victoriaJ1, victoriaJ2 = False, False
        tablero = crearTablero(tablero, columnas, filas)

        while victoriaJ1 == False and victoriaJ2 == False:
            tablero = turnoMaquinaContraMaquina(turno, tablero, columnas, filas, dificultad)
            victoriaJ1, victoriaJ2 = comprobarVictoria(tablero, columnas, filas, turno, victoriaJ1, victoriaJ2)
            victoriaJ1, victoriaJ2 = comprobarTableroLleno(tablero, columnas, filas, turno, victoriaJ1, victoriaJ2)
            turno = cambioTurno(turno)

        if(victoriaJ1 == True and victoriaJ2 == True):
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Empate!")        
        elif(victoriaJ1 == True):
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Gana la máquina 1!")
        else:
            visualizarTablero(tablero, columnas, filas)
            print("\n\n¡Gana la máquina 2!")
        
        tablero.clear()
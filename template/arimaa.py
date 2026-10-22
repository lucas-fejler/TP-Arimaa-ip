from definiciones import *

#### Algunas funciones ya dadas

def son_posiciones_vecinas(pos1 : Posicion, pos2 : Posicion) -> bool: # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) \
        or (pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1)

def direccion_desde_hasta(pos1 : Posicion, pos2 : Posicion) -> Direccion: # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
       return NORTE
    elif pos1.fila > pos2.fila:
       return SUR
    elif pos1.columna < pos2.columna:
       return ESTE
    else:
       return OESTE

def pasar_turno(j : Juego) -> Juego: # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)

#### Ejercicio 1

def tablero_bien_formado(t : Tablero) -> bool:
    """
    Indica si el tablero está bien formado, es decir, si tiene 8 filas
    y cada fila tiene 8 columnas.

    PRE: True

    Args:
        t (Tablero): El tablero que se quiere comprobar.

    Returns:
        True si el tablero está bien formado y False si no.
    """

    cant_columnas_correcta: bool=True
    for i in t:
        if len(i)!=ANCHO:
            cant_columnas_correcta=False
    return len(t)==ALTO and cant_columnas_correcta


def posicion_en_tablero(pos : Posicion) -> bool:
    """
    Indica si la posición *pos* es una posición existente del tablero, es decir la fila 
    y columna de posición estén entre 0 y 7.

    PRE: True

    Args:
        pos (Posición): La posición que se quiere comprobar.

    Returns:
        True si la posición esta dentro del tablero y False si no.
    """
        
    fila:int=pos.fila
    columna:int=pos.columna
    return (fila<ALTO and fila>=0) and (columna<ANCHO and columna>=0)

def movimiento_bien_formado(m : Movimiento) -> bool:
    """
    Indica si el movimiento *m* está bien formado, es decir, si su posición de
    origen está en el tablero y la cantidad de pasos es la que corresponde a su
    acción: 1 paso para MOVER_A_SECAS y 2 pasos para ARRASTRAR y EMPUJAR.

    PRE: True

    Args:
        m (Movimiento): Es el movimiento que se quiere comprobar.

    Returns:
        True si el Movimiento está bien formado y False si no.
    """

    cant_pasos_bien:bool=False
    if m.accion==MOVER_A_SECAS:
        cant_pasos_bien= (len(m.pasos)==1)
    if m.accion==ARRASTRAR or m.accion==EMPUJAR:
        cant_pasos_bien= (len(m.pasos)==2)
    return (posicion_en_tablero(m.origen) and cant_pasos_bien)

def juego_bien_formado(j : Juego) -> bool:
    """
    Indica si el juego *j* está bien formado, es decir que el tablero 
    j.tablero este bien formado y los pasos j.pasos_consumidos esten entre 0 y 4

    PRE: True

    Args:
        j (Juego): El juego que se quiere comprobar

    Returns:
        True si el juego está bien formado y False si no.
    """    
    return (tablero_bien_formado(j.tablero) and (j.pasos_consumidos<MAX_PASOS and j.pasos_consumidos>=0))

#### Ejercicio 2

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    raise Exception("No implementado")

def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    raise Exception("No implementado")

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    raise Exception("No implementado")

#### Ejercicio 3

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    raise Exception("No implementado")

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    raise Exception("No implementado")

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

#### Ejercicio 4

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    raise Exception("No implementado")

#### Ejercicio 5

def activar_trampas(t : Tablero) -> Tablero:
    raise Exception("No implementado")

#### Ejercicio 6

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    raise Exception("No implementado")

#### Ejercicio 7

def es_inicio_de_turno(j: Juego, col: Color)-> bool:
    return (j.turno==col and j.pasos_consumidos==0)

def hay_conejo_en_tablero(j: Juego, col: Color)-> bool:
    hay_conejo: bool= False
    for fila in range(ALTO):
        for columna in range(ANCHO):
            if (casilla_en_posicion(j.tablero, Posicion(fila,columna))==Pieza(CONEJO, col)):
                hay_conejo=True
    return hay_conejo

def hay_conejo_en_fila_inicial_oponente(j: Juego, col: Color)-> bool:
    hay:bool=False
    if col==PLATEADO:
        fila_inicial_oponente:int=0
    if col==DORADO:
        fila_inicial_oponente:int=7
    for columna in range(ANCHO):
        if (casilla_en_posicion(j.tablero, Posicion(fila_inicial_oponente,columna))==Pieza(CONEJO, col)):
            hay=True
    return hay
    
def condicion_de_ganador(j: Juego, col:Color)-> bool:
    return (hay_conejo_en_fila_inicial_oponente(j,col) or not hay_conejo_en_tablero(j,oponente(col)))

def condicion_de_ganador_exclusivo(j: Juego, col: Color)-> bool:
    return (condicion_de_ganador(j,col) and not condicion_de_ganador(j,oponente(col)))

def es_jugador_ganador(j: Juego, col: Color)-> bool:
    return (es_inicio_de_turno(j, oponente(col)) and condicion_de_ganador(j,col)) or (es_inicio_de_turno(j,col) and condicion_de_ganador_exclusivo(j,col))

def hay_ganador_determinado(j : Juego) -> bool:
    return (es_jugador_ganador(j, DORADO) or es_jugador_ganador(j, PLATEADO))

def ganador_del_juego(j : Juego) -> Color:
    ganador: Color=PLATEADO
    if es_jugador_ganador(j, DORADO):
        ganador=DORADO
    return ganador
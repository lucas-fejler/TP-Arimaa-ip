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
    raise Exception("No implementado")

def posicion_en_tablero(pos : Posicion) -> bool:
    raise Exception("No implementado")

def movimiento_bien_formado(m : Movimiento) -> bool:
    raise Exception("No implementado")

def juego_bien_formado(j : Juego) -> bool:
    raise Exception("No implementado")

#### Ejercicio 2

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    if d == NORTE:
        pos = Posicion(pos.fila+1,pos.columna)
    elif d == SUR:
        pos = Posicion(pos.fila-1,pos.columna)
    elif d == ESTE:
        pos = Posicion(pos.fila,pos.columna+1)
    elif d == OESTE:
        pos = Posicion(pos.fila,pos.columna-1)
    return pos

def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    return t[p.fila][p.columna]

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    return t[pos.fila][pos.columna] == VACIA

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    c:Casilla = casilla_en_posicion(t,pos)
    return not hay_casilla_vacia(t,pos) and c.color == col

#### Ejercicio 3

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    pos_vecina:Posicion = posicion_vecina_hacia(pos,d)
    res:bool = False
    if posicion_en_tablero(pos_vecina):
        res= hay_casilla_vacia(t,pos_vecina)
    return res

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    encontro_pieza_amiga:bool = False
    i:int = 0
    direcciones:list[Direccion] = [NORTE,SUR,ESTE,OESTE]
    while i < len(direcciones) and not encontro_pieza_amiga:
        d:Direccion = direcciones[i]
        encontro_pieza_amiga = aux_hay_pieza_amiga_hacia(t,pos,d)
        i+=1
    return encontro_pieza_amiga

def aux_hay_pieza_amiga_hacia(t:Tablero, pos:Posicion, d: Direccion) -> bool:
    res:bool = False
    if not hay_casilla_vacia(t,pos):
        c:Casilla = casilla_en_posicion(t,pos)
        pos_vecina:Posicion = posicion_vecina_hacia(pos,d)
        res= posicion_en_tablero(pos_vecina) and hay_pieza_de_color(t,pos_vecina,c.color)
    return res

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    res: bool = False
    pos_hacia:Posicion = posicion_vecina_hacia(pos,d)
    if posicion_en_tablero(pos_hacia) and not hay_casilla_vacia(t,pos_hacia):
        c_vecina : Casilla = casilla_en_posicion(t,pos_hacia)
        f_vecina : Figura = c_vecina.figura
        col_vecino : Color = c_vecina.color
        c:Casilla = casilla_en_posicion(t,pos)
        f:Figura = c.figura
        col:Color = c.color
        res = col_vecino == oponente(col) and fuerza(f) > fuerza(f_vecina)
    return res

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

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")

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

def realizar_movimiento(j: Juego, m: Movimiento) -> Juego:
    """
    Devuelve el juego que resulta de realizar el movimiento m en el juego j.
    Si con este movimiento se completan los pasos del turno, el turno pasa al oponente.

    PRE: juego_bien_formado(j), movimiento_bien_formado(m) y puede_realizar_movimiento(j, m)
    """
    nuevo_tablero = tablero_post_movimiento(j.tablero, m)
    nuevos_pasos = j.pasos_consumidos + len(m.pasos)
    
    if nuevos_pasos == MAX_PASOS:
        return Juego(nuevo_tablero, oponente(j.turno), 0)
    else:
        return Juego(nuevo_tablero, j.turno, nuevos_pasos)


def tablero_post_movimiento(t: Tablero, m: Movimiento) -> Tablero:
    """
    Devuelve el tablero que resulta de aplicar el movimiento m, según cuál sea su acción.

    PRE: tablero_bien_formado(t) y movimiento_bien_formado(m)
    """
    if m.accion == MOVER_A_SECAS:
        return tablero_post_mover_a_secas(t, m.origen, m.pasos[0])
    elif m.accion == ARRASTRAR:
        return tablero_post_arrastrar(t, m.origen, m.pasos[0], m.pasos[1])
    else:  # EMPUJAR
        return tablero_post_empujar(t, m.origen, m.pasos[0], m.pasos[1])


def tablero_post_mover_a_secas(t: Tablero, pos: Posicion, d: Direccion) -> Tablero:
    """
    Devuelve el tablero que resulta de mover la pieza de pos una casilla hacia d.

    PRE: tablero_bien_formado(t), posicion_en_tablero(pos) y hay_casilla_vacia_hacia(t, pos, d)
    """
    destino = posicion_vecina_hacia(pos, d)
    tablero = [fila[:] for fila in t]
    tablero[destino.fila][destino.columna] = tablero[pos.fila][pos.columna]
    tablero[pos.fila][pos.columna] = VACIA
    return activar_trampas(tablero)


def tablero_post_arrastrar(t: Tablero, pos: Posicion, d: Direccion, d_arrastre: Direccion) -> Tablero:
    """
    Devuelve el tablero que resulta de mover la pieza de pos hacia d,
    arrastrando a la pieza enemiga que se mueve hacia d_arrastre.

    PRE: tablero_bien_formado(t), posicion_en_tablero(pos) y
         hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(d_arrastre))
    """
    destino = posicion_vecina_hacia(pos, d)
    enemiga = posicion_vecina_hacia(pos, opuesta(d_arrastre))
    tablero = [fila[:] for fila in t]
    
    tablero[destino.fila][destino.columna] = tablero[pos.fila][pos.columna]
    tablero[pos.fila][pos.columna] = tablero[enemiga.fila][enemiga.columna]
    tablero[enemiga.fila][enemiga.columna] = VACIA
    
    return activar_trampas(tablero)


def tablero_post_empujar(t: Tablero, pos: Posicion, d: Direccion, d_empuje: Direccion) -> Tablero:
    """
    Devuelve el tablero que resulta de que la pieza de pos empuje hacia d_empuje
    a la pieza enemiga vecina en la dirección d, ocupando su lugar.

    PRE: tablero_bien_formado(t), posicion_en_tablero(pos) y
         hay_pieza_enemiga_mas_debil_hacia(t, pos, d)
    """
    enemiga = posicion_vecina_hacia(pos, d)
    destino_enemiga = posicion_vecina_hacia(enemiga, d_empuje)
    tablero = [fila[:] for fila in t]
    
    tablero[destino_enemiga.fila][destino_enemiga.columna] = tablero[enemiga.fila][enemiga.columna]
    tablero[enemiga.fila][enemiga.columna] = tablero[pos.fila][pos.columna]
    tablero[pos.fila][pos.columna] = VACIA
    
    return activar_trampas(tablero)

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")
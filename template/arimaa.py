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

def copiar_tablero(t: Tablero) -> Tablero:
    """
    Devuelve una copia profunda del tablero utilizando bucles tradicionales.

    PRE: tablero_bien_formado(t)

    Args:
        t (Tablero): El tablero que se desea copiar.

    Returns:
        Una nueva matriz idéntica a t pero independiente en memoria.
    """
    tablero: Tablero = []
    for fila in t:
        nueva_fila = []
        for casilla in fila:
            nueva_fila.append(casilla)
        tablero.append(nueva_fila)
        
    res: Tablero = tablero
    return res

def realizar_movimiento(j: Juego, m: Movimiento) -> Juego:
    """
    Devuelve el juego resultante de realizar un movimiento válido.

    PRE: juego_bien_formado(j) and movimiento_bien_formado(m) and puede_realizar_movimiento(j, m)

    Args:
        j (Juego): El estado actual del juego antes de realizar el movimiento.
        m (Movimiento): El movimiento válido que se desea ejecutar.

    Returns:
        El juego resultante con el tablero actualizado, los pasos consumidos y el turno avanzado si corresponde.
    """
    nuevo_tablero: Tablero = tablero_post_movimiento(j.tablero, m)
    nuevos_pasos: int = j.pasos_consumidos + len(m.pasos)
    res: Juego
    
    if nuevos_pasos == MAX_PASOS:
        res = Juego(nuevo_tablero, oponente(j.turno), 0)
    else:
        res = Juego(nuevo_tablero, j.turno, nuevos_pasos) 
    return res

def tablero_post_movimiento(t: Tablero, m: Movimiento) -> Tablero:
    """
    Despacha y calcula el tablero resultante según la acción especificada en el movimiento.

    PRE: tablero_bien_formado(t) and movimiento_bien_formado(m)

    Args:
        t (Tablero): El estado actual del tablero.
        m (Movimiento): El movimiento que define la acción a realizar.

    Returns:
        El tablero resultante tras aplicar la acción correspondiente.
    """
    res: Tablero
    if m.accion == MOVER_A_SECAS:
        res = tablero_post_mover_a_secas(t, m.origen, m.pasos[0])
    elif m.accion == ARRASTRAR:
        res = tablero_post_arrastrar(t, m.origen, m.pasos[0], m.pasos[1])
    else:
        res = tablero_post_empujar(t, m.origen, m.pasos[0], m.pasos[1])
    return res

def tablero_post_mover_a_secas(t: Tablero, pos: Posicion, d: Direccion) -> Tablero:
    """
    Devuelve el tablero tras mover una pieza a una casilla vacía y activar trampas.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)

    Args:
        t (Tablero): El tablero inicial.
        pos (Posicion): La posición de origen de la pieza.
        d (Direccion): La dirección hacia donde se mueve la pieza.

    Returns:
        El tablero actualizado con la pieza reubicada y las trampas activadas.
    """
    destino: Posicion = posicion_vecina_hacia(pos, d)
    tablero: Tablero = copiar_tablero(t)
    tablero[destino.fila][destino.columna] = tablero[pos.fila][pos.columna]
    tablero[pos.fila][pos.columna] = VACIA
    res: Tablero = activar_trampas(tablero)
    return res


def tablero_post_arrastrar(t: Tablero, pos: Posicion, d: Direccion, d_arrastre: Direccion) -> Tablero:
    """
    Devuelve el tablero tras mover una pieza propia y arrastrar a una enemiga.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)

    Args:
        t (Tablero): El tablero inicial.
        pos (Posicion): La posición de origen de la pieza propia.
        d (Direccion): La dirección de movimiento de la pieza propia.
        d_arrastre (Direccion): La dirección de arrastre de la pieza oponente.

    Returns:
        El tablero actualizado con ambas piezas desplazadas y las trampas activadas.
    """
    destino: Posicion = posicion_vecina_hacia(pos, d)
    enemiga: Posicion = posicion_vecina_hacia(pos, opuesta(d_arrastre))
    tablero: Tablero = copiar_tablero(t)
    tablero[destino.fila][destino.columna] = tablero[pos.fila][pos.columna]
    tablero[pos.fila][pos.columna] = tablero[enemiga.fila][enemiga.columna]
    tablero[enemiga.fila][enemiga.columna] = VACIA
    res: Tablero = activar_trampas(tablero)
    return res


def tablero_post_empujar(t: Tablero, pos: Posicion, d: Direccion, d_empuje: Direccion) -> Tablero:
    """
    Devuelve el tablero tras empujar a una pieza enemiga y ocupar su lugar.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)

    Args:
        t (Tablero): El tablero inicial.
        pos (Posicion): La posición de origen de la pieza propia.
        d (Direccion): La dirección hacia la pieza enemiga adyacente.
        d_empuje (Direccion): La dirección hacia donde es empujada la pieza enemiga.

    Returns:
        El tablero actualizado tras el empuje y la activación de trampas.
    """
    enemiga: Posicion = posicion_vecina_hacia(pos, d)
    destino_enemiga: Posicion = posicion_vecina_hacia(enemiga, d_empuje)
    tablero: Tablero = copiar_tablero(t)
    tablero[destino_enemiga.fila][destino_enemiga.columna] = tablero[enemiga.fila][enemiga.columna]
    tablero[enemiga.fila][enemiga.columna] = tablero[pos.fila][pos.columna]
    tablero[pos.fila][pos.columna] = VACIA
    res: Tablero = activar_trampas(tablero)
    return res

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")
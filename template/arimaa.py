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
    Devuelve el estado del juego resultante de realizar un movimiento válido.
    
    PRE: juego_bien_formado(j) and movimiento_bien_formado(m) and puede_realizar_movimiento(j, m)
    
    Args:
        j (Juego): El estado actual del juego antes de realizar el movimiento.
        m (Movimiento): El movimiento válido que se desea ejecutar.
        
    Returns:
        Un nuevo objeto Juego con el tablero actualizado, los pasos consumidos recalculados
        y el turno avanzado en caso de corresponder.
    """
    nuevo_tablero = tablero_post_movimiento(j.tablero, m)
    nuevos_pasos = j.pasos_consumidos + len(m.pasos)
    
    if nuevos_pasos == MAX_PASOS:
        return Juego(nuevo_tablero, oponente(j.turno), 0)
    else:
        return Juego(nuevo_tablero, j.turno, nuevos_pasos)


def tablero_post_movimiento(t: Tablero, m: Movimiento) -> Tablero:
    """
    Despacha y calcula el tablero resultante según la acción especificada en el movimiento.
    
    PRE: tablero_bien_formado(t) and movimiento_bien_formado(m)
    
    Args:
        t (Tablero): El estado actual del tablero.
        m (Movimiento): El movimiento que define la acción a realizar.
        
    Returns:
        El tablero resultante tras aplicar la acción correspondiente y activar las trampas.
    """
    if m.accion == MOVER_A_SECAS:
        return tablero_post_mover_a_secas(t, m.origen, m.pasos[0])
    elif m.accion == ARRASTRAR:
        return tablero_post_arrastrar(t, m.origen, m.pasos[0], m.pasos[1])
    else:  # EMPUJAR
        return tablero_post_empujar(t, m.origen, m.pasos[0], m.pasos[1])


def tablero_post_mover_a_secas(t: Tablero, pos: Posicion, d: Direccion) -> Tablero:
    """
    Devuelve el tablero tras mover una pieza propia a una casilla vecina vacía y activar las trampas.
    
    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)
    
    Args:
        t (Tablero): El tablero inicial.
        pos (Posicion): La posición de origen de la pieza que se mueve.
        d (Direccion): La dirección hacia donde se mueve la pieza.
        
    Returns:
        El tablero actualizado con la pieza reubicada y las trampas evaluadas.
    """
    destino = posicion_vecina_hacia(pos, d)
    tablero = [fila[:] for fila in t]
    tablero[destino.fila][destino.columna] = tablero[pos.fila][pos.columna]
    tablero[pos.fila][pos.columna] = VACIA
    return activar_trampas(tablero)


def tablero_post_arrastrar(t: Tablero, pos: Posicion, d: Direccion, d_arrastre: Direccion) -> Tablero:
    """
    Devuelve el tablero tras mover una pieza propia y arrastrar consigo a una pieza enemiga adyacente.
    
    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)
    
    Args:
        t (Tablero): El tablero inicial.
        pos (Posicion): La posición de origen de la pieza propia.
        d (Direccion): La dirección de movimiento de la pieza propia.
        d_arrastre (Direccion): La dirección de arrastre de la pieza oponente.
        
    Returns:
        El tablero actualizado con ambas piezas desplazadas y las trampas evaluadas.
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
    Devuelve el tablero tras empujar a una pieza enemiga adyacente y ocupar su lugar.
    
    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)
    
    Args:
        t (Tablero): El tablero inicial.
        pos (Posicion): La posición de origen de la pieza propia.
        d (Direccion): La dirección hacia donde se empuja al oponente.
        d_empuje (Direccion): La dirección de destino del oponente empujado.
        
    Returns:
        El tablero actualizado tras el empuje de ambas piezas y la evaluación de trampas.
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
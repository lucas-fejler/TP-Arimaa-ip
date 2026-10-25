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

def direccion_de_movimiento_habilitada(t : Tablero , pos : Posicion , d : Direccion)-> bool:
    """
    Chequea si la pieza en *pos* puede moverse en la dirección *d*.
    
    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)
    
    Args: 
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición actual de la pieza.
        d (Direccion): Dirección en la que se verifica si el movimiento está habilitado.
        
    Returns:
        True si en *pos* hay una pieza que puede moverse en la dirección *d* y False si no. 
        
    """
    
    res:bool = False
    casilla: Casilla = casilla_en_posicion(t,pos)
    
    if not hay_casilla_vacia(t,pos):    
        if casilla.figura == CONEJO:
            if casilla.color == DORADO:
                res =  d != SUR
            else:
                res =  d != NORTE
        else:
            res = True
                       
    return res
            

def puede_mover_a_secas(t:Tablero, pos:Posicion, d:Direccion)-> bool:
    """
    Chequea si la pieza en *pos* puede moverse a secas en la dirección *d*.
        
    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)
        
    Args: 
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición actual de la pieza.
        d (Direccion): Dirección en la que se verifica si la acción está habilitada.
            
    Returns:
        True si la pieza puede moverse a secas en la dirección *d* y False si no. 
            
    """
    return hay_casilla_vacia_hacia(t,pos,d)

def puede_arrastrar(t:Tablero, pos:Posicion, d:Direccion, direc_arrastre:Direccion)-> bool:
    """
    Chequea si la pieza en *pos* puede moverse en la dirección *d* arrastrando a una pieza enemiga en la dirección *direc_arrastre*.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos) and not hay_casilla_vacia(t, pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la pieza que realiza el arrastre.
        d (Direccion): Dirección en la que se mueve la pieza en *pos*.
        direc_arrastre (Direccion): Dirección en la que se mueve la pieza enemiga arrastrada.

    Returns:
        True si la pieza en *pos* puede realizar el arrastre y False en caso contrario.

    """
    return (hay_casilla_vacia_hacia(t,pos,d) and hay_pieza_enemiga_mas_debil_hacia(t,pos,opuesta(direc_arrastre)))

def puede_empujar(t:Tablero, pos:Posicion, d:Direccion, direc_empuje:Direccion)-> bool:
    """
    Chequea si la pieza en *pos* puede moverse en la dirección *d* empujando a una pieza enemiga en la dirección *direc_empuje*.
    
    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos) and not hay_casilla_vacia(t, pos)
    
    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la pieza que realiza el empuje.
        d (Direccion): Dirección en la que se mueve la pieza en *pos*.
        direc_empuje (Direccion): Dirección en la que se mueve la pieza enemiga empujada.
    
    Returns:
        True si la pieza en *pos* puede realizar el empuje y False en caso contrario.
    
    """    
    pos_vecina:Posicion = posicion_vecina_hacia(pos,d)
    
    return (hay_pieza_enemiga_mas_debil_hacia(t, pos, d) and hay_casilla_vacia_hacia(t, pos_vecina, direc_empuje))        

def puede_realizar_accion(t:Tablero, m:Movimiento)-> bool:
    """
    Chequea si la pieza en *m.origen* puede realizar la acción *m.accion*.
        
    PRE: tablero_bien_formado(t) and movimiento_bien_formado(m) and not hay_casilla_vacia(t, m.origen)
        
    Args:
        t (Tablero): Tablero del juego.
        m (Movimiento): Acción, posición de la pieza y pasos.
        
    Returns:
        True si la pieza en *m.origen* puede realizar la acción *m.accion* y False en caso contrario.
        
    """
    res:bool = False
    
    if m.accion == MOVER_A_SECAS:
        res = puede_mover_a_secas(t,m.origen,m.pasos[0])
    elif m.accion == ARRASTRAR:
        res =  puede_arrastrar(t,m.origen,m.pasos[0],m.pasos[1])
    else: 
        res = puede_empujar(t,m.origen,m.pasos[0],m.pasos[1])
        
    return res    
    
def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:    
    """
    Chequea si se puede realizar el movimiento *m* en el juego *j*.
            
    PRE: juego_bien_formado(j) and movimiento_bien_formado(m)
            
    Args:
        j (Juego): Tablero del juego, color del turno actual y pasos consumidos en el turno.
        m (Movimiento): Acción, posición de la pieza y pasos.
            
    Returns:
        True si se puede realizar el movimiento *m* en el juego *j* y False si no.
            
    """
    return (hay_pieza_de_color(j.tablero,m.origen,j.turno) 
            and not hay_pieza_congelada(j.tablero,m.origen)
            and direccion_de_movimiento_habilitada(j.tablero,m.origen,m.pasos[0])
            and (j.pasos_consumidos + len(m.pasos)) <= MAX_PASOS 
            and puede_realizar_accion(j.tablero,m))
    
    

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


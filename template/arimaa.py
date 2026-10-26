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
    Indica si el juego *j* está bien formado, es decir que su tablero este bien formado
    y los pasos pasos consumidos de juego estén entre 0 y 3.

    PRE: True

    Args:
        j (Juego): El juego que se quiere comprobar

    Returns:
        True si el juego está bien formado y False si no.
    """

    return (tablero_bien_formado(j.tablero) and (j.pasos_consumidos<MAX_PASOS and j.pasos_consumidos>=0))

#### Ejercicio 2

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    """
    Devuelve la posición vecina a *pos* en la dirección *d*.

    PRE: True

    Args:
        pos (Posicion): Posición de partida.
        d (Direccion): Dirección en la que se busca la posición vecina.

    Returns:
        La posición vecina a *pos* en la dirección *d* (puede quedar fuera del tablero).

    """
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
    """
    Devuelve la casilla de *t* que está en la posición *p*.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(p)

    Args:
        t (Tablero): Tablero del juego.
        p (Posicion): Posición de la casilla.

    Returns:
        La casilla en la posición *p*: VACIA o la pieza que la ocupa.

    """
    return t[p.fila][p.columna]

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    """
    Chequea si la casilla en *pos* está vacía.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la casilla.

    Returns:
        True si la casilla en *pos* está vacía y False si no.

    """
    return t[pos.fila][pos.columna] == VACIA

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    """
    Chequea si en *pos* hay una pieza de color *col*.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la casilla.
        col (Color): Color de la pieza que se busca.

    Returns:
        True si en *pos* hay una pieza de color *col* y False si no.

    """
    c:Casilla = casilla_en_posicion(t,pos)
    return not hay_casilla_vacia(t,pos) and c.color == col

#### Ejercicio 3

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Chequea si la casilla vecina a *pos* en la dirección *d* existe y está vacía.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la casilla.
        d (Direccion): Dirección en la que se busca la casilla vecina.

    Returns:
        True si la casilla vecina a *pos* en la dirección *d* está dentro del tablero y vacía, y False si no.

    """
    pos_vecina:Posicion = posicion_vecina_hacia(pos,d)
    res:bool = False
    if posicion_en_tablero(pos_vecina):
        res= hay_casilla_vacia(t,pos_vecina)
    return res

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    """
    Chequea si la pieza en *pos* tiene alguna pieza amiga vecina.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos) and not hay_casilla_vacia(t, pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la pieza.

    Returns:
        True si la pieza en *pos* tiene al menos una pieza de su mismo color al norte, sur, este u oeste, y False si no.

    """
    encontro_pieza_amiga:bool = False
    i:int = 0
    direcciones:list[Direccion] = [NORTE,SUR,ESTE,OESTE]
    while i < len(direcciones) and not encontro_pieza_amiga:
        d:Direccion = direcciones[i]
        encontro_pieza_amiga = aux_hay_pieza_amiga_hacia(t,pos,d)
        i+=1
    return encontro_pieza_amiga

def aux_hay_pieza_amiga_hacia(t:Tablero, pos:Posicion, d: Direccion) -> bool:
    """
    Chequea si la pieza en *pos* tiene una pieza amiga vecina en la dirección *d*.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la pieza.
        d (Direccion): Dirección en la que se busca la pieza amiga.

    Returns:
        True si en *pos* hay una pieza y su casilla vecina en la dirección *d* tiene una pieza de su mismo color, y False si no.

    """
    res:bool = False
    if not hay_casilla_vacia(t,pos):
        c:Casilla = casilla_en_posicion(t,pos)
        pos_vecina:Posicion = posicion_vecina_hacia(pos,d)
        res= posicion_en_tablero(pos_vecina) and hay_pieza_de_color(t,pos_vecina,c.color)
    return res

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Chequea si la pieza en *pos* tiene una pieza enemiga más débil vecina en la dirección *d*.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos) and not hay_casilla_vacia(t, pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la pieza.
        d (Direccion): Dirección en la que se busca la pieza enemiga.

    Returns:
        True si la casilla vecina a *pos* en la dirección *d* tiene una pieza enemiga más débil que la pieza en *pos*, y False si no.

    """
    res:bool = False
    if aux_hay_pieza_enemiga_hacia_direccion(t,pos,d):
        pos_hacia:Posicion = posicion_vecina_hacia(pos,d)
        c_vecina : Casilla = casilla_en_posicion(t,pos_hacia)
        c:Casilla = casilla_en_posicion(t,pos)
        f:Figura = c.figura
        f_vecina : Figura = c_vecina.figura
        res = fuerza(f) > fuerza(f_vecina)
    return res

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    """
    Chequea si la pieza en *pos* tiene alguna pieza enemiga más fuerte vecina.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos) and not hay_casilla_vacia(t, pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la pieza.

    Returns:
        True si la pieza en *pos* tiene al menos una pieza enemiga más fuerte al norte, sur, este u oeste, y False si no.

    """
    encontro_pieza_enemiga_mas_fuerte:bool = False
    i:int = 0
    direcciones:list[Direccion] = [NORTE,SUR,ESTE,OESTE]
    while i < len(direcciones) and not encontro_pieza_enemiga_mas_fuerte:
        d:Direccion = direcciones[i]
        encontro_pieza_enemiga_mas_fuerte = aux_hay_pieza_enemiga_mas_fuerte_hacia(t,pos,d)
        i+=1
    return encontro_pieza_enemiga_mas_fuerte

def aux_hay_pieza_enemiga_mas_fuerte_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Chequea si la pieza en *pos* tiene una pieza enemiga más fuerte vecina en la dirección *d*.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos) and not hay_casilla_vacia(t, pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la pieza.
        d (Direccion): Dirección en la que se busca la pieza enemiga.

    Returns:
        True si la casilla vecina a *pos* en la dirección *d* tiene una pieza enemiga más fuerte que la pieza en *pos*, y False si no.

    """
    res:bool = False
    if aux_hay_pieza_enemiga_hacia_direccion(t,pos,d):
        pos_hacia:Posicion = posicion_vecina_hacia(pos,d)
        c_vecina : Casilla = casilla_en_posicion(t,pos_hacia)
        c:Casilla = casilla_en_posicion(t,pos)
        f:Figura = c.figura
        f_vecina : Figura = c_vecina.figura
        res = fuerza(f) < fuerza(f_vecina)
    return res

def aux_hay_pieza_enemiga_hacia_direccion(t:Tablero, pos:Posicion, d: Direccion) -> bool:
    """
    Chequea si la pieza en *pos* tiene una pieza enemiga vecina en la dirección *d*.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos) and not hay_casilla_vacia(t, pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la pieza.
        d (Direccion): Dirección en la que se busca la pieza enemiga.

    Returns:
        True si la casilla vecina a *pos* en la dirección *d* está dentro del tablero y tiene una pieza del color opuesto, y False si no.

    """
    pos_hacia:Posicion = posicion_vecina_hacia(pos,d)
    c:Casilla = casilla_en_posicion(t,pos)
    return posicion_en_tablero(pos_hacia) and hay_pieza_de_color(t,pos_hacia,oponente(c.color))

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    """
    Chequea si en *pos* hay una pieza congelada.

    PRE: tablero_bien_formado(t) and posicion_en_tablero(pos)

    Args:
        t (Tablero): Tablero del juego.
        pos (Posicion): Posición de la casilla.

    Returns:
        True si en *pos* hay una pieza con alguna pieza enemiga más fuerte vecina y ninguna pieza amiga vecina, y False si no.

    """
    res: bool = False
    c:Casilla = casilla_en_posicion(t,pos)
    if not hay_casilla_vacia(t,pos):
        res  = hay_pieza_enemiga_mas_fuerte_vecina(t,pos) and not hay_pieza_amiga_vecina(t,pos)
    return res

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
    """
    Devuelve una copia de *t* en la que se eliminan las piezas que están en una trampa sin ninguna pieza amiga vecina.

    PRE: tablero_bien_formado(t)

    Args:
        t (Tablero): Tablero del juego.

    Returns:
        Un tablero nuevo igual a *t*, salvo que las trampas ocupadas por una pieza sin piezas amigas vecinas quedan vacías.

    """
    tablero_con_trampas_activadas : Tablero = []
    for i in range(len(t)):
        tablero_con_trampas_activadas.append([])
        for casilla in t[i]:
            tablero_con_trampas_activadas[i].append(casilla)
    for trampa in POSICIONES_TRAMPA:
        if not hay_casilla_vacia(tablero_con_trampas_activadas,trampa) and not hay_pieza_amiga_vecina(tablero_con_trampas_activadas,trampa):
            tablero_con_trampas_activadas[trampa.fila][trampa.columna]= VACIA
    return tablero_con_trampas_activadas

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

def es_inicio_de_turno(j: Juego, col: Color)-> bool:
    """
    Indica si el juego *j* está al inicio del turno del color *col*, 
    es decir si le toca jugar a *col* y los pasos consumidos son 0.

    PRE: True

    Args:
        j (Juego): El juego que queremos mirar.
        col (Color): El color por el que se pregunta.

    Returns:
        True si j.turno es *col* y j.pasos_consumidos es 0, False si no.
    """

    return (j.turno==col and j.pasos_consumidos==0)

def hay_conejo_en_tablero(j: Juego, col: Color)-> bool:
    """
    Indica si en el juego *j* hay un conejo en el tablero de color *col*. 

    PRE: juego_bien_formado(j)

    Args:
        j (Juego): El juego que queremos mirar.
        col (Color): El color de conejo por el que se pregunta.

    Returns:
        True si en alguna casilla del tablero hay un conejo de color *col* y 
        False si no.
    """

    hay_conejo: bool= False
    for fila in range(ALTO):
        for columna in range(ANCHO):
            if (casilla_en_posicion(j.tablero, Posicion(fila,columna))==Pieza(CONEJO, col)):
                hay_conejo=True
    return hay_conejo

def hay_conejo_en_fila_inicial_oponente(j: Juego, col: Color)-> bool:
    """
    Indica si en el tablero del juego *j* hay un conejo de color *col*
    en la fila inicial del oponente (la fila 7 si *col* es DORADO y la fila 0 si
    *col* es PLATEADO)

    PRE: juego_bien_formado(j)    

    Args:
        j (Juego): El juego que queremos mirar.
        col (Color): El color del jugador cuyo conejo se busca.

    Returns:
        True si existe una casilla de esa fila con un conejo de color *col*,
        y False si no.
    """

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
    """
    Indica si en el juego *j* el jugador de color *col* cumple la condición de ganador,
    es decir, si tiene un conejo en la fila inicial del oponente o si el oponente no 
    tiene conejos en el tablero.

    PRE: juego_bien_formado(j)

    Args:
        j (Juego): El juego que queremos mirar.
        col (Color): El color de jugador por el que se pregunta.

    Returns:
        True si *col* tiene un conejo en la fila inicial del oponente o si el oponente 
        no tiene conejos en el tablero y False si no.
    """
    
    return (hay_conejo_en_fila_inicial_oponente(j,col) or not hay_conejo_en_tablero(j,oponente(col)))

def condicion_de_ganador_exclusivo(j: Juego, col: Color)-> bool:
    """
    Indica si en el juego *j* el jugador de color *col* cumple la condición de ganador
    exclusivo, es decir que cumple la condición de ganador y su oponente no.

    PRE: juego_bien_formado(j)

    Args:
        j (Juego): El juego que queremos mirar.
        col (Color): El color de jugador por el que se pregunta.

    Returns:
        True si *col* cumple la condición de ganador y su oponente no, False si no.
    """

    return (condicion_de_ganador(j,col) and not condicion_de_ganador(j,oponente(col)))

def es_jugador_ganador(j: Juego, col: Color)-> bool:
    """
    Indica si en el juego *j* el jugador de color *col* es ganador, es decir 
    si reúne las condiciones de ganador al inicio del turno del oponente, o si
    las reúne en forma exclusiva al inicio de su  turno.

    PRE: juego_bien_formado(j)

    Args:
        j (Juego): El juego que queremos mirar.
        col (Color): El color de jugador por el que se pregunta.

    Returns:
        True si *col* es el ganador del juego y False si no.
    """

    return (es_inicio_de_turno(j, oponente(col)) and condicion_de_ganador(j,col)) or (es_inicio_de_turno(j,col) and condicion_de_ganador_exclusivo(j,col))

def hay_ganador_determinado(j : Juego) -> bool:
    """
    Indica si en el juego *j* hay un ganador determinado, es decir si alguno de los dos
    colores es jugador ganador.

    PRE: juego_bien_formado(j)

    Args:
        j (Juego): El juego que queremos mirar.

    Returns:
        True si alguno de los jugadores (DORADO o PLATEADO) es ganador y False si no.
    """

    return (es_jugador_ganador(j, DORADO) or es_jugador_ganador(j, PLATEADO))

def ganador_del_juego(j : Juego) -> Color:
    """
    Devuelve el color del ganador del juego *j*
    
    PRE: juego_bien_formado(j) y hay_ganador_determinado(j)


    Args:
        j (Juego): El juego que queremos mirar.

    Returns:
        DORADO si el jugador dorado es el ganador, o PLATEADO si lo es el plateado.
    """

    ganador: Color=PLATEADO
    if es_jugador_ganador(j, DORADO):
        ganador=DORADO
    return ganador
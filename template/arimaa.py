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

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    raise Exception("No implementado")

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")

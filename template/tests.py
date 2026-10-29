import unittest
from arimaa import *

# Las piezas se representan con las siguientes letras:
#   E : elefante
#   M : camello
#   H : caballo
#   D : perro
#   C : gato
#   R : ratón
# donde
#   mayúscula : dorado
#   minúscula : plateado

def tablero_8x8_vacio():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

def tablero_8x8_inicial_ejemplo():
    return leer_tablero([
              'hcdmedch', #7
              'rrrrrrrr', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              'RRRRRRRR', #1
              'HCDMEDCH', #0
              #01234567
            ])

#### Ejercicio 1

class test_tablero_bien_formado(unittest.TestCase):

    def test_8x8_lleno(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

class test_posicion_en_tablero(unittest.TestCase):

    def test_posicion_ok(self):
        self.assertTrue(posicion_en_tablero(Posicion(5, 3)))

class test_movimiento_bien_formado(unittest.TestCase):

    def test_movimiento_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])))

class test_juego_bien_formado(unittest.TestCase):

    def test_juego_ok(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))

#### Ejercicio 2

class test_posicion_vecina_hacia(unittest.TestCase):

    def test_vecina_al_norte(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))

class test_son_posiciones_vecinas(unittest.TestCase):

    def test_vecinas(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))

class test_casilla_en_posicion(unittest.TestCase):

    def test_casilla_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))

class test_hay_casilla_vacia(unittest.TestCase):

    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))

class test_hay_pieza_de_color(unittest.TestCase):

    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))

#### Ejercicio 3

class test_hay_casilla_vacia_hacia(unittest.TestCase):

    def test_hay_casilla_vacia_hacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(0, 0), NORTE))

class test_hay_pieza_amiga_vecina(unittest.TestCase):

    def test_hay_pieza_amiga_vecina(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 3)))

class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), OESTE))

class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = leer_tablero([
              'R-e--mRr', #7
              '------dE', #6
              'h--Rr-RR', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

class test_hay_pieza_congelada(unittest.TestCase):

    def test_hay_pieza_congelada(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_congelada(t, Posicion(6, 1)))

#### Ejercicio 4

class test_puede_realizar_movimiento(unittest.TestCase):

    def test_mover_a_secas_ok(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

#### Ejercicio 5

class test_activar_trampas(unittest.TestCase):

    def test_activar_trampas_ok(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H--m--', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

#### Ejercicio 6

def tablero_con_piezas(piezas: list[tuple[Posicion, Casilla]]) -> Tablero:
    """Construye un tablero vacío y coloca las piezas indicadas."""
    tablero: Tablero = tablero_8x8_vacio()
    posicion: Posicion
    pieza: Casilla
 
    for posicion, pieza in piezas:
        tablero[posicion.fila][posicion.columna] = pieza
 
    return tablero
 
def copia_del_tablero(tablero: Tablero) -> Tablero:
    """Copia casilla por casilla, sin usar el código que se está probando."""
    copia: Tablero = []
    fila_original: list[Casilla]
    fila_copia: list[Casilla]
    casilla: Casilla
 
    for fila_original in tablero:
        fila_copia = []
        for casilla in fila_original:
            fila_copia.append(casilla)
        copia.append(fila_copia)
 
    return copia
 
 
class test_realizar_movimiento(unittest.TestCase):
 
    ## Mover a secas
 
    def test_mover_a_secas_norte(self):
        origen: Posicion = Posicion(3, 1)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        tablero: Tablero = tablero_con_piezas([(origen, caballo)])
        esperado: Tablero = tablero_con_piezas([(Posicion(4, 1), caballo)])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_mover_a_secas_sur(self):
        origen: Posicion = Posicion(3, 1)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        tablero: Tablero = tablero_con_piezas([(origen, caballo)])
        esperado: Tablero = tablero_con_piezas([(Posicion(2, 1), caballo)])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [SUR])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_mover_a_secas_este(self):
        origen: Posicion = Posicion(3, 1)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        tablero: Tablero = tablero_con_piezas([(origen, caballo)])
        esperado: Tablero = tablero_con_piezas([(Posicion(3, 2), caballo)])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [ESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_mover_a_secas_oeste(self):
        origen: Posicion = Posicion(3, 1)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        tablero: Tablero = tablero_con_piezas([(origen, caballo)])
        esperado: Tablero = tablero_con_piezas([(Posicion(3, 0), caballo)])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_mover_a_secas_acumula_un_paso(self):
        origen: Posicion = Posicion(4, 6)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        tablero: Tablero = tablero_con_piezas([(origen, caballo)])
        esperado: Tablero = tablero_con_piezas([(Posicion(4, 7), caballo)])
        juego: Juego = Juego(tablero, DORADO, 1)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [ESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
        self.assertEqual(resultado.turno, DORADO)
        self.assertEqual(resultado.pasos_consumidos, 2)
 
    def test_mover_a_secas_con_el_ultimo_paso_cambia_el_turno_a_plateado(self):
        origen: Posicion = Posicion(4, 6)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        tablero: Tablero = tablero_con_piezas([(origen, caballo)])
        esperado: Tablero = tablero_con_piezas([(Posicion(4, 5), caballo)])
        juego: Juego = Juego(tablero, DORADO, 3)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
        self.assertEqual(resultado.turno, PLATEADO)
        self.assertEqual(resultado.pasos_consumidos, 0)
 
    def test_mover_a_secas_con_el_ultimo_paso_cambia_el_turno_a_dorado(self):
        origen: Posicion = Posicion(4, 6)
        caballo: Pieza = Pieza(CABALLO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([(origen, caballo)])
        esperado: Tablero = tablero_con_piezas([(Posicion(3, 6), caballo)])
        juego: Juego = Juego(tablero, PLATEADO, 3)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [SUR])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
        self.assertEqual(resultado.turno, DORADO)
        self.assertEqual(resultado.pasos_consumidos, 0)
 
    def test_mover_a_secas_pieza_sola_que_entra_a_trampa_se_retira(self):
        origen: Posicion = Posicion(2, 3)
        conejo: Pieza = Pieza(CONEJO, DORADO)
        tablero: Tablero = tablero_con_piezas([(origen, conejo)])
        esperado: Tablero = tablero_8x8_vacio()
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_mover_a_secas_pieza_con_amiga_que_entra_a_trampa_se_queda(self):
        origen: Posicion = Posicion(2, 6)
        conejo: Pieza = Pieza(CONEJO, DORADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, conejo),
            (Posicion(1, 5), conejo),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(2, 5), conejo),
            (Posicion(1, 5), conejo),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_mover_a_secas_pieza_en_trampa_se_retira_si_su_amiga_se_va(self):
        origen: Posicion = Posicion(5, 6)
        conejo: Pieza = Pieza(CONEJO, DORADO)
        tablero: Tablero = tablero_con_piezas([
            (Posicion(5, 5), conejo),
            (origen, conejo),
        ])
        esperado: Tablero = tablero_con_piezas([(Posicion(6, 6), conejo)])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    ## Arrastrar
 
    def test_arrastrar_norte_y_oeste(self):
        origen: Posicion = Posicion(3, 1)
        camello: Pieza = Pieza(CAMELLO, DORADO)
        gato: Pieza = Pieza(GATO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(3, 2), gato),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(4, 1), camello),
            (origen, gato),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [NORTE, OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_arrastrar_este_y_sur(self):
        origen: Posicion = Posicion(3, 1)
        camello: Pieza = Pieza(CAMELLO, DORADO)
        gato: Pieza = Pieza(GATO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(4, 1), gato),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(3, 2), camello),
            (origen, gato),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [ESTE, SUR])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_arrastrar_sur_y_oeste(self):
        origen: Posicion = Posicion(3, 1)
        camello: Pieza = Pieza(CAMELLO, DORADO)
        gato: Pieza = Pieza(GATO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(3, 2), gato),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(2, 1), camello),
            (origen, gato),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [SUR, OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_arrastrar_oeste_y_norte(self):
        origen: Posicion = Posicion(3, 1)
        camello: Pieza = Pieza(CAMELLO, DORADO)
        gato: Pieza = Pieza(GATO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(2, 1), gato),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(3, 0), camello),
            (origen, gato),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [OESTE, NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_arrastrar_acumula_dos_pasos(self):
        origen: Posicion = Posicion(4, 6)
        camello: Pieza = Pieza(CAMELLO, DORADO)
        gato: Pieza = Pieza(GATO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(3, 6), gato),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(4, 5), camello),
            (origen, gato),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [OESTE, NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
        self.assertEqual(resultado.turno, DORADO)
        self.assertEqual(resultado.pasos_consumidos, 2)
 
    def test_arrastrar_con_el_ultimo_paso_cambia_el_turno(self):
        origen: Posicion = Posicion(4, 6)
        camello: Pieza = Pieza(CAMELLO, PLATEADO)
        gato: Pieza = Pieza(GATO, DORADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(3, 6), gato),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(4, 5), camello),
            (origen, gato),
        ])
        juego: Juego = Juego(tablero, PLATEADO, 2)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [OESTE, NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
        self.assertEqual(resultado.turno, DORADO)
        self.assertEqual(resultado.pasos_consumidos, 0)
 
    def test_arrastrar_pieza_enemiga_a_trampa_se_retira(self):
        origen: Posicion = Posicion(5, 2)
        camello: Pieza = Pieza(CAMELLO, DORADO)
        conejo_dorado: Pieza = Pieza(CONEJO, DORADO)
        conejo_plateado: Pieza = Pieza(CONEJO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(5, 1), conejo_dorado),
            (Posicion(5, 3), conejo_plateado),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(6, 2), camello),
            (Posicion(5, 1), conejo_dorado),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [NORTE, OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_arrastrar_pieza_propia_sola_que_entra_a_trampa_se_retira(self):
        origen: Posicion = Posicion(4, 5)
        camello: Pieza = Pieza(CAMELLO, DORADO)
        gato: Pieza = Pieza(GATO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(4, 6), gato),
        ])
        esperado: Tablero = tablero_con_piezas([(origen, gato)])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [NORTE, OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_arrastrar_pieza_propia_con_amiga_que_entra_a_trampa_se_queda(self):
        origen: Posicion = Posicion(4, 5)
        camello: Pieza = Pieza(CAMELLO, DORADO)
        conejo: Pieza = Pieza(CONEJO, DORADO)
        gato: Pieza = Pieza(GATO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, camello),
            (Posicion(4, 6), gato),
            (Posicion(5, 4), conejo),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(5, 5), camello),
            (origen, gato),
            (Posicion(5, 4), conejo),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [NORTE, OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    ## Empujar
 
    def test_empujar_norte_y_este(self):
        origen: Posicion = Posicion(3, 1)
        elefante: Pieza = Pieza(ELEFANTE, DORADO)
        perro: Pieza = Pieza(PERRO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, elefante),
            (Posicion(4, 1), perro),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(4, 1), elefante),
            (Posicion(4, 2), perro),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [NORTE, ESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_empujar_este_y_norte(self):
        origen: Posicion = Posicion(3, 1)
        elefante: Pieza = Pieza(ELEFANTE, DORADO)
        perro: Pieza = Pieza(PERRO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, elefante),
            (Posicion(3, 2), perro),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(3, 2), elefante),
            (Posicion(4, 2), perro),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [ESTE, NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_empujar_sur_y_oeste(self):
        origen: Posicion = Posicion(3, 1)
        elefante: Pieza = Pieza(ELEFANTE, DORADO)
        perro: Pieza = Pieza(PERRO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, elefante),
            (Posicion(2, 1), perro),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(2, 1), elefante),
            (Posicion(2, 0), perro),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [SUR, OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_empujar_oeste_y_sur(self):
        origen: Posicion = Posicion(3, 1)
        elefante: Pieza = Pieza(ELEFANTE, DORADO)
        perro: Pieza = Pieza(PERRO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, elefante),
            (Posicion(3, 0), perro),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(3, 0), elefante),
            (Posicion(2, 0), perro),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [OESTE, SUR])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_empujar_acumula_dos_pasos(self):
        origen: Posicion = Posicion(4, 6)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        conejo: Pieza = Pieza(CONEJO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, caballo),
            (Posicion(4, 7), conejo),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(4, 7), caballo),
            (Posicion(5, 7), conejo),
        ])
        juego: Juego = Juego(tablero, DORADO, 1)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [ESTE, NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
        self.assertEqual(resultado.turno, DORADO)
        self.assertEqual(resultado.pasos_consumidos, 3)
 
    def test_empujar_con_el_ultimo_paso_cambia_el_turno(self):
        origen: Posicion = Posicion(4, 6)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        conejo: Pieza = Pieza(CONEJO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, caballo),
            (Posicion(4, 7), conejo),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(4, 7), caballo),
            (Posicion(5, 7), conejo),
        ])
        juego: Juego = Juego(tablero, DORADO, 2)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [ESTE, NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
        self.assertEqual(resultado.turno, PLATEADO)
        self.assertEqual(resultado.pasos_consumidos, 0)
 
    def test_empujar_pieza_enemiga_a_trampa_se_retira(self):
        origen: Posicion = Posicion(4, 1)
        caballo: Pieza = Pieza(CABALLO, DORADO)
        conejo: Pieza = Pieza(CONEJO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, caballo),
            (Posicion(4, 2), conejo),
        ])
        esperado: Tablero = tablero_con_piezas([(Posicion(4, 2), caballo)])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [ESTE, NORTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_empujar_pieza_propia_sola_que_ocupa_trampa_se_retira(self):
        origen: Posicion = Posicion(1, 5)
        elefante: Pieza = Pieza(ELEFANTE, DORADO)
        conejo: Pieza = Pieza(CONEJO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, elefante),
            (Posicion(2, 5), conejo),
            (Posicion(2, 6), conejo),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(2, 4), conejo),
            (Posicion(2, 6), conejo),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [NORTE, OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    def test_empujar_pieza_propia_con_amiga_que_ocupa_trampa_se_queda(self):
        origen: Posicion = Posicion(1, 5)
        elefante: Pieza = Pieza(ELEFANTE, DORADO)
        conejo_dorado: Pieza = Pieza(CONEJO, DORADO)
        conejo_plateado: Pieza = Pieza(CONEJO, PLATEADO)
        tablero: Tablero = tablero_con_piezas([
            (origen, elefante),
            (Posicion(2, 5), conejo_plateado),
            (Posicion(3, 5), conejo_dorado),
        ])
        esperado: Tablero = tablero_con_piezas([
            (Posicion(2, 5), elefante),
            (Posicion(2, 4), conejo_plateado),
            (Posicion(3, 5), conejo_dorado),
        ])
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [NORTE, OESTE])
 
        resultado: Juego = realizar_movimiento(juego, movimiento)
 
        self.assertEqual(resultado.tablero, esperado)
 
    ## No modifica los datos recibidos
 
    def test_mover_a_secas_no_modifica_el_tablero_original(self):
        origen: Posicion = Posicion(3, 1)
        tablero: Tablero = tablero_con_piezas([(origen, Pieza(CABALLO, DORADO))])
        copia: Tablero = copia_del_tablero(tablero)
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(MOVER_A_SECAS, origen, [NORTE])
 
        realizar_movimiento(juego, movimiento)
 
        self.assertEqual(tablero, copia)
 
    def test_arrastrar_no_modifica_el_tablero_original(self):
        origen: Posicion = Posicion(3, 1)
        tablero: Tablero = tablero_con_piezas([
            (origen, Pieza(CAMELLO, DORADO)),
            (Posicion(3, 2), Pieza(GATO, PLATEADO)),
        ])
        copia: Tablero = copia_del_tablero(tablero)
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(ARRASTRAR, origen, [NORTE, OESTE])
 
        realizar_movimiento(juego, movimiento)
 
        self.assertEqual(tablero, copia)
 
    def test_empujar_no_modifica_el_tablero_original(self):
        origen: Posicion = Posicion(3, 1)
        tablero: Tablero = tablero_con_piezas([
            (origen, Pieza(ELEFANTE, DORADO)),
            (Posicion(4, 1), Pieza(PERRO, PLATEADO)),
        ])
        copia: Tablero = copia_del_tablero(tablero)
        juego: Juego = Juego(tablero, DORADO, 0)
        movimiento: Movimiento = Movimiento(EMPUJAR, origen, [NORTE, ESTE])
 
        realizar_movimiento(juego, movimiento)
 
        self.assertEqual(tablero, copia)

#### Ejercicio 7

class test_ganador_del_juego(unittest.TestCase):

    def test_promueve_conejo_dorado_turno_del_oponente(self):
        t = leer_tablero([
              'rr----Rr', #7
              'c-----me', #6
              '---Ed-R-', #5
              '-M---R--', #4
              '---R----', #3
              '-rrrr---', #2
              '-H---DCC', #1
              'R-----RR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)
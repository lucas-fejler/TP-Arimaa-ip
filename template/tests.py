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

def tablero_con_piezas(piezas):
    """Auxiliar para armar tableros rápido en los tests."""
    t = tablero_8x8_vacio()
    for pos, p in piezas:
        t[pos.fila][pos.columna] = p
    return t


class test_realizar_movimiento(unittest.TestCase):

    def test_mover_secas_ok(self):
        origen = Posicion(3, 3)
        destino = Posicion(4, 3)
        t = tablero_con_piezas([(origen, Pieza(CONEJO, DORADO))])
        esperado = tablero_con_piezas([(destino, Pieza(CONEJO, DORADO))])
        j = Juego(t, DORADO, 1)
        m = Movimiento(MOVER_A_SECAS, origen, [NORTE])

        res = realizar_movimiento(j, m)

        self.assertEqual(res.tablero, esperado)
        self.assertEqual(res.turno, DORADO)
        self.assertEqual(res.pasos_consumidos, 2)

    def test_mover_secas_cambia_turno(self):
        origen = Posicion(3, 3)
        destino = Posicion(4, 3)
        t = tablero_con_piezas([(origen, Pieza(CONEJO, DORADO))])
        esperado = tablero_con_piezas([(destino, Pieza(CONEJO, DORADO))])
        j = Juego(t, DORADO, 3) # Con este llega a 4 y corta
        m = Movimiento(MOVER_A_SECAS, origen, [NORTE])

        res = realizar_movimiento(j, m)

        self.assertEqual(res.tablero, esperado)
        self.assertEqual(res.turno, PLATEADO)
        self.assertEqual(res.pasos_consumidos, 0)

    def test_aux_mover_secas(self):
        origen = Posicion(3, 3)
        t = tablero_con_piezas([(origen, Pieza(CONEJO, DORADO))])
        esperado = tablero_con_piezas([(Posicion(4, 3), Pieza(CONEJO, DORADO))])

        res = tablero_post_mover_a_secas(t, origen, NORTE)
        self.assertEqual(res, esperado)

    def test_aux_arrastrar(self):
        origen = Posicion(3, 3)
        t = tablero_con_piezas([
            (origen, Pieza(CABALLO, DORADO)),
            (Posicion(3, 4), Pieza(CONEJO, PLATEADO)),
        ])
        esperado = tablero_con_piezas([
            (Posicion(4, 3), Pieza(CABALLO, DORADO)),
            (origen, Pieza(CONEJO, PLATEADO)),
        ])

        res = tablero_post_arrastrar(t, origen, NORTE, OESTE)
        self.assertEqual(res, esperado)

    def test_aux_empujar(self):
        origen = Posicion(3, 3)
        t = tablero_con_piezas([
            (origen, Pieza(CABALLO, DORADO)),
            (Posicion(4, 3), Pieza(CONEJO, PLATEADO)),
        ])
        esperado = tablero_con_piezas([
            (Posicion(4, 3), Pieza(CABALLO, DORADO)),
            (Posicion(4, 4), Pieza(CONEJO, PLATEADO)),
        ])

        res = tablero_post_empujar(t, origen, NORTE, ESTE)
        self.assertEqual(res, esperado)

    def test_despachador_acciones(self):
        origen = Posicion(3, 3)
        t = tablero_con_piezas([(origen, Pieza(CONEJO, DORADO))])
        esperado = tablero_con_piezas([(Posicion(4, 3), Pieza(CONEJO, DORADO))])
        m = Movimiento(MOVER_A_SECAS, origen, [NORTE])
        self.assertEqual(tablero_post_movimiento(t, m), esperado)

    def test_arrastre_acumula_pasos(self):
        origen = Posicion(3, 3)
        t = tablero_con_piezas([
            (origen, Pieza(CABALLO, DORADO)),
            (Posicion(3, 4), Pieza(CONEJO, PLATEADO)),
        ])
        esperado = tablero_con_piezas([
            (Posicion(4, 3), Pieza(CABALLO, DORADO)),
            (origen, Pieza(CONEJO, PLATEADO)),
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(ARRASTRAR, origen, [NORTE, OESTE])

        res = realizar_movimiento(j, m)

        self.assertEqual(res.tablero, esperado)
        self.assertEqual(res.turno, DORADO)
        self.assertEqual(res.pasos_consumidos, 2)

    def test_realizar_movimiento_empujar(self):
        """Cubre la acción EMPUJAR y la rama else del despachador."""
        origen = Posicion(3, 3)
        t = tablero_con_piezas([
            (origen, Pieza(CABALLO, DORADO)),
            (Posicion(3, 4), Pieza(CONEJO, PLATEADO)),
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(EMPUJAR, origen, [ESTE, NORTE])

        res = realizar_movimiento(j, m)
        self.assertEqual(res.turno, DORADO)
        self.assertEqual(res.pasos_consumidos, 2)

    def test_realizar_movimiento_activa_trampa(self):
        """Verifica que se disparen las trampas correctamente al mover una pieza."""
        origen = Posicion(2, 1)
        t = tablero_con_piezas([
            (origen, Pieza(CONEJO, DORADO)),
        ])
        m = Movimiento(MOVER_A_SECAS, origen, [ESTE])
        res = tablero_post_movimiento(t, m)
        
        #No hay piezas amigas adyacentes = VACIA
        self.assertEqual(res[2][2], VACIA)

    def test_inmutabilidad_tablero(self):
        origen = Posicion(3, 3)
        t = tablero_con_piezas([(origen, Pieza(CONEJO, DORADO))])
        
        # Copia manual del tablero
        t_copia = []
        for fila in t:
            nueva_fila = []
            for casilla in fila:
                nueva_fila.append(casilla)
            t_copia.append(nueva_fila)
            
        m = Movimiento(MOVER_A_SECAS, origen, [NORTE])
        realizar_movimiento(Juego(t, DORADO, 0), m)

        self.assertEqual(t, t_copia)

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
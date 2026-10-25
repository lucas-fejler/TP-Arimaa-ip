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

    def test_8x8_vacio(self):
        t=tablero_8x8_vacio()
        self.assertTrue(tablero_bien_formado(t))
    
    def test_una_fila_corta(self):
        t = tablero_8x8_vacio()
        t[3] = t[3][:7]
        self.assertFalse(tablero_bien_formado(t))

    def test_una_fila_larga(self):
        t=tablero_8x8_vacio()
        t[3].append(VACIA)
        self.assertFalse(tablero_bien_formado(t))

    def test_faltan_filas(self):
        t = tablero_8x8_vacio()
        self.assertFalse(tablero_bien_formado(t[:7]))

    def test_sobran_filas(self):
        t=tablero_8x8_vacio()
        t2=t+ [t[0]]
        self.assertFalse(tablero_bien_formado(t2))

class test_posicion_en_tablero(unittest.TestCase):

    def test_posicion_ok(self):
        self.assertTrue(posicion_en_tablero(Posicion(5, 3)))

    def test_posicion_limite1(self):
        self.assertTrue(posicion_en_tablero(Posicion(7,7)))

    def test_posicion_limite2(self):
        self.assertTrue(posicion_en_tablero(Posicion(0,0)))

    def test_fila_erronea1(self):
        self.assertFalse(posicion_en_tablero(Posicion(-1,0)))

    def test_fila_erronea2(self):
        self.assertFalse(posicion_en_tablero(Posicion(8,0)))

    def test_columna_erronea1(self):
        self.assertFalse(posicion_en_tablero(Posicion(0,-1)))

    def test_columna_erronea2(self):
        self.assertFalse(posicion_en_tablero(Posicion(0,8)))

class test_movimiento_bien_formado(unittest.TestCase):

    def test_movimiento_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])))

    def test_moverasecas_con_dos_pasos(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE,SUR])))

    def test_moverasecas_sin_pasos(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(1, 1), [])))

    def test_arrastrar_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(1, 1), [NORTE, SUR])))

    def test_arrastrar_con_un_paso(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(1, 1), [NORTE])))

    def test_empujar_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(1, 1), [ESTE, NORTE])))

    def test_empujar_con_tres_pasos(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(1, 1), [ESTE, NORTE, SUR])))

    def test_origen_fuera_de_tablero(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(8, 1), [NORTE])))

class test_juego_bien_formado(unittest.TestCase):

    def test_juego_ok(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))

    def test_tablero_mal_formado(self):
        t = tablero_8x8_vacio()
        t[3] = t[3][:7]
        j=Juego(t,DORADO,0)
        self.assertFalse(juego_bien_formado(j))

    def test_pasos_consumidos_fuera_de_rango(self):
            j=Juego(tablero_8x8_vacio(),DORADO,4)
            self.assertFalse(juego_bien_formado(j))

    def test_pasos_consumidos_max(self):
        j=Juego(tablero_8x8_vacio(),DORADO,3)
        self.assertTrue(juego_bien_formado(j))

    def test_pasos_consumidos_negativo(self):
            j=Juego(tablero_8x8_vacio(),DORADO,-1)
            self.assertFalse(juego_bien_formado(j))

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

class test_realizar_movimiento(unittest.TestCase):
 
    def test_mover_a_secas(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---m----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '---m----', #5
               '--------', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, PLATEADO, 0) 
        jN = Juego(tN, PLATEADO, 1) 
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

#### Ejercicio 7
VACIO = '--------'


class test_hay_ganador_determinado(unittest.TestCase):

    def test_tablero_inicial_sin_ganador(self):
        j = Juego(tablero_8x8_inicial_ejemplo(), DORADO, 0)
        self.assertFalse(hay_ganador_determinado(j))

    def test_conejo_en_meta_pero_a_mitad_de_turno(self):
        t = leer_tablero(['R-------', VACIO, VACIO, VACIO, VACIO, VACIO, 'r-------', VACIO])
        j = Juego(t, DORADO, 2)
        self.assertFalse(hay_ganador_determinado(j))

    def test_ambos_con_conejos_nadie_en_meta(self):
        t = leer_tablero(['r-------', VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, 'R-------'])
        j = Juego(t, DORADO, 0)
        self.assertFalse(hay_ganador_determinado(j))
    

class test_ganador_del_juego(unittest.TestCase):

    def test_conejo_dorado_en_meta_turno_del_oponente(self):
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

    def test_conejo_plateado_en_meta_turno_del_oponente(self):
        t = leer_tablero(['r-------', VACIO, VACIO, VACIO, VACIO, VACIO, 'R-------', 'r-------'])
        j = Juego(t, DORADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), PLATEADO)

    def test_plateado_sin_conejos(self):
        t = leer_tablero(['c-------', VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, 'R-------'])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)

    def test_dorado_sin_conejos(self):
        t = leer_tablero(['r-------', VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, 'C-------'])
        j = Juego(t, DORADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), PLATEADO)

    def test_ambos_en_meta_gana_quien_jugo(self):
        t = leer_tablero(['R-------', VACIO, VACIO, VACIO, VACIO, VACIO, VACIO, 'r-------'])
        self.assertEqual(ganador_del_juego(Juego(t, DORADO, 0)), PLATEADO)
        self.assertEqual(ganador_del_juego(Juego(t, PLATEADO, 0)), DORADO)


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

    def test_vecina_al_sur(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(4, 3), SUR), Posicion(3, 3))

    def test_vecina_al_este(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(4, 3), ESTE), Posicion(4, 4))

    def test_vecina_al_oeste(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(4, 3), OESTE), Posicion(4, 2))

    def test_vecina_al_norte_fuera_del_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(7, 3), NORTE), Posicion(8, 3))

    def test_vecina_al_sur_fuera_del_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 3), SUR), Posicion(-1, 3))

    def test_vecina_al_este_fuera_del_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(4, 7), ESTE), Posicion(4, 8))

    def test_vecina_al_oeste_fuera_del_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(4, 0), OESTE), Posicion(4, -1))

class test_son_posiciones_vecinas(unittest.TestCase):

    def test_vecinas(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))

class test_casilla_en_posicion(unittest.TestCase):

    def test_casilla_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))

    def test_casilla_en_posicion_plateada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(7, 4)), Pieza(ELEFANTE, PLATEADO))

    def test_casilla_en_posicion_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(4, 4)), VACIA)

    def test_casilla_en_posicion_esquina(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(7, 7)), Pieza(CABALLO, PLATEADO))

    def test_casilla_en_posicion_conejo(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(1, 5)), Pieza(CONEJO, DORADO))

class test_hay_casilla_vacia(unittest.TestCase):

    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))

    def test_casilla_vacia_borde(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(5, 7)))

    def test_casilla_con_pieza_dorada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(0, 3)))

    def test_casilla_con_pieza_plateada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(6, 2)))

    def test_casilla_con_pieza_esquina(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(0, 0)))

class test_hay_pieza_de_color(unittest.TestCase):

    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))

    def test_hay_pieza_de_color_plateado_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(6, 4), PLATEADO))

    def test_pieza_dorada_NO_es_plateada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(0, 7), PLATEADO))

    def test_pieza_plateada_NO_es_dorada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(7, 0), DORADO))

    def test_casilla_vacia_NO_es_dorada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(3, 5), DORADO))

    def test_casilla_vacia_NO_es_plateada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(3, 5), PLATEADO))

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

    def test_vacia_hacia_sur(self):
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
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(1, 3), SUR))

    def test_vacia_hacia_este(self):
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
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(4, 0), ESTE))

    def test_vacia_hacia_oeste(self):
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
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(5, 5), OESTE))

    def test_vacia_desde_casilla_vacia(self):
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
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(2, 2), NORTE))

    def test_ocupada_por_enemiga(self):
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
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(1, 3), NORTE))

    def test_ocupada_por_amiga(self):
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
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(0, 6), ESTE))

    def test_fuera_del_tablero_al_norte(self):
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
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(7, 7), NORTE))

    def test_fuera_del_tablero_al_sur(self):
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
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(0, 0), SUR))

    def test_fuera_del_tablero_al_este(self):
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
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(4, 7), ESTE))

    def test_fuera_del_tablero_al_oeste(self):
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
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(4, 0), OESTE))

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

    def test_amiga_al_sur(self):
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
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(7, 0)))

    def test_amiga_al_este(self):
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
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(5, 5)))

    def test_amiga_al_oeste(self):
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
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(5, 6)))

    def test_amiga_en_esquina(self):
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
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(0, 0)))

    def test_solo_enemigas_vecinas(self):
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
        self.assertFalse(hay_pieza_amiga_vecina(t, Posicion(1, 2)))

    def test_sin_piezas_vecinas(self):
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
        self.assertFalse(hay_pieza_amiga_vecina(t, Posicion(5, 1)))

    def test_esquina_sin_amiga(self):
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
        self.assertFalse(hay_pieza_amiga_vecina(t, Posicion(7, 7)))

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

    def test_enemiga_mas_debil_al_norte(self):
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
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(4, 4), NORTE))

    def test_enemiga_mas_debil_al_sur(self):
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
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(6, 4), SUR))

    def test_enemiga_mas_debil_al_este(self):
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
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(3, 5), ESTE))

    def test_enemiga_mas_fuerte(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(5, 4), NORTE))

    def test_enemiga_de_igual_fuerza(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(6, 3), ESTE))

    def test_amiga_mas_debil(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(3, 4), OESTE))

    def test_casilla_vecina_vacia(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(6, 3), SUR))

    def test_vecina_fuera_del_tablero(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(7, 2), NORTE))

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

    def test_enemiga_mas_fuerte_al_norte(self):
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
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(2, 4)))

    def test_enemiga_mas_fuerte_al_sur(self):
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
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(7, 7)))

    def test_enemiga_mas_fuerte_al_este(self):
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
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(0, 5)))

    def test_solo_enemigas_mas_debiles(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(1, 4)))

    def test_enemiga_de_igual_fuerza(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(5, 3)))

    def test_solo_amigas_vecinas(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 3)))

    def test_sin_piezas_vecinas(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(7, 2)))

    def test_elefante(self):
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
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(6, 7)))

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

    def test_congelada_por_enemiga_al_norte(self):
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
        self.assertTrue(hay_pieza_congelada(t, Posicion(5, 2)))

    def test_congelada_por_enemiga_al_este(self):
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
        self.assertTrue(hay_pieza_congelada(t, Posicion(3, 1)))

    def test_enemiga_mas_fuerte_con_amiga_vecina(self):
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
        self.assertFalse(hay_pieza_congelada(t, Posicion(3, 3)))

    def test_solo_enemigas_mas_debiles(self):
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
        self.assertFalse(hay_pieza_congelada(t, Posicion(6, 2)))

    def test_solo_amiga_vecina(self):
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
        self.assertFalse(hay_pieza_congelada(t, Posicion(2, 3)))

    def test_pieza_sin_vecinas(self):
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
        self.assertFalse(hay_pieza_congelada(t, Posicion(6, 6)))

    def test_casilla_vacia(self):
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
        self.assertFalse(hay_pieza_congelada(t, Posicion(4, 4)))

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
        
    def test_arrastrar_ok(self):
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
        m = Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,OESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
            
    def test_empujar_ok(self):
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
        m = Movimiento(EMPUJAR, Posicion(0, 1), [ESTE,ESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
                
    def test_direccion_permitida_conejo_dorado(self):
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
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 1), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))      
    
    def test_direccion_permitida_conejo_plateado(self):
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
        j = Juego(t,PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 6), [SUR])
        self.assertTrue(puede_realizar_movimiento(j, m))  

    def test_direccion_NO_permitida_conejo_dorado(self):
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
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 1), [SUR])
        self.assertFalse(puede_realizar_movimiento(j, m))
        
    def test_direccion_NO_permitida_conejo_plateado(self):
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
        j = Juego(t,PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 6), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m)) 
        
    def test_casilla_vacia(self):
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
        j = Juego(t,PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(6,0), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))
        
    def test_pieza_congelada(self):
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
        j = Juego(t,PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(3,4), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))
        
    def test_pasos_de_mas(self):
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
        j = Juego(t,PLATEADO, 3)
        m = Movimiento(EMPUJAR, Posicion(0,1), [ESTE,NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))
        
    def test_mover_a_secas_sin_lugar(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '--------', #2
              '-D------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))
        
    def test_no_hay_pieza_para_arrastrar(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '----D---', #1
              '-m---mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,OESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))
        
    def test_no_hay_pieza_para_empujar(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '----D---', #1
              '-m---mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(0, 1), [NORTE,OESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))
    
    def test_empujar_sin_lugar(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '------r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--R-----', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(0, 1), [ESTE,NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))
        
    def test_completar_exactamente_cuatro_pasos(self):
        t = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '---Hr---', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        j = Juego(t, DORADO, 3)
        m = Movimiento(MOVER_A_SECAS, Posicion(3, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

        j = Juego(t, DORADO, 2)
        m = Movimiento(ARRASTRAR, Posicion(3, 3), [NORTE, OESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

        m = Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

    def test_no_puede_mover_pieza_del_oponente(self):
        t = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '---h----', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(3, 3), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_arrastrar_sin_lugar(self):
        t = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---C----', #4
              '---Hr---', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(3, 3), [NORTE, OESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

class test_direccion_de_movimiento_habilitada(unittest.TestCase):

    def test_casilla_vacia(self):
        t = tablero_8x8_vacio()
        self.assertFalse(
            direccion_de_movimiento_habilitada(t, Posicion(3, 3), NORTE)
        )

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

    def test_trampas_vacias(self):
        t0 = leer_tablero([
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
        self.assertEqual(t2, t1)

    def test_pieza_amiga_al_norte(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-R-----', #3
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
               'R-R-----', #3
               'R-H-----', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

    def test_pieza_amiga_al_sur(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H--m--', #2
               'R-R-----', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H-----', #2
               'R-R-----', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

    def test_pieza_amiga_al_este(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-HR-m--', #2
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
               'R-HR----', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

    def test_pieza_amiga_al_oeste(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'RRH--m--', #2
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
               'RRH-----', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

    def test_pieza_plateada_con_amiga(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--c-----', #6
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
               '--c-----', #6
               'H-r-----', #5
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

    def test_pieza_solo_con_enemigas_vecinas(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-r-----', #3
               'RrHr-m--', #2
               'R-r-----', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-r-----', #3
               'Rr-r----', #2
               'R-r-----', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

    def test_pieza_amiga_en_diagonal(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R--R----', #3
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
               'R--R----', #3
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

    def test_inmutabilidad_tablero(self):
        origen = Posicion(3, 3)
        t = tablero_con_piezas([(origen, Pieza(CONEJO, DORADO))])
        t_copia = [fila[:] for fila in t]
        m = Movimiento(MOVER_A_SECAS, origen, [NORTE])

        realizar_movimiento(Juego(t, DORADO, 0), m)

        self.assertEqual(t, t_copia)

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


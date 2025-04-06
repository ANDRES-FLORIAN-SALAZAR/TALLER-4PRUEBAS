import pytest
from lucesfuera.game.board import Posicion

@pytest.mark.parametrize(
    "pos_inicial,posicion_final",
    [   ((0, 0), (0, 1) ),  #1
        ((0, -5), (0, -4) ), #2
        ((0, 100), (0, 101) ),#3
        ((-5, 0), (-5, 1) ),  #4
        ((-5, -5), (-5, -4) ),#5
        ((-5, 100), (-5, 101) ),#6
        ((10, 10), (10, 11) ), #7
        ((-10, -10), (-10, -9) ),#8
        ((5, -5), (5, -4) ),   #9
        ((-5, 5), (-5, 6) ),   #10
    ]
)
def test_posicion_deberia_mover_a_la_derecha(pos_inicial:tuple, posicion_final:tuple):
    p: Posicion = Posicion(fila=pos_inicial[0], columna=pos_inicial[1])
    resultado: Posicion = p.new_posicion_derecha()
    esperado: Posicion = Posicion(fila=posicion_final[0], columna=posicion_final[1])
    
    assert resultado == esperado

@pytest.mark.parametrize(
    "pos_inicial,posicion_final",
    [   ((0, 0), (0, -1) ),  #1
        ((0, -5), (0, -6) ),  #2
        ((0, 100), (0, 99) ), #3
        ((-5, 0), (-5, -1) ), #4
        ((-5, -5), (-5, -6) ),#5
        ((-5, 100), (-5, 99) ),#6
        ((10, 10), (10, 9) ),  #7
        ((-10, -10), (-10, -11) ),#8
        ((5, -5), (5, -6) ),   #9
        ((-5, 5), (-5, 4) ),   #10
    ]
)
def test_posicion_deberia_mover_a_la_izquierda(pos_inicial:tuple, posicion_final:tuple):
    p: Posicion = Posicion(fila=pos_inicial[0], columna=pos_inicial[1])
    resultado: Posicion = p.new_posicion_izquierda()
    esperado: Posicion = Posicion(fila=posicion_final[0], columna=posicion_final[1])
    
    assert resultado == esperado

@pytest.mark.skip("No se ha implementado el movimiento hacia abajo")
@pytest.mark.parametrize(
    "pos_inicial,posicion_final",
    [   ((0, 0), (-1, 1) ), #1
        ((0, -5), (-1, -4) ),#2
        ((0, 100), (-1, 101) ),#3
        ((-5, 0), (-6, 1) ),  #4
        ((-5, -5), (-6, -4) ),#5
        ((-5, 100), (-6, 101) ),#6
        ((10, 10), (9, 11) ),  #7
        ((-10, -10), (-11, -9) ),#8
        ((5, -5), (4, -4) ),   #9
        ((-5, 5), (-6, 6) ),   #10
    ]
)
def test_posicion_deberia_mover_arriba(pos_inicial:tuple, posicion_final:tuple):
    p: Posicion = Posicion(fila=pos_inicial[0], columna=pos_inicial[1])
    resultado: Posicion = p.new_posicion_arriba()
    esperado: Posicion = Posicion(fila=posicion_final[0], columna=posicion_final[1])
    
    assert resultado == esperado

@pytest.mark.parametrize(
    "pos_inicial,posicion_final",
    [   ((0, 0), (-1, 0) ),  #1
        ((0, -5), (-1, -5) ), #2
        ((0, 100), (-1, 100) ),#3
        ((-5, 0), (-6, 0) ),  #4
        ((-5, -5), (-6, -5) ),#5
        ((-5, 100), (-6, 100) ),#6
        ((10, 10), (9, 10) ),  #7
        ((-10, -10), (-11, -10) ),#8
        ((5, -5), (4, -5) ),   #9
        ((-5, 5), (-6, 5) ),   #10
    ]
)
def test_posicion_deberia_mover_abajo(pos_inicial:tuple, posicion_final:tuple):
    p: Posicion = Posicion(fila=pos_inicial[0], columna=pos_inicial[1])
    resultado: Posicion = p.new_posicion_abajo()
    esperado: Posicion = Posicion(fila=posicion_final[0], columna=posicion_final[1])
    
    assert resultado == esperado

@pytest.mark.parametrize(
    "pos_inicial,posicion_final",
    [   ((0, 0), (-1, 0) ),  #1
        ((0, -5), (-1, -5) ), #2
        ((0, 100), (-1, 100) ),#3
        ((-5, 0), (-6, 0) ),  #4
        ((-5, -5), (-6, -5) ),#5
        ((-5, 100), (-6, 100) ),#6
        ((10, 10), (9, 10) ),  #7
        ((-10, -10), (-11, -10) ),#8
        ((5, -5), (4, -5) ),   #9
        ((-5, 5), (-6, 5) ),   #10
    ]
)
def test_posicion_deberia_mover_diagonal_arriba(pos_inicial:tuple, posicion_final:tuple):
    p: Posicion = Posicion(fila=pos_inicial[0], columna=pos_inicial[1])
    resultado: Posicion = p.new_posicion_diagonal_arriba()
    esperado: Posicion = Posicion(fila=posicion_final[0], columna=posicion_final[1])
    
    assert resultado == esperado

@pytest.mark.parametrize(
    "pos_inicial,posicion_final",
    [   ((0, 0), (1, -1) ),  #1
        ((0, -5), (1, -6) ),  #2
        ((0, 100), (1, 99) ), #3
        ((-5, 0), (-4, -1) ), #4
        ((-5, -5), (-4, -6) ),#5
        ((-5, 100), (-4, 99) ),#6
        ((10, 10), (11, 9) ),  #7
        ((-10, -10), (-9, -11) ),#8
        ((5, -5), (6, -6) ),   #9
        ((-5, 5), (-4, 4) ),   #10
    ]
)
def test_posicion_deberia_mover_diagonal_abajo(pos_inicial:tuple, posicion_final:tuple):
    p: Posicion = Posicion(fila=pos_inicial[0], columna=pos_inicial[1])
    resultado: Posicion = p.new_posicion_diagonal_abajo()
    esperado: Posicion = Posicion(fila=posicion_final[0], columna=posicion_final[1])
    
    assert resultado == esperado

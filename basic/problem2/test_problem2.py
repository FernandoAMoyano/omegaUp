import pytest
from problem2 import calculate_the_fun_level

def test_calculate_the_fun_level():
    juguetes = [10, 5, 8]
    resultado = calculate_the_fun_level(juguetes)
    assert resultado == 18

def test_con_numeros_negativos():
    juguetes = [10, -2, 5]
    resultado = calculate_the_fun_level(juguetes)
    assert resultado == 15

def test_con_un_solo_juguete():
    juguetes = [7]
    resultado = calculate_the_fun_level(juguetes)
    assert resultado == 0
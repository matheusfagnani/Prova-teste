# teste da função classificar_triangulo
import pytest
from classificar_triangulo.geometria import classificar_triangulo


# Teste equilátero, isósceles, escaleno e não triângulo
def test_equilatero():
    assert classificar_triangulo(3, 3, 3) == "Equilátero"
def test_isosceles():
    assert classificar_triangulo(3, 3, 2) == "Isósceles"
def test_escaleno():
    assert classificar_triangulo(3, 4, 5) == "Escaleno"
def test_nao_triangulo():
    assert classificar_triangulo(1, 2, 3) == "Não é um triângulo"

# Teste com lados negativos ou zero
def test_lados_negativos():
    assert classificar_triangulo(-1, 2, 3) == "Não é um triângulo"
    assert classificar_triangulo(1, -2, 3) == "Não é um triângulo"
    assert classificar_triangulo(1, 2, -3) == "Não é um triângulo"
    assert classificar_triangulo(0, 2, 3) == "Não é um triângulo"


# Teste com valores float
def test_valores_float():
    assert classificar_triangulo(  3.5, 3.5, 3.5) == "Equilátero"
    assert classificar_triangulo(3.5, 3.5, 2.5) == "Isósceles"
    assert classificar_triangulo(3.5, 4.5, 5.5) == "Escaleno"


# valor com tudo zero
def test_valores_zero():
    assert classificar_triangulo(0, 0, 0) == "Não é um triângulo"
    assert classificar_triangulo(0.0, 0.0, 0.0) == "Não é um triângulo"
    assert classificar_triangulo(0, 0, 0) == "Não é um triângulo"



# teste com valores certos mas em ordem diferente
def test_valores_outra_ordem():
    assert classificar_triangulo(3, 2, 3) == "Isósceles"
    assert classificar_triangulo(5, 4, 3) == "Escaleno"
    assert classificar_triangulo(2, 3, 3) == "Equilátero"



# teste com valores grandes
def test_valores_grandes():
    assert classificar_triangulo(3000, 3000, 3000) == "Equilátero"
    assert classificar_triangulo(3000, 3000, 2000) == "Isósceles"
    assert classificar_triangulo(3000, 4000, 5000) == "Escaleno"
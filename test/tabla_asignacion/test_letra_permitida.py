from _pytest.recwarn import T
import pytest
from src.tabla_asignacion import * 

tabla = Tabla_asignacion()

no_permitidas = ['I', 'Ñ', 'O', 'U']

@pytest.mark.letra_permitida
def test_letra_permitida():
    assert tabla.letraPermitida('A')
    assert tabla.letraPermitida('T')

@pytest.mark.letra_no_permitida
def test_letras_no_permitidas():
    for letra in no_permitidas:
        assert tabla.letraPermitida(letra) == False

@pytest.mark.letras_minusculas
def test_letras_minusculas():
    for letra in tabla.tabla:
        assert tabla.letraPermitida(letra.lower()) == False

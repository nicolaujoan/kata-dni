import pytest
from src.tabla_asignacion import *

tabla = Tabla_asignacion()

@pytest.mark.get_modulo
def test_get_modulo():
    assert tabla.getModulo() == 23
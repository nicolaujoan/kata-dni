import pytest
from src.tabla_asignacion import *

tabla = Tabla_asignacion()

@pytest.mark.get_letra
def test_get_letra():
    
    # caso fuera de rango
    assert tabla.getLetra(25) == 'posicion fuera de rango'

    # caso válido
    assert tabla.getLetra(20) == 'C'

    # caso válido contando al revés
    assert tabla.getLetra(-2) == 'K'

    
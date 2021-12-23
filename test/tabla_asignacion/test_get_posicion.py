from _pytest.recwarn import T
import pytest
from src.tabla_asignacion import * 

tabla = Tabla_asignacion()

numerosDniOk = ["78484464","72376173","01817200","95882054","63587725",
				 "26861694","21616083","26868974","40135330","89044648",
				 "80117501","34168723","76857238","66714505","66499420"]

@pytest.mark.get_posicion
def test_get_posicion():
    assert tabla.getPosicion(numerosDniOk[0]) == 0
    assert tabla.getPosicion(numerosDniOk[1]) == 3
    assert tabla.getPosicion(numerosDniOk[len(numerosDniOk) - 1]) == 3
    assert tabla.getPosicion(numerosDniOk[7]) == 6

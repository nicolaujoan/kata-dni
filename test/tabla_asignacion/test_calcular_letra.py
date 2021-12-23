import pytest
from src.tabla_asignacion import *

tabla = Tabla_asignacion()

dnis_ok = ["78484464T","72376173A","01817200Q","95882054E","63587725Q",
				 "26861694V","21616083Q","26868974Y","40135330P","89044648X",
				 "80117501Z","34168723S","76857238R","66714505S","66499420A"]

@pytest.mark.calcular_letra
def test_calcular_letra():
    for dni in dnis_ok:
        assert tabla.calcularLetra(dni[:-1]) == dni[-1]
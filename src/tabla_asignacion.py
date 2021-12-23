class Tabla_asignacion:
    
    def __init__(self) -> None:
        self.tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
    
    def getLetra(self, posicion):
        try:
            return self.tabla[posicion]
        except:
            return 'posicion fuera de rango'
    
    def getModulo(self):
        return len(self.tabla)
    
    def letraPermitida(self, letra):
        return letra in self.tabla

    def getPosicion(self, DNI_NUM):
        return (int(DNI_NUM) % self.getModulo())
    
    def calcularLetra(self, DNI_NUM):
        return self.getLetra(self.getPosicion(DNI_NUM))
    
    def mostrarTabla(self):
        print(self.tabla)
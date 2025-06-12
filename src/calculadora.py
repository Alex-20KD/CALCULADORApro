from operaciones import Operacion

class Calculadora:
    def ejecutar_operacion(self, operacion: Operacion, a, b=None):
        return operacion.ejecutar(a, b)

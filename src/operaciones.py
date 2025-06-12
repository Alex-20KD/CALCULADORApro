from abc import ABC, abstractmethod
import math

class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, a, b=None):
        pass

class Suma(Operacion):
    def ejecutar(self, a, b=None):
        return a + b

class Resta(Operacion):
    def ejecutar(self, a, b=None):
        return a - b

class Multiplicacion(Operacion):
    def ejecutar(self, a, b=None):
        return a * b

class Division(Operacion):
    def ejecutar(self, a, b=None):
        if b == 0:
            raise ZeroDivisionError("División por cero")
        return a / b

class Potencia(Operacion):
    def ejecutar(self, a, b=None):
        return a ** b

class RaizCuadrada(Operacion):
    def ejecutar(self, a, b=None):
        if a < 0:
            raise ValueError("Raíz cuadrada de número negativo")
        return math.sqrt(a)

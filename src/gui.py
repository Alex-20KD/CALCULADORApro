import tkinter as tk
import re
import logging
from calculadora import Calculadora
from operaciones import Suma, Resta, Multiplicacion, Division, Potencia, RaizCuadrada
from data_source import guardar_operacion_log

# Configurar logging
logging.basicConfig(
    filename='smart_calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SmartCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("320x470")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.calculadora = Calculadora()
        self.display_text = tk.StringVar()
        self.expression = ""

        self._crear_pantalla()
        self._crear_botones()

    def _crear_pantalla(self):
        display = tk.Entry(
            self.root, textvariable=self.display_text, font=('Helvetica', 28),
            bd=0, bg="#1e1e1e", fg="#00FF99", justify='right', insertbackground='white'
        )
        display.pack(expand=True, fill="both", ipadx=8, ipady=20, padx=10, pady=10)

    def _crear_botones(self):
        botones = [
            ["C", "√", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""]
        ]

        for fila in botones:
            frame = tk.Frame(self.root, bg="#1e1e1e")
            frame.pack(expand=True, fill="both")

            for texto in fila:
                if texto:
                    boton = tk.Button(
                        frame, text=texto, font=("Helvetica", 18),
                        fg="white", bg="#333333", bd=0,
                        activebackground="#555555", activeforeground="#00FF99",
                        command=lambda txt=texto: self._boton_presionado(txt)
                    )
                else:
                    boton = tk.Label(frame, text="", bg="#1e1e1e")
                boton.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def _boton_presionado(self, tecla):
        operadores = "+-*/^"
        if tecla == "C":
            self.expression = ""
        elif tecla == "=":
            self._evaluar()
            return
        elif tecla == "√":
            self._evaluar_raiz()
            return
        elif tecla in operadores:
            if self.expression and self.expression[-1] not in operadores:
                self.expression += tecla
        else:
            self.expression += tecla

        self.display_text.set(self.expression)

        def _evaluar(self):
            try:
                if not self.expression:
                    return

            match = re.fullmatch(r'\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*/\^])\s*(-?\d+(?:\.\d+)?)\s*', self.expression)
            if not match:
                resultado = eval(self.expression)

                # 🧨 Code smell: duplicación innecesaria
                log_entry = f"Evaluación eval(): {self.expression} = {resultado}"
                logging.info(log_entry)
                guardar_operacion_log(log_entry, resultado)

                logging.info(log_entry)  # ← duplicado innecesario
                guardar_operacion_log(log_entry, resultado)  # ← duplicado innecesario

                self.expression = str(resultado)
                self.display_text.set(self.expression)
                return

            a = float(match.group(1))
            operador = match.group(2)
            b = float(match.group(3))

            operacion = self._obtener_operacion(operador)
            resultado = self.calculadora.ejecutar_operacion(operacion, a, b)

            log_text = f"{a} {operador} {b} = {resultado}"
            logging.info(log_text)
            guardar_operacion_log(log_text, resultado)

            self.expression = str(resultado)
            self.display_text.set(self.expression)

        except Exception as e:
            print(f"Excepción capturada: {e}")
            logging.error(f"Error al evaluar: {e}")
            self.display_text.set("ERROR")
            self.expression = ""


    def _evaluar_raiz(self):
        try:
            if not self.expression:
                return
            valor = float(self.expression)
            operacion = RaizCuadrada()
            resultado = self.calculadora.ejecutar_operacion(operacion, valor)
            log_text = f"√{valor} = {resultado}"
            logging.info(log_text)
            guardar_operacion_log(log_text, resultado)  

            self.expression = str(resultado)
            self.display_text.set(self.expression)
        except Exception as e:
            logging.error(f"Error en raíz cuadrada: {e}")
            self.display_text.set("ERROR")
            self.expression = ""

    def _obtener_operacion(self, operador_str):
        return {
            '+': Suma(),
            '-': Resta(),
            '*': Multiplicacion(),
            '/': Division(),
            '^': Potencia()
        }.get(operador_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartCalculator(root)
    root.mainloop()

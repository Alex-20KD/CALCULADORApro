import tkinter as tk
import math
import logging

# Configuración del logger
logging.basicConfig(
    filename='smart_calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SmartCalculator:
    """
    Calculadora con funciones básicas y estilo moderno.
    """

    def __init__(self, root):  # ← CORREGIDO el constructor
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("320x470")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_text = tk.StringVar()

        self._crear_pantalla()
        self._crear_botones()

    def _crear_pantalla(self):
        """
        Interfaz de la calculadora
        """
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
                if texto != "":
                    boton = tk.Button(
                        frame, text=texto, font=("Helvetica", 18),
                        fg="white", bg="#333333", bd=0,
                        activebackground="#555555", activeforeground="#00FF99",
                        command=lambda txt=texto: self._boton_presionado(txt)
                    )
                else:
                    boton = tk.Label(frame, text="", bg="#1e1e1e")  # Espacio vacío

                boton.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    def _boton_presionado(self, tecla):
        """
        Define lo que hace cada botón
        """
        try:
            if tecla == "C":
                self.expression = ""
            elif tecla == "=":
                self._evaluar()
                return
            elif tecla == "√":
                self._evaluar_raiz()
                return
            elif tecla == "^":
                self.expression += "**"
            else:
                self.expression += str(tecla)

            self.display_text.set(self.expression)
        except Exception as e:
            self.display_text.set("ERROR")
            logging.error(f"Error al presionar tecla {tecla}: {e}")

    def _evaluar(self):
        """
        Evalúa la expresión matemática actual
        """
        try:
            resultado = eval(self.expression)
            self.expression = str(resultado)
            self.display_text.set(self.expression)
            logging.info(f"Operación exitosa: {resultado}")
        except Exception as e:
            self.display_text.set("ERROR")
            self.expression = ""
            logging.error(f"Error al evaluar expresión: {e}")

    def _evaluar_raiz(self):
        """
        Calcula la raíz cuadrada del valor actual
        """
        try:
            valor = eval(self.expression)
            if valor < 0:
                raise ValueError("Raíz negativa no permitida")
            resultado = math.sqrt(valor)
            self.expression = str(resultado)
            self.display_text.set(self.expression)
            logging.info(f"Raíz cuadrada de {valor}: {resultado}")
        except Exception as e:
            self.display_text.set("ERROR")
            self.expression = ""
            logging.error(f"Error en raíz cuadrada: {e}")


# CORREGIDO el nombre del bloque principal
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartCalculator(root)
    root.mainloop()

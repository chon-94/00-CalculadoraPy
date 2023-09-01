import tkinter as tk
from tkinter import messagebox

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.display_var = tk.StringVar()
        self.display_var.set("")

        self.create_widgets()

    def create_widgets(self):
        # Crear la caja de texto para mostrar la entrada y el resultado
        self.display = tk.Entry(self.root, textvariable=self.display_var, font=("Helvetica", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        # Definir la disposición de los botones en una lista
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Crear los botones en función de la disposición definida
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 15), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == "=":
            try:
                # Evaluar la expresión ingresada y mostrar el resultado en la caja de texto
                result = eval(self.display_var.get())
                self.display_var.set(str(result))
            except:
                messagebox.showerror("Error", "Operación inválida")
        else:
            # Agregar el valor del botón presionado a la caja de texto
            current_text = self.display_var.get()
            self.display_var.set(current_text + value)

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    
    # Crear la instancia de la aplicación de la calculadora
    app = CalculadoraApp(root)
    
    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()

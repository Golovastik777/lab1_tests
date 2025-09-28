import tkinter as tk

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой калькулятор")

        self.entry = tk.Entry(root, width=20, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+', '.'
        ]

        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(root, text=button_text, width=5, foreground="black", background="orange", activebackground="red",  height=2, command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Ошибка")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)

class RectangleCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор прямоугольника")

        label1 = tk.Label(root, text="Введите длину:")
        label1.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        label2 = tk.Label(root, text="Введите ширину:")
        label2.pack()

        self.width_entry = tk.Entry(root)
        self.width_entry.pack()

        calculate_area_button = tk.Button(root, foreground="black", background="orange", activebackground="red", text="Рассчитать площадь", command=self.calculate_area)
        calculate_area_button.pack()

        calculate_perimeter_button = tk.Button(root, foreground="black", background="orange", activebackground="red", text="Рассчитать периметр", command=self.calculate_perimeter)
        calculate_perimeter_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()


        calculate_canvas_button = tk.Button(root, foreground="black", background="orange", activebackground="red", text="Нарисовать Фигуру", command=self.look_figure)
        calculate_canvas_button.pack()

        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()

    def calculate_area(self):
        length = float(self.length_entry.get())
        width = float(self.width_entry.get())
        area = length * width
        self.result_label.config(text=f"Площадь: {area}")

    def calculate_perimeter(self):
        length = float(self.length_entry.get())
        width = float(self.width_entry.get())
        perimeter = 2 * (length + width)
        self.result_label.config(text=f"Периметр: {perimeter}")

    def look_figure(self):
        length = float(self.length_entry.get())
        width = float(self.width_entry.get())
        self.canvas.delete("all")
        self.canvas.create_rectangle(50, 50, 50 + length * 10, 50 + width * 10, outline="black")



class Options:
    def __init__(self, root):
        self.root = root
        self.root.title("Справка")

        label1 = tk.Label(root, text="Справка")
        label1.pack()
        label2 = tk.Label(root, text="В Python есть довольно много GUI фреймворков (graphical user interface), однако только Tkinter встроен в стандартную библиотеку языка.")
        label2.pack()

def show_calculator():
    calculator_window = tk.Toplevel()
    app = CalculatorGUI(calculator_window)

def show_rectangle_calculator():
    rectangle_calculator_window = tk.Toplevel()
    app = RectangleCalculatorGUI(rectangle_calculator_window)

def exit_app():
    root.destroy()

def show_options():
    options_window = tk.Toplevel()
    app = Options(options_window)

root = tk.Tk()
root.title("Меню выбора")

menu = tk.Menu(root)
root.config(menu=menu)

calc_menu = tk.Menu(menu)
menu.add_cascade(label="Выберите", menu=calc_menu)
calc_menu.add_command(label="Калькулятор", command=show_calculator)
calc_menu.add_command(label="Прямоугольник", command=show_rectangle_calculator)

exit_menu = tk.Menu(menu)
menu.add_cascade(label="Выход", command=exit_app)

options_menu = tk.Menu(menu)
menu.add_cascade(label="Справка", command=show_options)

root.mainloop()

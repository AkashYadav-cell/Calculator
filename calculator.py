import tkinter as tk
from tkinter import ttk
import math

class SC_Calculator():
    def __init__(self, root):
        self.root = root
        self.root.title('Scientific Calculator')
        self.root.configure(bg='#2c3e50')
        self.root.resizable(width=False, height=False)

        self.current = ''
        self.inp_value = True
        self.result = False

        self.create_widgets()

    def create_widgets(self):
        self.ent_field = ttk.Entry(self.root, font=('Arial', 25), justify="right")
        self.ent_field.grid(row=0, columnspan=8, padx=10, pady=10, sticky='nsew')
        self.ent_field.insert(0, '0')

        button_texts = [
            ('CE', 1, 0), ('√', 1, 1), ('π', 1, 2), ('e', 1, 3), ('Deg', 1, 4), ('Rad', 1, 5), ('Exp', 1, 6), ('x!', 1, 7),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('sin', 2, 4), ('cos', 2, 5), ('tan', 2, 6), ('1/x', 2, 7),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('sinh', 3, 4), ('cosh', 3, 5), ('tanh', 3, 6), ('|x|', 3, 7),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('ln', 4, 4), ('log10', 4, 5), ('log2', 4, 6), ('x^2', 4, 7),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3), ('x^3', 5, 4), ('10^x', 5, 5)
        ]

        for (text, row, col) in button_texts:
            button = ttk.Button(self.root, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

        for i in range(8):
            self.root.columnconfigure(i, weight=1)
        for i in range(6):
            self.root.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char.isdigit() or char == '.':
            self.enter_num(char)
        elif char in '+-*/':
            self.standard_ops(char)
        elif char == '=':
            self.standard_ops(char)
        elif char == 'CE':
            self.clear_entry()
        elif char == '√':
            self.sq_root()
        elif char == 'π':
            self.pi()
        elif char == 'e':
            self.e()
        elif char == 'Deg':
            self.deg()
        elif char == 'Rad':
            self.rad()
        elif char == 'Exp':
            self.exp()
        elif char == 'x!':
            self.fact()
        elif char == 'sin':
            self.sin()
        elif char == 'cos':
            self.cos()
        elif char == 'tan':
            self.tan()
        elif char == 'sinh':
            self.sinh()
        elif char == 'cosh':
            self.cosh()
        elif char == 'tanh':
            self.tanh()
        elif char == 'ln':
            self.ln()
        elif char == 'log10':
            self.log_10()
        elif char == 'log2':
            self.log_2()
        elif char == 'x^2':
            self.pow_2()
        elif char == 'x^3':
            self.pow_3()
        elif char == '10^x':
            self.pow_10_n()
        elif char == '1/x':
            self.one_div_x()
        elif char == '|x|':
            self.abs()

    def entry(self, value):
        self.ent_field.delete(0, 'end')
        self.ent_field.insert(0, value)

    def enter_num(self, num):
        self.result = False
        firstnum = self.ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum + secondnum
        self.entry(self.current)

    def standard_ops(self, val):
        temp_str = self.ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.entry(ans)
            else:
                self.entry(temp_str + val)
            self.inp_value = False
        except (ValueError, SyntaxError):
            self.entry('Error')

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.entry(0)
        self.inp_value = True

    def sq_root(self):
        try:
            self.current = math.sqrt(float(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def pi(self):
        self.result = False
        self.current = math.pi
        self.entry(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.entry(self.current)

    def deg(self):
        try:
            self.result = False
            self.current = math.degrees(float(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def rad(self):
        try:
            self.result = False
            self.current = math.radians(float(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def exp(self):
        try:
            self.result = False
            self.current = math.exp(float(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def fact(self):
        try:
            self.result = False
            self.current = math.factorial(int(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def sin(self):
        try:
            self.result = False
            self.current = math.sin(math.radians(float(self.ent_field.get())))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def cos(self):
        try:
            self.result = False
            self.current = math.cos(math.radians(float(self.ent_field.get())))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def tan(self):
        try:
            self.result = False
            self.current = math.tan(math.radians(float(self.ent_field.get())))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def sinh(self):
        try:
            self.result = False
            self.current = math.sinh(math.radians(float(self.ent_field.get())))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def cosh(self):
        try:
            self.result = False
            self.current = math.cosh(math.radians(float(self.ent_field.get())))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def tanh(self):
        try:
            self.result = False
            self.current = math.tanh(math.radians(float(self.ent_field.get())))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def ln(self):
        try:
            self.result = False
            self.current = math.log(float(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def log_10(self):
        try:
            self.result = False
            self.current = math.log10(float(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def log_2(self):
        try:
            self.result = False
            self.current = math.log2(float(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def pow_2(self):
        try:
            self.result = False
            self.current = int(self.ent_field.get())**2
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def pow_3(self):
        try:
            self.result = False
            self.current = int(self.ent_field.get())**3
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def pow_10_n(self):
        try:
            self.result = False
            self.current = 10**int(self.ent_field.get())
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def one_div_x(self):
        try:
            self.result = False
            self.current = 1 / float(self.ent_field.get())
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

    def abs(self):
        try:
            self.result = False
            self.current = abs(float(self.ent_field.get()))
            self.entry(self.current)
        except (ValueError, SyntaxError):
            self.entry('Error')

if __name__ == '__main__':
    root = tk.Tk()
    app = SC_Calculator(root)
    root.mainloop()

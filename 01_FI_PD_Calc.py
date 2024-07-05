import tkinter as tk
import re
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x450")
        self.expression = ""

        self.input_text = tk.StringVar()
        input_frame = tk.Frame(self.root, width=100, height=20, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=27, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=5)
        self.create_buttons()

    def create_buttons(self):
        btns_frame = tk.Frame(self.root, width=400, height=450, bg="light pink")
        btns_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('%', 5, 2), ('C', 5, 3),
            ('√', 6, 0), ('^', 6, 1), ('!', 6, 2), ('DEL', 6, 3)
        ]

        for button in buttons:
            if len(button) == 3:
                text, row, col = button
                self.create_button(text, row, col, btns_frame)
            else:
                text, row, col, colspan = button
                self.create_button(text, row, col, btns_frame, colspan)

    def create_button(self, text, row, col, frame, colspan=1):
        btn_width = 8 if colspan == 1 else 17 
        btn = tk.Button(frame, text=text, fg="black",font=('arial',12,'bold'), width=btn_width, height=3, bd=0, bg="grey", cursor="hand2",
                        command=lambda t=text: self.on_button_click(t))
        btn.grid(row=row, column=col, columnspan=colspan, padx=1, pady=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                processed_expression = self.preprocess_expression(self.expression)
                result = str(eval(processed_expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        elif char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == 'DEL':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == '√':
            try:
                result = str(math.sqrt(eval(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        elif char == '!':
            try:
                result = str(math.factorial(int(self.expression)))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def preprocess_expression(self, expr):
        expr = re.sub(r'(\d)(\()', r'\1*\2', expr)
        expr = re.sub(r'(\d+)%', r'\1/100', expr)
        expr = re.sub(r'\^', r'**', expr)
        return expr

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()

import tkinter as tk
import re

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.expression = ""

        self.input_text = tk.StringVar()

        # Create the input field
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Create the buttons
        self.create_buttons()

    def create_buttons(self):
        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('%', 5, 2), ('C', 5, 3),
            ('DEL', 6, 0,4)  # Adjusted DEL button to span across multiple columns
        ]

        for button in buttons:
           if len(button) == 3:
                text, row, col = button
                self.create_button(text, row, col, btns_frame)
           else:
                text, row, col, colspan = button
                self.create_button(text, row, col, btns_frame, colspan)


    def create_button(self, text, row, col, frame,colspan = 1):
        btn_width = 10 if colspan == 1 else 21  # Adjust button width based on colspan
        btn = tk.Button(frame, text=text, fg="black", width=btn_width, height=3, bd=0, bg="blue", cursor="hand2",
                        command=lambda t=text: self.on_button_click(t))
        btn.grid(row=row, column=col, columnspan=colspan, padx=1, pady=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                # Preprocess the expression to handle cases like 9(6*7)
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
        else:
            # Allow addition of parentheses and other characters
            self.expression += str(char)
            self.input_text.set(self.expression)

    def preprocess_expression(self, expr):
        # Insert multiplication operator where needed
        expr = re.sub(r'(\d)(\()', r'\1*\2', expr)
        expr = re.sub(r'(\d+)%',r'\1/100',expr)
        return expr

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()

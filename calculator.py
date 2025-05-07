import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the current expression
        self.entry = tk.Entry(self.root, font=("Arial", 20), justify="right", bd=10)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Buttons for digits and operations
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for i, button in enumerate(buttons):
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, font=("Arial", 18), command=action, width=5, height=2).grid(row=(i // 4) + 1, column=i % 4)

        # Adjust grid weights for responsiveness
        for i in range(5):  # 4 rows + 1 for entry
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i % 4, weight=1)

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
        elif button == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += button
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

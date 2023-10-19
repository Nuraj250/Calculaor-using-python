# used for library for creating the GUI
import tkinter as tk
from tkinter import *


class Calculator(tk.Tk):

    # used to define constructor method in  python
    def __init__(self):

        # used to call the constructor of the parent class (tk.Tk) to initialize the main window of the GUI application.
        super().__init__()

        # used to set the title of the calculator window to "Calculator."
        self.title("Calculator")

        #  This line sets the initial size and position of the calculator window.
        #  (465x600) specifies the window size to be 465 pixels in width and 600 pixels in heigh.
        #  (100+200) part indicates the initial position of the window on the screen,
        self.geometry("465x600+500+100")

        # used to configure the background color of the calculator window
        self.configure(bg="#17161b")

        # used to  create an instance of StringVar, which is a special Tkinter variable used to store and track changes to the text or string values.
        self.expression_var = StringVar()

        # used to create a Text widget within the calculator window.
        self.display = Text(self, font=('Arial', 30), width=20, height=2)

        # used to place the Text widget in the calculator window using the grid geometry manager
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # used for create and place  calculator buttons:
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        # This is a for loop that iterates through each button_text in the buttons list.

        # r and c are initialized to 1 and 0, to keep track of the current row (r) and column (c) where the buttons are being placed on the calculator's grid.
        r = 1
        c = 0

        # This is a for loop that iterates through each button_text in the buttons list.
        for button_text in buttons:

            # used to create button view
            button = Button(self, text=button_text, font=("Arial", 15, "bold"),
                            command=lambda text=button_text: self.on_button_click(text), width=8, height=4,
                            bg="#2a2d36", bd=1, fg="#fff")
            button.grid(row=r, column=c, padx=3, pady=3)

            # c is incremented by 1 for each button placed, and if c exceeds 3 it's reset to 0, and r is incremented to move to the next row.
            c += 1
            if c > 3:
                c = 0
                r += 1

    # used for every button click
    def on_button_click(self, text):

        current_text = self.display.get("1.0",
                                        "end-1c")  # Get the current text with the range "1.0" to "end-1c" to fetch the entire contents of the Text widget.
        if text == "=":
            try:
                # set calculation current text calculation to string
                result = str(eval(current_text))

                # Clear the text
                self.display.delete("1.0", "end")

                # Insert the result
                self.display.insert("end", result)
            except Exception as e:

                # Clear the text
                self.display.delete("1.0", "end")

                # Insert the result
                self.display.insert("end", "Error")

        # when enter c button
        elif text == "C":

            # clear the text
            self.display.delete("1.0", "end")

        else:
            # keep the text till press "=" or "c"
            self.display.insert("end", text)


# The code checks if the script is run as the main program,(__name__= build in variable)
# and if so, it creates an instance of the Calculator class and starts the GUI event loop using app.mainloop(),
# which keeps the calculator window running until the user closes it.

if __name__ == "__main__":
    app = Calculator()

    # main loop provide by tkinter lib to proces  user event like button click window resize
    app.mainloop()

import tkinter as tk


root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x530")
root.configure(bg="Gray")

# Create a display
display = tk.Entry(root, font=("Helvetica", 32), justify="right", bd=20, background="#363431", foreground="#cfcfcf")
display.grid(row=0, column=0, columnspan=4, pady=5, sticky="NSEW")
display.insert(0, "0")

# Setting up desired buttons
buttons = [
    ["C", "", "<--", ""],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]


# Creates grids for buttons, that can retain size if changing screen size.
# noinspection PyUnresolvedReferences
def create_grids():
    total_rows = 6
    total_columns = 4

    for row in range(total_rows):
        tk.Grid.rowconfigure(root, row, weight=1)
    for column in range(total_columns):
        tk.Grid.columnconfigure(root, column, weight=1)


# Creating buttons that were set previously. I really need to work on that lambda. I barely understand whati did.
def create_buttons():
    for x_pos, row in enumerate(buttons):
        for y_pos, curr_btn in enumerate(row):
            if x_pos == 0 and curr_btn != "":
                command = lambda btn=curr_btn: button_press(btn)
                button = tk.Button(root, text=curr_btn, font=("Helvetica", 16), width=10, height=2,
                                   command=command, bg="#363431", foreground="#cfcfcf")
                button.grid(row=x_pos + 1, column=y_pos, columnspan=2, sticky="NSEW")
                continue
            elif x_pos == 0 and curr_btn == "":
                continue
            command = lambda btn=curr_btn: button_press(btn)
            button = tk.Button(root, text=curr_btn, font=("Helvetica", 16), width=10, height=3,
                               command=command, bg="#363431", foreground="#cfcfcf")
            button.grid(row=x_pos+1, column=y_pos, sticky="NSEW")


# Makes decimals only appear when it is available
def fix_decimal(value):
    for x in reversed(str(value)):
        if x == "0":
            display.delete(len(display.get()) - 1, "end")
            print(display.get())
            return False
        elif x == ".":
            display.delete(len(display.get()) - 1, "end")
            print(display.get())
            return True
        else:
            return True


# Makes buttons do their bidding in various ways...
def button_press(btn):
    operator_list = ["+", "-", "*", "/", "."]
    for operator in operator_list:
        if operator == btn:
            display.insert("end", operator)
            return
    # Clears display and makes it 0
    if btn == "C":
        display.delete(0, "end")
        display.insert(0, "0")
    # Erase last symbol.
    elif btn == "<--":
        display.delete(len(display.get())-1, "end")
        if display.get() == "":
            display.insert(0, "0")
        return
    elif btn == "=":
        # Evaluate the expression and display the result.
        # This should be reworked as it's full of flaws, but for now it does its job well enough.
        try:
            result = eval(display.get())
            display.delete(0, "end")
            display.insert(0, result)
            fixed_decimal = False
            while not fixed_decimal:
                fixed_decimal = fix_decimal(display.get())
        # More like placeholder. Needs work.
        except Exception:
            display.delete(0, "end")
            display.insert(0, "Error")
    else:
        # Adds number button press to display
        for number in range(10):
            if str(number) == btn:
                if display.get() == "0":
                    display.delete(0)
                display.insert("end", str(number))


# For determining button positions in X and Y positions. Can be Deleted.
def print_numbers():
    for x_pos, row in enumerate(buttons):
        for y_pos, curr_btn in enumerate(row):
            print(curr_btn, end="  ")
            print("x:" + str(x_pos) + "  " + "y:" + str(y_pos))


create_grids()
create_buttons()
root.mainloop()

# Requires Python 3+
# Creates a window and asks for three arguments to generate the CWT. Last entry takes weight of an individual item and generates the rate for an individual case of that weight

import tkinter as tk

# Calculates CWT using 3 parameters, it was written in this way to allow for more ease of copy/pasting
def CWT_Calc(weight,freight,pallets):
    try:
        weight = weight - pallets * 50
        if not weight == 0:
            return freight/(weight*.01)
        else:
            return 0
    except(ValueError):
        "NaN"

def Warning_pane():
    win_warning = tk.Toplevel()
    win_warning.title("Value Error")
    win_warning.geometry("400x50")
    lbl_warning = tk.Label(master = win_warning,text = "Value Error: all entries must be numbers with no letters or symbols")
    lbl_warning.pack()

    win_warning.mainloop()

# Calculate is the function to actually calculate the individual case weight
def Calculate():
    try:
        return round(CWT_Calc(float(ent_weight.get()),float(ent_total.get()),int(ent_pallets.get())) * .01 * float(ent_rate2.get())+.01,2)
    except(ValueError):
        return "NaN"

# Handles the enter button for calculating and displaying CWT. Currently CWT is not stored anywhere and is just called every time it is used(change?)
def handle_enter():
    try:
        lbl_rate["text"] = f"CWT: ${CWT_Calc(float(ent_weight.get()),float(ent_total.get()),int(ent_pallets.get()))}"
    except(ValueError):
        Warning_pane()


# Handles the calculate button, which calls the calculate function and formats the result in a user friendly way.
def handle_calc():
    try:
        lbl_rate3["text"] = f"${Calculate()}/case"
    except(ValueError):
        Warning_pane()

window = tk.Tk()
window.title("CWT Freight Calculator")
window.geometry("400x300")
frm_main = tk.Frame()
frm_pallets = tk.Frame(master = frm_main)
frm_weight = tk.Frame(master = frm_main)
frm_total = tk.Frame(master = frm_main)
frm_buttons = tk.Frame(master = frm_main)
frm_rate = tk.Frame(master = frm_main)
frm_rate2 = tk.Frame(master = frm_main)
frm_rate3 = tk.Frame(master = frm_main)
frm_pallets.columnconfigure([0,1],minsize=50,weight=1)
frm_pallets.rowconfigure(0,minsize=15,weight=1)
frm_weight.columnconfigure([0,1],minsize=50,weight=1)
frm_weight.rowconfigure(0,minsize=15,weight=1)
frm_total.columnconfigure([0,1],minsize=50,weight=1)
frm_total.rowconfigure(0,minsize=15,weight=1)
frm_buttons.columnconfigure(0,minsize=50,weight=1)
frm_buttons.rowconfigure(0,minsize=15,weight=1)
frm_rate.columnconfigure([0,1],minsize=50,weight=1)
frm_rate.rowconfigure(0,minsize=15,weight=1)
frm_rate2.columnconfigure([0,1],minsize=50,weight=1)
frm_rate2.rowconfigure(0,minsize=15,weight=1)
frm_rate3.columnconfigure(0,minsize=50,weight=1)
frm_rate3.rowconfigure([0,1],minsize=15,weight=1)

lbl_pallets = tk.Label(master = frm_pallets, text ="Number of pallets being used:")
lbl_weight = tk.Label(master = frm_weight, text ="Total weight of the order(including pallets):")
lbl_total = tk.Label(master = frm_total, text ="Total Freight cost of order:")
lbl_rate = tk.Label(master = frm_rate, text = "CWT: $0.00")
lbl_rate3 = tk.Label(master = frm_rate3, text = "$0.00/case")
lbl_rate2 = tk.Label(master = frm_rate2, text = "Enter Weight of indivdual case:")
lbl_rate3.grid(row = 1, column = 0, sticky = "nsew")
lbl_rate2.grid(row = 0, column = 0, sticky = "nsew")
lbl_rate.grid(row = 0, column = 0, sticky = "nsew")
lbl_pallets.grid(row = 0, column = 0, sticky = "nsew")
lbl_weight.grid(row = 0, column = 0, sticky = "nsew")
lbl_total.grid(row = 0, column = 0, sticky = "nsew")

ent_pallets = tk.Entry(master = frm_pallets)
ent_weight = tk.Entry(master = frm_weight)
ent_total = tk.Entry(master  = frm_total)
ent_rate2 = tk.Entry(master = frm_rate2)
ent_rate2.grid(row = 0, column = 1, sticky = "nsew")
ent_pallets.grid(row = 0, column = 1, sticky = "nsew")
ent_weight.grid(row = 0, column = 1, sticky = "nsew")
ent_total.grid(row = 0, column = 1, sticky = "nsew")

btn_enter = tk.Button(master = frm_buttons, text = "Enter",command = handle_enter)
btn_calc = tk.Button(master = frm_rate3, text = "Calculate", command = handle_calc)
btn_calc.grid(row = 0, column = 0, sticky = "nsew")
btn_enter.grid(row = 0, column = 0, sticky = "nsew")

frm_pallets.pack()
frm_weight.pack()
frm_total.pack()
frm_buttons.pack()
frm_rate.pack()
frm_rate2.pack()
frm_rate3.pack()
frm_main.pack()

window.mainloop()
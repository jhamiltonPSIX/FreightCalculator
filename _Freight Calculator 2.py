#Simplified version of _Freight Calculator, I removed the second window and removed the option to have multiple items at once. But now the program actually works
#I replaced that multiple item functionality with a pallet entry (soon to be automated?). Will calculate more accurate CWT by assigning all cost to the item

import tkinter as tk

def CWT_Calc(weight,freight,pallets):
    weight = weight - pallets * 50
    if not weight == 0:
        return freight/(weight*.01)
    else:
        return 0

def Calculate():
    return CWT_Calc(float(ent_weight.get()),float(ent_total.get()),int(ent_pallets.get())) * .01 * float(ent_rate2.get())

def handle_enter():
    lbl_rate["text"] = f"CWT: ${CWT_Calc(float(ent_weight.get()),float(ent_total.get()),int(ent_pallets.get()))}"

def handle_calc():
    lbl_rate2["text"] = f"${Calculate()}"

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

lbl_pallets = tk.Label(master = frm_pallets, text ="Number of pallets being used:")
lbl_weight = tk.Label(master = frm_weight, text ="Total weight of the order(including pallets):")
lbl_total = tk.Label(master = frm_total, text ="Total Freight cost of order:")
lbl_rate = tk.Label(master = frm_rate,text = "0.00")
lbl_rate2 = tk.Label(master = frm_rate2,text = "0.00")
lbl_rate2.pack()
lbl_rate.pack()
lbl_pallets.pack()
lbl_weight.pack()
lbl_total.pack()

ent_pallets = tk.Entry(master = frm_pallets)
ent_weight = tk.Entry(master = frm_weight)
ent_total = tk.Entry(master  = frm_total)
ent_rate2 = tk.Entry(master = frm_rate2)
ent_rate2.pack()
ent_pallets.pack()
ent_weight.pack()
ent_total.pack()

btn_enter = tk.Button(master = frm_buttons, text = "Enter",command = handle_enter)
btn_calc = tk.Button(master = frm_rate2, text = "Calculate", command = handle_calc)
btn_calc.pack()
btn_enter.pack()

frm_pallets.pack()
frm_weight.pack()
frm_total.pack()
frm_buttons.pack()
frm_rate.pack()
frm_rate2.pack()
frm_main.pack()

window.mainloop()

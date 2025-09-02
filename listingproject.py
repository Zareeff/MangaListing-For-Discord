import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def getinfo0():
    val0 = input_text0.get()
    val1 = input_text1.get()
    val2 = input_text2.get()
    val3 = input_text3.get()
    val4 = input_text4.get()
    val5 = input_text4.get()
    val6= input_text4.get()
    val7 = input_text4.get()
    val8 = input_text4.get()
    val9 = input_text4.get()
    val10 = input_text4.get()
    val11 = input_text4.get()
    val12 = input_text4.get()
    
    output_text.config(text=f"-# **||**{val0}**||** \n-#*{val1}*")
    
window = tk.Tk()
window.title("DEMO")
window.configure(bg="#121212")
window.geometry("600x400+100+200")

window.grid_columnconfigure(1, weight=1)



label = tk.Label(window, bg="#121212", foreground="#FAFAFA", text="DEMO", font=("arial", 10))
label.grid(row=1, column=1)

label2 = tk.Label(window, bg="#121212", fg="#FAFAFA", text="Enter all the Informations", font=("Arial", 10))
label2.grid(row=2, column=1)

input_text0 = tk.Entry(window, width=40, font=("Arial", 11))
input_text0.grid(row=3, column=1,)

input_text1 = tk.Entry(window, width=40, font=("Arial", 11))
input_text1.grid(row=4, column=1)

input_text2 = tk.Entry(window, width=40, font=("Arial", 11))
input_text2.grid(row=5, column=1)

input_text3 = tk.Entry(window, width=40, font=("Arial", 11))
input_text3.grid(row=7, column=1)

input_text4 = tk.Entry(window, width=40, font=("Arial", 11), justify="center")
input_text4.grid(row=8, column=1,)

input_text5 = tk.Entry(window, width=40, font=("Arial", 11))
input_text5.grid(row=9, column=1)

input_text6 = tk.Entry(window, width=40, font=("Arial", 11))
input_text6.grid(row=10, column=1)

input_text7 = tk.Entry(window, width=40, font=("Arial", 11))
input_text7.grid(row=11, column=1)

enterbtn = ttk.Button(window, text="Done", command=getinfo0)
enterbtn.grid(row=13, column=1)

output_text = tk.Label(window, bg="#121212", fg="#FAFAFA", font=("Arial", 11))
output_text.grid(row=15, column=1)

window.mainloop()
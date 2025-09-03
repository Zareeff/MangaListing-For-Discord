import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def getinfo0():
    type = input_text0.get()
    read_time = input_text1.get()
    name = input_text2.get()
    author = input_text3.get()
    author_twitter = input_text4.get()
    writter = input_text5.get()
    writter_twitter = input_text6.get()
    genre = input_text7.get()
    read_number = input_text8.get()
    favourite = input_text9.get()
    val10 = input_text10.get()
    val11 = input_text11.get()
    val12 = input_text12.get()
    
    output_text.config(text=f"-# **||**{type}**||** \n-#*{read_time}*")
                       
    if favourite == "yes":
        output_text.cof(text=f"# {favourite}")
    else:
        output_text(text=f"## {favourite}")

window = tk.Tk()
window.title("DEMO")
window.configure(bg="#121212")
window.geometry("600x400+100+200")

window.grid_columnconfigure(1, weight=1)



label = tk.Label(window, bg="#121212", foreground="#FAFAFA", text="DEMO", font=("arial", 10))
label.grid(row=1, column=1)

label2 = tk.Label(window, bg="#121212", fg="#FAFAFA", text="Enter all the Informations", font=("Arial", 10))
label2.grid(row=2, column=1)


label3 = tk.Label(window, bg="#121212", fg="#FAFAFA", text="Type", font=("Arial", 10))
label3.grid(row=3, column=0)
label4 = tk.Label(window, bg="#121212", fg="#FAFAFA", text="Start reading time", font=("Arial", 10))
label4.grid(row=4, column=0)
label5 = tk.Label(window, bg="#121212", fg="#FAFAFA", text="Name", font=("Arial", 10))
label5.grid(row=5, column=0)
label6 = tk.Label(window, bg="#121212", fg="#FAFAFA", text="By", font=("Arial", 10))
label6.grid(row=6, column=0)


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

input_text8 = tk.Entry(window, width=40, font=("Arial", 11))
input_text8.grid(row=12, column=1)

input_text9 = tk.Entry(window, width=40, font=("Arial", 11))
input_text9.grid(row=13, column=1)

input_text10= tk.Entry(window, width=40, font=("Arial", 11))
input_text10.grid(row=14, column=1)

input_text11 = tk.Entry(window, width=40, font=("Arial", 11))
input_text11.grid(row=15, column=1)

input_text12 = tk.Entry(window, width=40, font=("Arial", 11))
input_text12.grid(row=16, column=1)

input_text13 = tk.Entry(window, width=40, font=("Arial", 11))
input_text13.grid(row=17, column=1)



enterbtn = ttk.Button(window, text="Done", command=getinfo0)
enterbtn.grid(row=20, column=1)

output_text = tk.Label(window, bg="#121212", fg="#FAFAFA", font=("Arial", 11))
output_text.grid(row=3, column=2)



window.mainloop()





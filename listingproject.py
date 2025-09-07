import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip 
# Main Functions To Get Everything To Work
def getinfo0():
    type = input_text0.get()
    read_time = input_text1.get()
    name = input_text2.get()
    author = input_text3.get()
    author_twitter = input_text4.get()
    art_author = input_text5.get()
    art_author_twitter = input_text6.get()
    genre = input_text7.get()
    read_number = input_text8.get()
    favourite = input_text9.get()
    favourite_genre = input_text10.get()
    description = input_text11.get("1.0", tk.END).strip()
    val12 = input_text12.get()
    art = input_text13.get()
    story = input_text14.get()
    overall = input_text15.get()
    mangaupdates_link = input_text16.get()
    myanimelist_link = input_text17.get()
    entry = input_text9.get().strip().lower()
    if entry == "yes":
        favourite2 = "## favourite"
        favourite_genre = f"-#  {favourite_genre}"
        display_name = f"# {name}"
        word = favourite_genre.split()
        word = [w.capitalize() for w in word] 
        favourite_genress = '-# **|** ' + ' **|** '.join(word) + ' **|**'
    elif entry == "no":
        favourite2 = ""
        favourite_genress = ""
        display_name = f"## {name}"
    elif entry == "":
        favourite2 = ""
        favourite_genress = ""
        display_name = f"## {name}" 
    else:
        display_name = f"# {name}"  
        favourite_genress = ""    

    words = genre.split()
    words = [w.capitalize() for w in words] 
    genres = '-# **||** ' + ' **||** '.join(words) + ' **||**'
    
    output_lines = [
    f"-# **||**{type}**||**",
    f"-# *{read_time}*",
    display_name,
    f"**||** By [{author}]({author_twitter}) **||‌**",
    f"**||** Art By [{art_author}]({art_author_twitter})",
    "**Genre:**",
    genres,
    f"**{read_number}**",
    f"-# *{description}"]

    output_lines = [
    f"-# **||**{type}**||**",
    f"-# *{read_time}*",
    display_name,
    f"**||** By [{author}]({author_twitter}) **||‌**",
    f"**||** Art By [{art_author}]({art_author_twitter})",
    "**Genre:**",
    genres,
    f"**{read_number}**"
]
    if favourite2:
     output_lines.append(favourite2)
    if favourite_genress:
     output_lines.append(favourite_genress)

    output_lines.append("-# ----------")
    output_lines.append(f"-# *{description}*")

    output_text.config(text="\n".join(output_lines))
# GUI setup
window = tk.Tk()
window.title("DEMO")
window.configure(bg="#121212")
window.geometry("600x400+100+200")
window.grid_columnconfigure(1, weight=1)

# Make the center expand
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# Frame in the center
frame = tk.Frame(window, bg="#121212")
frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Configure frame’s columns (label vs entry)
frame.columnconfigure(0, weight=0)  # labels don’t stretch
frame.columnconfigure(1, weight=1)  # entries expand

# Labels 
label = tk.Label(frame, bg="#121212", foreground="#FAFAFA", text="DEMO", font=("arial", 10))
label.grid(row=1, column=1, sticky="w")
label2 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Enter all the Informations", font=("Arial", 10))
label2.grid(row=2, column=1,  sticky="w")

label3 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Type (Manga/Manhwa)", font=("Arial", 11))
label3.grid(row=3, column=0, sticky="e")
label4 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Start reading time (m/d/y)", font=("Arial", 10))
label4.grid(row=4, column=0, sticky="e")
label5 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Name", font=("Arial", 10))
label5.grid(row=5, column=0, sticky="e")
label6 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Author name", font=("Arial", 10))
label6.grid(row=6, column=0, sticky="e")
label7 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Author Twitter Account link", font=("Arial", 10))
label7.grid(row=7, column=0, sticky="e")
label8 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Artist name (Leave black if none)", font=("Arial", 10))
label8.grid(row=8, column=0, sticky="e")
label9 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Artist T witter Account Link", font=("Arial", 10))
label9.grid(row=9, column=0, sticky="e")
label10= tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Genre (split them by space ( ))", font=("Arial", 10))
label10.grid(row=10, column=0, sticky="e")
label11 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Number", font=("Arial", 10))
label11.grid(row=11, column=0, sticky="e")
label12 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Is this your favourite (yes/no or leave black for no)", font=("Arial", 10))
label12.grid(row=12, column=0, sticky="e")
label13 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="favourite genres (if youve said yes to 'favoit')")
label13.grid(row=13, column=0, sticky="e")
label14 = tk.Label(frame, bg="#121212", fg="#FAFAFA", text="Enter description", font=("Arial", 10))
label14.grid(row=14, column=0, sticky="e")
# Input fields
input_text0 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text0.grid(row=3, column=1, sticky="w")
input_text1 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text1.grid(row=4, column=1, sticky="w")
input_text2 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text2.grid(row=5, column=1, sticky="w")
input_text3 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text3.grid(row=6, column=1,  sticky="w")
input_text4 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text4.grid(row=7, column=1, sticky="w")
input_text5 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text5.grid(row=8, column=1, sticky="w")
input_text6 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text6.grid(row=9, column=1, sticky="w")
input_text7 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text7.grid(row=10, column=1, sticky="w")
input_text8 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text8.grid(row=11, column=1, sticky="w")
input_text9 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text9.grid(row=12, column=1, sticky="w")
input_text10= tk.Entry(frame, width=40, font=("Arial", 11))
input_text10.grid(row=13, column=1, sticky="w")
input_text11 = tk.Text(frame, width=40, height=2, font=("Arial", 11))
input_text11.grid(row=14, column=1, sticky="w")
input_text12 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text12.grid(row=15, column=1, sticky="w")
input_text13 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text13.grid(row=16, column=1, sticky="w")
input_text14 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text14.grid(row=17, column=1, sticky="w")
input_text15 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text15.grid(row=18, column=1, sticky="w")
input_text16 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text16.grid(row=19, column=1, sticky="w")
input_text17 = tk.Entry(frame, width=40, font=("Arial", 11))
input_text17.grid(row=20, column=1, sticky="w")
# Buttons
enterbtn = ttk.Button(frame, text="Done", command=getinfo0)
enterbtn.grid(row=21, column=1, sticky="w")
# PyperClip Copy buttons
def copy_output():
    output = output_text.cget("text")     
    pyperclip.copy(output)
copybtn = ttk.Button(frame, text="Copy Text", command=copy_output)
copybtn.grid(row=22, column=1, sticky="w")
# Output display
output_text = tk.Label(frame, bg="#121212", fg="#FAFAFA", font=("Arial", 11))
output_text.grid(row=12, column=2, sticky="w")
# Running loop
window.mainloop()

# Importing All Nessecary Modules
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import messagebox

# Making Variables
inputval = None

# Setting Up The Screen
Screen = tk.ThemedTk()
Screen.title("Auto Window Resizer")
Screen.geometry("300x300")
Screen.minsize(150, 150)

# Setting Theme
Screen.get_themes()
Screen.set_theme("arc")

# Making The Entry Labels
width_label = ttk.Label(text="Width/x: ")
height_label = ttk.Label(text="Height/y: ")

# Making The Size Entries
width = ttk.Entry(Screen)
height = ttk.Entry(Screen)

# Defining The Functions
def setsize():
    # Setting Global Variables
    global inputval

    # Getting The User Input
    screen_width = width.get()
    screen_height = height.get()
    width_count = len((screen_width))
    height_count = len((screen_height))

    # Deleting InputField Data To Make Space For New Inputs
    width.delete(0, END)
    height.delete(0, END)

    # Error Handling
    if width_count == 0:
        inputval = True
    elif height_count == 0:
        inputval = False

    try:
        Screen.geometry(f"{screen_width}x{screen_height}")
    except:
        if inputval == True:
            messagebox.showerror("Auto Window Resizer", "Invalid Width")
        elif inputval == False:
            messagebox.showerror("Auto Window Resizer", "Invalid Height")


def size150():
    Screen.geometry("150x150")


def size200():
    Screen.geometry("200x200")


def size300():
    Screen.geometry("300x300")


def size400():
    Screen.geometry("400x400")


def size500():
    Screen.geometry("500x500")


def size600():
    Screen.geometry("600x600")


def size700():
    Screen.geometry("700x700")


def size800():
    Screen.geometry("800x800")


# Making The Buttons
size = ttk.Button(Screen, text="Resize", command=setsize)

# Packing Everything
width_label.pack()
width.pack(pady=5)
height_label.pack()
height.pack(pady=5)
size.pack(pady=5, ipadx=10)

# Menubar Of The GUI
resize = Menu(Screen)
sizes = Menu(resize, tearoff=0)
exitm = Menu(resize, tearoff=0)

# Adding Commands To The MenuBar
sizes.add_command(label="150x150", command=size150)
sizes.add_command(label="200x200", command=size200)
sizes.add_command(label="300x300", command=size300)
sizes.add_command(label="400x400", command=size400)
sizes.add_command(label="500x500", command=size500)
sizes.add_command(label="600x600", command=size600)
sizes.add_command(label="700x700", command=size700)
sizes.add_command(label="800x800", command=size800)

# Configuring The Screen
Screen.config(menu=resize)

# Adding Cascades To The Menubar
resize.add_cascade(label="Sizes", menu=sizes)
resize.add_cascade(label="Exit", command=Screen.destroy)

# Mainloop Of The Program
Screen.mainloop()


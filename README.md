## Hey There, My Name Is Rookie-Coder1234 And I Have Created A Simple Window Resizer Using Python(Tkinter).

> *I Hope You Will Improve This Project As I Am A Beginner And Learning Python*

## Full Code
```python
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import messagebox

inputval = None

Screen = tk.ThemedTk()
Screen.title("Auto Window Resizer")
Screen.geometry("300x300")
Screen.minsize(150, 150)

Screen.get_themes()
Screen.set_theme("arc")

width_label = ttk.Label(text="Width/x: ")
height_label = ttk.Label(text="Height/y: ")

width = ttk.Entry(Screen)
height = ttk.Entry(Screen)

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

size = ttk.Button(Screen, text="Resize", command=setsize)

width_label.pack()
width.pack(pady=5)
height_label.pack()
height.pack(pady=5)
size.pack(pady=5, ipadx=10)

resize = Menu(Screen)
sizes = Menu(resize, tearoff=0)
exitm = Menu(resize, tearoff=0)

sizes.add_command(label="150x150", command=size150)
sizes.add_command(label="200x200", command=size200)
sizes.add_command(label="300x300", command=size300)
sizes.add_command(label="400x400", command=size400)
sizes.add_command(label="500x500", command=size500)
sizes.add_command(label="600x600", command=size600)
sizes.add_command(label="700x700", command=size700)
sizes.add_command(label="800x800", command=size800)

Screen.config(menu=resize)

resize.add_cascade(label="Sizes", menu=sizes)
resize.add_cascade(label="Exit", command=Screen.destroy)

Screen.mainloop()
```

## Explanation
Here I Am Importing All The Nessecary Modules Needed In This Project
```python
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import messagebox
```

Here I Am Creating All The Variables
```python
inputval = None
```

Now I Am Creating A Screen Using Tkinter Which I Just Imported Above
```python
Screen = tk.ThemedTk()
Screen.title("Auto Window Resizer")
Screen.geometry("300x300")
Screen.minsize(150, 150)
```

Now I Am Setting The Theme Of The Window, Just To Make It Look Beautiful(Optional)
```python
Screen.get_themes()
Screen.set_theme("arc")
```

Here I Am Creating The Entry Labels Just To Tell The User In What Input Box They Have To Input Which Value
```python
width_label = ttk.Label(text="Width/x: ")
height_label = ttk.Label(text="Height/y: ")
```

Now I Have Created A Input Field For The User To Input The Values
```python
width = ttk.Entry(Screen)
height = ttk.Entry(Screen)
```

Now I Have Defined All The Functions Which Will Change The Size
```python
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
```

Now I Am Making A Submit Button Which Will Call The Function setsize() And Change The Width And Height Of The Window As Givin In The InputFields
```python
size = ttk.Button(Screen, text="Resize", command=setsize)
```

Here I Am Packing Everything Onto The Screen
```python
width_label.pack()
width.pack(pady=5)
height_label.pack()
height.pack(pady=5)
size.pack(pady=5, ipadx=10)
```

Now I Have Created A MenuBar Which Will Have Two Options, One, To Resize According To The Preset Sizes, Two, To Exit
```python
resize = Menu(Screen)
sizes = Menu(resize, tearoff=0)
exitm = Menu(resize, tearoff=0)
```

Now I Have Added Commands To The Sizes Menu
```python
sizes.add_command(label="150x150", command=size150)
sizes.add_command(label="200x200", command=size200)
sizes.add_command(label="300x300", command=size300)
sizes.add_command(label="400x400", command=size400)
sizes.add_command(label="500x500", command=size500)
sizes.add_command(label="600x600", command=size600)
sizes.add_command(label="700x700", command=size700)
sizes.add_command(label="800x800", command=size800)
```

Here I Am Configuring The Screen
```python
Screen.config(menu=resize)
```

Now I Have Added Cascades To The Main Menu
```python
resize.add_cascade(label="Sizes", menu=sizes)
resize.add_cascade(label="Exit", command=Screen.destroy)
```

Now At Last After Every Tkinter Project The Mainloop To Check For User Events
```python
Screen.mainloop()
```

## Thank You For Reading

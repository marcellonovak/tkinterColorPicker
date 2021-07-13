import tkinter as tk
from tkinter import *
import random

window = tk.Tk()

containerFrame = LabelFrame(
    window, 
    text = "Color Picker Grid", 
    font = ('arial bold', '12'), 
    fg = "white", 
    highlightthickness = 5, 
    bg = "dark grey"
)

def displayGrid(): 

    for x in range(5):
        containerFrame.columnconfigure(x, weight=1, minsize=75)
        containerFrame.rowconfigure   (x, weight=1, minsize=75)

        for y in range(5):
            gridFrame = tk.Frame(
                master = containerFrame,
                relief = tk.RAISED,
                borderwidth = 3
            )
                
            gridFrame.grid(row = x, column = y, padx = 5, pady = 5)  # Sets position of the color square
            gridColor = "#" + ("%06x" % random.randint(0, 0xFFFFFF)) # Creates the randomized color
            gridLabel = tk.Label(                                    # Creates the square itself with the color
                master = gridFrame, 
                text = gridColor,
                font = ('arial bold', '12'),
                fg = "white",
                anchor = "sw",
                height = 10,
                width = 20,
                bg = gridColor
            )

            gridLabel.pack(padx = 5, pady = 5)

    containerFrame.pack(fill = "both", expand = "yes")

displayGrid()

refreshButton = Button(window, text = "Refresh Colors", command = displayGrid)
refreshButton.pack(padx = 5, pady = 5)

window.mainloop()
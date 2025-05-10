from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("600x600")
window.configure(background = "grey")

l1 = Label(window, text = "Celsius to Farenheit converter", font = ("Comic Ms Sans", 25))
l1.pack(row = 0, column = 0, padx = 15, pady = 20, columnspan = 20)

l2 = Label(window, text = "Enter temperature in Celsius", )
l2.pack(row = 1 ,column = 3, padx = 15, pady = 25)

b1 = Button(window)
b1.pack(row = 1 ,column = 10, padx = 15, pady = 35)







window.mainloop()
from tkinter import *
# Blank Window
root = Tk()

# Main layout
#   Frame is a invisible retangle to put things inside him. Similar to DIV
topFrame = Frame(root)
bottomFrame = Frame(root)

# Place in somewhere. In pack, you can tell him where to stay.
topFrame.pack()
bottomFrame.pack(side=BOTTOM)

label = Label(topFrame, text = "To criando teliha em Pitão ! :D")
button1 = Button(topFrame, text = "button1")
button2 = Button(topFrame, text = "button2")
button3 = Button(topFrame, text = "button3")
button4 = Button(bottomFrame, text = "button4")

label.pack()
button2.pack()
button1.pack()
button3.pack()
button4.pack()
# Stay opened window.
root.mainloop()

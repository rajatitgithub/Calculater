from tkinter import *

def button_click(number):
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(END, str(current) + str(number))

def button_clear():
    entry_field.delete(0, END)

def button_equal():
    expression = entry_field.get()
    try:
        result = eval(expression)
        entry_field.delete(0, END)
        entry_field.insert(END, result)
    except:
        entry_field.delete(0, END)
        entry_field.insert(END, "Error")
        
def delete():
        a = entry_field.get()
        entry_field.delete(first=len(a)-1,last="end")        

window = Tk()
window.title("Calculator")
window.geometry("360x380")

entry_field = Entry(window, width=25, borderwidth=5, font=("Arial", 14))
entry_field.grid(row=0, column=0, columnspan=4, padx=30, pady=30)

button_width = 5
button_height = 2
button_font = ("Arial", 12, "bold")
button_radius= 30

button_1 = Button(window, text="1", width=button_width, height=button_height, font=button_font, command=lambda: button_click(1))
button_2 = Button(window, text="2", width=button_width, height=button_height, font=button_font, command=lambda: button_click(2))
button_3 = Button(window, text="3", width=button_width, height=button_height, font=button_font, command=lambda: button_click(3))
button_4 = Button(window, text="4", width=button_width, height=button_height, font=button_font, command=lambda: button_click(4))
button_5 = Button(window, text="5", width=button_width, height=button_height, font=button_font, command=lambda: button_click(5))
button_6 = Button(window, text="6", width=button_width, height=button_height, font=button_font, command=lambda: button_click(6))
button_7 = Button(window, text="7", width=button_width, height=button_height, font=button_font, command=lambda: button_click(7))
button_8 = Button(window, text="8", width=button_width, height=button_height, font=button_font, command=lambda: button_click(8))
button_9 = Button(window, text="9", width=button_width, height=button_height, font=button_font, command=lambda: button_click(9))
button_0 = Button(window, text="0", width=button_width, background="orange", height=button_height, font=button_font, command=lambda: button_click(0))

button_add = Button(window, text="+", width=button_width, height=button_height, font=button_font, command=lambda: button_click('+'))
button_subtract = Button(window, text="-", width=button_width, height=button_height, font=button_font, command=lambda: button_click('-'))
button_multiply = Button(window, text="x", width=button_width, height=button_height, font=button_font, command=lambda: button_click('*'))
button_divide = Button(window, text="/", width=button_width, height=button_height, font=button_font, command=lambda: button_click('/'))
button_equal = Button(window, text="=", width=button_width,background="green", height=button_height,font=button_font, command=button_equal)
button_clear = Button(window, text="C", width=button_width,background="orange", height=button_height, font=button_font, command=button_clear)
button_greaterthan = Button(window,text=">", width=button_width, height=button_height, font=button_font, command=lambda: button_click('>'))
button_per=Button(window,text="%", width=button_width, height=button_height, font=button_font, command=lambda: button_click('%'))
button_dec=Button(window,text=".", width=button_width, height=button_height, font=button_font, command=lambda: button_click('.'))
button_lessthan = Button(window,text="<", width=button_width, height=button_height, font=button_font, command=lambda: button_click('<'))


button_clear.grid(row=1, column=0)
button_per.grid(row=1, column=1)
button_divide.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_dec.grid(row=4,column=3)

button_0.grid(row=5, column=0)
button_lessthan.grid(row=5, column=1)
button_greaterthan.grid(row=5, column=2)
button_equal.grid(row=5,column=3)

window.mainloop()
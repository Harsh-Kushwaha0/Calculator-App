import tkinter as tk 
from tkinter import *

#function for numbers 
def get_degit(degit):
    current = result_class["text"]
    new = current + str(degit)
    result_class.config(text=new)

#function for clear
def clear ():
    result_class.config(text="")

#for operators
first_number = second_number = operator = None

#function for operator
def for_operator(op):
    global first_number,operator

    first_number = int(result_class["text"])
    operator = op
    result_class.config(text="")

def for_result():
    global first_number,second_number,operator

    second_number = int(result_class["text"])

    if operator == "+":
        result_class.config(text = str(first_number + second_number))

    elif operator == "-":
        result_class.config(text = str(first_number - second_number))

    elif operator == "*":
        result_class.config(text = str(first_number * second_number))

    else:
        if second_number == 0:
            result_class.config(text = "∞")
        else:
            result_class.config(text = str(first_number / second_number))


#main window 
root = tk.Tk()
root.title("calculator")
root.geometry("353x500")
root.resizable(0,0)
root.configure(background ="black")

#result window
result_class = Label(root,text = "",bg ="black",fg = "white")
result_class.grid(row = 0,column = 0,columnspan=100,pady = (70,30), sticky="w")
result_class.configure(font = ("verdana",30,"bold"))


#button7
result_butt7 = Button(root,text = "7",bg = "orange",fg = "black", width = 6, height = 3,command = lambda: get_degit(7))
result_butt7.grid(row = 1,column = 0)
result_butt7.configure(font = ("verdana",14,"bold"))

#button8
result_butt8 = Button(root,text= "8",bg = "orange",fg = "black",width = 6,height= 3,command = lambda: get_degit(8))
result_butt8.grid(row = 1,column = 1)
result_butt8.configure(font =("verdana",14,"bold"))

#button9
result_butt9 = Button(root,text = "9",bg = "orange",fg = "black",width= 6,height = 3, command = lambda: get_degit(9))
result_butt9.grid(row = 1,column =2)
result_butt9.configure(font = ("verdana",14,"bold"))

#button_add
result_add = Button(root,text = "+",bg = "orange",fg = "black",width= 6,height = 3, command= lambda: for_operator("+"))
result_add.grid(row = 1,column = 3)
result_add.configure(font = ("verdana",14,"bold"))


#button4
result_butt4 = Button(root,text = "4",bg = "orange",fg = "black",width= 6,height = 3, command=lambda: get_degit(4))
result_butt4.grid(row = 2,column = 0)
result_butt4.configure(font = ("verdana",14,"bold"))

#button5
result_butt5 = Button(root,text = "5",bg = "orange",fg = "black",width= 6,height = 3, command = lambda: get_degit(5))
result_butt5.grid(row = 2,column = 1)
result_butt5.configure(font = ("verdana",14,"bold"))

#button6
result_butt6 = Button(root,text = "6",bg = "orange",fg = "black",width= 6,height = 3, command = lambda: get_degit(6))
result_butt6.grid(row = 2,column =2)
result_butt6.configure(font = ("verdana",14,"bold"))

#button_subtract
result_sub = Button(root,text = "-",bg = "orange",fg = "black",width= 6, height = 3, command = lambda: for_operator("-"))
result_sub.grid(row = 2,column = 3)
result_sub.configure(font= ("verdana",14,"bold"))


#button1
result_butt1 = Button(root,text = "1",bg = "orange",fg = "black",width= 6, height = 3, command = lambda: get_degit(1))
result_butt1.grid(row = 3,column = 0)
result_butt1.configure(font= ("verdana",14,"bold"))

#button2
result_butt2 = Button(root,text = "2",bg = "orange",fg = "black",width= 6, height = 3, command = lambda: get_degit(2))
result_butt2.grid(row = 3,column = 1)
result_butt2.configure(font= ("verdana",14,"bold"))

#button3
result_butt3 = Button(root,text = "3",bg = "orange",fg = "black",width= 6, height = 3,command = lambda: get_degit(3))
result_butt3.grid(row = 3,column = 2)
result_butt3.configure(font= ("verdana",14,"bold"))

#button_multiply
result_mul = Button(root,text = "X",bg = "orange",fg = "black",width= 6, height = 3, command = lambda: for_operator("*"))
result_mul.grid(row = 3,column = 3)
result_mul.configure(font= ("verdana",14,"bold"))


#button_clear
result_clear = Button(root,text = "C",bg = "orange",fg = "black",width= 6, height = 3,command = lambda: clear())
result_clear.grid(row = 4,column = 0)
result_clear.configure(font= ("verdana",14,"bold"))

#button_zero
result_zero = Button(root,text = "0",bg = "orange",fg = "black",width= 6, height = 3,command = lambda: get_degit(0))
result_zero.grid(row = 4,column = 1)
result_zero.configure(font= ("verdana",14,"bold"))

#button_equal
result_eql = Button(root,text = "=",bg = "orange",fg = "black",width= 6, height = 3, command = lambda: for_result())
result_eql.grid(row = 4,column = 2)
result_eql.configure(font= ("verdana",14,"bold"))

#button_divide 
result_div = Button(root,text = "/",bg = "orange",fg = "black",width= 6, height = 3,command = lambda: for_operator("/"))
result_div.grid(row = 4,column = 3)
result_div.configure(font= ("verdana",14,"bold"))


root.mainloop()
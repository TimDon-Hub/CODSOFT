'''
CODSOFT Task 2

CALCULATOR
    Design a simple calculator with basic arithmetic operations.
    Prompt the user to input two numbers and an operation choice.
    Perform the calculation and display the result
'''

from tkinter import *

# Create main window
main = Tk()
main.title("Simple Calculator")
main.geometry("400x400")


# Display frame
display_frame = LabelFrame(main, padx=10, pady=10, bg="#f2f2f2")
display_frame.pack()

# Entry box
input_box = Entry(display_frame, width=30, borderwidth=5, font=('Arial', 14), justify='right')
input_box.grid(row=0, column=0, columnspan=4, ipady=10)

global f_num 
global operation

def button_click(number):
    current = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, current + str(number))

def button_clear():
    input_box.delete(0, END)

def convert(num):
    return float(num) if '.' in num else int(num)

def handle_operation(op_type):
    global f_num, operation
    try:
        f_num = convert(input_box.get())
        operation = op_type
        input_box.delete(0, END)
    except ValueError:
        input_box.delete(0, END)
        input_box.insert(0, "Error")

def handle_equal():
    try:
        second_num = convert(input_box.get())
        input_box.delete(0, END)
        result = 0
        if operation == 'add':
            result = f_num + second_num
        elif operation == 'sub':
            result = f_num - second_num
        elif operation == 'mul':
            result = f_num * second_num
        elif operation == 'div':
            result = f_num / second_num if second_num != 0 else "Err"
        input_box.insert(0, result)
    except:
        input_box.insert(0, "Err")

# # Button definitions
button_0 = Button(display_frame, text='0', width=7, height=2, font=('Arial', 12), command=lambda: button_click(0))
button_1 = Button(display_frame, text='1', width=7, height=2, font=('Arial', 12), command=lambda: button_click(1))
button_2 = Button(display_frame, text='2', width=7, height=2, font=('Arial', 12), command=lambda: button_click(2))
button_3 = Button(display_frame, text='3', width=7, height=2, font=('Arial', 12), command=lambda: button_click(3))
button_4 = Button(display_frame, text='4', width=7, height=2, font=('Arial', 12), command=lambda: button_click(4))
button_5 = Button(display_frame, text='5', width=7, height=2, font=('Arial', 12), command=lambda: button_click(5))
button_6 = Button(display_frame, text='6', width=7, height=2, font=('Arial', 12), command=lambda: button_click(6))
button_7 = Button(display_frame, text='7', width=7, height=2, font=('Arial', 12), command=lambda: button_click(7))
button_8 = Button(display_frame, text='8', width=7, height=2, font=('Arial', 12), command=lambda: button_click(8))
button_9 = Button(display_frame, text='9', width=7, height=2, font=('Arial', 12), command=lambda: button_click(9))
button_dot = Button(display_frame, text='.', width=7, height=2, font=('Arial', 12), command=lambda: button_click('.'))

button_add = Button(display_frame, text='+', width=7, height=2, font=('Arial', 12), command=lambda: handle_operation('add'))
button_div = Button(display_frame, text='/', width=7, height=2, font=('Arial', 12), command=lambda: handle_operation('div'))
button_mul = Button(display_frame, text='X', width=7, height=2, font=('Arial', 12), command=lambda: handle_operation('mul'))
button_sub = Button(display_frame, text='-', width=7, height=2, font=('Arial', 12), command=lambda: handle_operation('sub'))
button_clear = Button(display_frame, text='Clear', width=7, height=2, font=('Arial', 12), command=button_clear)



# Row 1
button_7.grid(row=1, column=0, padx=3, pady=3)
button_8.grid(row=1, column=1, padx=3, pady=3)
button_9.grid(row=1, column=2, padx=3, pady=3)
button_div.grid(row=1, column=3, padx=3, pady=3)

# Row 2
button_4.grid(row=2, column=0, padx=3, pady=3)
button_5.grid(row=2, column=1, padx=3, pady=3)
button_6.grid(row=2, column=2, padx=3, pady=3)
button_mul.grid(row=2, column=3, padx=3, pady=3)

# Row 3
button_1.grid(row=3, column=0, padx=3, pady=3)
button_2.grid(row=3, column=1, padx=3, pady=3)
button_3.grid(row=3, column=2, padx=3, pady=3)
button_sub.grid(row=3, column=3, padx=3, pady=3)

# Row 4
button_0.grid(row=4, column=0, padx=3, pady=3)
button_dot.grid(row=4, column=1, padx=3, pady=3)
button_clear.grid(row=4, column=2, padx=3, pady=3)
button_add.grid(row=4, column=3, padx=3, pady=3) 

# Row 5
button_equal = Button(display_frame, text='=', width=32, height=2, font=('Arial', 12), command=handle_equal)
button_equal.grid(row=5, column=0, columnspan=4, padx=3, pady=5)

main.mainloop()
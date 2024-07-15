import tkinter as tk


def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def button_equal():
    try:
        global expression
        result = str(eval(expression))  
        input_text.set(result)          
        expression = ""                 
    except:
        input_text.set("Error")         
        expression = ""                 


def button_clear():
    global expression
    expression = ""                     
    input_text.set("")                  


root = tk.Tk()                          
root.title("Simple Calculator")         


input_text = tk.StringVar()


entry = tk.Entry(root, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)  


expression = ""


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=('arial', 18, 'bold'), bd=5, padx=20, pady=20,
                       command=lambda item=text: button_click(item))  


clear_button = tk.Button(root, text='C', font=('arial', 18, 'bold'), bd=5, padx=20, pady=20, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=3)  


equal_button = tk.Button(root, text='=', font=('arial', 18, 'bold'), bd=5, padx=20, pady=20, command=button_equal)
equal_button.grid(row=5, column=3)  


root.mainloop()  

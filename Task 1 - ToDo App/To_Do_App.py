"""
CODSOFT TASK 1

 TO-DO LIST
    A To-Do List application is a useful project that helps users manage
    and organize their tasks efficiently. This project aims to create a
    command-line or GUI-based application using Python, allowing
    users to create, update, and track their to-do lists
"""
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

main = Tk()
main.title('TO-DO LIST APP')
main.iconbitmap('file_icon.ico')

# Adding of Task window
def create_task():
    global wind
    global task
    wind = Toplevel()
    task = Entry(wind)
    task.pack(pady=10, padx=10)
    add_button = Button(wind, text='Create Task', command=get_input)
    add_button.pack(padx=10)

    wind.title('Add Task')
    wind.geometry('300x100')
    wind.iconbitmap('file_icon.ico')

    
def delete_row(row):
    # Loop through all widgets in the taskbox
    for widget in taskbox.grid_slaves():
        if widget.grid_info()["row"] == row:
            widget.destroy()


track_row = 0
            
def get_input():
    global track_row
    task_input = task.get()
    if task_input.strip():  
        task_var = IntVar()

        # Get the current row index
        current_row = track_row
        track_row += 1

        # Create a Checkbutton for the task
        task_checkbox = Checkbutton(taskbox, text=task_input, variable=task_var, anchor='w')
        task_checkbox.grid(row=current_row, column=0, columnspan=2, sticky='w', padx=5, pady=5)

        # Load the image for the delete button
        delete_image = PhotoImage(file="trash_icon.png")
        delete_image = delete_image.subsample(3, 3) 

        # Create a delete button with the image
        delete_button = Button(taskbox, image=delete_image, borderwidth=0, command=lambda: delete_row(current_row))
        delete_button.image = delete_image 
        delete_button.grid(row=current_row, column=2, padx=5, pady=5)
    else:
        messagebox.showerror('Input Error', 'Please enter a task.')

    task.delete(0, END)
    wind.destroy()

heading = Label(main, text='Tasks', font=('Arial', 18))
heading.pack()

taskbox = LabelFrame(main, width=350, height=380, bd=3)
taskbox.pack(padx=5)
taskbox.grid_propagate(False)


# Load the image
task_image = PhotoImage(file="plus-icon.png") 
task_image = task_image.subsample(2, 2)  # Resize the image  

# Create the button with the image
add_task = Button(main, text='ADD TASK', image=task_image, compound=TOP, bd=5, padx=5, pady=5, command=create_task)
add_task.pack(pady=15)



main.mainloop()
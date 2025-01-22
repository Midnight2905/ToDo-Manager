import tkinter as tk
from tkinter import messagebox
import datetime
#ToDo list
amountOfTask = 0
class Task:
    #Add task
    def addToDo():
        task = taskTextBox.get()
        if task == "":
            messagebox.showwarning("Input Error","Please enter in a task")
        else:
            taskListBox.insert(tk.END, task)
    #Delete task
    def deleteTask():
        taskComplete = taskListBox.curselection()[0]
        taskListBox.delete(taskComplete)
    #Complete Task
    def completeTask():
        taskComplete = taskListBox.curselection()[0]
        task = taskListBox.get(taskComplete)
        taskListBox.delete(taskComplete)
        taskListBox.insert(tk.END, f"{task} (Complete) {datetime.date.today()}")
#Load tk
root = tk.Tk()
#Set window size and the name
root.title("To Do")
root.minsize(700, 700)
#locations of buttons and stuff
buttonColumn = 2
#
appFrame = tk.Frame(root)
appFrame.pack()
#the input from the user goes here
textToDo = tk.Label(appFrame, text="Add Task ->")
textToDo.grid(row=0, column=0, padx=5)
taskTextBox = tk.Entry(appFrame, width=10)
taskTextBox.grid(row=0, column=1, padx=0)

#task list 
taskListBox = tk.Listbox(root, width=70, height=10)
taskListBox.pack(pady=10)
#buttons
addToDoButton = tk.Button(appFrame, text="Add Task", command=Task.addToDo)
addToDoButton.grid(row=buttonColumn, column=0, padx=5)

addToDoButton = tk.Button(appFrame,text="Delete Task", command=Task.deleteTask)
addToDoButton.grid(row=buttonColumn, column=1, padx=5)

addToDoButton = tk.Button(appFrame,text="Complete Task", command=Task.completeTask)
addToDoButton.grid(row=buttonColumn, column=2, padx=5)

root.mainloop()

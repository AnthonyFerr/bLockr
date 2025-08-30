from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.geometry("400x300")
root.title("BlockGUI")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Label(mainframe, text="Running Apps").grid(column=1, row=1)

#run tasklist batch file
batchResult = subprocess.run(["simpleBatch.bat"],
               capture_output=True,
               text=True)

#get the tasklist from batch as a list, each line is a process
#first 9 lines are junk, slice off
taskList = [item.split(" ")[0] for item in batchResult.stdout.split("\n")[9:]]
runningvar = StringVar(value=taskList)
tasks = Listbox(mainframe, listvariable=runningvar, width=40)
tasks.grid(column=1, row=2)


root.mainloop()
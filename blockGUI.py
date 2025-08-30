from tkinter import *
from tkinter import ttk
import subprocess

def block():
    selection = tasks.curselection()
    if not selection:
        return  # nothing selected
    

    for i in selection:
        app = taskList[i]  # get the actual app name
        subprocess.run(["axe.bat", app], shell=True)
        if app and app not in blockedApps:  # avoid empty strings / duplicates
            blockedApps.append(app)
            taskList.remove(app)

    blockedList.set(blockedApps)  # refresh the listbox
    runningvar.set(taskList)


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
tasks = Listbox(mainframe, listvariable=runningvar, width=20)
tasks.grid(column=1, row=2)

blockedApps = []
blockedList = StringVar(value=blockedApps)
blockButton = Button(mainframe, text="Block", command=block)
blockButton.grid(column=2, row=2)
blockLabel = Label(mainframe, text="Blocked Apps")
blockLabel.grid(column=3, row=1)
blockedBox = Listbox(mainframe, listvariable=blockedList, width=20)
blockedBox.grid(column=3, row=2)




root.mainloop()
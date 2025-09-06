from tkinter import *
from tkinter import ttk
import subprocess
import time
import multiprocessing



def block():
    blockButton.grid_forget()
    for task in tasks.curselection():
        blockedBox.insert(0, taskList[task])
        blockedApps.append(taskList[task])
        tasks.delete(task)
    unblockButton.grid(column=2, row=2)
    blocker.start()

def unblock():
    #hide the unblock button
    unblockButton.grid_forget()
    #redisplay the block button
    blockButton.grid(column=2, row=2)
    #remove all blocked tasks from list
    blockedBox.delete(0, END)
    blockedApps.clear()
    blocker.kill()

def chopping(interval):
    #Attempt to kill the blocked tasks every X seconds
    while True:
        for task in blockedApps:
            subprocess.run(["axe.bat", task], shell=True)
            print(task)
        time.sleep(interval)

if __name__ == "__main__":
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
    tasks = Listbox(mainframe, listvariable=runningvar, width=20, selectmode="multiple")
    tasks.grid(column=1, row=2)

    blockedApps = []
    blockedList = StringVar(value=blockedApps)

    blockButton = Button(mainframe, text="Block", command=block)
    blockButton.grid(column=2, row=2)

    unblockButton = Button(mainframe, text="Unblock", command=unblock)

    blockLabel = Label(mainframe, text="Blocked Apps")

    blockedBox = Listbox(mainframe, listvariable=blockedList, width=20, selectmode="multiple")
    blockedBox.grid(column=3, row=2)
    blocker = multiprocessing.Process(target=chopping, args=[2])




    root.mainloop()
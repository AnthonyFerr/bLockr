import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("BlockGUI")

        self._setup_widgets()

    def _setup_widgets(self):
        frame = ttk.Frame(self.root, padding="3 3 12 12")
        frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.tasks = tk.Listbox(frame, width=20, selectmode="multiple")
        self.tasks.grid(column=1, row=2)

        self.unblock_button = tk.Button(frame, text="Unblock", command=self.on_unblock)
        self.unblock_button.grid(column=2, row=2)
        #Initialize button location with grid, then hide it for startup
        self.unblock_button.grid_remove()

        self.block_button = tk.Button(frame, text="Block", command=self.on_block)
        self.block_button.grid(column=2, row=2)


        self.blocked_box = tk.Listbox(frame, width=20, selectmode="multiple")
        self.blocked_box.grid(column=3, row=2)

    # --- Event Handlers ---
    def on_block(self):
        print("Block clicked")
        self.toggle(self.block_button)
        self.toggle(self.unblock_button)

    def on_unblock(self):
        print("Unblock clicked")
        self.toggle(self.block_button)
        self.toggle(self.unblock_button)

    
    def toggle(self, element: tk.Widget):
        """ Toggle the visibility of a tKinter widget. 
        """
        if (element.winfo_ismapped()):
            element.grid_remove()
            print(f"{element.widgetName} removed")
        else:
            element.grid()
            print(f"{element.widgetName} shown")

    def run(self):
        self.root.mainloop()

window = GUI()
window.run()
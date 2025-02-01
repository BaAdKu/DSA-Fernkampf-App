# here we will write part of the code
import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Basti's und Ted's Fernkampf App")

    weapon_frame = ttk.Frame(root)
    weapon_frame.grid(column=0, row=0)

    modifier_frame = tk.Frame(root)
    modifier_frame.grid(column=1, row=0)

    container = ttk.Frame(modifier_frame)
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    for i in range(50):
        # ttk.Label(scrollable_frame, text="Sample scrolling label").pack()
        ttk.Checkbutton(scrollable_frame, text="test").pack()

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    greeting = tk.Label(
        text="This is the first test of our App!",
        master=weapon_frame,
    )
    greeting.pack()

    button = tk.Button(
        text="Exit Application!",
        width=30,
        height=1,
        bg="grey",
        fg="black",
        master=modifier_frame,
        command=exit,
    )
    button.pack()


    # layout on the root window
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()

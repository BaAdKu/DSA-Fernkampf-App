# here we will write part of the code
import tkinter as tk


def main():
    window = tk.Tk()
    frameLeft = tk.Frame()
    frameLeft.pack()
    frameRight = tk.Frame()
    frameRight.pack()
    greeting = tk.Label(
        text="This is the first test of our App!",
        master=frameLeft,
    )
    greeting.pack()
    button = tk.Button(
        text="Please press here to start application!",
        width=30,
        height=1,
        bg="grey",
        fg="black",
        master=frameRight,
    )
    button.pack()
    window.mainloop()

if __name__ == "__main__":
    main()

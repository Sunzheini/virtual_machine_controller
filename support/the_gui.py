import tkinter as tk


class MyGui:
    def __init__(self, controller_object):
        self.window = tk.Tk()
        self.window.title("VM Controller")
        self.window.geometry("300x350")

        self.controller_object = controller_object

        self.label = tk.Label(self.window, text="Click to start linux test sequence", font=("Arial", 14))
        self.label.pack(pady=10)

        self.button = tk.Button(self.window, text="Start", command=self.button_clicked, font=("Arial", 12))
        self.button.pack(pady=5)

        self.label1 = tk.Label(self.window, text="Click to start win test sequence", font=("Arial", 14))
        self.label1.pack(pady=30)

        self.button1 = tk.Button(self.window, text="Start", command=self.button_clicked1, font=("Arial", 12))
        self.button1.pack(pady=5)

    def button_clicked(self):
        self.label.config(text="Wait and don't touch...")
        self.button.config(text="Running...")
        self.button.config(state=tk.DISABLED)
        self.window.update()

        self.controller_object.linux_test_sequence()

        self.label.config(text="Click to start linux test sequence")
        self.button.config(text="Start")
        self.button.config(state=tk.NORMAL)
        self.window.update()

    def button_clicked1(self):
        self.label1.config(text="Wait and don't touch...")
        self.button1.config(text="Running...")
        self.button1.config(state=tk.DISABLED)
        self.window.update()

        self.controller_object.win_test_sequence()

        self.label1.config(text="Click to start win test sequence")
        self.button1.config(text="Start")
        self.button1.config(state=tk.NORMAL)
        self.window.update()

    def start(self):
        self.window.mainloop()

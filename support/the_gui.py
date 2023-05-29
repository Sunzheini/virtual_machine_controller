import tkinter as tk


class MyGui:
    def __init__(self, controller_object):
        self.window = tk.Tk()
        self.window.title("VM Controller")
        self.window.geometry("300x120")

        self.controller_object = controller_object

        self.label = tk.Label(self.window, text="Click to start test sequence", font=("Arial", 14))
        self.label.pack(pady=20)

        self.button = tk.Button(self.window, text="Start", command=self.button_clicked, font=("Arial", 12))
        self.button.pack(pady=10)

    def button_clicked(self):
        self.label.config(text="Wait and don't touch...")
        self.button.config(text="Running...")
        self.button.config(state=tk.DISABLED)
        self.window.update()

        self.controller_object.test_sequence()

        self.label.config(text="Click to start test sequence")
        self.button.config(text="Start")
        self.button.config(state=tk.NORMAL)
        self.window.update()

    def start(self):
        self.window.mainloop()

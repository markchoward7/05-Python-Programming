import tkinter as tk
from tkinter import ttk

def program_1():
    window = tk.Tk()

    label1 = tk.Label()
    
    def on_click():
        label1.configure(text = "My name and address are not for you.")
        label1.grid()

    button1 = tk.Button(text = "Click This", command = on_click)
    button1.grid()

    window.mainloop()

def program_2():
    window = tk.Tk()

    def on_click_sinister():
        label1.configure(text = "left")
    
    def on_click_dexter():
        label1.configure(text = "right")
    
    def on_click_medium():
        label1.configure(text = "center")
    
    button1 = tk.Button(text = "sinister", command = on_click_sinister)
    button2 = tk.Button(text = "dexter", command = on_click_dexter)
    button3 = tk.Button(text = "center", command = on_click_medium)
    button1.grid()
    button2.grid()
    button3.grid()
    
    label1 = tk.Label()
    label1.grid()

    window.mainloop()

def program_3():
    window = tk.Tk()

    entry1 = tk.Entry()
    entry1.grid()
    label1 = tk.Label(text = "Tank size (gallons)")
    label1.grid()
    entry2 = tk.Entry()
    entry2.grid()
    label2 = tk.Label(text = "Distance on full tank (miles)")
    label2.grid()
    label3 = tk.Label()

    def on_click():
        label3.configure(text = f"{int(entry2.get()) / int(entry1.get())} mpg")
        label3.grid()

    button1 = tk.Button(text = "Calculate", command = on_click)
    button1.grid()

    window.mainloop()

def program_4():
    window = tk.Tk()

    label1 = tk.Label(text = "F")
    label1.grid()

    entry1 = tk.Entry()
    entry1.grid()

    label2 = tk.Label()

    def on_click():
        label2.configure(text = f"{(int(entry1.get())-32) * 5 / 9} C")
        label2.grid()
    
    button1 = tk.Button(text = "Convert", command = on_click)
    button1.grid()

    window.mainloop()

def program_5():
    window = tk.Tk()

    label1 = tk.Label(text = "Property value")
    label1.grid()

    entry1 = tk.Entry()
    entry1.grid()

    label2 = tk.Label()
    label3 = tk.Label()

    def on_click():
        label2.configure(text = f'Assessment: ${int(entry1.get()) * 0.6}')
        label3.configure(text = f'Tax: ${int(entry1.get()) * 0.6 * 0.0064}')
        label2.grid()
        label3.grid()

    button1 = tk.Button(text = "Calculate", command = on_click)
    button1.grid()

    window.mainloop()

def program_6():
    window = tk.Tk()

    label1 = tk.Label(text = "Oil Change - $26")
    label2 = tk.Label(text = "Lube Job - $18")
    label3 = tk.Label(text = "Radiator Flush - $30")
    label4 = tk.Label(text = "Transmission Flush - $80")
    label5 = tk.Label(text = "Inspection - $15")
    label6 = tk.Label(text = "Muffler Replacement - $100")
    label7 = tk.Label(text = "Tire Rotation - $20")

    label1.grid()
    label2.grid()
    label3.grid()
    label4.grid()
    label5.grid()
    label6.grid()
    label7.grid()

    checks = [ttk.Checkbutton() for _ in range(7)]
    for index, check in enumerate(checks):
        check.grid(row=index, column = 1)
        check.state(['!alternate'])

    label8 = tk.Label()

    def on_click():
        total = 0
        for index, check in enumerate(checks):
            if "selected" in check.state():
                if index == 0:
                    total += 26
                elif index == 1:
                    total += 18
                elif index == 2:
                    total += 30
                elif index == 3:
                    total += 80
                elif index == 4:
                    total += 15
                elif index == 5:
                    total += 100
                elif index == 6:
                    total += 20
        label8.configure(text = f"Total: ${total}")
        label8.grid()
    
    button1 = tk.Button(text = "Get Total", command = on_click)
    button1.grid()

    window.mainloop()
program_6()
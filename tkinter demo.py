import tkinter as tk

# window = tk.Tk()

# window.title("This is my title")

# window.geometry("400x400")

# title = tk.Label(text = 'A message')
# title.grid()
# #title.pack()

# entry_field1 = tk.Entry()
# entry_field1.grid()

# button1 = tk.Button(text = "Click Here")
# button1.grid()

# textbox1 = tk.Text(master = window, height = 10, width = 30)
# textbox1.grid()

window = tk.Tk()
window.title("POOP")
window.geometry("640x480")

label1 = tk.Label(text = "Yo")
label1.grid()

label2 = tk.Label(text = "Name please?")
label2.grid()

entry = tk.Entry()
entry.grid()

def on_click():
    label2.configure(text = f'{entry.get()}? What a stupid name.')
    #newLabel = tk.Label(text = f'{entry.get()}? What a stupid name.')
    #newLabel.grid()

button1 = tk.Button(text = "Click This", command = on_click)
button1.grid()

window.mainloop()
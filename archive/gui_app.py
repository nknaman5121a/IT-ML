# GUI - Graphical User Interface

import tkinter as ttk
app = ttk.Tk()
app.title('My app')
app.geometry('600x400')

ttk.Label(app, text = 'A simple TExt Label').place(x=50,y=50)
ttk.Label(app, text = 'Naman kumawat').place(x=70,y=30)

app.mainloop()
# GUI - Graphical User Interface

import tkinter as ttk
app = ttk.Tk()
app.title('My app')
app.geometry('600x400')

msg = ttk.Variable(app)
print(msg.get())
msg.set('Empty')
print(msg.get())

ttk.Label(app, text = 'A simple TExt Label').place(x=50,y=50)
ttk.Label(app, textvariable =msg, font=('Arial',25)).place(x=70,y=30)

def abc():
    print('wow')
    msg.set('anything')

ttk.Button(app, text = 'Isko click kardo', command = abc) .place(x=100,y=100)

ttk.Button(app, text = 'ye wala bhi h', command = lambda:msg.set('nothing')) .place(x=200,y=200)

f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result = ttk.Variable(app)

ttk.Entry(app, textvariable=f1, font=('Arial',22)).place(x=50,y=200)
ttk.Entry(app, textvariable=f2, font=('Arial',22)).place(x=200,y=200)
ttk.Label(app, text='Result').place(x=100,y=300)
ttk.Label(app, textvariable=result,font=('Arial',23)).place(x=100,y=330)

def calci(op):
    print('calculating..')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app, text='+', command=lambda:calci('+'),font = ('Arial',23)).place(x=50,y=250)

ttk.Button(app, text='-', command=lambda:calci('-'),font = ('Arial',23)).place(x=100,y=250)

ttk.Button(app, text='*', command=lambda:calci('*'),font = ('Arial',23)).place(x=150,y=250)

ttk.Button(app, text='/', command=lambda:calci('/'),font = ('Arial',23)).place(x=200,y=250)

box = ttk.Listbox(app, height=5, fg= 'red', activestyle='dotbox')
box.insert(1,'sample1')
box.insert(2,'sample2')
box.insert(3,'sample3')
box.place(x=350,y=40)

def show():
    print(box.get(box.curselection()))

ttk.Button(app, text='show', command=show).place(x=350,y=250)    
app.mainloop()
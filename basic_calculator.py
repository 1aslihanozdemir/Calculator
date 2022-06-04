from tkinter import *

app= Tk()
app.geometry('300x300')
app.configure(background='powder blue')


app.title('CALCULATOR')

entry_1= Entry(app,justify='right',background='white')
entry_1.pack(fill=BOTH,ipady=10,padx=10,pady=5)
entry_1.focus()

def write(x):
    i = len(entry_1.get())
    entry_1.insert(i,str(x))

h=""
num1 =0
num2=0
def islem(x):
    global h
    h = x
    global num1
    num1 = float(entry_1.get())
    entry_1.delete(0,'end')

def calculate():
    global num2
    global h 
    num2 = float(entry_1.get())
    result = 0
    if h=="+": result = toplama(num1,num2)
    elif h=="-": result = cikarma(num1,num2)
    elif h=="*": result = carpma(num1,num2)
    elif h=="/": result = bolme(num1,num2)
    elif h=="^": result = us_alma(num1,num2)
    entry_1.delete(0,"end")
    entry_1.insert(0,str(result))
    





Bt1 = Button(text=str(1),font='Arial 15 bold',command=lambda x=1:write(x))
Bt1.place(x=10,y=50)
Bt2 = Button(text=str(2),font='Arial 15 bold',command=lambda x=2:write(x))
Bt2.place(x=60,y=50)
Bt3 = Button(text=str(3),font='Arial 15 bold',command=lambda x=3:write(x))
Bt3.place(x=110,y=50)
Bt4 = Button(text=str(4),font='Arial 15 bold',command=lambda x=4:write(x))
Bt4.place(x=10,y=100)
Bt5 = Button(text=str(5),font='Arial 15 bold',command=lambda x=5:write(x))
Bt5.place(x=60,y=100)
Bt6 = Button(text=str(6),font='Arial 15 bold',command=lambda x=6:write(x))
Bt6.place(x=110,y=100)
Bt7 = Button(text=str(7),font='Arial 15 bold',command=lambda x=7:write(x))
Bt7.place(x=10,y=150)
Bt8 = Button(text=str(8),font='Arial 15 bold',command=lambda x=8:write(x))
Bt8.place(x=60,y=150)
Bt9 = Button(text=str(9),font='Arial 15 bold',command=lambda x=9:write(x))
Bt9.place(x=110,y=150)
Bt0 = Button(text=str(0),font='Arial 15 bold',command=lambda x=0:write(x))
Bt0.place(x=10,y=200)
button_point = Button(app,text='.',font=('Arial',15))
button_point.place(x=60,y=200)


button_toplama = Button(app,text='+',font=('Arial',15),command=lambda x='+' :islem(x))
button_toplama.place(x=160,y=50)
button_cikarma = Button(app,text='-',font=('Arial',15),command=lambda x='-' :islem(x))
button_cikarma.place(x=160,y=100)
button_carpma = Button(app,text='*',font=('Arial',15),command=lambda x='*' :islem(x))
button_carpma.place(x=160,y=150)
button_bolme = Button(app,text='/',font=('Arial',15),command=lambda x='/' :islem(x))
button_bolme.place(x=160,y=200)
button_us_alma= Button(app,text='^',font=('Arial',15),command=lambda x='^' :islem(x))
button_us_alma.place(x=210,y=50)
button_ = Button(app,text='=',fg='dark red',font=('Arial',15),command=calculate)
button_.place(x=110,y=200)
button_clear = Button(app,text='C',fg='dark blue',font=('Arial',14),command=lambda x="C":entry_1.delete(0,"end") )
button_clear.place(x=210,y=100)




def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def us_alma(a,b):
    return a**b

app.mainloop()
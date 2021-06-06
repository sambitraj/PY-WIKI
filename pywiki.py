import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

win=Tk()
win.title("py-wikipedia")
win.geometry('250x70')

def serach_wiki():
    search=entry.get()
    answer=wikipedia.summary(search)
    showinfo("PY-WIKIPEDIA ANSWER",answer)

label=Label(win,text="py-wikipedia search")
label.grid(row=0,column=0)

entry=Entry(win)
entry.grid(row=1,column=0)

button=Button(win,text="search",command=serach_wiki)
button.grid(row=1,column=1,padx=10)

win.mainloop()





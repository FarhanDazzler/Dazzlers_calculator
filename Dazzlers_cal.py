from tkinter import *
'''Thank you for coming here...
May Dazzler's light shine upon u all..'''
root =Tk()
root.geometry("350x350+300+300")
root.resizable(0,0)
root.title("Dazzler's Calculater v1.0")
root.wm_iconbitmap("k.ico")


#Dazzler's coding
def click(event):
    global sc
    text=event.widget.cget("text")
    if text=="=":
        if sc.get().isdigit():
            value=int(sc.get())
        else:
            try:
                value=eval(sc.get())
                sc.set(value)
            except Exception as e:
                value="Error!"
                sc.set(value)
    elif text=="C":
        sc.set("")
        #screen.update()

    else:
        sc.set(sc.get() + text)
        #screen.update()


#Screen
#dazzler's code
sc=StringVar()
sc.set("")
screen=Entry(root,font="Verdana 27",textvar=sc,bg="black",fg='white').pack(expand=True,fill="both")

#frame
#dazzler's code
btnrow1=Frame(root,bg="#000000")
btnrow1.pack(expand=True,fill="both")

btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both")

btnrow3=Frame(root,)
btnrow3.pack(expand=True,fill="both")

btnrow4=Frame(root)
btnrow4.pack(expand=True,fill="both")

btnrow5=Frame(root)
btnrow5.pack(expand=True,fill="both")



#button
#dazzler's code
#first row
btn1=Button(btnrow1,text="1",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn1.pack(side="left",expand=True,fill="both")
btn1.bind("<Button-1>",click)

btn2=Button(btnrow1,text="2",font="Verdana 20",relief="groove",border="0",fg="white",bg='black',activebackground="gray37")
btn2.pack(side="left",expand=True,fill="both")
btn2.bind("<Button-1>",click)

btn3=Button(btnrow1,text="3",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn3.pack(side="left",expand=True,fill="both")
btn3.bind("<Button-1>",click)

btnplus=Button(btnrow1,text="+",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btnplus.pack(side="left",expand=True,fill="both")
btnplus.bind("<Button-1>",click)

#second row
btn4=Button(btnrow2,text="4",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn4.pack(side="left",expand=True,fill="both")
btn4.bind("<Button-1>",click)

btn5=Button(btnrow2,text="5",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn5.pack(side="left",expand=True,fill="both")
btn5.bind("<Button-1>",click)


btn6=Button(btnrow2,text="6",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn6.pack(side="left",expand=True,fill="both")
btn6.bind("<Button-1>",click)

btnmin=Button(btnrow2,text="-",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btnmin.pack(side="left",expand=True,fill="both")
btnmin.bind("<Button-1>",click)

#third row
btn7=Button(btnrow3,text="7",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn7.pack(side="left",expand=True,fill="both")
btn7.bind("<Button-1>",click)

btn8=Button(btnrow3,text="8",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn8.pack(side="left",expand=True,fill="both")
btn8.bind("<Button-1>",click)

btn9=Button(btnrow3,text="9",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn9.pack(side="left",expand=True,fill="both")
btn9.bind("<Button-1>",click)

btnmul=Button(btnrow3,text="*",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btnmul.pack(side="left",expand=True,fill="both")
btnmul.bind("<Button-1>",click)

#forth row
btn0=Button(btnrow4,text=".",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn0.pack(side="left",expand=True,fill="both")
btn0.bind("<Button-1>",click)

btn5=Button(btnrow4,text="0",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn5.pack(side="left",expand=True,fill="both")
btn5.bind("<Button-1>",click)

btn6=Button(btnrow4,text="00",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btn6.pack(side="left",expand=True,fill="both")
btn6.bind("<Button-1>",click)

btnmin=Button(btnrow4,text="/",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btnmin.pack(side="left",expand=True,fill="both")
btnmin.bind("<Button-1>",click)




#forth row
btnmod=Button(btnrow5,text="%",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btnmod.pack(side="left",expand=True,fill="both")
btnmod.bind("<Button-1>",click)

btnclr=Button(btnrow5,text="C",font="Verdana 20",relief="groove",border="0",fg='white',bg='black',activebackground="gray37")
btnclr.pack(side="left",expand=True,fill="both")
btnclr.bind("<Button-1>",click)

btnmin=Button(btnrow5,text="=",font="Verdana 20",relief="groove",border="0",padx="5",pady=5,fg='white',bg="firebrick4",activebackground="gray37")
btnmin.pack(side="left",expand=True,fill="both")
btnmin.bind("<Button-1>",click)

root.mainloop()


#dazzler's code
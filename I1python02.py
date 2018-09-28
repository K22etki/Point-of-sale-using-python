from tkinter import *
from tkinter import Tk,StringVar,ttk
import random 
import time
import datetime
from tkinter import messagebox

root=Tk()
root.geometry()
root.title("Smoothie Center")
root.configure(background='black')

mylist=[]
#--------------------Functions------------------------------------------
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator=" "
    text_Input.set(" ")
 
def btnEqualsInput():
   global operator
   sumup=str(eval(operator))
   text_Input.set(sumup)
   operator=" "
   
def iExit():
  qExit=messagebox.askyesno("Quit System","Do youu want to quit?")
  if qExit==True:
       root.destroy()
       return
        
def Reset():
    Tax.set("0")
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    SubTotal.set("0")
    txtMango.delete(0)
    txtGrape.delete(0)
    txtChikoo.delete(0)
    txtPineApple.delete(0)
    txtPapaya.delete(0)
    txtOrange.delete(0)
    txtChocolate.delete(0)
    txtDutchAlmonds.delete(0)
    txtEspresso.delete(0)
    txtIcedcoffee.delete(0)
    txtCappuccino.delete(0)
    txtJelly.delete(0)
    
    
    Total.set("0")
    text_Input.set("0")
    Ticketclass.set("")
    TicketPrice.set("")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    From_Destinations.set("")
    To_Destinations.set("")
    Fee_Price.set("")
    
    mylist=[]
    txtReceipt.delete(1.0,'end')

def  total():
    global mylist
    mylist=[]
    if(var4.get()==1):
        q=int(txtMango.get())
        Cost=50*q
        print(Cost)
        mylist.append(['Mango',q,50,Cost])
    if(var5.get()==1):
         q=int(txtGrape.get())
         Cost=60*q
         mylist.append(['Grape',q,60,Cost])
    if(var6.get()==1):
         q=int(txtChikoo.get())
         Cost=70*q
         mylist.append(['Chikoo',q,70,Cost])
    if(var7.get()==1):
         q=int(txtPapaya.get())
         Cost=70*q
         mylist.append(['Papaya',q,70,Cost])
    if(var8.get()==1):
         q=int(txtPineApple.get())
         Cost=70*q
         mylist.append(['PineApple',q,70,Cost])
    if(var9.get()==1):
         q=int(txtOrange.get())
         Cost=70*q
         mylist.append(['Orange',q,70,Cost])



    if(var1.get()==1):
         q=int(txtEspresso.get())
         Cost=40*q
         mylist.append(['Espresso',q,40,Cost])
    
    if(var2.get()==1):
         q=int(txtIcedcoffee.get())
         Cost=50*q
         mylist.append(['Icedcoffee',q,50,Cost])

       
    if(var3.get()==1):
         q=int(txtCappuccino.get())
         Cost=60*q
         mylist.append(['Cappuccino',q,60,Cost])

           
    if(var13.get()==1):
         q=int(txtChocolate.get())
         Cost=50*q
         mylist.append(['Black Forest',q,50,Cost])



    if(var14.get()==1):
         q=int(txtDutchAlmonds.get())
         Cost=60*q
         mylist.append(['DutchAlmonds',q,60,Cost])


    
    if(var15.get()==1):
         q=int(txtJelly.get())
         Cost=70*q
         mylist.append(['Devils Delight',q,70,Cost])
         print(mylist)

    print(mylist)
    txtb123=''
    txtReceipt.insert('insert','Item\tquantity\tcost\ttotal\n')
    for i in mylist:
        txtb123+=str(i[0])+"\t   "+str(i[1])+"\t"+str(i[2])+"\t"+str(i[3])+"\n"
    txtReceipt.insert('insert',txtb123)
    txtReceipt.insert('insert','\t\t\t%d\n'%(sum([i[3] for i in mylist])))
import printing
def GenrateRec():
    printing.PrintReceipt(random.randint(1,10000000000),mylist,sum([i[3] for i in mylist]))
    
#------------------------------------Variables---------------
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar() 
Tax=StringVar()
var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
SubTotal=StringVar()
Total=StringVar()
text_Input=StringVar()
operator=""
Tax=IntVar()
#-----------------------------Frame work---------------------------------------------------------------
Tops=Frame(root,width=1350,height=100,bd=14,relief='raise')
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,relief='raise')
f1.pack(side=LEFT)
f2=Frame(root,width=440,height=650,bd=8,relief='raise')
f2.pack(side=RIGHT)


frameTopRight=Frame(f2,width=440,height=650,bd=12,relief='raise')
frameTopRight.pack(side=TOP)
frameBottomRight=Frame(f2,width=440,height=50,bd=16,relief='raise')
frameBottomRight.pack(side=BOTTOM)


f1a=Frame(f1,width=900,height=330,bd=8,relief='raise')
f1a.pack(side=TOP)
f2a=Frame(f1,width=900,height=330,bd=6,relief='raise')
f2a.pack(side=BOTTOM)


topLeft1=Frame(f1a,width=300,height=200,bd=16,relief='raise')
topLeft1.pack(side=LEFT)
topLeft2=Frame(f1a,width=300,height=200,bd=16,relief='raise')
topLeft2.pack(side=RIGHT)
"""topLeft3=Frame(f1a,width=300,height=200,bd=16,relief='raise')
topLeft3.pack(side=RIGHT)"""


bottomleft1=Frame(f2a,width=450,height=450,bd=14,relief='raise')
bottomleft1.pack(side=LEFT)
bottomleft2=Frame(f2a,width=450,height=450,bd=14,relief='raise')
bottomleft2.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
lbltitle=Label(Tops,font=('arial',40,'bold'),text="  Smoothie center  ",bd=10,width=41,justify='left')
lbltitle.grid(row=0,column=0)

#------------------------------------Calculator-----------------------------------------------
text_Input=StringVar()
txtDisplay = Entry(bottomleft2,font=('arial',10,'bold'), textvariable=text_Input, bd=10,bg="powder blue",width=40,justify="right")
txtDisplay.grid(columnspan=4)

btn7=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="7",bg="powder blue",width=4,command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="8",bg="powder blue",width=4, command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="9",bg="powder blue",width=4, command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="+",bg="powder blue",command=lambda:btnClick("+"),width=4).grid(row=2,column=3)
#-----------------------------------------------------------------------------------------------------------------------
btn4=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="4",bg="powder blue",width=4, command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="5",bg="powder blue",width=4, command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="6",bg="powder blue",width=4, command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="-",bg="powder blue",command=lambda:btnClick("-"),width=4).grid(row=3,column=3)

#-----------------------------------------------------------------------------------------------------------------------------

btn1=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="1",bg="powder blue",width=4, command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="2",bg="powder blue",width=4, command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="3",bg="powder blue",width=4, command=lambda:btnClick(3)).grid(row=4,column=2)


Multiply=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="*",bg="powder blue",command=lambda:btnClick("*"),width=4).grid(row=4,column=3)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
btn0=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="0",bg="powder blue",width=4, command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="C",bg="powder blue",width=4,command= btnClearDisplay).grid(row=5,column=1)
btnEquals=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="=",bg="powder blue",width=4,command=btnEqualsInput).grid(row=5,column=2)

Division=Button(bottomleft2,padx=8,pady=8,bd=8,fg="black",font=('arial',10,'bold'),text="/",bg="powder blue",command=lambda:btnClick("/"),width=4).grid(row=5,column=3)
#-----------------------------------------------------------------------------------------------------------------

lblReceipt=Label(frameTopRight,font=('arial',16,'bold'),text="Receipt",bd=10,width=41,height=3,justify='center')
lblReceipt.grid(row=0,column=0)


txtReceipt=Text(frameBottomRight,width=50,height=20,bg='white',bd=8,font=('arial',11,'bold'))
txtReceipt.grid(row=1,column=0,columnspan=4) 
  

btnTotal=Button(frameBottomRight,text='Total',padx=2,pady=2,bd=2,fg='black',font=('arial',20,'bold'),
                width=6,height=1,command=total).grid(row=7,column=0)        
       
btnClear=Button(frameBottomRight,text='Clear',padx=2,pady=2,bd=2,fg='black',font=('arial',20,'bold'),
                width=6,height=1,command=Reset).grid(row=7,column=1)        


btnReceipt=Button(frameBottomRight,text='Receipt',padx=2,pady=2,bd=2,fg='black',font=('arial',20,'bold'),
                width=6,height=1,command=GenrateRec).grid(row=7,column=2)        



btnExit=Button(frameBottomRight,text='Exit',padx=2,pady=2,bd=2,fg='black',font=('arial',20,'bold'),
                width=6,height=1,command=iExit).grid(row=7,column=3)        
              


#---------------------------------------------------------
lblType=Label(topLeft1,font=('arial',22,'bold'),text="Breverage",bd=8)
lblType.grid(row=0,column=0,sticky=W)

chkEspresso=Checkbutton(topLeft1,font=('arial',20,'bold'),text="Espresso      -/40",variable=var1,onvalue=1,offvalue=0)
chkEspresso.grid(row=1,column=0,sticky=W)
txtEspresso=Spinbox(topLeft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtEspresso.grid(row=1,column=1)

chkIcedcoffee=Checkbutton(topLeft1,font=('arial',20,'bold'),text="Iced coffee    -/50",variable=var2,onvalue=1,offvalue=0)
chkIcedcoffee.grid(row=2,column=0,sticky=W)
txtIcedcoffee=Spinbox(topLeft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtIcedcoffee.grid(row=2,column=1)

chkCappuccino=Checkbutton(topLeft1,font=('arial',20,'bold'),text="Cappuccino -/60",variable=var3,onvalue=1,offvalue=0)
chkCappuccino.grid(row=3,column=0,sticky=W)
txtCappuccino=Spinbox(topLeft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtCappuccino.grid(row=3,column=1)
#------------------------------Menu---------------------------------------------------------------------------
lblType=Label(bottomleft1,font=('arial',22,'bold'),text="Smoothie",bd=8)
lblType.grid(row=0,column=0,sticky=N)

lblMango=Checkbutton(bottomleft1,font=('arial',20,'bold'),text="Mango        50/-",variable=var4,onvalue=1,offvalue=0)
lblMango.grid(row=3,column=0)
txtMango=Spinbox(bottomleft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtMango.grid(row=3,column=1)

lblGrape=Checkbutton(bottomleft1,font=('arial',20,'bold'),text="Grape        60/-",variable=var5,onvalue=1,offvalue=0)
lblGrape.grid(row=4,column=0)
txtGrape=Spinbox(bottomleft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtGrape.grid(row=4,column=1)

lblChikoo=Checkbutton(bottomleft1,font=('arial',20,'bold'),text="Chikoo      70/-",variable=var6,onvalue=1,offvalue=0)
lblChikoo.grid(row=5,column=0)
txtChikoo=Spinbox(bottomleft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtChikoo.grid(row=5,column=1)



lblPapaya=Checkbutton(bottomleft1,font=('arial',20,'bold'),text="Papaya      70/-",variable=var7,onvalue=1,offvalue=0)
lblPapaya.grid(row=6,column=0)
txtPapaya=Spinbox(bottomleft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtPapaya.grid(row=6,column=1)


lblPineApple=Checkbutton(bottomleft1,font=('arial',20,'bold'),text="PineApple   70/-",variable=var8,onvalue=1,offvalue=0)
lblPineApple.grid(row=7,column=0)
txtPineApple=Spinbox(bottomleft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtPineApple.grid(row=7,column=1)

lblOrange=Checkbutton(bottomleft1,font=('arial',20,'bold'),text="Orange     70/-",variable=var9,onvalue=1,offvalue=0)
lblOrange.grid(row=8,column=0)
txtOrange=Spinbox(bottomleft1, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtOrange.grid(row=8,column=1)

#--------------------------------------------------------------------------------------------------

"""lblSelect=Label(topLeft3,font=('arial',22,'bold'),text="Customize your Cup",bd=8)
lblSelect.grid(row=0,column=0,sticky=W,columnspan=10)
lblDestinations=Label(topLeft3,font=('arial',22,'bold'),text="Categories",bd=8)
lblDestinations.grid(row=1,column=0,sticky=W)

cboDestination=ttk.Combobox(topLeft3,textvariable=var12,state='readonly',fon=('arial',20),width=8)
cboDestination['value']=(' ', 'Avengers',
    'Dc legends',         
     'Classic',
    'Barcelona ',
    'Real Madrid'
     )
     

cboDestination.current(0)
cboDestination.grid(row=1,column=1)

chkSmall=Checkbutton(topLeft3,font=('arial',20,'bold'),text="Small",variable=var10,onvalue=1,offvalue=0)
chkSmall.grid(row=3,column=0,sticky=W)
chkLarge=Checkbutton(topLeft3,font=('arial',20,'bold'),text="Large",variable=var11,onvalue=1,offvalue=0)
chkLarge.grid(row=4,column=0,sticky=W)"""

#--------------------------------------------------------------------------------------------------------
lblPastry=Label(topLeft2,font=('arial',22,'bold'),text="Pastry ",bd=8)
lblPastry.grid(row=0,column=0,sticky=W)

chkChocolate=Checkbutton(topLeft2,font=('arial',20,'bold'),text="Black    forest  -50/",variable=var13,onvalue=1,offvalue=0)
chkChocolate.grid(row=1,column=0,sticky=W)
txtChocolate=Spinbox(topLeft2, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtChocolate.grid(row=1,column=1)


chkDutchAlmonds=Checkbutton(topLeft2,font=('arial',20,'bold'),text="Dutch Almond  -60/",variable=var14,onvalue=1,offvalue=0)
chkDutchAlmonds.grid(row=2,column=0,sticky=W)
txtDutchAlmonds=Spinbox(topLeft2, from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtDutchAlmonds.grid(row=2,column=1)


chkJelly=Checkbutton(topLeft2,font=('arial',22,'bold'),text="Devils Delight -70/",variable=var15,onvalue=1,offvalue=0)
chkJelly.grid(row=3,column=0,sticky=W)
txtJelly=Spinbox(topLeft2,from_=0, to=10,font=('arial',16,'bold'),bd=8,width=6,justify='left')
txtJelly.grid(row=3,column=1)

#---------------------------------------------------------------------------------------------------


root.mainloop()

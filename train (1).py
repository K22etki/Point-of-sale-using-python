from tkinter import *
from tkinter import Tk,StringVar,ttk
import random 
import time
import datetime
from tkinter import messagebox

root=Tk()
root.geometry()
root.title("Train ticket")
root.configure(background='black')

Date1=StringVar()
time1=StringVar()
qExit=StringVar()

Ticketclass=StringVar()
TicketPrice=StringVar()
Child_Ticket=StringVar()
Adult_Ticket=StringVar()
From_Destinations=StringVar()
Fee_Price=StringVar()
Route=StringVar()
Receipt_Ref=StringVar()


Ticketclass.set("")
TicketPrice.set("")
Child_Ticket.set("")
Adult_Ticket.set("")
From_Destinations.set("")
Fee_Price.set("")
Route.set("")
Receipt_Ref.set("")





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
topLeft3=Frame(f1a,width=300,height=200,bd=16,relief='raise')
topLeft3.pack(side=RIGHT)


bottomleft1=Frame(f2a,width=450,height=450,bd=14,relief='raise')
bottomleft1.pack(side=LEFT)
bottomleft2=Frame(f2a,width=450,height=450,bd=14,relief='raise')
bottomleft2.pack(side=RIGHT)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
lbltitle=Label(Tops,font=('arial',40,'bold'),text="  Train Ticketing System  ",bd=10,width=41,justify='left')
lbltitle.grid(row=0,column=0)
#-------------------------------------------------------------------------------------

lblReceipt=Label(frameTopRight,font=('arial',14,'bold'),text="Travelling Ticketing System",bd=10,width=31,height=8,justify='center')
lblReceipt.grid(row=0,column=0)


lblClass1=Label(frameBottomRight,font=('arial',12,'bold'),text="Class",width=8,justify='center',relief="sunken")
lblClass1.grid(row=0,column=0)


lblClass2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblClass2.grid(row=1,column=0)


lblTicket1=Label(frameBottomRight,font=('arial',12,'bold'),text="Ticket",width=8,justify='center',relief="sunken")
lblTicket1.grid(row=0,column=1)
lblTicket2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblTicket2.grid(row=1,column=1)


lblAdult1=Label(frameBottomRight,font=('arial',12,'bold'),text="Adult",width=8,justify='center',relief="sunken")
lblAdult1.grid(row=0,column=2)
lblAdult2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblAdult2.grid(row=1,column=2)

lblChild1=Label(frameBottomRight,font=('arial',12,'bold'),text="Child",width=8,justify='center',relief="sunken")
lblChild1.grid(row=0,column=3)
lblChild2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblChild2.grid(row=1,column=3)


lblFrom1=Label(frameBottomRight,font=('arial',12,'bold'),text="From",width=8,justify='center',relief="sunken")
lblFrom1.grid(row=2,column=1)
lblFrom2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblFrom2.grid(row=2,column=2 )

lblTo1=Label(frameBottomRight,font=('arial',12,'bold'),text="To",width=8,justify='center',relief="sunken")
lblTo1.grid(row=3,column=1)
lblTo2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblTo2.grid(row=3,column=2 )

lblPrice1=Label(frameBottomRight,font=('arial',12,'bold'),text="Price",width=8,justify='center',relief="sunken")
lblPrice1.grid(row=4,column=1)
lblPrice2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblPrice2.grid(row=4,column=2 )



lblRefNo1=Label(frameBottomRight,font=('arial',12,'bold'),text="Ref no:",width=8,justify='center',relief="sunken")
lblRefNo1.grid(row=5,column=0)
lblRefNo2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblRefNo2.grid(row=6,column=0 )


lblTime1=Label(frameBottomRight,font=('arial',12,'bold'),text="Time",width=8,justify='center',relief="sunken")
lblTime1.grid(row=5,column=1)
lblTime2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken",textvariable=time1)
lblTime2.grid(row=6,column=1)


lblDate1=Label(frameBottomRight,font=('arial',12,'bold'),text="Date",width=8,justify='center',relief="sunken")
lblDate1.grid(row=5,column=2)
lblDate2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken",textvariable=Date1)
lblDate2.grid(row=6,column=2)


lblRoute1=Label(frameBottomRight,font=('arial',12,'bold'),text="Route",width=8,justify='center',relief="sunken")
lblRoute1.grid(row=5,column=3)
lblRoute2=Label(frameBottomRight,font=('arial',12,'bold'),width=8,justify='center',relief="sunken")
lblRoute2.grid(row=6,column=3 )











#---------------------------------------------------------------
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
 
def btnEqualsInput():
   global operator
   sumup=str(eval(operator))
   text_Input.set(sumup)
   operator=""
   
def iExit():
  qExit=messagebox.askyesno("Quit System","Do youu want to quit?")
  if qExit:
       root.destroy()
       root.quit()
        
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
    SubTotal.set("0")
    Total.set("0")
    text_Input.set("0")
    Ticketclass.set("")
    TicketPrice.set("")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    From_Destinations.set("")
    To_Destinations.set("")
    Fee_Price.set("")
    
  




def chkbutton_value():
    if(var7.get()==1):
        var8.set("")
        entSingle.configure(state=NORMAL)
    elif var7.get()==0:
        entSingle.configure(state=DISABLED)
        var8.set("0")
    if(var9.get()==1):
        var10.set("")
        entReturn.configure(state=NORMAL)
    elif(var9.get()==0):
        entReturn.configure(state=DISABLED)
        var10.set("0")
        
        
def Travel_Cost():
    if (var4.get()=="Wadala Road" and var1.get()==1 and var5.get()==1):
        Tcost=float(30.8)
        Single=float(var12.get())
        Adult_Tax="Rs." ,str('%.2f'%((Tcost*Single)*0.03))
        Adult_Fees="Rs." ,str('%.2f'%(Tcost*Single))
        TotalCost="Rs." ,str('%.2f'%((Tcost*Single)+((Tcost*Single)*0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("SecondClass")
        TicketPrice.set(Adult_Fees)
        Child_Ticet.set("NO")
        Adult_Ticket.set("YES")
        From_Destination.set("Panvel")
        To_Destination.set("Wadala Road")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")
        
        
        x=random.randint(109,5876)
        randomRef=str(x)
        Receipt_Ref.set("TFL"+randomRef)
     
    elif (var4.get()=="Wadala Road" and var1.get()==1 and var6.get()==1):
        Tcost=float(23.8)
        Single=float(var12.get())
        Child_Tax="Rs.",str('%.2f'%(Tcost*0))
        Child_Fees="Rs." ,str('%.2f'%(Tcost*Single))
        TotalCost="Rs." ,str('%.2f'%((Tcost*Single)+((Tcost*Single)*0)))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        Ticketclass.set("SecondClass")
        TicketPrice.set(Child_Fees)
        Child_Ticet.set("YES")
        Adult_Ticket.set("NO")
        From_Destination.set("Panvel")
        To_Destination.set("Wadala Road")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")
        
        x=random.randint(109,5876)
        randomRef=str(x)
        Receipt_Ref.set("TFL"+randomRef)
        
         
        
        

#------------------------------------------------

Tax=StringVar()
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
SubTotal=StringVar()
TotalCost=StringVar()
text_Input=StringVar()
operator=""

#----------------------------------------------------------------
Date1.set(time.strftime("%d/%m/%y"))
time1.set(time.strftime('%H:%M:%S'))



#----------------------------------------------------------------
lblClass=Label(topLeft1,font=('arial',22,'bold'),text="Class",bd=8)
lblClass.grid(row=0,column=0,sticky=W)

chkSecondclass=Checkbutton(topLeft1,font=('arial',20,'bold'),text="Second Class",variable=var1,onvalue=1,offvalue=0)
chkSecondclass.grid(row=1,column=0,sticky=W)
chkFirstclass=Checkbutton(topLeft1,font=('arial',20,'bold'),text="First Class",variable=var2,onvalue=1,offvalue=0)
chkFirstclass.grid(row=2,column=0,sticky=W)
chkACclass=Checkbutton(topLeft1,font=('arial',20,'bold'),text="AC Class",variable=var3,onvalue=1,offvalue=0)
chkACclass.grid(row=3,column=0,sticky=W)

#---------------------------------------------------------------
lblSelect=Label(topLeft3,font=('arial',22,'bold'),text="Select A destination",bd=8)
lblSelect.grid(row=0,column=0,sticky=W,columnspan=10)
lblDestinations=Label(topLeft3,font=('arial',22,'bold'),text="Destinations",bd=8)
lblDestinations.grid(row=1,column=0,sticky=W)

cboDestination=ttk.Combobox(topLeft3,textvariable=var4,state='readonly',fon=('arial',20),width=8)
cboDestination['value']=(' ', 'Wadala Road',
	'Guru Tegh Bahadur Nagar', 		
 	'Chunabhatti 	',	
	'Kurla ',		
 	'Tilak Nagar', 		 	
    'Chembur', 		
	'Govandi ',		
	'Mankhurd 	',	
	'Vashi ',		
	'Sanpada', 		
	'Juinagar 	',	
 	'Nerul ',		
 	'Seawoods-Darave', 
 	'CBD Belapur ',		
 	'Kharghar',	
	'Mansarovar',
 	'Khandeshwar' ,		
	'Panvel' )
cboDestination.current(0)
cboDestination.grid(row=1,column=1)
chkAdult=Checkbutton(topLeft3,font=('arial',20,'bold'),text="Adult",variable=var5,onvalue=1,offvalue=0)
chkAdult.grid(row=3,column=0,sticky=W)
chkChild=Checkbutton(topLeft3,font=('arial',20,'bold'),text="Child",variable=var6,onvalue=1,offvalue=0)
chkChild.grid(row=4,column=0,sticky=W)

#-------------------------------------------------------------------------------------------


lblClass=Label(topLeft2,font=('arial',22,'bold'),text="Ticket Type",bd=8)
lblClass.grid(row=0,column=0,sticky=W)

chkSingle=Checkbutton(topLeft2,font=('arial',20,'bold'),text="Single",command=chkbutton_value,variable=var7,onvalue=1,offvalue=0)
chkSingle.grid(row=1,column=0,sticky=W)
entSingle=Entry(topLeft2,font=('arial',22,'bold'),textvariable=var8,bd=2,width=8)
entSingle.grid(row=1,column=1,sticky=W)


chkReturn=Checkbutton(topLeft2,font=('arial',20,'bold'),text="Return",variable=var9,onvalue=1,offvalue=0,command=chkbutton_value)
chkReturn.grid(row=2,column=0,sticky=W)
entReturn=Entry(topLeft2,font=('arial',22,'bold'),textvariable=var10,bd=2,width=8)
entReturn.grid(row=2,column=1,sticky=W)

lblComment=Label(topLeft2,font=('arial',22,'bold'),text="Comment",bd=8)
lblComment.grid(row=3,column=0,sticky=W)
entComment=Entry(topLeft2,font=('arial',22,'bold'),textvariable=var11,bd=2,width=8)
entComment.grid(row=3,column=1,sticky=W)
#----------------------------------------------------------------------------------
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
lblStateTax=Label(bottomleft1,font=('arial',24,'bold'),text="State Tax",bd=16,anchor='w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(bottomleft1,font=('arial',24,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtStateTax.grid(row=3,column=3)               
 

lblSubTotal=Label(bottomleft1,font=('arial',24,'bold'),text="Sub Total",bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(bottomleft1,font=('arial',24,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtSubTotal.grid(row=4,column=3)    


lblTotalCost=Label(bottomleft1,font=('arial',24,'bold'),text="Total Cost",bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)
txtCost=Entry(bottomleft1,font=('arial',24,'bold'),textvariable=TotalCost,bd=10,insertwidth=4,bg="#ffffff",justify='right')
txtTotalCost.grid(row=5,column=3)          

#-------------------------------------------------------------------------------------------------------------------
lblSpace=Label(bottomleft1,font=('arial',24,'bold'),text="    \n             ",bd=16,anchor="w")
lblSpace.grid(row=6,column=2) 
#------------------------------------------------------------------------------------------------------------
lblSpace=Label(bottomleft2,font=('arial',24,'bold'),text="    \n             ",bd=16,anchor="w")
lblSpace.grid(row=6,columnspan=4) 
#--------------------------------------------------------------------------------------------------------------
"""lblsp=Label(frameBottomRight,font=('arial',14,'bold'),width=10,height=1,relief="sunken",justify='center')
lblsp.grid(row=9,column=0)"""
#--------------------------------------------------------------------------------------------------------------------------------

lblReceipt=Label(frameBottomRight,font=('arial',14,'bold'),text="Receipt",bd=2,anchor='w')
lblReceipt.grid(row=9,column=0,sticky=W) 


txtReceipt=Text(frameBottomRight,width=40,height=7,bg='white',bd=8,font=('arial',11,'bold'))
txtReceipt.grid(row=10,column=0,columnspan=4) 
#----------------------------------------------------------------------------------------------------------


btnTotal=Button(frameBottomRight,text='Total',padx=2,pady=2,bd=2,fg='black',font=('arial',12,'bold'),
                width=6,height=1,command=Travel_Cost).grid(row=7,column=0)        
       
btnClear=Button(frameBottomRight,text='Clear',padx=2,pady=2,bd=2,fg='black',font=('arial',12,'bold'),
                width=6,height=1,command=Reset).grid(row=7,column=1)        


btnReset=Button(frameBottomRight,text='Reset',padx=2,pady=2,bd=2,fg='black',font=('arial',12,'bold'),
                width=6,height=1,command=Reset).grid(row=7,column=2)        



btnExit=Button(frameBottomRight,text='Exit',padx=2,pady=2,bd=2,fg='black',font=('arial',12,'bold'),
                width=6,height=1,command=iExit).grid(row=7,column=3)        
              




root.mainloop()



 
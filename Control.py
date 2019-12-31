from tkinter import *
from tkinter import ttk, Text, messagebox
from DbConnect import DBConnect
from ListRequest import ListTicket


dbConnect=DBConnect()
root=Tk()
root.title("Ticket Reservation")
root.configure(background='#e1d8b2')

#style
style=ttk.Style()
style.theme_use('classic')
style.configure("TLabel", backgroun="#eld8b2")
style.configure('TButton',backgroun="#eld8b2")
style.configure('TRadiobutton',backgroun="#eld8b2")

#Full Name
ttk.Label(root,text="Full Name:").grid(row=0,column=0,padx=10,pady=10)
EnterFullName=ttk.Entry(root, width=30,font=('Arial',16))
EnterFullName.grid(row=0,column=1,columnspan=2,pady=10)
#Gender
ttk.Label(root, text="Gender:").grid(row=1,column=0)
SpanGender=StringVar()
ttk.Radiobutton(root,text="Male",variable=SpanGender,value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Femal",variable=SpanGender,value="Femal").grid(row=1,column=2)

#Comment
ttk.Label(root,text="Comments:").grid(row=2,column=0)
txtComments=Text(root, width=30, height=15, font=('Arial',16))
txtComments.grid(row=2,column=1,columnspan=2)

#buttons
buSubmit=ttk.Button(root,text="Submit")
buSubmit.grid(row=3,column=3)
buList=ttk.Button(root,text="List Res.")
buList.grid(row=3,column=2)

#Function
def BuSaveData():
    #print("Full Name:{}".format(EnterFullName.get()))
    #print("Gender:{}".format(SpanGender.get()))
    #print("Comments:{}".format(txtComments.get(1.0,'end')))

    msg=dbConnect.Add(EnterFullName.get(),SpanGender.get(),txtComments.get(1.0,'end'))
    messagebox.showinfo(title="Add info",message=msg)
    EnterFullName.delete(0,'end')
    txtComments.delete(1.0, 'end')





def BuListData():
        #TODO: show orders
        print('not implemented yet')
        ListRequest=ListTicket()


buSubmit.config(command=BuSaveData)
buList.config(command=BuListData)


root.mainloop()



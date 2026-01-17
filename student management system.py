from tkinter import *
from tkinter import ttk

import mysql.connector

win=Tk()
win.title("Student Management System")
win.geometry('1400x670')

connec=mysql.connector.connect(host='localhost',user='root',password='',db='SMS')
mycur=connec.cursor(buffered=True)




    
#TITLE FRAM7
tframe=Frame(win,bg="lightblue",height=20,bd=5,relief="groove",cursor="hand2")
tframe.pack(fill="x")
t_label=Label(tframe,text="Students Management System",font=('arial',28,'bold')
                  ,bg='lightblue').pack(pady=20)


#/BODY FRAME
b_frame=Frame(win,bd=1,relief="solid")
b_frame.pack(fill="both",expand=True)
win.columnconfigure(0,weight=1)
win.columnconfigure(0,weight=3)

#LEFT FRAME
l_frame=Frame(b_frame,width=100,height=40,bd=1,relief="solid")
l_frame.pack(side="left",pady=15,padx=15,ipadx=10,ipady=20,fill='y')

l_label=Label(l_frame,text="Manage Students",font=('arial',20,'bold')).grid(row=0,column=0,columnspan=2,padx=10,pady=10)

l_label1=Label(l_frame,text="Roll No.",font=('times new roman',15,'bold')).grid(row=2,column=0,sticky='w',padx=(10,20),pady=(5,10))
l_entry1=Entry(l_frame,width=21,font=('times new roman',15,'bold'),bd=1,relief='solid')
l_entry1.grid(row=2,column=1,padx=(0,15))

l_label2=Label(l_frame,text="Name",font=('times new roman',15,'bold')).grid(row=1,column=0,sticky='w',padx=(10,20),pady=(5,10))
l_entry2=Entry(l_frame,width=21,font=('times new roman',15,'bold'),bd=1,relief='solid')
l_entry2.grid(row=1,column=1,padx=(0,15))

l_label3=Label(l_frame,text="Email",font=('times new roman',15,'bold')).grid(row=3,column=0,sticky='w',padx=(10,20),pady=(5,10))
l_entry3=Entry(l_frame,width=21,font=('times new roman',15,'bold'),bd=1,relief='solid')
l_entry3.grid(row=3,column=1,padx=(0,15))

l_label4=Label(l_frame,text="Gender",font=('times new roman',15,'bold')).grid(row=4,column=0,sticky='w',padx=(10,20),pady=(5,10))
l_entry4=Entry(l_frame,width=21,font=('times new roman',15,'bold'),bd=1,relief='solid')
l_entry4.grid(row=4,column=1,padx=(0,15))

l_label5=Label(l_frame,text="Contact",font=('times new roman',15,'bold')).grid(row=5,column=0,sticky='w',padx=(10,20),pady=(5,10))
l_entry5=Entry(l_frame,width=21,font=('times new roman',15,'bold'),bd=1,relief='solid')
l_entry5.grid(row=5,column=1,padx=(0,15))

l_label6=Label(l_frame,text="D.O.B",font=('times new roman',15,'bold')).grid(row=6,column=0,sticky='w',padx=(10,20),pady=(5,10))
l_entry6=Entry(l_frame,width=21,font=('times new roman',15,'bold'),bd=1,relief='solid')
l_entry6.grid(row=6,column=1,padx=(0,15))

l_label7=Label(l_frame,text="Address",font=('times new roman',15,'bold')).grid(row=7,column=0,sticky='w',padx=(10,20),pady=(5,10))
l_entry7=Text(l_frame,width=21,height=5,font=('times new roman',15,'bold'),bd=1,relief='solid')
l_entry7.grid(row=7,column=1,padx=(0,15))

#LEFT BUTTONS
l_bframe=Frame(l_frame,height=30,bd=6,relief='groove')

l_bframe.grid(row=9,column=0,columnspan=2,pady=30,padx=(10,0),sticky="nsew")
l_bframe.rowconfigure(9,weight=1)
l_bframe.columnconfigure(0,weight=1)





#RIGHT FRAME
r_frame=Frame(b_frame,relief="sunken",bd=1,bg="lightgrey")
r_frame.pack(side="right",fill='both',expand=True)

r_frame.rowconfigure(1,weight=1)
r_frame.columnconfigure(0,weight=1)

#RIGHT BUTTONS
r_label=Label(r_frame,text="Search By",font=('times new roman',15,'bold'),bg="lightgrey").grid(row=0,column=0,ipady=6,padx=(10,0))

r_entry1=ttk.Combobox(r_frame,values=('Roll No.','Name','Email','Gender','Conatct','D.O.B','Address'),width=25)
r_entry1.current(1)
r_entry1.grid(row=0,column=1,padx=10,pady=15,ipady=6)

r_entry2=Entry(r_frame,width=30,bd=2,relief='groove').grid(row=0,column=2,padx=10,pady=15,ipady=6)

r_button1=Button(r_frame,text="Search",font=('times new roman',12,'bold'),width=9,height=1,relief="raised",cursor="hand2").grid(row=0,column=3,padx=20)
r_button2=Button(r_frame,text="Show All",font=('times new roman',12,'bold'),width=9,height=1,relief="raised",cursor="hand2").grid(row=0,column=4)

#EXCEL LIKE TABLE
r_bframe = ttk.Frame(r_frame)
r_bframe.grid(row=1,column=0,columnspan=22,sticky='nsew')

r_bframe.rowconfigure(0, weight=1)
r_bframe.columnconfigure(0, weight=1)

var_column=("roll", "name", "email", "gender", "contact","dob", "address")
table = ttk.Treeview(r_bframe,columns=var_column,show="headings")

table.heading("roll", text="Roll No")
table.heading("name", text="Name")
table.heading("email", text="E-mail")
table.heading("gender", text="Gender")
table.heading("contact", text="Contact")
table.heading("dob", text="D.O.B")
table.heading("address", text="Address")

table.grid(row=0, column=0, sticky="nsew")

for col in var_column:
   table.column(col, width=130,anchor="center",stretch=False)

v_scroll = ttk.Scrollbar(r_bframe, orient="vertical", command=table.yview)
h_scroll = ttk.Scrollbar(r_bframe, orient="horizontal", command=table.xview)

table.configure(yscrollcommand=v_scroll.set)
table.configure(xscrollcommand=h_scroll.set)

v_scroll.grid(row=0, column=1, sticky="ns")
h_scroll.grid(row=1, column=0, sticky="ew")



style = ttk.Style()
style.configure("Treeview", rowheight=28)

def load():
    table.delete(*table.get_children())
    
    mycur.execute('select * from details')
    #RULE use fetchall after select * from table
    rows=mycur.fetchall()   #stores list of tuples
    
    for r in rows:
        table.insert("","end",values=r)    # "" ---- top level window

def Add():
    
    _name=l_entry2.get()
    _rollno=l_entry1.get()
    _email=l_entry3.get()
    _gender=l_entry4.get()
    _contact=l_entry5.get()
    _dob=l_entry6.get()
    _address=l_entry7.get(1.0,END)
    val=(_rollno,_name,_email,_gender,_contact,_dob,_address)
    sql=('insert into details() values(%s,%s,%s,%s,%s,%s,%s)')   
    mycur.execute(sql,val)
    connec.commit()
    load() #this if for delete delete previous add and add new to avoid repeating lines
   

l_button1=Button(l_bframe,text="Add",font=('times new roman',9,'bold'),width=9,height=1,bd=2,relief="ridge",cursor="hand2",command=Add).grid(row=0,column=0,padx=8,pady=8)


def takedata(event):
    selected = table.selection()          # get selected row--return id of selected row
    values = table.item(selected, "values")

    l_entry1.delete(0, END)
    l_entry2.delete(0, END)
    l_entry3.delete(0, END)
    l_entry4.delete(0, END)
    l_entry5.delete(0, END)
    l_entry6.delete(0, END)
    l_entry7.delete("1.0", END)

    l_entry1.insert(0, values[0])
    l_entry2.insert(0, values[1])
    l_entry3.insert(0, values[2])
    l_entry4.insert(0, values[3])
    l_entry5.insert(0, values[4])
    l_entry6.insert(0, values[5])
    l_entry7.insert("1.0", values[6])

 
table.bind("<<TreeviewSelect>>", takedata)

def update():
    selected = table.focus()   #id of selected row
    if selected == "":
        return
    new_values=(l_entry1.get(),l_entry2.get(),l_entry3.get(),l_entry4.get(),l_entry5.get(),l_entry6.get(),l_entry7.get("1.0",END))
    table.item(selected, values=new_values)

l_button2=Button(l_bframe,text="Update",font=('times new roman',9,'bold'),width=9,height=1,bd=2,relief="ridge",cursor="hand2",command=update).grid(row=0,column=1,padx=8,pady=8)

def delete():
    selected = table.selection()
    if not selected:
        return
    table.delete(selected)
  
l_button3=Button(l_bframe,text="Delete",font=('times new roman',9,'bold'),width=9,height=1,bd=2,relief="ridge",cursor="hand2",command=delete).grid(row=0,column=2,padx=8,pady=8)
l_button3=Button(l_bframe,text="Clear",font=('times new roman',9,'bold'),width=9,height=1,bd=2,relief="ridge",cursor="hand2").grid(row=0,column=3,padx=8,pady=8)

win.mainloop()







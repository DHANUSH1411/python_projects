import tkinter
import mysql.connector as mysqlcon
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import StringVar,messagebox

s=tkinter.Tk()
w=s.winfo_screenwidth()
h=s.winfo_screenheight()
s.configure(width=w,height=h)

l=[0]

imagepath=Image.open ("G:/images/karunya.jpg")
res=ImageTk.PhotoImage(imagepath)
imglbl=tkinter.Label(s,image=res)
imglbl.place(y=0,x=0,height=h,width=w)


def clearall():
    mysqldb=mysqlcon.connect(host="localhost",user="root",password="12345",database="trilochan")
    mycursor=mysqldb.cursor()
    query="truncate table student1"
    mycursor.execute(query)
    mysqldb.commit()
    messagebox.showinfo("!","SUCESSFULLY DELETED ")
    for i in l:
        l.remove(i)

def clear():
    rnotb.delete(0,"end")
    snametb.delete(0,"end")
    marktb.delete(0,"end")
    phnotb.delete(0,'end')
    addrestb.delete(0,"end")
    rb.set('Male')
    deltb.delete(0,"end")
    gettb.delete(0,"end")    
    rnotb.focus()
    
cleartable=tkinter.Button(s,text="CLEAR TABLE",font="50",command=clearall,bg="red")
cleartable.place(x=230,y=660)

def insert():
    
    
    rno=int(rnotb.get())
    sname=(snametb.get())
    mark=int(marktb.get())
    phno=int(phnotb.get())
    addres=(addrestb.get())
    if rno not in l:
        mysqldb=mysqlcon.connect(host="localhost",user="root",password="12345",database="trilochan")
        mycursor=mysqldb.cursor()
        insqury="insert into student1 values(%d,'%s',%d,%d,'%s','%s')"%(rno,sname,mark,phno,addres,rb.get())
        mycursor.execute(insqury)                  
        messagebox.showinfo("Insert","Inserted success")
        clear()
        mysqldb.commit()
        l.insert(0,rno)
            
    else:
        messagebox.showinfo("ERROR"," ROLL NUMBER ALREADY EXISTS ")
        clear()    

def delete():
    rno=int(deltb.get())
    mysqldb=mysqlcon.connect(host="localhost",user="root",password="12345",database="trilochan")
    mycursor=mysqldb.cursor()
    mycursor.execute("select * from student1 where rno=%d"%rno)
    data=mycursor.fetchone()
    my_str.set(data)
    deleteddetails=tkinter.Label(s,text="LAST Deleted ROW",width=75,height=3,font="30",fg="black",bg="white")
    deleteddetails.place(x=650,y=150)
    
    
    if rno>=0:   
        mysqldb=mysqlcon.connect(host="localhost",user="root",password="12345",database="trilochan")
        mycursor=mysqldb.cursor()
        query="delete from student1 where rno=%d"%rno
        mycursor.execute(query)
        mysqldb.commit()
        messagebox.showinfo("delete","Delete success")
        clear()
        l.remove(rno)
        
    else:
        messagebox.showinfo("delete","Delete unsuccesful")
def show():
    mysqldb=mysqlcon.connect(host="localhost",user="root",password="12345",database="trilochan")
    mycursor=mysqldb.cursor()
    mycursor.execute("select rno,sname,mark from student1")
    out=tkinter.Label(s,textvariable=my_str,width=75,height=8,fg='black',font="60",background="white")
    out.place(x=650,y=170)        
    data=mycursor.fetchall()
    
    my_str.set(data)
    
def update():
    
        sname=(snametb.get())
        mark=int(marktb.get())
        phno=int(phnotb.get())
        addres=(addrestb.get())
        rno=int(rnotb.get())
        mysqldb=mysqlcon.connect(host="localhost",user="root",password="12345",database="trilochan")
        mycursor=mysqldb.cursor()
        mycursor.execute("select * from student1 where rno=%d"%rno)
        data=mycursor.fetchone()
        updatedetails=tkinter.Label(s,text="LAST Updated ROW",width=75,height=3,font="30",fg="black",bg="white")
        updatedetails.place(x=650,y=150)
        my_str.set(data)
        if rno in l:
            
            mysqldb=mysqlcon.connect(host="localhost",user="root",password="12345",database="trilochan")
            mycursor=mysqldb.cursor()
            insqury="update student1 set sname='%s',mark =%d,phone=%d,address='%s',gender='%s'where rno=%d"%(sname,mark,phno,addres,rb.get(),rno,)
            mycursor.execute(insqury)
            mysqldb.commit()
            messagebox.showinfo("update","Update success")
            clear()
        else:
            messagebox.showinfo("ERROR","NOT SUCH ROLL NUMBER")
                    
sname=tkinter.Label(s,text="Enter Name",font="30",bg="#BDF6FE")
sname.place(x=100,y=220)
snametb=tkinter.Entry(s,font="30")
snametb.place(x=250,y=220)

rno=tkinter.Label(s,text="Roll No",font="30",bg="#BDF6FE")
rno.place(x=100,y=150)
rnotb=tkinter.Entry(s,font="20")
rnotb.place(x=250,y=150)

mark=tkinter.Label(s,text="Enter Mark",font="30",bg="#BDF6FE")
mark.place(x=100,y=280)
marktb=tkinter.Entry(s,font="30")
marktb.place(x=250,y=280)

phno=tkinter.Label(s,text="PhNO",font="20",bg="#BDF6FE")
phno.place(x=100,y=340)
phnotb=tkinter.Entry(s,font="20")
phnotb.place(x=250,y=340)

addres=tkinter.Label(s,text="Address",font="30",bg="#BDF6FE")
addres.place(x=100,y=410)
addrestb=tkinter.Entry(s,font="30")
addrestb.place(x=250,y=410)

add=tkinter.Button(s,text="Insert",font="30",command=insert,bg="red")
add.place(x=140,y=570)

update=tkinter.Button(s,text="Update",font="30",command=update,bg="Red")
update.place(x=380,y=570)

get=tkinter.Button(s,text="Get",font="30",bg="Red",command=lambda: my_details(gettb.get()))
get.place(x=1100,y=460)

my_str=tkinter.StringVar()
my_str.set('Output here')


out=tkinter.Label(s,textvariable=my_str,width=75,height=8,fg='black',font="60",background="white")
out.place(x=650,y=170)

getlb=tkinter.Label(s,text="enter rno",font="30",height=2,width=8,bg='#BDF6FE')
getlb.place(x=700,y=460)

gettb=tkinter.Entry(s,font="50")
gettb.place(x=830,y=465)

gettext=tkinter.Label(s,text="TO GET VALUES",font="20",height=2,width=20,fg='white',background="red")
gettext.place(x=700,y=390)

deltext=tkinter.Label(s,text="TO DELETE VALUES",font="20",height=2,width=20,fg='white',background="red")
deltext.place(x=700,y=570)

dellb=tkinter.Label(s,text="enter rno",font="30",height=2,width=8,bg='#BDF6FE')
dellb.place(x=700,y=640)

delete=tkinter.Button(s,text="Delete",font="30",command=delete,bg="Red")
delete.place(x=1100,y=640)

deltb=tkinter.Entry(s,font="50")
deltb.place(x=830,y=650)

def my_details(id):
    getdetails=tkinter.Label(s,text="THE VALUE THAT YOU WANTED",width=75,height=3,font="30",fg="black",bg="white")
    getdetails.place(x=650,y=150)
    v=id
    if type(v)==str:
        my_str.set('ERROR Check input')
        clear()
    val=int(id)
    if val>=0:             
        my_data=(val,)
        mysqldb=mysqlcon.connect(host="localhost",user="root",password="12345",database="trilochan")
        mycursor=mysqldb.cursor()
        mycursor.execute("select *from student1 where rno=%d"%my_data)
        data=mycursor.fetchone()
        my_str.set(data)
        clear()
showtablelb=tkinter.Button(s,text="SHOW BASIC DETAIL OF TABLE",command=show,font="50",bg="red")
showtablelb.place(x=230,y=740)  

rb=StringVar()
rb.set("Male")

gender=tkinter.Label(s,text="Gender",font='30',bg="#BDF6FE")
gender.place(x=100,y=490)
mradio=tkinter.Radiobutton(s,text="Male",variable=rb,font="30",value="Male",height=1,width=7)
fradio=tkinter.Radiobutton(s,text="Female",variable=rb,font="30",value="Female",height=1,width=7)
oradio=tkinter.Radiobutton(s,text="Others",variable=rb,font="30",value="Others",height=1,width=7)

mradio.place(x="250",y="480")
fradio.place(x="385",y="480")
oradio.place(x="520",y="480")

s.mainloop()

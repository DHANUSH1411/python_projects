#Import library
from tkinter import *

#Initialize Window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Vaibhav - Website Blocker")

#Heading
Label(root, text = 'WEBSITE BLOCKER' , font = 'arial 20 bold').pack()
Label(root,text = 'Vaibhav' , font = 'arial 20 bold').pack(side = BOTTOM)

#Path of our host file and ip address 
host_path = ' '#stores the path of our host file
ip_address = ' '#stores the IP address used by localhost

#Enter Website
Label(root, text= 'Enter Website :', font = 'arial 13 bold').place(x=5,y=60)
Websites = Text(root, font = 'arial 10', height ='2', width = '40', wrap = WORD,padx = 5, pady=5)
Websites.place(x = 140, y =60)

#Block Function
def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

block_btn = Button(root, text = 'BLOCK' , font = 'arial 12 bold', command = Blocker, width = 6 , bg = 'royal blue1', activebackground = 'sky blue')
block_btn.place(x = 230, y =150)

root.mainloop
    

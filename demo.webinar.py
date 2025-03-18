from tkinter import *
from PIL import  ImageTk,Image
from tkinter import messagebox

root = Tk()

def handle_login():
   email =  email_input.get()
   password = password_input.get()

   if email =="SRMist.com" and password == "1234":
      messagebox.showinfo("login Sucessfully")
    
   else :
      messagebox.showerror("error","login failed")
      





root.title("login")
#providing the max size
#root.minsize(100,100)
#providing the minimun size
#root.maxsize(300, 300)

root.geometry("350x500")

#adding a icon 
root.iconbitmap("Designer.ico")
root.configure(background="blue")

img = Image.open("logo.png")

resize_img = img.resize((100,100))

#adding image to gui
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image=img)


#to display the lebel
img_label.pack(pady = (10,10))
text_label = Label(root,text ="flipkart",fg="white",bg ="blue")
text_label.pack()
text_label.config(font =("verdan",24))

email_label = Label(root,text="enter the email id",fg = "white",bg = "blue")
email_label.pack()
email_label.config(font =("vardan",14))

#to get a boxbar
email_input = Entry(root,width = 50)
email_input.pack(ipady = 6 ,pady = (20,5))

#for password

password =Label(root,text="enter the password",fg = "white",bg = "blue") 
password.pack()
password.config(font =("vardan",14))

password_input= Entry(root,show = "*" ,width = 50)
password_input.pack(ipady = 6 ,pady = (20,5))

#for button

login_btn = Button(root,text ="Login here",width = 20,height = 2,command =handle_login )
login_btn.pack()
login_btn.config(font =("vardan",14))


























root.mainloop()


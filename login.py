from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Kamya' and passwordEntry.get()=='102213026':
        messagebox.showinfo('Success','Logged In')
        window.destroy()
        import sms
    elif usernameEntry.get()=='Manunjay' and passwordEntry.get()=='102203009':
        messagebox.showinfo('Success','Logged In')
        window.destroy()
        import sms
    elif usernameEntry.get()=='Pranjal' and passwordEntry.get()=='102203290':
        messagebox.showinfo('Success','Logged In')
        window.destroy()
        import sms
    elif usernameEntry.get()=='Ojasvi' and passwordEntry.get()=='102203960':
        messagebox.showinfo('Success','Logged In')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter the correct credentials')


window=Tk()

window.geometry('1338x900+0+0')
window.title('Student Management System')

#window.resizeable(False,False)

backgroundImage=ImageTk.PhotoImage(file="background.jpg")

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='bisque3')
loginFrame.place(x=550,y=200)

logoImage=ImageTk.PhotoImage(file="logoimage.jpg")

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=5, pady=10)
usernameImage=PhotoImage(file="username.png")
usernameLabel=Label(loginFrame,image=usernameImage,text="Username", compound=LEFT
                    ,font=('Times New Roman',18,'bold', 'italic'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry=Entry(loginFrame,font=('Times New Roman',15,'italic'),bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=10)

passwordImage=PhotoImage(file="password.png")
passwordLabel=Label(loginFrame,image=passwordImage,text="Password", compound=LEFT
                    ,font=('Times New Roman',18,'bold', 'italic'), bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry=Entry(loginFrame,font=('Times New Roman',15,'italic'),bd=5, fg='royalblue')
passwordEntry.grid(row=2, column=1, pady=10, padx=10)

loginButton=Button(loginFrame,text="Login", font=('Times New Roman', 14, 'bold'), fg='white', bg='cornflowerblue', activebackground='cornflowerblue', activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=20, padx=30)




window.mainloop()




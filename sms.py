from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox,filedialog
import pymysql,pandas
def export_data():
    url =filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','First Name','Last Name','Mobile','Email','Address','Dob','Gender','Date','Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfully')
def iexit():
    result=messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
def update_student():
    def update_data():
        query = 'update student set firstname=%s, lastname=%s, mobile=%s, email=%s, address=%s, dob=%s, gender=%s, date=%s, time=%s WHERE id=%s'
        mycursor.execute(query, (fnameEntry.get(), lnameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), dobEntry.get(),
        genderEntry.get(), date, current_time, idEntry.get()))
        con.commit()
        messagebox.showinfo('Successful Update', f'Successfully Updated')
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    idLabel = Label(update_window, text="Student Id", font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'))
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    fnameLabel = Label(update_window, text="First Name", font=('times new roman', 20, 'bold'))
    fnameLabel.grid(row=1, column=0, padx=30, pady=15)
    fnameEntry = Entry(update_window, font=('roman', 15, 'bold'))
    fnameEntry.grid(row=1, column=1, padx=10, pady=15)

    lnameLabel = Label(update_window, text="Last Name", font=('times new roman', 20, 'bold'))
    lnameLabel.grid(row=2, column=0, padx=30, pady=15)
    lnameEntry = Entry(update_window, font=('roman', 15, 'bold'))
    lnameEntry.grid(row=2, column=1, padx=10, pady=15)

    mobileLabel = Label(update_window, text="Mobile No.", font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=3, column=0, padx=30, pady=15)
    mobileEntry = Entry(update_window, font=('roman', 15, 'bold'))
    mobileEntry.grid(row=3, column=1, padx=10, pady=15)

    emailLabel = Label(update_window, text="Email", font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=4, column=0, padx=30, pady=15)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'))
    emailEntry.grid(row=4, column=1, padx=10, pady=15)

    addressLabel = Label(update_window, text="Address", font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=30, pady=15)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'))
    addressEntry.grid(row=5, column=1, padx=10, pady=15)

    dobLabel = Label(update_window, text="DOB", font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15)
    dobEntry = Entry(update_window, font=('roman', 15, 'bold'))
    dobEntry.grid(row=6, column=1, padx=10, pady=15)

    genderLabel = Label(update_window, text="Gender", font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=7, column=0, padx=30, pady=15)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'))
    genderEntry.grid(row=7, column=1, padx=10, pady=15)

    update_student_button = ttk.Button(update_window, text='Update Student', command=update_data)
    update_student_button.grid(row=8, columnspan=2, pady=15)


    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    fnameEntry.insert(0,listdata[1])
    lnameEntry.insert(0,listdata[2])
    mobileEntry.insert(0,listdata[3])
    emailEntry.insert(0,listdata[4])
    addressEntry.insert(0,listdata[5])
    dobEntry.insert(0,listdata[6])
    genderEntry.insert(0,listdata[7])


def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)
def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'This{content_id} is deleted')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
def search_student():
    def search_data():
        query = 'select * from student where id=%s or mobile=%s or email=%s or address=%s or dob=%s or gender=%s'
        mycursor.execute(query, (idEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), dobEntry.get(), genderEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    idLabel = Label(search_window, text="Student Id", font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'))
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    # fnameLabel = Label(search_window, text="First Name", font=('times new roman', 20, 'bold'))
    # fnameLabel.grid(row=1, column=0, padx=30, pady=15)
    # fnameEntry = Entry(search_window, font=('roman', 15, 'bold'))
    # fnameEntry.grid(row=1, column=1, padx=10, pady=15)
    #
    # lnameLabel = Label(search_window, text="Last Name", font=('times new roman', 20, 'bold'))
    # lnameLabel.grid(row=2, column=0, padx=30, pady=15)
    # lnameEntry = Entry(search_window, font=('roman', 15, 'bold'))
    # lnameEntry.grid(row=2, column=1, padx=10, pady=15)

    mobileLabel = Label(search_window, text="Mobile No.", font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=3, column=0, padx=30, pady=15)
    mobileEntry = Entry(search_window, font=('roman', 15, 'bold'))
    mobileEntry.grid(row=3, column=1, padx=10, pady=15)

    emailLabel = Label(search_window, text="Email", font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=4, column=0, padx=30, pady=15)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'))
    emailEntry.grid(row=4, column=1, padx=10, pady=15)

    addressLabel = Label(search_window, text="Address", font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=30, pady=15)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'))
    addressEntry.grid(row=5, column=1, padx=10, pady=15)

    dobLabel = Label(search_window, text="DOB", font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'))
    dobEntry.grid(row=6, column=1, padx=10, pady=15)

    genderLabel = Label(search_window, text="Gender", font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=7, column=0, padx=30, pady=15)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'))
    genderEntry.grid(row=7, column=1, padx=10, pady=15)

    search_student_button = ttk.Button(search_window, text="Search Student", command=search_data)
    search_student_button.grid(row=8, columnspan=2, pady=15)


def add_student():
    def add_data():
        if idEntry.get()=='' or fnameEntry.get()=='' or lnameEntry.get()=='' or mobileEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All Fields are required', parent=add_window)
        else:

            try:
                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (idEntry.get(), fnameEntry.get(), lnameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), dobEntry.get(), genderEntry.get(), date, current_time))
                con.commit()
                result = messagebox.askyesno('Confirm','Data added succesfully. Do you want to clean the form?', parent=add_window)
                print(result)
                if result:
                    idEntry.delete(0, END)
                    fnameEntry.delete(0, END)
                    lnameEntry.delete(0, END)
                    mobileEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    dobEntry.delete(0, END)
                    genderEntry.delete(0, END)
                else:
                    pass

            except:
                messagebox.showerror('Error', 'Student Id should be unique. It can not be repeated', parent=add_window)
                return


            query='select * from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:

                studentTable.insert('',END,values=data)



    add_window=Toplevel()
    add_window.title('Add Student')
    add_window.grab_set()
    idLabel = Label(add_window,text="Student Id",font=('times new roman',20,'bold'))
    idLabel.grid(row=0, column=0 , padx=30, pady=15)
    idEntry = Entry(add_window, font=('roman', 15, 'bold'))
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    fnameLabel = Label(add_window, text="First Name", font=('times new roman', 20, 'bold'))
    fnameLabel.grid(row=1, column=0, padx=30, pady=15)
    fnameEntry = Entry(add_window, font=('roman', 15, 'bold'))
    fnameEntry.grid(row=1, column=1, padx=10, pady=15)

    lnameLabel = Label(add_window, text="Last Name", font=('times new roman', 20, 'bold'))
    lnameLabel.grid(row=2, column=0, padx=30, pady=15)
    lnameEntry = Entry(add_window, font=('roman', 15, 'bold'))
    lnameEntry.grid(row=2, column=1, padx=10, pady=15)

    mobileLabel = Label(add_window, text="Mobile No.", font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=3, column=0, padx=30, pady=15)
    mobileEntry = Entry(add_window, font=('roman', 15, 'bold'))
    mobileEntry.grid(row=3, column=1, padx=10, pady=15)

    emailLabel = Label(add_window, text="Email", font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=4, column=0, padx=30, pady=15)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'))
    emailEntry.grid(row=4, column=1, padx=10, pady=15)

    addressLabel = Label(add_window, text="Address", font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=30, pady=15)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'))
    addressEntry.grid(row=5, column=1, padx=10, pady=15)

    dobLabel = Label(add_window, text="DOB", font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'))
    dobEntry.grid(row=6, column=1, padx=10, pady=15)

    genderLabel = Label(add_window, text="Gender", font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=7, column=0, padx=30, pady=15)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'))
    genderEntry.grid(row=7, column=1, padx=10, pady=15)

    add_student_button = ttk.Button(add_window, text="Add Student", command=add_data)
    add_student_button.grid(row=8, columnspan=2, pady=15)





def connect_database():
    def connect():
        global mycursor, con
        try:
            con= pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
            messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)

        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connectWindow)
        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            query ='use studentmanagementsystem'
            mycursor.execute(query)
            query = 'create table student(id int not null primary key, firstname varchar(50), lastname varchar(50), mobile varchar(10), email varchar(50), address varchar(100), dob varchar(50), gender varchar(50),date varchar(50), time varchar(50))'
            mycursor.execute(query)

        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)

        messagebox.showinfo("Success", "Connected Successfully", parent=connectWindow)
        connectWindow.destroy()
        addStudentButton.config(state=NORMAL)
        searchStudentButton.config(state=NORMAL)
        updateStudentButton.config(state=NORMAL)
        showStudentButton.config(state=NORMAL)
        exportdataButton.config(state=NORMAL)
        deleteStudentButton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)


    hostnameLabel=Label(connectWindow,text='Host Name', font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)


    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text+s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)


def clock():
    global date,current_time
    date = time.strftime('%d/%m/%Y')
    current_time = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'    Date: {date}\nTime: {current_time}')
    datetimeLabel.after(1000, clock)



root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('itft1')

root.geometry("1338x900+0+0")

root.title("Student Management System")

datetimeLabel=Label(root, font=("Times New Roman", 20, "bold", "italic"))
datetimeLabel.place(x=5, y=5)
clock()

s="Student Management System"
sliderLabel=Label(root, font=("Times New Roman", 30, "bold", "italic"), width=30)
sliderLabel.place(x=500, y=0)
slider()

connectButton = ttk.Button(root, text="Connect Database", command=connect_database)
connectButton.place(x=1300, y=0)

leftFrame = Frame(root, bg='SlateGray2')
leftFrame.place(x=30, y=80, width=300, height=680)

logo_image = PhotoImage(file='recordlogo.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=10, pady=20)

addStudentButton = ttk.Button(leftFrame, text="Add Student", width=15, state=DISABLED, command=add_student)
addStudentButton.grid(row=1, column=10, pady=20, padx=100)

searchStudentButton = ttk.Button(leftFrame, text="Search Student", width=15, state=DISABLED, command=search_student)
searchStudentButton.grid(row=2, column=10, pady=20, padx=100)

deleteStudentButton = ttk.Button(leftFrame, text="Delete Student", width=15, state=DISABLED, command=delete_student)
deleteStudentButton.grid(row=3, column=10, pady=20, padx=100)

updateStudentButton = ttk.Button(leftFrame, text="Update Student", width=15, state=DISABLED,command=update_student)
updateStudentButton.grid(row=4, column=10, pady=20, padx=100)

showStudentButton = ttk.Button(leftFrame, text="Show Student", width=15, state=DISABLED,command=show_student)
showStudentButton.grid(row=5, column=10, pady=20, padx=100)

exportdataButton = ttk.Button(leftFrame, text="Export Data", width=15, state=DISABLED,command=export_data)
exportdataButton.grid(row=6, column=10, pady=20, padx=100)

exitButton = ttk.Button(leftFrame, text="Exit", width=15,command=iexit)
exitButton.grid(row=7, column=10, pady=20, padx=100)

rightFrame = Frame(root, bg='SlateGray2')
rightFrame.place(x=350, y=80, width=1150, height=680)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=('Student ID', 'First Name', 'Last Name', 'Mobile No', 'Email', 'Address', 'DOB', 'Gender', 'Added Date', 'Added Time'), xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarX.pack(side=RIGHT, fill=Y)

studentTable.pack(expand=1, fill='both')

studentTable.heading('Student ID', text='Student ID')
studentTable.heading('First Name', text='First Name')
studentTable.heading('Last Name', text='Last Name')
studentTable.heading('Mobile No', text='Mobile No')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('DOB', text='DOB')
studentTable.heading('Gender', text='Gender')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')

studentTable.column('Student ID', width=200,anchor=CENTER)
studentTable.column('First Name', width=200,anchor=CENTER)
studentTable.column('Last Name', width=200,anchor=CENTER)
studentTable.column('Mobile No', width=200,anchor=CENTER)
studentTable.column('Email', width=300,anchor=CENTER)
studentTable.column('Address', width=200,anchor=CENTER)
studentTable.column('DOB', width=200,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview', rowheight=30, font=('arial',12,'bold'), background='SlateGray2')
style.configure('Treeview.Heading', font=('arial',15,'bold'))


studentTable.config(show='headings')

root.mainloop()
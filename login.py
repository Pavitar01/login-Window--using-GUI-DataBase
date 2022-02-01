from tkinter import *
from PIL import Image, ImageTk  # install pillow
from tkinter import messagebox
from tkinter import ttk
import pymysql


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window_By-Pavi")
        self.root.geometry("1020x550+200+50")
        self.root.config(bg="#4682b4")
        self.root.resizable(False, False)
        ##################### bg image ######################

        # root window ka object

        image = Image.open("bg01.png")

        # Resize the image using resize() method
        resize_image = image.resize((200, 400))

        img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label1 = Label(image=img, bg="#4682b4")
        label1.image = img
        label1.place(x=20, y=80, width=400, height=400)

        image1 = Image.open("avatar.png")

        # Resize the image using resize() method
        resize_image = image1.resize((250, 290))

        img1 = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label2 = Label(image=img1, bg="#dcdcdc")
        label2.image = img1
        label2.place(x=120, y=80, width=199, height=300)







        frame1 = Frame(self.root, bg='#dcdcdc')
        frame1.place(x=320, y=80, width=550, height=400)

        title = Label(frame1, text="LOGIN HERE !", font=('times new roman', 30, "bold"), bg='#dcdcdc',
                      fg='#008b8b').place(
            x=50, y=30)

        ####################################### VARIABLE ###################################################
        self.txt_email = StringVar()
        self.txt_pass = StringVar()

        Email = Label(frame1, text="Email Address", font=('times new roman', 20, "bold"), bg='#dcdcdc',
                      fg='#3d4035').place(
            x=50, y=120)
        txt_email = Entry(frame1, font=('times new roman', 15), bg='#f4f0ec', textvariable=self.txt_email).place(x=50,
                                                                                                                 y=160,
                                                                                                                 width=280)

        Password = Label(frame1, text="Password", font=('times new roman', 20, "bold"), bg='#dcdcdc',
                         fg='#3d4035').place(x=50, y=190)
        txt_pass = Entry(frame1, font=('times new roman', 15), bg='#f4f0ec', textvariable=self.txt_pass).place(x=50,
                                                                                                               y=230,
                                                                                                               width=280)

        reg = Button(frame1, text='Create A New Account', bd=0, cursor='hand2', command=self.Register_window,
                     font=('', 10, "bold"), bg='#dcdcdc',
                     fg='red', activebackground='#dcdcdc').place(x=26, y=260, width=180, height=40)
        forgot = Button(frame1, text='Forgot Password ', bd=0, cursor='hand2', command=self.forgot_window,
                        font=('', 10, "bold"), bg='#dcdcdc',
                        fg='red', activebackground='#dcdcdc').place(x=200, y=260, width=180, height=40)

        login_btn = Button(frame1, text='Login', bd=3, cursor='hand2', font=('', 10, "bold"), bg='green', fg='#e5e4e2',
                           activebackground='green', command=self.Login).place(x=50, y=310, width=200, height=40)

    def Login(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All Feilds Are Required..")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="registration")
            cur = con.cursor()
            cur.execute("SELECT * FROM register WHERE Email=%s and Password=%s",
                        (self.txt_email.get(), self.txt_pass.get()))
            row = cur.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", 'Invalid UserName & Password')
            else:
                messagebox.showinfo("Success", "Login Successfully")
                self.root.destroy()
                import sms

                con.commit()
                self.clear1()
                con.close()

    def clear1(self):
        self.txt_email.set("")
        self.txt_pass.set("")

    def Register_window(self):
        self.root.destroy()
        import main

    def forgot_window(self):
        self.root2 = Toplevel()
        self.root2.title("Forgot Password")
        self.root2.geometry("350x480+650+140")
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.config(bg="#1a2421")
        self.root2.resizable(False, False)


        ####################################### VARIABLE ###################################################
        self.txt_Email_ = StringVar()
        self.cmb_sec_ques_ = StringVar()
        self.txt_sec_ = StringVar()
        self.txt_new_pass = StringVar()


        title = Label(self.root2, text="Forgot Password", font=('times new roman', 20, "bold"), bg="#1a2421",
                      fg='white').place(x=80, y=10)

        Email_ = Label(self.root2, text="Email Address", font=('times new roman', 15, "bold"), bg='#1a2421',
                       fg='white').place(x=50, y=100)
        txt_Email_ = Entry(self.root2, font=('times new roman', 15), bg='lightgrey',textvariable=self.txt_Email_).place(x=50, y=140, width=250)

        #############################  Security Question #################################################

        Sec_ques = Label(self.root2, text="Select Security Question", font=('times new roman', 15, "bold"), bg='#1a2421',
                         fg='white').place(x=50, y=180)
        cmb_sec_ques_ = ttk.Combobox(self.root2,textvariable=self.cmb_sec_ques_ ,font=('times new roman', 15),
                                    state='readonly', justify=CENTER)
        cmb_sec_ques_['values'] = ('Select', 'Your First School Name', 'Your BestFriend Name', 'your First Pet Name')
        cmb_sec_ques_.place(x=50, y=215, width=250)
        cmb_sec_ques_.current(0)


        #############################  Ans  #################################################

        sec_ans = Label(self.root2, text="Security Answer", font=('times new roman', 15, 'bold'), bg='#1a2421',fg='white').place(x=50, y=250)
        txt_sec_ = Entry(self.root2, font=('times new roman', 15), bg='lightgrey',textvariable=self.txt_sec_).place(x=50,y=280,width=250)


        #############################  New Pass  #################################################


        new_pass = Label(self.root2, text="New Password", font=('times new roman', 15, 'bold'), bg='#1a2421',fg='white').place(x=50, y=310)
        txt_new_pass = Entry(self.root2, font=('times new roman', 15), bg='lightgrey',textvariable=self.txt_new_pass).place(x=50,y=340,width=250)


        confirm_btn = Button(self.root2, text='Confirm', bd=3, cursor='hand2', font=('', 10, "bold"), bg='green', fg='#e5e4e2',
                           activebackground='green', command=self.Confirm).place(x=75, y=390, width=200, height=40)



    def Confirm(self):
        if self.txt_Email_.get() == "" or self.txt_sec_.get() == "" or self.cmb_sec_ques_.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "All Feilds Are Required..")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="registration")
            cur = con.cursor()
            cur.execute("SELECT * FROM register WHERE Email=%s and Question=%s and Answer=%s",
                        (self.txt_Email_.get(), self.cmb_sec_ques_.get(),self.txt_sec_.get()))
            row2 = cur.fetchone()

            if row2 == None:
                messagebox.showerror("Error", 'Invalid UserName Or Please Select Correct Question For Security Answer')
            else:
                cur.execute(
                    "UPDATE register set Password=%s WHERE  Email = %s ",
                    (self.txt_new_pass.get(), self.txt_Email_.get()))
                con.commit()
                self.clear2()
                con.close()
                messagebox.showinfo("Success", "Password Change Succesfully,Please Login With New Password")


    def clear2(self):
        self.txt_Email_.set("")
        self.txt_new_pass.set("")
        self.txt_sec_.set("")
        self.cmb_sec_ques_.set("Select")



root = Tk()
ob = Register(root)
root.mainloop()


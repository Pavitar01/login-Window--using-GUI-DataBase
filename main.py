from tkinter import *
from PIL import Image, ImageTk  # install pillow
from tkinter import messagebox
from tkinter import ttk
from pymysql import connect


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form Window_By Pavi")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="darkblue")
        self.root.resizable(False, False)

        ##################### bg image ######################

        self.bg = ImageTk.PhotoImage(file="new1.jpg")
        bg = Label(self.root, image=self.bg, bd=0).place(x=0, y=0, relwidth=1, relheight=1)
        # root window ka object

        #self.left = ImageTk.PhotoImage(file="image/bg01.png")
        bg = Label(self.root,bg='#f5f5f5').place(x=150, y=100, width=400, height=500)

        image = Image.open("new.png")

        # Resize the image using resize() method
        resize_image = image.resize((340, 400))

        img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=150, y=100, width=300, height=300)


        frame1 = Frame(self.root,bg='#f5f5f5')
        frame1.place(x=450, y=100, width=700, height=500)

        title = Label(frame1, text="SIGN UP", font=('times new roman', 25, "bold"), bg='#f5f5f5', fg='green').place(
            x=50, y=30)
        ####################################### VARIABLE ###################################################
        self.txt_Fname = StringVar()
        self.txt_Lname = StringVar()
        self.txt_contact = StringVar()
        self.txt_Email = StringVar()
        self.cmb_sec_ques = StringVar()
        self.txt_sec = StringVar()
        self.txt_pass = StringVar()
        self.txt_con_pass = StringVar()

        Fname = Label(frame1, text="First Name", font=('times new roman', 15, "bold"), bg='#f5f5f5', fg='#3d4035').place(
            x=50, y=90)
        txt_Fname = Entry(frame1, font=('times new roman', 15), bg='lightgrey', textvariable=self.txt_Fname).place(x=50,
                                                                                                                   y=120,
                                                                                                                   width=250)

        #############################  Last Name #################################################
        Lname = Label(frame1, text="Last Name", font=('times new roman', 15, "bold"), bg='#f5f5f5', fg='#3d4035').place(
            x=370, y=90)
        txt_Lname = Entry(frame1, font=('times new roman', 15), bg='lightgrey', textvariable=self.txt_Lname).place(
            x=370, y=120, width=250)

        #############################  contact No #################################################

        contact = Label(frame1, text="Contact No.", font=('times new roman', 15, "bold"), bg='#f5f5f5',
                        fg='#3d4035').place(
            x=50, y=150)
        txt_contact = Entry(frame1, font=('times new roman', 15), bg='lightgrey', textvariable=self.txt_contact).place(
            x=50, y=180, width=250)

        #############################  Email.id #################################################

        Email_ = Label(frame1, text="Email Id", font=('times new roman', 15, "bold"), bg='#f5f5f5', fg='#3d4035').place(
            x=370, y=150)
        txt_Email = Entry(frame1, font=('times new roman', 15), bg='lightgrey', textvariable=self.txt_Email).place(
            x=370, y=180, width=250)

        #############################  Security Question #################################################

        Sec_ques = Label(frame1, text="Select Security Question", font=('times new roman', 15, "bold"), bg='#f5f5f5',
                         fg='#3d4035').place(x=50, y=210)
        cmb_sec_ques = ttk.Combobox(frame1, textvariable=self.cmb_sec_ques, font=('times new roman', 15),
                                    state='readonly', justify=CENTER)
        cmb_sec_ques['values'] = ('Select', 'Your First School Name', 'Your BestFriend Name', 'your First Pet Name')
        cmb_sec_ques.place(x=50, y=240, width=250)
        cmb_sec_ques.current(0)

        #############################  Question  #################################################

        sec_ans = Label(frame1, text="Security Answer", font=('times new roman', 15, 'bold'), bg='#f5f5f5',
                        fg='#3d4035').place(
            x=370, y=210)
        txt_sec = Entry(frame1, font=('times new roman', 15), bg='lightgrey', textvariable=self.txt_sec).place(x=370,
                                                                                                               y=240,
                                                                                                               width=250)

        #############################  Password  #################################################

        pass_ = Label(frame1, text="Password", font=('times new roman', 15, "bold"), bg='#f5f5f5', fg='#3d4035').place(
            x=50, y=270)
        txt_pass = Entry(frame1, font=('times new roman', 15), bg='lightgrey', textvariable=self.txt_pass).place(x=50,
                                                                                                                 y=300,
                                                                                                                 width=250)

        #############################  Question  #################################################

        con_pass = Label(frame1, text="Confirm Password", font=('times new roman', 15, "bold"), bg='#f5f5f5',
                         fg='#3d4035').place(x=370, y=270)
        txt_con_pass = Entry(frame1, font=('times new roman', 15), bg='lightgrey',
                             textvariable=self.txt_con_pass).place(x=370, y=300, width=250)

        ############################ Check Btn ####################################################

        self.txt_check = IntVar()
        check_btn = Checkbutton(frame1, text="I Agree The Term & Condition", font=('times new roman', 15, 'bold'),
                                onvalue=1, offvalue=0, bg='#f5f5f5', fg='#3d4035', activebackground='white',
                                variable=self.txt_check).place(x=50,
                                                               y=350)

        #####################  reg btn image ######################

        reg = Button(frame1, text='CREATE ACCOUNT', bd=3, cursor='hand2', command=self.Register_data,
                     font=('', 10, "bold"), bg='green', fg='#e5e4e2', activebackground='green').place(x=50, y=420,
                                                                                                      width=200,
                                                                                                      height=40)

        s_al = Label(self.root, text="Already Have An Account ?", font=('times new roman', 15, "bold"), bg='#f5f5f5',
                     fg='black').place(x=180, y=400)
        signin = Button(self.root, text='Sign In', bd=2, cursor='hand2', command=self.login_window,
                        font=('times new roman', 20, "bold"),
                        bg='#f5f5f5',
                        fg='black').place(x=250, y=450, width=100, height=40)

    def Register_data(self):
        if self.txt_Fname.get() == "" or self.txt_Lname.get() == "" or self.txt_contact.get() == "" or self.txt_Email.get() == "" or self.cmb_sec_ques.get() == "" or self.txt_sec.get() == "" or self.txt_pass.get() == "" or self.txt_con_pass.get() == "":
            messagebox.showerror("ERROR", "All Feilds Are Required", parent=self.root)

        elif self.txt_pass.get() != self.txt_con_pass.get():
            messagebox.showerror("ERROR", "Both Password Should Match", parent=self.root)

        elif self.txt_check.get() == 0:
            messagebox.showerror("ERROR", "Please Accept The Term & Condition", parent=self.root)
        else:
            con = connect(host="localhost", user="root", password="", database="registration")
            cur = con.cursor()
            cur.execute("SELECT * FROM `register` WHERE  Email=%s", self.txt_Email.get())
            row = cur.fetchone()
            print(row)
            if row != None:
                messagebox.showerror("Error", 'User Already Exist With This Main, Please Try With Another Email ')

            else:
                messagebox.showinfo("SUCCESS", "Account Create Successfully", parent=self.root)

                cur.execute('INSERT INTO  `register`  values(%s,%s,%s,%s,%s,%s,%s)', (
                    self.txt_Fname.get(), self.txt_Lname.get(), self.txt_contact.get(), self.txt_Email.get(),
                    self.cmb_sec_ques.get(), self.txt_sec.get(), self.txt_pass.get()))
                con.commit()
                self.clear1()
                con.close()

    def clear1(self):
        self.txt_Fname.set("")
        self.txt_Lname.set("")
        self.txt_contact.set("")
        self.txt_Email.set("")
        self.cmb_sec_ques.set("Select")
        self.txt_sec.set("")
        self.txt_pass.set("")
        self.txt_con_pass.set("")

    def login_window(self):
        self.root.destroy()
        import login


root = Tk()
ob = Register(root)
root.mainloop()

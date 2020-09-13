from tkinter import *
from tkinter import ttk #for combobox in address
import pymysql 
from tkinter import messagebox

class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="indigo",fg="red")
        title.pack(side=TOP,fill=X)



        ####======All variables======####
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


        ############ manage frame ############
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="navy")
        Manage_frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_frame,text="Manage student",bg="navy",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_frame,text="Roll No",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_frame,text="Name",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email=Label(Manage_frame,text="Email",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender=Label(Manage_frame,text="Gender",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=20,padx=10)

        
        lbl_contact=Label(Manage_frame,text="Contact",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(Manage_frame,text="D.O.B",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(Manage_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_addr=Label(Manage_frame,text="Address",bg="navy",fg="white",font=("times new roman",20,"bold"))
        lbl_addr.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_addr=Text(Manage_frame,width=30,height=3,font=("",10))
        self.txt_addr.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        ## Button Frame ##

        Bttn_frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="plum")
        Bttn_frame.place(x=10,y=510,width=430)


        Addbtn=Button(Bttn_frame,text="Add",width=10,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(Bttn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(Bttn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(Bttn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        





        ############ detail frame ############
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="dark green")
        detail_frame.place(x=500,y=100,width=800,height=580)

        lbl_search=Label(detail_frame,text="Search By",bg="dark green",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("roll_no","pname","contact")
        combo_search.grid(row=0,column=1,pady=20,padx=10)

        txt_search=Entry(detail_frame,textvariable=self.search_txt,font=("times new roman",13,"bold"),width=15,bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(detail_frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showbtn=Button(detail_frame,text="Show",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        
        ## table frame ##

        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="dark green")
        table_frame.place(x=10,y=70,width=760,height=500)


        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("Address",text="Address")
        self.student_table['show']='headings'  #this will not show extra column which is default 
        
        self.student_table.column("roll",width=100)   #setting our sizes not using default sizes
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.pack(fill=BOTH,expand=1)  # for showing in a page
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_student(self):
        
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are require!!")
        
        elif self.dob_var.get()=="" or self.contact_var.get()=="":
            messagebox.showerror("Error","All fields are require!!")
        
        
        else:
            con=pymysql.connect(host="localhost",user="root",password="password",database="stm")
            cur=con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_addr.get('1.0',END)
                                                                        ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="password",database="stm")
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_addr.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_addr.delete("1.0",END)
        self.txt_addr.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="password",database="stm")
        cur=con.cursor()
        cur.execute("update student set pname=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_addr.get('1.0',END),
                                                                        self.Roll_No_var.get()
                                                                        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="password",database="stm")
        cur=con.cursor()
        cur.execute("delete from student where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="password",database="stm")
        cur=con.cursor()

        cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()




root=Tk()
ob=student(root)
root.mainloop()
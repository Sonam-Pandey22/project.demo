from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")


      # variable

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_dob=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_photo=StringVar()
        self.var_teacher=StringVar()
        
        




# first image
        img=Image.open(r"C:\Users\pande\OneDrive\Desktop\face recognition system\college_images\facial recognition related images - Search Images_files\5e831650276529.58cbf962698eb.jpg")
        img = img.resize((500, 150), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=150)

        # second image

        img1=Image.open(r"C:\Users\pande\OneDrive\Desktop\face recognition system\college_images\facial recognition related images - Search Images_files\college-project-study-for-college-entrance-exam-university-concept-modern-flat-illustration-vector.jpg")
        img1 = img1.resize((500, 150), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=450,height=150)

         # third image

        img2=Image.open(r"C:\Users\pande\OneDrive\Desktop\face recognition system\college_images\facial recognition related images - Search Images_files\D430_50_041_1200.jpg")
        img2 = img2.resize((450, 150), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=450,height=150)

       # bg image

        img3=Image.open(r"C:\Users\pande\OneDrive\Desktop\face recognition system\college_images\facial recognition related images - Search Images_files\Best-Website-New-Wallpaper.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENTS MANAGEMENT SYSTEM" ,font=("times new roman",20,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=34)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=40,width=1330,height=600)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=640,height=480)

        # current course

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information")
        current_course_frame.place(x=5,y=5,width=625,height=150)

         # department 

        dep_label=Label(current_course_frame,text="Department",font=("times now roman",12,"bold",),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep,font=("times now roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select department","CS","AI","Machine Learning","IT","Civil","MBA","MCA","BCA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # course

        course_label=Label(current_course_frame,text="Course",font=("times now roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times now roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select course","Computer science","Management")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year

        year_label=Label(current_course_frame,text="Year",font=("times now roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times now roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select year","2018-20","2018-20","2020-24","2024-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # semester

        semester_label=Label(current_course_frame,text="Semester",font=("times now roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times now roman",13,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","sem-1","sem2","sem-3","sem-4","sem-5","sem-6","sem-7","sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

         # class students information

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Students information")
        class_student_frame.place(x=5,y=160,width=625,height=280)

         #student id

        studentId_label=Label(class_student_frame,text="StudentID:",font=("times now roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=2,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times now roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=2,sticky=W)


         #student name
         
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times now roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=2, pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=18,font=("times now roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #class division
         
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times now roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=2, pady=5,sticky=W)
        
        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=18,font=("times now roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

       
        #Roll no
         
        roll_no_label=Label(class_student_frame,text="Roll NO:",font=("times now roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=2, pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18,font=("times now roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

       # Gender
         
        gender_label=Label(class_student_frame,text="Gender:",font=("times now roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=2, pady=5,sticky=W)
        
        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=18,font=("times now roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

       
        # DOB
         
        dob_label=Label(class_student_frame,text="DOB:",font=("times now roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=2, pady=5,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times now roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

       
      # Email
         
        email_label=Label(class_student_frame,text="Email:",font=("times now roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=2, pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times now roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)

       # Phone NO
         
        phone_label=Label(class_student_frame,text="Phone NO:",font=("times now roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=2, pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times now roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)

       # Address
         
        address_label=Label(class_student_frame,text="Address:",font=("times now roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=2, pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=18,font=("times now roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

       # Teachers Name
         
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times now roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=2, pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=18,font=("times now roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

       # radio buttons
        
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio2,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # button frame

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=620,height=30)

        save_btn=Button(btn_frame,text="Save", command=self.add_data,width=15,font=("times now roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=15,font=("times now roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=15,font=("times now roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=15,font=("times now roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=230,width=620,height=30)

        take_photo_btn=Button(btn_frame1,text="Take Photo sample",width=30,font=("times now roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=30,font=("times now roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)




        #Right label frame

        Reft_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students details",font=("times new roman",12,"bold"))
        Reft_frame.place(x=660,y=10,width=660,height=480)

        # Search system
       
        search_frame=LabelFrame(Reft_frame,bd=2,bg="white",relief=RIDGE,text="Search System")
        search_frame.place(x=5,y=5,width=640,height=60)

        search_label=Label(search_frame,text="Search By:",font=("times now roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=2, pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times now roman",13,"bold"),state="readonly",width=12)
        search_combo["values"]=("Select","Semester","Roll No","Phone no","Department","Year")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=12,font=("times now roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times now roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times now roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        # table frame

        table_frame=Frame(Reft_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=70,width=640,height=380)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","sem","student id","course","year","name","div","roll no","gender","dob","email","phone no","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("student id",text="Student ID")
        self.student_table.heading("roll no",text="Roll NO")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone no",text="Phone NO")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

         
        self.student_table.column("dep",width=100) 
        self.student_table.column("course",width=100) 
        self.student_table.column("year",width=100) 
        self.student_table.column("sem",width=100) 
        self.student_table.column("student id",width=100)
        self.student_table.column("roll no",width=100) 
        self.student_table.column("name",width=100) 
        self.student_table.column("div",width=100) 
        self.student_table.column("dob",width=100) 
        self.student_table.column("gender",width=100) 
        self.student_table.column("email",width=100) 
        self.student_table.column("phone no",width=100) 
        self.student_table.column("address",width=100) 
        self.student_table.column("teacher",width=100) 
        self.student_table.column("photo",width=150) 
        

        self.student_table.pack(fill=BOTH,expand=1)
        
      #  function declaration

        def add_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required")
            else:
                pass    



        

       
       

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
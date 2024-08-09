from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
        


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM", bg="white", fg="black",bd=10,relief=RIDGE,font=("arial",20,"bold"),padx=0,pady=3)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=100,width=1530,height=400)
        
        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION", bg="powder blue", fg="black",bd=10,relief=RIDGE,font=("arial",13,"bold"))
        DataFrameLeft.place(x=0,y=5,width=850,height=340)
        
        lblMember=Label(DataFrameLeft,font=("arial",10,"bold"),text="MemberType",padx=2,pady=6,bg="powder blue")
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",font=("arial",10,"bold"),width=37)
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        
        lblPRN_NO=Label(DataFrameLeft,font=("arial",10,"bold"),text="PRN_NO",padx=2,bg="powder blue")
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.prn_var,width=40)
        txtPRN_NO.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,font=("arial",10,"bold"),text="ID NO",padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.id_var,width=40)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,font=("arial",10,"bold"),text="First Name",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.firstname_var,width=40)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,font=("arial",10,"bold"),text="LastName",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.lastname_var,width=40)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,font=("arial",10,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.address1_var,width=40)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,font=("arial",10,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.address2_var,width=40)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,font=("arial",10,"bold"),text="Post Code",padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.postcode_var,width=40)
        txtPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,font=("arial",10,"bold"),text="Mobile",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.mobile_var,width=40)
        txtMobile.grid(row=8,column=1)
        
        lblBookID=Label(DataFrameLeft,font=("arial",10,"bold"),text="Book ID",padx=2,pady=6,bg="powder blue")
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.bookid_var,width=40)
        txtBookID.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,font=("arial",10,"bold"),text="BookTitle",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.booktitle_var,width=40)
        txtBookTitle.grid(row=1,column=3)
        
        lblAutherName=Label(DataFrameLeft,font=("arial",10,"bold"),text="Auther Name",padx=2,pady=6,bg="powder blue")
        lblAutherName.grid(row=2,column=2,sticky=W)
        txtAutherName=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.auther_var,width=40)
        txtAutherName.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,font=("arial",10,"bold"),text="Date Borrowed",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.dateborrowed_var,width=40)
        txtDateBorrowed.grid(row=3,column=3)
        
        lblDateDue=Label(DataFrameLeft,font=("arial",10,"bold"),text="Date Due",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.datedue_var,width=40)
        txtDateDue.grid(row=4,column=3)
        
        lblDatesOnBook=Label(DataFrameLeft,font=("arial",10,"bold"),text="Days ON Book",padx=2,pady=6,bg="powder blue")
        lblDatesOnBook.grid(row=5,column=2,sticky=W)
        txtDatesOnBook=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.daysonbook_var,width=40)
        txtDatesOnBook.grid(row=5,column=3)
        
        lblLateReturnFine=Label(DataFrameLeft,font=("arial",10,"bold"),text="Late Return Fine",padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.latereturnfine_var,width=40)
        txtLateReturnFine.grid(row=6,column=3)
        
        lblDateOverDue=Label(DataFrameLeft,font=("arial",10,"bold"),text="Date Over Due",padx=2,pady=6,bg="powder blue")
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.datedue_var,width=40)
        txtDateOverDue.grid(row=7,column=3)
        
        lblActualPrice=Label(DataFrameLeft,font=("arial",10,"bold"),text="Actual Price",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",10,"bold"),textvariable=self.finalprice_var,width=40)
        txtActualPrice.grid(row=8,column=3)
        
        
        
        DataFrameRight=LabelFrame(frame,text="BOOK DETAILS", bg="powder blue", fg="black",bd=10,relief=RIDGE,font=("arial",13,"bold"))
        DataFrameRight.place(x=910,y=5,width=560,height=360)
        
        self.txtBox=Text(DataFrameRight, font=("arial",10,"bold"),width=40,height=19,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        listBooks=["To Kill a Mockingbird","The Great Gatsby","Pride and Prejudice","The Catcher in the Rye","Moby-Dick","War and Peace","The Odyssey", "Crime and Punishment","One Hundred Years of Solitude","Guns, Germs, and Steel","A People's History of the United States",
                            "The Silk Roads",
                            "Team of Rivals",
                            "The Diary of a Young Girl","Atomic Habits",
                            "The Power of Habit",
                            "How to Win Friends and Influence People",
                            "Man's Search for Meaning",
                            "The 7 Habits of Highly Effective People",]
        
        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if (x=="To Kill a Mockingbird"):
                self.bookid_var.set("BKID001")
                self.booktitle_var.set("Python")
                self.auther_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.788")
                
            elif (x=="The Great Gatsby"):
                self.bookid_var.set("BKID002")
                self.booktitle_var.set("Python")
                self.auther_var.set("Berry")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1100")
                
            elif (x=="The Great Gatsby"):
                self.bookid_var.set("BKID002")
                self.booktitle_var.set("Python")
                self.auther_var.set("Berry")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1100")
                
            elif (x=="Pride and Prejudice"):
                self.bookid_var.set("BKID003")
                self.booktitle_var.set("Python")
                self.auther_var.set("Jane Austen")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1200")
                
            elif (x=="The Catcher in the Rye"):
                self.bookid_var.set("BKID004")
                self.booktitle_var.set("Python")
                self.auther_var.set("J.D. Salinger.")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1500")
                
            elif (x=="Moby-Dick"):
                self.bookid_var.set("BKID005")
                self.booktitle_var.set("Python")
                self.auther_var.set("Herman Melville")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1600")
                
            elif (x=="War and Peace" ):
                self.bookid_var.set("BKID006")
                self.booktitle_var.set("Python")
                self.auther_var.set("Leo Tolstoy")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1750")
            
            elif (x=="The Odyssey"):
                self.bookid_var.set("BKID007")
                self.booktitle_var.set("Python")
                self.auther_var.set("Homer")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1800")
            
            elif (x=="Crime and Punishment" ):
                self.bookid_var.set("BKID008")
                self.booktitle_var.set("Python")
                self.auther_var.set(" Fyodor Dostoevsky")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1200")
                
            elif (x=="One Hundred Years of Solitude"):
                self.bookid_var.set("BKID009")
                self.booktitle_var.set("Python")
                self.auther_var.set("Gabriel García Márquez")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1350")
                
            elif (x=="Guns, Germs, and Steel"):
                self.bookid_var.set("BKID010")
                self.booktitle_var.set("Python")
                self.auther_var.set("Jared Diamond")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1900")
                
            elif (x=="A People's History of the United States" ):
                self.bookid_var.set("BKID011")
                self.booktitle_var.set("Python")
                self.auther_var.set("Howard Zinn")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.2400")
                
            elif (x=="The Silk Roads"):
                self.bookid_var.set("BKID012")
                self.booktitle_var.set("Python")
                self.auther_var.set("Peter Frankopan")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.3000")
            
            elif (x=="Team of Rivals"):
                self.bookid_var.set("BKID013")
                self.booktitle_var.set("Python")
                self.auther_var.set("Doris Kearns Goodwin")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.2500")
                
            elif (x=="The Diary of a Young Girl" ):
                self.bookid_var.set("BKID014")
                self.booktitle_var.set("Python")
                self.auther_var.set("Anne Frank")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.3500")
                
            elif (x=="Atomic Habits" ):
                self.bookid_var.set("BKID015")
                self.booktitle_var.set("Python")
                self.auther_var.set("James Clear")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.2050")
                
            elif (x=="The Power of Habit"):
                self.bookid_var.set("BKID016")
                self.booktitle_var.set("Python")
                self.auther_var.set("Charles Duhigg")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1500")
                
            elif (x=="How to Win Friends and Influence People"):
                self.bookid_var.set("BKID017")
                self.booktitle_var.set("Python")
                self.auther_var.set("Dale Carnegie")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.2500")
                
            elif (x=="Man's Search for Meaning" ):
                self.bookid_var.set("BKID018")
                self.booktitle_var.set("Python")
                self.auther_var.set("Viktor E. Frankl")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1800")
                
            elif(x=="The 7 Habits of Highly Effective People"):
                self.bookid_var.set("BKID019")
                self.booktitle_var.set("Python")
                self.auther_var.set("Stephen R. Covey")
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1650")
            
                
                
            
        
        
        listbox=Listbox(DataFrameRight,font=("arial",10,"bold"),width=30,height=18)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)
        
        for item in listBooks:
            listbox.insert(END,item)
    
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="white")
        Framebutton.place(x=0,y=510,width=1530,height=50)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnShowData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnShowData.grid(row=0,column=1)
        
        btnUpdate=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnUpdate.grid(row=0,column=2)
        
        btnDelete=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnDelete.grid(row=0,column=3)
        
        btnReset=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnReset.grid(row=0,column=4)
        
        btnExit=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnExit.grid(row=0,column=5)
        
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="white")
        FrameDetails.place(x=0,y=570,width=1530,height=195)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=175)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","prnno","idno","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN NO.")
        self.library_table.heading("idno",text="ID_NO")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Adress1")
        self.library_table.heading("adress2",text="Adress2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("days",text="Dates On Books")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("adress2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
       
    def add_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="librarysystem")
        my_cursor = conn.cursor()
        values = (
        self.member_var.get(),
        self.prn_var.get(),
        self.id_var.get(),
        self.firstname_var.get(),
        self.lastname_var.get(),
        self.address1_var.get(),
        self.address2_var.get(),
        self.postcode_var.get(),
        self.mobile_var.get(),
        self.bookid_var.get(),
        self.booktitle_var.get(),
        self.auther_var.get(),
        self.dateborrowed_var.get(),
        self.datedue_var.get(),
        self.daysonbook_var.get(),
        self.latereturnfine_var.get(),
        self.dateoverdue_var.get(),
        self.finalprice_var.get()
    )
        sql_query = """INSERT INTO library (Member, PRN_NO, ID_NO, FirstName, LastName, Address1, Address2, Postid, Mobile, 
                    Bookid, Booktitle, Auther, Dateborrowed, Datedue, Daysonbook, Latereturnfine, Dateoverdue, Finalprice) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
   
        my_cursor.execute(sql_query, values)
    
        conn.commit()
        self.fatch_data()
        self.reset()
        my_cursor.close()
        conn.close()
        
       
        messagebox.showinfo("Success", "Member has been inserted successfully")
        
    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="librarysystem")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member= %s, PRN_NO = %s, ID_NO = %s, FirstName = %s, LastName = %s, Address1 = %s, Address2 = %s, Postid = %s, Mobile = %s, Bookid = %s, Booktitle = %s, Auther = %s, Dateborrowed = %s, Datedue = %s, Daysonbook = %s, Latereturnfine = %s, Dateoverdue = %s, Finalprice = %s where PRN_NO = %s",(
        self.member_var.get(),
        self.prn_var.get(),
        self.id_var.get(),
        self.firstname_var.get(),
        self.lastname_var.get(),
        self.address1_var.get(),
        self.address2_var.get(),
        self.postcode_var.get(),
        self.mobile_var.get(),
        self.bookid_var.get(),
        self.booktitle_var.get(),
        self.auther_var.get(),
        self.dateborrowed_var.get(),
        self.datedue_var.get(),
        self.daysonbook_var.get(),
        self.latereturnfine_var.get(),
        self.dateoverdue_var.get(),
        self.finalprice_var.get(),
        self.prn_var.get() 
            ))
        
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been updated")


        
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="librarysystem")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
         
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for  i in  rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
        
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN_NO\t\t"+ self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID_NO\t\t"+ self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName\t\t"+ self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName\t\t"+ self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1\t\t"+ self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2\t\t"+ self.address2_var.get()+"\n")
        self.txtBox.insert(END,"PostCode\t\t"+ self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile\t\t"+ self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"BookID\t\t"+ self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"BookTitle\t\t"+ self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author\t\t"+ self.auther_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed\t\t"+ self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue\t\t"+ self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook\t\t"+ self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateReturnFine\t\t"+ self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+ self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice\t\t"+ self.finalprice_var.get()+"\n")
       
        
        
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)
        
    def iExit(self) :
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you wat to exit ?")   
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First select the member") 
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="librarysystem")
            my_cursor = conn.cursor() 
            query="delete from library where PRN_NO=%s"  
            value =(self.prn_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success","Member has been deleted")
        

    
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()

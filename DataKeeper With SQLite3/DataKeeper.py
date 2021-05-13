import random
import smtplib
from captcha.image import ImageCaptcha
import sqlite3
import string
import tkinter.messagebox as tkMessageBox
from tkinter import *
import re
from tkinter import ttk,messagebox
import base64
from PIL import ImageTk,Image
import cv2
import tkinter as tk 
from tkinter import ttk 





root = Tk()
root.title("Our DB Project is Here \U0001F600  !!!")


width = 1250
height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.configure(bg="Black")


# =======================================VARIABLES=====================================
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()
CPASSWORD = StringVar()
CAPTCHA = StringVar()
NEWPASSWORD = StringVar()
CONNEWPASSWORD = StringVar()
OLDPASS = StringVar()
image_captcha = ""
status = FALSE
FKEYTABLE = StringVar() ; FKEYCOLUMN = StringVar()
A1NAME = StringVar() ; A1DTYPE = StringVar() ; A1DLENGTH = StringVar() ; A1NNULL = StringVar() ; A1PK = StringVar() ; A1FK = StringVar()
A2NAME = StringVar() ; A2DTYPE = StringVar() ; A2DLENGTH = StringVar() ; A2NNULL = StringVar() ; A2PK = StringVar() ; A2FK = StringVar()
A3NAME = StringVar() ; A3DTYPE = StringVar() ; A3DLENGTH = StringVar() ; A3NNULL = StringVar() ; A3PK = StringVar() ; A3FK = StringVar()
A4NAME = StringVar() ; A4DTYPE = StringVar() ; A4DLENGTH = StringVar() ; A4NNULL = StringVar() ; A4PK = StringVar() ; A4FK = StringVar()
A5NAME = StringVar() ; A5DTYPE = StringVar() ; A5DLENGTH = StringVar() ; A5NNULL = StringVar() ; A5PK = StringVar() ; A5FK = StringVar()
A6NAME = StringVar() ; A6DTYPE = StringVar() ; A6DLENGTH = StringVar() ; A6NNULL = StringVar() ; A6PK = StringVar() ; A6FK = StringVar()
A7NAME = StringVar() ; A7DTYPE = StringVar() ; A7DLENGTH = StringVar() ; A7NNULL = StringVar() ; A7PK = StringVar() ; A7FK = StringVar()
A8NAME = StringVar() ; A8DTYPE = StringVar() ; A8DLENGTH = StringVar() ; A8NNULL = StringVar() ; A8PK = StringVar() ; A8FK = StringVar()
A9NAME = StringVar() ; A9DTYPE = StringVar() ; A9DLENGTH = StringVar() ; A9NNULL = StringVar() ; A9PK = StringVar() ; A9FK = StringVar()
A10NAME = StringVar() ; A10DTYPE = StringVar() ; A10DLENGTH = StringVar() ; A10NNULL =StringVar() ; A10PK = StringVar() ; A10FK = StringVar()
AUTNAME = StringVar() ;AUTDTYPE = StringVar() ; AUTDLENGTH = StringVar() ; AUTNNULL =StringVar() ; AUTPK = StringVar() ; AUTFK = StringVar()
TABLENAME = StringVar()
EXISTTABLENAME = StringVar()
TABLENAMEUT =StringVar() ; COLUMNNAMEUT = StringVar() ; RENAMEDUT=StringVar()
TABLENAMEDT =StringVar() 

global FKTBNAME , FKCLNAME
# =======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")


def BasicInformation():
    top=Toplevel()
    top.geometry("650x600")
    top.configure(bg ='#120940')
    top.title("Developer Information")
    top1 = Label(top,text="Front end language (for GUI) - Pyhton Tkinter",font=('times new roman',20),bg="black",fg="white")
    top1.grid(row=0)
    top2 = Label(top,text="Backgrong Language - SQLite3 ",font=('times new roman',20),bg="black",fg="white")
    top2.grid(row=1)
    top3 = Label(top,text="Developer's Details are as follows",font=('times new roman',18),fg="blue")
    top3.grid(row=2,)
    top4 = Label(top,text=" Onkar B. Madhekar  rollno.29  AY 2020-21   TE student NKOCET",font=('Algerian', 15),bg="yellow")
    top4.grid(row=3)
    top5 = Label(top,text=" Krishna P. Khandelwal rollno.23  AY 2020-21  TE student NKOCET",font=('Algerian', 15),bg="yellow")
    top5.grid(row=4)
    top6 = Label(top,text=" Shreyas S. Kulkarni  rollno.26  AY 2020-21   TE student NKOCET",font=('Algerian', 15),bg="yellow")
    top6.grid(row=5)
    top7 = Label(top,text=" Ujwal L. Maradkar  rollno.31  AY 2020-21   TE student NKOCET",font=('Algerian', 15),bg="yellow")
    top7.grid(row=6)
    top8 = Label(top,text=" Mahesh G. Mhetre  rollno.32  AY 2020-21   TE student NKOCET",font=('Algerian', 15),bg="yellow")
    top8.grid(row=7)
    top9 = Label(top,text="You need min 2GB of RAM and 1GB of Graphic card  ",font=('Algerian', 15),fg="red",bg="blue")
    top9.grid(row=8)
    top10 = Label(top,text=",a 2 core procesor (intel i3 or ryzen 3500 with any version)",font=('Algerian', 15),fg="red",bg="blue")
    top10.grid(row=9)

def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def show1():
    root.configure(background = "blue")
    print("THANKS FOR USING OUR SERVICE ")

#=======================================Encrypt & Decrypt================================
def encrypt(message1):
    message_bytes = message1.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def decrypt(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message


# =======================================Login Screen=======================================
def LoginForm():
    
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    
    lbl_username = Label(LoginFrame, text="Username* ", font=('times new roman', 22), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password* ", font=('times new roman', 22), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('times new roman', 18),fg="red")
    lbl_result1.grid(row=5, columnspan=2)
    username = Entry(LoginFrame, font=('times new roman', 20), textvariable=USERNAME,bg="lavender", width=20)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('times new roman', 20), textvariable=PASSWORD,bg="lavender", width=20, show="*")
    password.grid(row=2, column=1)
    generate_first_image_log()
    captcha = Entry(LoginFrame, font=('times new roman', 20),bg="lavender", textvariable=CAPTCHA, width=20)
    captcha.grid(row=3, column=1)
    btn_rgcaptcha = Button(LoginFrame, text="🔁",font=("times new roman",18),fg="black",cursor="hand2", width=2,activebackground="springgreen2",height=1,command=regenerate_image_captcha_log)
    btn_rgcaptcha.grid(row=3,column=2)
    btn_login = Button(LoginFrame, text="LOGIN", font=('times new roman', 18),bg="green",fg="white",bd=5,activebackground="green1",cursor="hand2", width=35, command=Login)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="REGISTER", fg="brown4", font=('algerian', 13,"bold underline"),cursor="hand2")
    lbl_register.grid(row=0, sticky=SW)
    lbl_register.bind('<Button-1>', Toggle_FromLogin_ToRegister)
    lbl_forgetpassword = Label(LoginFrame, text="Forgot Password?", fg="Blue4", font=('algerian', 12),cursor="hand2")
    lbl_forgetpassword.grid(row=7,columnspan=2, pady=4)
    lbl_forgetpassword.bind('<Button-1>', Toggle_FromLogin_ToForgetPass)
    USERNAME.set("")
    PASSWORD.set("")
    CAPTCHA.set("")

# =======================================Register Screen=======================================
def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=5)
    lbl1=Label(RegisterFrame, text="")
    lbl1.grid(row=1)
    lbl2=Label(RegisterFrame, text="")
    lbl2.grid(row=2)
    lbl_username = Label(RegisterFrame, text="Username* ", font=('times new roman', 22), bd=18)
    lbl_username.grid(row=3)
    lbl_password = Label(RegisterFrame, text="Password* ", font=('times new roman', 22), bd=18)
    lbl_password.grid(row=4)
    lbl_password = Label(RegisterFrame, text="Confirm Password* ", font=('times new roman', 22), bd=25)
    lbl_password.grid(row=5)
    lbl_firstname = Label(RegisterFrame, text="Firstname* ", font=('times new roman', 22), bd=18)
    lbl_firstname.grid(row=6)
    lbl_lastname = Label(RegisterFrame, text="Lastname* ", font=('times new roman', 22), bd=18)
    lbl_lastname.grid(row=7)
    lbl_result2 = Label(RegisterFrame, text="", font=('times new roman', 18))
    lbl_result2.grid(row=9, columnspan=2)
    username = Entry(RegisterFrame,text="Email-ID*", font=('times new roman', 20),bg="lavender", textvariable=USERNAME, width=20)
    username.grid(row=3, column=1)
    password = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=PASSWORD, width=20, show="*")
    password.grid(row=4, column=1)
    password = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=CPASSWORD, width=20, show="*")
    password.grid(row=5, column=1)
    firstname = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=FIRSTNAME, width=20)
    firstname.grid(row=6, column=1)
    lastname = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=LASTNAME, width=20)
    lastname.grid(row=7, column=1)
    generate_first_image()
    captcha = Entry(RegisterFrame, font=('times new roman', 20),bg="lavender", textvariable=CAPTCHA, width=20)
    captcha.grid(row=8, column=1)
    btn_rgcaptcha = Button(RegisterFrame, text="🔁",font=("times new roman",18),fg="black",cursor="hand2", width=2,activebackground="springgreen2",command=regenerate_image_captcha)
    btn_rgcaptcha.grid(row=8,column=3)
    RegisterFrame.var=IntVar()
    check= Checkbutton(RegisterFrame,text="Agree to the Terms & Condition's",variable=RegisterFrame.var,onvalue=1,offvalue=0,font=("aerial",10)).place(x=90,y=550)
    btn_login = Button(RegisterFrame, text="REGISTER", font=('times new roman', 18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=35, command=Register)
    btn_login.grid(row=10, columnspan=2, pady=85)
    lbl_login = Label(RegisterFrame, text="LOGIN PAGE",cursor="hand2", fg="Brown4", font=('algerian ', 12,"bold underline"))
    lbl_login.grid(row=2, sticky=W)
    lbl_login.bind('<Button-1>', Toggle_FromRegister_ToLogin)
    USERNAME.set("")
    PASSWORD.set("")
    FIRSTNAME.set("")
    LASTNAME.set("")
    CAPTCHA.set("")

# =======================================Forget Password Screen=======================================
def ForgetPasswordForm():
    global ForgetPasswordFrame, lbl_result3
    ForgetPasswordFrame = Frame(root)
    ForgetPasswordFrame.pack(side=TOP, pady=80)
    lbl_username = Label(ForgetPasswordFrame, text="Username* ", font=('times new roman', 23), bd=18)
    lbl_username.grid(row=2)
    lbl_result3 = Label(ForgetPasswordFrame, text="", font=('times new roman', 18))
    lbl_result3.grid(row=4, columnspan=2)
    username = Entry(ForgetPasswordFrame, font=('times new roman', 20),bg="lavender", textvariable=USERNAME, width=23)
    username.grid(row=2, column=1)
    btn_ForgetPassword = Button(ForgetPasswordFrame, text="SEND E-MAIL",font=("times new roman",18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=35,
                                command=ForgetPassword)
    btn_ForgetPassword.grid(row=5, columnspan=2, pady=20)
    lbl_login1 = Label(ForgetPasswordFrame, text="LOGIN", fg="brown4",cursor="hand2", font=('algerian', 12,"bold underline"))
    lbl_login1.grid(row=0, sticky=W)
    lbl_login1.bind('<Button-1>', Toggle_FromForgetPass_ToLogin)
    USERNAME.set("")

# =======================================Navigation Screen=======================================
def NavigationForm():
    global NavigationFrame, lbl_result4 , lbl_menu
    NavigationFrame = Frame(root)
    NavigationFrame.pack(side=TOP, pady=80)
    '''lbl_menu = Label(NavigationFrame, text="MENU", fg="brown4",cursor="hand2", font=('algerian', 30,"bold underline"))
    lbl_menu.grid(row=1, columnspan=2)
    #lbl_logout = Label(NavigationFrame, text="Logout", fg="brown4",cursor="hand2", font=('algerian', 20,"bold underline"))
    #lbl_logout.grid(row=0, sticky=SW)
    #lbl_logout.bind('<Button-1>', Toggle_FromNavigation_ToLogin)
    #btn_ChangePass = Button(NavigationFrame, text="Change Password",font=("times new roman",20),bg="green",fg="white",bd=5,activebackground="blue",cursor="hand2", width=35,
    #                            command=Toggle_FromNavigation_ToChangePass)
    #btn_ChangePass.grid(row=2, columnspan=2, pady=20)
    btn_CreateTab = Button(NavigationFrame, text="Crate new Table",font=("times new roman",20),bg="green",fg="white",bd=5,activebackground="blue",cursor="hand2", width=35,
                                command=Toggle_FromNavigation_ToCreateTab)
    btn_CreateTab.grid(row=3, columnspan=2, pady=20)
    btn_ViewTab = Button(NavigationFrame, text="View all Tables",font=("times new roman",20),bg="green",fg="white",bd=5,activebackground="blue",cursor="hand2", width=35,
                                command=Toggle_FromNavigation_ToViewTab)
    btn_ViewTab.grid(row=4, columnspan=2, pady=20)
    btn_DeleteTab = Button(NavigationFrame, text="Delete the Tables",font=("times new roman",20),bg="green",fg="white",bd=5,activebackground="blue",cursor="hand2", width=35,
                                command=Toggle_FromNavigation_ToDeleteTab)
    btn_DeleteTab.grid(row=5, columnspan=2, pady=20)
    btn_EditTab = Button(NavigationFrame, text="Update the Tables",font=("times new roman",20),bg="green",fg="white",bd=5,activebackground="blue",cursor="hand2", width=35,
                                command=Toggle_FromNavigation_ToEditTab)
    btn_EditTab.grid(row=6, columnspan=2, pady=20)'''
    lbl_result4 = Label(NavigationFrame, text="Welcome to Database", font=('algerian', 30))
    lbl_result4.grid(row=11, columnspan=2)


# =======================================Change Password Screen=======================================
def ChangePassForm():
    global ChangePassFrame, lbl_result5
    ChangePassFrame = Frame(root)
    ChangePassFrame.pack(side=TOP, pady=80)
    lbl_username = Label(ChangePassFrame, text="Username* ", font=('times new roman', 23), bd=18)
    lbl_username.grid(row=2)
    lbl_OldPass = Label(ChangePassFrame, text="Old Password* ", font=('times new roman', 23), bd=18)
    lbl_OldPass.grid(row=3)
    lbl_NewPass = Label(ChangePassFrame, text="New Password* ", font=('times new roman', 23), bd=18)
    lbl_NewPass.grid(row=4)
    lbl_ConNewPass = Label(ChangePassFrame, text="Confirm New Password* ", font=('times new roman', 23), bd=18)
    lbl_ConNewPass.grid(row=5)
    lbl_result5 = Label(ChangePassFrame, text="", font=('times new roman', 18))
    lbl_result5.grid(row=7, columnspan=2)
    Username = Entry(ChangePassFrame, font=('times new roman', 20),bg="lavender", textvariable=USERNAME, width=23)
    Username.grid(row=2, column=1)
    OldPass = Entry(ChangePassFrame, font=('times new roman', 20),bg="lavender", textvariable=OLDPASS, width=23)
    OldPass.grid(row=3, column=1)
    NewPass = Entry(ChangePassFrame, font=('times new roman', 20),bg="lavender", textvariable=NEWPASSWORD, width=23)
    NewPass.grid(row=4, column=1)
    ConNewPass = Entry(ChangePassFrame, font=('times new roman', 20),bg="lavender", textvariable=CONNEWPASSWORD, width=23)
    ConNewPass.grid(row=5, column=1)
    btn_ChangePass = Button(ChangePassFrame, text="CHANGE PASSWORD",font=("times new roman",18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=35,
                                command=ChangePassword)
    btn_ChangePass.grid(row=6, columnspan=2, pady=20)
    lbl_Back = Label(ChangePassFrame, text="BACK", fg="brown4",cursor="hand2", font=('algerian', 12,"bold underline"))
    lbl_Back.grid(row=0, sticky=W)
    lbl_Back.bind('<Button-1>', Toggle_FromChangePass_ToNaviagtion)
    USERNAME.set("")


#=================================================FKey screen=======================================
'''def FkeyTable():
    global Fkeytablescreen , lbl_result_FK , btn_next , ExistTab
    Fkeytablescreen = Toplevel(root)
    Fkeytablescreen.title("FOREIGN KEY")
    Fkeytablescreen.geometry("600x200")
    Fkeyframe = Frame(Fkeytablescreen)
    Fkeyframe.pack(side = TOP)
    Label(Fkeyframe, text="Enter FOREIGN KEY Details  for Table ").grid(row = 0)
    Label(Fkeyframe, text="Tables:").grid(row = 3 ,column = 0)
    ExistTab = ttk.Combobox(Fkeyframe, textvariable = FKEYTABLE) 
    ExistTab['values'] = DropDownList()

    ExistTab.grid(column = 1, row = 3) 
    ExistTab.current() 
    lbl_result_FK=Label(Fkeyframe, text="").grid(row = 5 , column = 2)
    btn_next = Button(Fkeyframe, text="NEXT", command=Fkeycolumn).grid(row =7, column = 1)
    setFKTBNAME()


def Fkeycolumn():
    global Fkeycolumnscreen , lbl_result_FK , ExistTabcol
    Fkeycolumnscreen = Toplevel(root)
    Fkeycolumnscreen.title("FOREIGN KEY")
    Fkeycolumnscreen.geometry("600x200")
    Fkeyframe = Frame(Fkeycolumnscreen)
    Fkeyframe.pack(side = TOP)
    Label(Fkeyframe, text="Enter FOREIGN KEY Details  for column ").grid(row = 0)
    Label(Fkeyframe, text="Column:     ").grid(row = 3 , column = 2)
    ExistTabcol = ttk.Combobox(Fkeyframe, textvariable = FKEYCOLUMN) 
    ExistTabcol['values'] = GetColumnNames()

    ExistTabcol.grid(column = 3, row = 3) 
    ExistTabcol.current() 
    lbl_result_FK=Label(Fkeyframe, text="").grid(row = 5 , column = 2)
    #Button(Fkeyframe, text="SUBMIT", command=delete_Fkeytablescreen).grid(row =7, column = 1)

def  setFKTBNAME():
    FKTBNAME = FKEYTABLE.get()
    print(FKTBNAME)

def setFKCLNAME():
    FKCLNAME = FKEYCOLUMN.get()
    print(FKCLNAME)

def delete_screen(event=None):
    Fkeytablescreen.destroy()
    Fkeycolumnscreen.destroy()

def GetColumnNames():
    Database()
    tab_name = FKEYTABLE.get()
    getColumnNames_msg = f"SELECT * FROM {tab_name}"
    print(getColumnNames_msg)
    cursor = conn.execute(getColumnNames_msg)
    names = [description[0] for description in cursor.description]
    return tuple(names)
'''


#=================================================================Update Table Form ==============================================================================================
global  lbl_resUT
def UpdateTableForm():
    global UpdateTabFrame , UpdateTabFrame2, lbl_resUT , TbName ,Clname
    UpdateTabFrame = Frame(root)
    UpdateTabFrame.pack(fill = "both" , expand = True , anchor = 'c', pady =40 , padx = 40)
    UpdateTabFrame0 = Frame(UpdateTabFrame)
    UpdateTabFrame0.pack(side=TOP, pady=20 , anchor = 'c')
    lbl_header = Label(UpdateTabFrame0 , text = "          Update Table          ", font=('helvetica 16 bold italic', 26), bd=22 ,bg= "light blue")
    lbl_header.grid(row = 0,columnspan =2)
    Label(UpdateTabFrame0, text="     ").grid(row = 1)
    Tb_Show(UpdateTabFrame0)
    lbl_Back = Label(UpdateTabFrame0, text="BACK", fg="brown4",cursor="hand2", font=('algerian', 12,"bold underline"))
    lbl_Back.grid(row=0, sticky=W)
    lbl_Back.bind('<Button-1>', Toggle_FromUpdateTab_ToNaviagation)

def GetColumnNamesUT():
    Database()
    tab_name = TABLENAMEUT.get()
    getColumnNames_msg = f"SELECT * FROM {tab_name}"
    cursor = conn.execute(getColumnNames_msg)
    names = [description[0] for description in cursor.description]
    return tuple(names)    

def Tb_Show(UpdateTabFrame0):
    Label(UpdateTabFrame0, text="SELECT TABLE NAME:").grid(row = 2,column=0)
    global btn_TB 
    btn_TB = Button(UpdateTabFrame0, text="NEXT",font=("times new roman",18),bd=2,activebackground="seagreen1",cursor="hand2", width=10,command= lambda:Cl_Show(UpdateTabFrame0) )
    btn_TB.grid(row=2 ,column =2, pady=20)
    TbName = ttk.Combobox(UpdateTabFrame0, textvariable = TABLENAMEUT ) 
    TbName['values'] = DropDownList()
    TbName.grid( row = 2, column = 1) 
    TbName.current() 


def Cl_Show(UpdateTabFrame0):
    btn_TB.destroy()
    global btn_CL
    Label(UpdateTabFrame0, text=" ").grid(row = 3,column=0)
    btn_CL = Button(UpdateTabFrame0, text="NEXT",font=("times new roman",18),bd=2,activebackground="seagreen1",cursor="hand2", width=10,command= lambda:Attr_Show(UpdateTabFrame0) )
    btn_CL.grid(row=4,column =2, pady=20)
    Label(UpdateTabFrame0, text="SELECT COLUMN NAME:").grid(row = 4,column =0)
    ClName = ttk.Combobox(UpdateTabFrame0, textvariable = COLUMNNAMEUT ) 
    ClName['values'] =  GetColumnNamesUT()
    ClName.grid(row = 4,column =1) 
    ClName.current()   
    

def Attr_Show(UpdateTabFrame0):
    btn_CL.destroy()
    dorpdown_menu_Up =("INT","INTEGER","TINYINT","SMALLINT","MEDIUMINT","BIGINT","UNSIGNED BIG INT","INT2","INT8","CHARACTER","VARCHAR","VARYING CHARACTER","NCHAR","NATIVE CHARACTER","NVARCHAR","TEXT","CLOB","BLOB","REAL","DOUBLE","DOUBLE PRECISION","FLOAT","NUMERIC","BOOLEAN","DATE","DATETIME")  
    UpdateTabFrame1 = Frame(UpdateTabFrame)
    UpdateTabFrame1.pack(side='top', pady=20 , anchor = 'c')
    lbl_DataType = Label(UpdateTabFrame1, text="  Datatype  ", font=('times new roman', 22), bd=10 , bg = "grey")
    lbl_DataType.grid(row=1, column=0)
    Label(UpdateTabFrame0, text=" ").grid(row = 1,column=1)
    lbl_DataLength = Label(UpdateTabFrame1, text="Datalength  ", font=('times new roman', 22), bd=10 , bg = "grey")
    lbl_DataLength.grid(row=1 , column=2)
    Label(UpdateTabFrame0, text=" ").grid(row = 1,column=3)
    lbl_NotNull = Label(UpdateTabFrame1, text="  NOTNULL ", font=('times new roman', 22), bd=10 , bg = "grey")
    lbl_NotNull.grid(row=1 , column=4)
    Label(UpdateTabFrame0, text=" ").grid(row = 1,column=5)
    lbl_PKey = Label(UpdateTabFrame1, text="  PK  ", font=('times new roman', 22), bd=10, bg = "grey")
    lbl_PKey.grid(row=1, column=6)
    Label(UpdateTabFrame1, text=" ").grid(row = 1,column=7)
    lbl_FKey = Label(UpdateTabFrame1, text="  FK ", font=('times new roman', 22), bd=10 , bg = "grey")
    lbl_FKey.grid(row=1 , column=8)
    Label(UpdateTabFrame1, text=" ").grid(row = 2,column=1)
    i = 3
    j = i+1
    Ent_DataType1 = ttk.Combobox(UpdateTabFrame1, textvariable = AUTDTYPE) 
    Ent_DataType1['values'] = dorpdown_menu_Up
    Ent_DataType1.grid(column = 0, row = i) 
    Ent_DataType1.current()
    Label(UpdateTabFrame0, text=" ").grid(row = 1,column=1)
    Ent_DataLen1 = Entry(UpdateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= AUTDLENGTH , width=10)
    Ent_DataLen1.grid(row= i, column=2)
    Label(UpdateTabFrame1, text=" ").grid(row = 1,column=3)
    RD_NotNull_Y1 = tk.Radiobutton(UpdateTabFrame1, text="YES", variable=AUTNNULL, value='y', indicatoron=0)
    RD_NotNull_Y1.grid(row= i, column=4 )
    RD_NotNull_N1 = tk.Radiobutton(UpdateTabFrame1, text="NO", variable=AUTNNULL, value='n', indicatoron=0)
    RD_NotNull_N1.grid(row= j, column=4 , rowspan = 5)
    Label(UpdateTabFrame1, text=" ").grid(row = 1,column=5)
    RD_PKey_Y1 = tk.Radiobutton(UpdateTabFrame1, text="YES", variable=AUTPK, value='y', indicatoron=0)
    RD_PKey_Y1.grid(row= i, column=6)
    RD_PKey_N1 = tk.Radiobutton(UpdateTabFrame1, text="NO", variable=AUTPK, value='n', indicatoron=0)
    RD_PKey_N1.grid(row= j, column=6 , rowspan = 5 )
    Label(UpdateTabFrame1, text=" ").grid(row = i,column=7)
    RD_FKey_Y1 = tk.Radiobutton(UpdateTabFrame1, text="YES", variable=AUTFK, value='y', indicatoron=0)
    RD_FKey_Y1.grid(row= i, column= 8)
    RD_FKey_N1 = tk.Radiobutton(UpdateTabFrame1, text="NO", variable=AUTFK, value='n', indicatoron=0)
    RD_FKey_N1.grid(row= j, column=8 , rowspan = 5 )

    UpdateTabFrame2 = Frame(UpdateTabFrame)
    UpdateTabFrame2.pack(side='top', pady=20 , anchor = 'c')
    lbl_resUT = Label(UpdateTabFrame2, text="", font=('times new roman', 18),fg="red")
    lbl_resUT.grid(row=1, column = 2 )
    btn_SUBMIT = Button(UpdateTabFrame2, text="SUBMIT",font=("times new roman",18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=20,
                                command= lambda:ModifyTable(lbl_resUT) )

    btn_SUBMIT.grid(row=2,column =3, pady=20)
    Label(UpdateTabFrame2, text=" ").grid(row = 1,column=2)
    btn_CANCEL = Button(UpdateTabFrame2, text="CANCEL",font=("times new roman",18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=20,
                                command= Toggle_FromUpdateTab_ToNaviagation )

    btn_CANCEL.grid(row=2,column =1, pady=20)

def ModifyTable(lbl_resUT):
    Database()
    RENAMEDUT = "TEMP_TABLES"
    Rename = f"ALTER TABLE {TABLENAMEUT.get()} RENAME TO TEMP_TABLES"
    cursor.execute(Rename)
    Temp_Tab = f"SELECT * FROM {RENAMEDUT} EXCEPT {COLUMNNAMEUT.get()}"
    #cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (username,))
    msg = AtrUT()
    final_msg = f"CREATE TABLE {TABLENAMEUT.get()} {Temp_Tab}{msg}"
    #cursor.execute(final_msg)
    conn.commit()
    lbl_resUT.config(text="Successfully Updated the table." , fg = 'red')
    conn.close()
    #Delete_Temp_Tab()
    #lbl_resUT.config(text="Successfully Updated the table." , fg = 'red')
    TABLENAMEUT.set("");COLUMNNAMEUT.set("") ; AUTNNULL.set(""); AUTPK.set(""); AUTFK.set(""); 
    
def Delete_Temp_Tab():
    msg2 = f"DROP TABLE {RENAMEDUT}"
    Database()
    cursor.execute(msg2)
    conn.commit()
    conn.close()

def AtrUT():
    if AUTNNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if AUTPK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if AUTFK.get() == "y":
        FkeyTable()
        chk_fk = f"FOREIGN KEY ({A1NAME.get()}) REFERENCES {FKEYTABLE.get()}({FKEYCOLUMN.get()})" 
        #delete_screen()
 
    else:
        chk_fk = ""

    msg1 = f"{COLUMNNAMEUT.get()} {AUTDTYPE.get()}({ AUTDLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    return msg1
    


    

#=================================================================Delete Table Form ==============================================================================================


def DeleteTableForm():
    global DeleteTabFrame, DeleteTabFrame0 ,  lbl_result_DT , TbName , btn_TBD , btn_TBS
    DeleteTabFrame = Frame(root)
    DeleteTabFrame.pack(fill = "both" , expand = True , anchor = 'c', pady =40 , padx = 40)
    DeleteTabFrame0 = Frame(DeleteTabFrame)
    DeleteTabFrame0.pack(side=TOP, pady=20 , anchor = 'c')
    lbl_header = Label(DeleteTabFrame0 , text = "          Delete Table          ", font=('helvetica 16 bold italic', 26), bd=22 ,bg= "light blue")
    lbl_header.grid(row = 0,columnspan =2)
    Label(DeleteTabFrame0, text="     ").grid(row = 1)
    lbl_Back = Label(DeleteTabFrame0, text="BACK", fg="brown4",cursor="hand2", font=('algerian', 12,"bold underline"))
    lbl_Back.grid(row=0, sticky=W)
    lbl_Back.bind('<Button-1>', Toggle_FromDeleteTab_ToNaviagation)
    '''btn_TBD = Button(DeleteTabFrame0, text="SELECT TABLE",font=("times new roman",18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=35,
                                command= lambda : Tb_ShowD(DeleteTabFrame0) )
    btn_TBD.grid(row=1, column =0, pady=20)'''
    Label(DeleteTabFrame0, text="SELECT TABLE NAME:").grid(row = 2,column=0)
    global btn_TBD 
    lbl_result_DT = Label(DeleteTabFrame0, text="", font=('times new roman', 18),fg="red")
    lbl_result_DT.grid(row=3, column = 2 )
    TbName = ttk.Combobox(DeleteTabFrame0, textvariable = TABLENAMEDT ) 
    TbName['values'] = DropDownList()
    TbName.grid( row = 2, column = 1) 
    TbName.current() 
    btn_TBS = Button(DeleteTabFrame0, text="SHOW",font=("times new roman",18),bg="green",fg="white",bd=2,activebackground="seagreen1",cursor="hand2", width=10,command= ViewDataTAB)
    btn_TBS.grid(row=4 ,column =1, pady=20)


def ViewDataTAB():
    btn_TBS.destroy()
    btn_TBD = Button(DeleteTabFrame0, text="Delete",font=("times new roman",18),bg="green",fg="white",bd=2,activebackground="seagreen1",cursor="hand2", width=10,command= DropTable)
    btn_TBD.grid(row=4 ,column =1, pady=20)
    Database()
    cursor.execute(SELECT * FROM )
    rows = cursor.fetchall()
    for i,row in rows:
        j = i + 4
        Label(DeleteTabFrame0, text=row).grid(row = j,column=0)
        print(row)


 
def DropTable():
    Database()
    msg = f"DROP TABLE {TABLENAMEDT.get()}"
    cursor.execute(msg)
    conn.commit()
    conn.close()
    lbl_result_DT.config(text="Successfully Deleted the table.", fg="red")
    TABLENAMEDT.set("")
    


#========================================Create Table Form GUI ====================================    
def CreateTabForm():

    global CreateTabFrame , lbl_result_CT ,ExistTab
    dorpdown_menu =("INT","INTEGER","TINYINT","SMALLINT","MEDIUMINT","BIGINT","UNSIGNED BIG INT","INT2","INT8","CHARACTER","VARCHAR","VARYING CHARACTER","NCHAR","NATIVE CHARACTER","NVARCHAR","TEXT","CLOB","BLOB","REAL","DOUBLE","DOUBLE PRECISION","FLOAT","NUMERIC","BOOLEAN","DATE","DATETIME")  
    CreateTabFrame = Frame(root)
    #CreateTabFrame.pack(side=TOP, pady=80)
    CreateTabFrame.pack(fill = "both" , expand = True , anchor = 'c', pady =40 , padx = 40)
    CreateTabFrame0 = Frame(CreateTabFrame)
    CreateTabFrame0.pack(side=TOP, pady=5)
    lbl_header = Label(CreateTabFrame0 , text = "New Table Creation", font=('helvetica 16 bold italic', 26), bd=22 ,bg= "light blue")
    lbl_header.grid(row = 0 ,column =1 , columnspan = 2)
    lbl_NewTabName = Label(CreateTabFrame0, text="New Table Name* : ", font=('times new roman', 22), bd=18)
    lbl_NewTabName.grid(row=1 , column=0)

    ExistTab = ttk.Combobox(CreateTabFrame0, textvariable = EXISTTABLENAME) 
    ExistTab['values'] = DropDownList()

    ExistTab.grid(column = 3, row = 1) 
    ExistTab.current() 
    lbl_AttriName = Label(CreateTabFrame0, text="  Attribute Name  ", font=('times new roman', 22), bd=18 , bg= "grey")
    lbl_AttriName.grid(row=2 , column=0)
    lbl_DataType = Label(CreateTabFrame0, text="  Datatype  ", font=('times new roman', 22), bd=18 , bg = "grey")
    lbl_DataType.grid(row=2, column=1)
    lbl_DataLength = Label(CreateTabFrame0, text="Datalength  ", font=('times new roman', 22), bd=18 , bg = "grey")
    lbl_DataLength.grid(row=2 , column=2)
    lbl_NotNull = Label(CreateTabFrame0, text="  NOTNULL ", font=('times new roman', 22), bd=18 , bg = "grey")
    lbl_NotNull.grid(row=2 , column=3)
    lbl_PKey = Label(CreateTabFrame0, text="  PK  ", font=('times new roman', 22), bd=18, bg = "grey")
    lbl_PKey.grid(row=2 , column=4)
    lbl_FKey = Label(CreateTabFrame0, text="  FK ", font=('times new roman', 22), bd=18 , bg = "grey")
    lbl_FKey.grid(row=2 , column=5)

    NewTabName = Entry(CreateTabFrame0,text="Name", font=('times new roman', 20),bg="lavender", textvariable= TABLENAME , width=20)
    NewTabName.grid(row=1, column=1)
    canvas = Canvas(CreateTabFrame)
    #canvas.pack(side = TOP , fill = "both" , anchor = 'c' , expand = True, pady = 70)
    CreateTabFrame1 = Frame(canvas)
    CreateTabFrame1.grid(row = 0 , column = 0, columnspan = 2 , rowspan = 2 ,padx = 5 , pady= 5 , sticky = 'w')
    scroll_y = tk.Scrollbar(CreateTabFrame, orient="vertical", command=canvas.yview)
    NOTNULL = StringVar()
    NOTNULL.set(" ")
    CreateTabFrame2 = Frame(CreateTabFrame)
    CreateTabFrame2.pack(side = 'bottom' , pady= 20 ,anchor = "c" )
    lbl_Back = Label(CreateTabFrame2, text="Cancel",cursor="hand2", font=('algerian', 22,"bold underline"), bg = "grey")
    lbl_Back.grid(row = 1 , column = 1)
    lbl_Back.bind('<Button-1>', Toggle_FromCreateTab_ToNaviagtion)
    lbl_result_CT = Label(CreateTabFrame2, text="", font=('times new roman', 18))
    lbl_result_CT.grid(row=0, column=3)
    lbl_result = Label(CreateTabFrame2, text="                                            ", font=('times new roman', 18))
    lbl_result.grid(row=1, column=3)
    lbl_Next = Label(CreateTabFrame2, text="Create Table",cursor="hand2", font=('algerian', 22,"bold underline"), bg = "grey")
    lbl_Next.grid(row = 1 , column = 5)
    lbl_Next.bind('<Button-1>', CreateTable)

    #1
    i = 0    
    Ent_Attri1 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A1NAME , width=20)
    Ent_Attri1.grid(row = i , column=0)
    lbl_1_1 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_1.grid(row= i , column=1)
    Ent_DataType1 = ttk.Combobox(CreateTabFrame1, textvariable = A1DTYPE) 
    Ent_DataType1['values'] = dorpdown_menu
    Ent_DataType1.grid(column = 2, row = i) 
    Ent_DataType1.current()
    lbl_2_1 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_1.grid(row= i , column=3)
    Ent_DataLen1 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A1DLENGTH , width=10)
    Ent_DataLen1.grid(row= i, column=4)
    lbl_3_1 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_1.grid(row= i , column=5)    
    RD_NotNull_Y1 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A1NNULL, value='y', indicatoron=0)
    RD_NotNull_Y1.grid(row= i, column=6 )
    RD_NotNull_N1 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A1NNULL, value='n', indicatoron=0)
    RD_NotNull_N1.grid(row= i, column=7)
    lbl_4_1 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_1.grid(row= i , column=8)    
    RD_PKey_Y1 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A1PK, value='y', indicatoron=0)
    RD_PKey_Y1.grid(row= i, column=9)
    RD_PKey_N1 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A1PK, value='n', indicatoron=0)
    RD_PKey_N1.grid(row= i, column=10 )
    lbl_5_1 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_1.grid(row= i , column=11)    
    RD_FKey_Y1 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A1FK, value='y', indicatoron=0)
    RD_FKey_Y1.grid(row= i, column= 12)
    RD_FKey_N1 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A1FK, value='n', indicatoron=0)
    RD_FKey_N1.grid(row= i, column=13 )
    
    #2
    i = 1
    Ent_Attri2 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A2NAME , width=20)
    Ent_Attri2.grid(row = i , column=0)
    lbl_1_2 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_2.grid(row= i , column=1)
    Ent_DataType2 = ttk.Combobox(CreateTabFrame1, textvariable = A2DTYPE) 
    Ent_DataType2['values'] = dorpdown_menu
    Ent_DataType2.grid(column = 2, row = i)
    Ent_DataType2.current()
    lbl_2_2 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_2.grid(row= i , column=3)
    Ent_DataLen2 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A2DLENGTH , width=10)
    Ent_DataLen2.grid(row= i, column=4) 
    lbl_3_2 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_2.grid(row= i , column=5)    
    RD_NotNull_Y2 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A2NNULL, value='y', indicatoron=0)
    RD_NotNull_Y2.grid(row= i, column=6 )
    RD_NotNull_N2 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A2NNULL, value='n', indicatoron=0)
    RD_NotNull_N2.grid(row= i, column=7 )
    lbl_4_2 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_2.grid(row= i , column=8)    
    RD_PKey_Y2 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A2PK, value='y', indicatoron=0)
    RD_PKey_Y2.grid(row= i, column=9)
    RD_PKey_N2 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A2PK, value='n', indicatoron=0)
    RD_PKey_N2.grid(row= i, column=10 )
    lbl_5_2 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_2.grid(row= i , column=11)    
    RD_FKey_Y2 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A2FK, value='y', indicatoron=0)
    RD_FKey_Y2.grid(row= i, column= 12)
    RD_FKey_N2 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A2FK, value='n', indicatoron=0)
    RD_FKey_N2.grid(row= i, column=13 )
    

    #3  
    i = 2    
    Ent_Attri3 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A3NAME , width=20)
    Ent_Attri3.grid(row = i , column=0)
    lbl_1_3 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_3.grid(row= i , column=1)
    Ent_DataType3 = ttk.Combobox(CreateTabFrame1, textvariable = A3DTYPE) 
    Ent_DataType3['values'] = dorpdown_menu
    Ent_DataType3.grid(column = 2, row = i) 
    Ent_DataType3.current()
    lbl_2_3 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_3.grid(row= i , column=3)    
    Ent_DataLen3 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A3DLENGTH , width=10)
    Ent_DataLen3.grid(row= i, column=4)
    lbl_3_3 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_3.grid(row= i , column=5)    
    RD_NotNull_Y3 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A3NNULL, value='y', indicatoron=0)
    RD_NotNull_Y3.grid(row= i, column=6 )
    RD_NotNull_N3 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A3NNULL, value='n', indicatoron=0)
    RD_NotNull_N3.grid(row= i, column=7 )
    lbl_4_3 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_3.grid(row= i , column=8)    
    RD_PKey_Y3 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A3PK, value='y', indicatoron=0)
    RD_PKey_Y3.grid(row= i, column=9)
    RD_PKey_N3 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A3PK, value='n', indicatoron=0)
    RD_PKey_N3.grid(row= i, column=10 )
    lbl_5_3 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_3.grid(row= i , column=11)    
    RD_FKey_Y3 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A3FK, value='y', indicatoron=0)
    RD_FKey_Y3.grid(row= i, column= 12)
    RD_FKey_N3 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A3FK, value='n', indicatoron=0)
    RD_FKey_N3.grid(row= i, column=13 )
    
    #4
    i = 3    
    Ent_Attri4 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A4NAME , width=20)
    Ent_Attri4.grid(row = i , column=0)
    lbl_1_4 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_4.grid(row= i , column=1)
    Ent_DataType4 = ttk.Combobox(CreateTabFrame1, textvariable = A4DTYPE) 
    Ent_DataType4['values'] = dorpdown_menu
    Ent_DataType4.grid(column = 2, row = i) 
    Ent_DataType4.current()
    lbl_2_4 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_4.grid(row= i , column=3)
    Ent_DataLen4 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A4DLENGTH , width=10)
    Ent_DataLen4.grid(row= i, column=4)
    lbl_3_4 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_4.grid(row= i , column=5)    
    RD_NotNull_Y4 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A4NNULL, value='y', indicatoron=0)
    RD_NotNull_Y4.grid(row= i, column=6 )
    RD_NotNull_N4 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A4NNULL, value='n', indicatoron=0)
    RD_NotNull_N4.grid(row= i, column=7 )
    lbl_4_4 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_4.grid(row= i , column=8)    
    RD_PKey_Y4 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A4PK, value='y', indicatoron=0)
    RD_PKey_Y4.grid(row= i, column=9)
    RD_PKey_N4 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A4PK, value='n', indicatoron=0)
    RD_PKey_N4.grid(row= i, column=10 )
    lbl_5_4 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_4.grid(row= i , column=11)    
    RD_FKey_Y4 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A4FK, value='y', indicatoron=0)
    RD_FKey_Y4.grid(row= i, column= 12)
    RD_FKey_N4 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A4FK, value='n', indicatoron=0)
    RD_FKey_N4.grid(row= i, column=13 )
    
    #5
    i = 4
    Ent_Attri_5 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A5NAME , width=20)
    Ent_Attri_5.grid(row = i , column=0)
    lbl_1_5 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_5.grid(row= i , column=1)
    Ent_DataType5 = ttk.Combobox(CreateTabFrame1, textvariable = A5DTYPE) 
    Ent_DataType5['values'] = dorpdown_menu
    Ent_DataType5.grid(column = 2, row = i) 
    Ent_DataType5.current()
    lbl_2_5 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_5.grid(row= i , column=3)
    Ent_DataLen5 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A5DLENGTH , width=10)
    Ent_DataLen5.grid(row= i, column=4)
    lbl_3_5 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_5.grid(row= i , column=5)    
    RD_NotNull_Y5 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A5NNULL, value='y', indicatoron=0)
    RD_NotNull_Y5.grid(row= i, column=6 )
    RD_NotNull_N5 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A5NNULL, value='n', indicatoron=0)
    RD_NotNull_N5.grid(row= i, column=7 )
    lbl_4_5 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_5.grid(row= i , column=8)    
    RD_PKey_Y5 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A5PK, value='y', indicatoron=0)
    RD_PKey_Y5.grid(row= i, column=9)
    RD_PKey_N5 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A5PK, value='n', indicatoron=0)
    RD_PKey_N5.grid(row= i, column=10 )
    lbl_5_5 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_5.grid(row= i , column=11)    
    RD_FKey_Y5 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A5FK, value='y', indicatoron=0)
    RD_FKey_Y5.grid(row= i, column= 12)
    RD_FKey_N5 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A5FK, value='n', indicatoron=0)
    RD_FKey_N5.grid(row= i, column=13 )
    
   
    #6
    i = 5
    Ent_Attri6 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A6NAME, width=20)
    Ent_Attri6.grid(row = i , column=0)
    lbl_1_6 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_6.grid(row= i , column=1)
    Ent_DataType6 = ttk.Combobox(CreateTabFrame1, textvariable = A6DTYPE) 
    Ent_DataType6['values'] = dorpdown_menu
    Ent_DataType6.grid(column = 2, row = i) 
    Ent_DataType6.current()
    lbl_2_6 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_6.grid(row= i , column=3)
    Ent_DataLen6 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A6DLENGTH , width=10)
    Ent_DataLen6.grid(row= i, column=4)
    lbl_3_6 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_6.grid(row= i , column=5)    
    RD_NotNull_Y6 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A6NNULL, value='y', indicatoron=0)
    RD_NotNull_Y6.grid(row= i, column=6 )
    RD_NotNull_N6 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A6NNULL, value='n', indicatoron=0)
    RD_NotNull_N6.grid(row= i, column=7 )
    lbl_4_6 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_6.grid(row= i , column=8)    
    RD_PKey_Y6 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A6PK, value='y', indicatoron=0)
    RD_PKey_Y6.grid(row= i, column=9)
    RD_PKey_N6 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A6PK, value='n', indicatoron=0)
    RD_PKey_N6.grid(row= i, column=10 )
    lbl_5_6 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_6.grid(row= i , column=11)    
    RD_FKey_Y6 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A6FK, value='y', indicatoron=0)
    RD_FKey_Y6.grid(row= i, column= 12)
    RD_FKey_N6 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A6FK, value='n', indicatoron=0)
    RD_FKey_N6.grid(row= i, column=13 )
    
    #7
    i = 6
    Ent_Attri7 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A7NAME , width=20)
    Ent_Attri7.grid(row = i , column=0)
    lbl_1_7 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_7.grid(row= i , column=1)
    Ent_DataType7 = ttk.Combobox(CreateTabFrame1, textvariable = A7DTYPE) 
    Ent_DataType7['values'] = dorpdown_menu
    Ent_DataType7.grid(column = 2, row = i) 
    Ent_DataType7.current() 
    lbl_2_7 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_7.grid(row= i , column=3)
    Ent_DataLen7 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A7DLENGTH , width=10)
    Ent_DataLen7.grid(row= i, column=4) 
    lbl_3_7 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_7.grid(row= i , column=5)    
    RD_NotNull_Y7 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A7NNULL, value='y', indicatoron=0)
    RD_NotNull_Y7.grid(row= i, column=6 )
    RD_NotNull_N7 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A7NNULL, value='n', indicatoron=0)
    RD_NotNull_N7.grid(row= i, column=7 )
    lbl_4_7 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_7.grid(row= i , column=8)    
    RD_PKey_Y7 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A7PK, value='y', indicatoron=0)
    RD_PKey_Y7.grid(row= i, column=9)
    RD_PKey_N7 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A7PK, value='n', indicatoron=0)
    RD_PKey_N7.grid(row= i, column=10 )
    lbl_5_7 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_7.grid(row= i , column=11)    
    RD_FKey_Y7 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A7FK, value='y', indicatoron=0)
    RD_FKey_Y7.grid(row= i, column= 12)
    RD_FKey_N7 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A7FK, value='n', indicatoron=0)
    RD_FKey_N7.grid(row= i, column=13  , columnspan = 2)
    
    #8
    i = 7
    Ent_Attri8 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A8NAME , width=20)
    Ent_Attri8.grid(row = i , column=0)
    lbl_1_8 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_8.grid(row= i , column=1)
    Ent_DataType8 = ttk.Combobox(CreateTabFrame1, textvariable = A8DTYPE) 
    Ent_DataType8['values'] = dorpdown_menu
    Ent_DataType8.grid(column = 2, row = i) 
    Ent_DataType8.current() 
    lbl_2_8 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_8.grid(row= i , column=3)
    Ent_DataLen8 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A8DLENGTH , width=10)
    Ent_DataLen8.grid(row= i, column=4)
    lbl_3_8 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_8.grid(row= i , column=5)    
    RD_NotNull_Y8 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A8NNULL, value='y', indicatoron=0)
    RD_NotNull_Y8.grid(row= i, column=6 )
    RD_NotNull_N8 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A8NNULL, value='n', indicatoron=0)
    RD_NotNull_N8.grid(row= i, column=7 )
    lbl_4_8 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_8.grid(row= i , column=8)    
    RD_PKey_Y8 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A8PK, value='y', indicatoron=0)
    RD_PKey_Y8.grid(row= i, column=9)
    RD_PKey_N8 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A8PK, value='n', indicatoron=0)
    RD_PKey_N8.grid(row= i, column=10 )
    lbl_5_8 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_8.grid(row= i , column=11)    
    RD_FKey_Y8 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A8FK, value='y', indicatoron=0)
    RD_FKey_Y8.grid(row= i, column= 12)
    RD_FKey_N8 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A8FK, value='n', indicatoron=0)
    RD_FKey_N8.grid(row= i, column=13)
    
    # 9
    i = 8
    Ent_Attri9 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A9NAME , width=20).grid(row = i , column=0) 
    lbl_1_9 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_9.grid(row= i , column=1)
    Ent_DataType9 = ttk.Combobox(CreateTabFrame1, textvariable = A9DTYPE) 
    Ent_DataType9['values'] = dorpdown_menu
    Ent_DataType9.grid(column = 2, row = i) 
    Ent_DataType9.current() 
    lbl_2_9 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_9.grid(row= i , column=3)
    Ent_DataLen9 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A9DLENGTH , width=10)
    Ent_DataLen9.grid(row= i, column=4)
    lbl_3_9 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_3_9.grid(row= i , column=5)    
    RD_NotNull_Y9 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A9NNULL, value='y', indicatoron=0)
    RD_NotNull_Y9.grid(row= i, column=6 )
    RD_NotNull_N9 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A9NNULL, value='n', indicatoron=0)
    RD_NotNull_N9.grid(row= i, column=7 )
    lbl_4_9 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_4_9.grid(row= i , column=8)    
    RD_PKey_Y9 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A9PK, value='y', indicatoron=0)
    RD_PKey_Y9.grid(row= i, column=9)
    RD_PKey_N9 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A9PK, value='n', indicatoron=0)
    RD_PKey_N9.grid(row= i, column=10 )
    lbl_5_9 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_9.grid(row= i , column=11)    
    RD_FKey_Y9 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A9FK, value='y', indicatoron=0)
    RD_FKey_Y9.grid(row= i, column= 12)
    RD_FKey_N9 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A9FK, value='n', indicatoron=0)
    RD_FKey_N9.grid(row= i, column=13)
    
    #10
    i = 9
    Ent_Attri10 = Entry(CreateTabFrame1 ,text="", font=('times new roman', 20),bg="lavender", textvariable= A10NAME , width=20)
    Ent_Attri10.grid(row = i , column=0)
    lbl_1_10 = Label(CreateTabFrame1, text="    ", font=('times new roman', 22), bd=18)
    lbl_1_10.grid(row= i , column=1)
    Ent_DataType10 = ttk.Combobox(CreateTabFrame1, textvariable = A10DTYPE) 
    Ent_DataType10['values'] = dorpdown_menu
    Ent_DataType10.grid(column = 2, row = i) 
    Ent_DataType10.current() 
    lbl_2_10 = Label(CreateTabFrame1, text="      ", font=('times new roman', 22), bd=18)
    lbl_2_10.grid(row= i , column=3)
    Ent_DataLen5 = Entry(CreateTabFrame1 , text="", font=('times new roman', 20),bg="lavender", textvariable= A10DLENGTH , width=10)
    Ent_DataLen5.grid(row= i, column=4)
    lbl_3_10 = Label(CreateTabFrame1, text="        ", font=('times new roman', 22), bd=18)
    lbl_3_10.grid(row= i , column=5)    
    RD_NotNull_Y10 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A10NNULL, value='y', indicatoron=0)
    RD_NotNull_Y10.grid(row= i, column=6 )
    RD_NotNull_N10 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A10NNULL, value='n', indicatoron=0)
    RD_NotNull_N10.grid(row= i, column=7 )
    lbl_4_10 = Label(CreateTabFrame1, text="       ", font=('times new roman', 22), bd=18)
    lbl_4_10.grid(row= i , column=8)    
    RD_PKey_Y10 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A10PK, value='y', indicatoron=0)
    RD_PKey_Y10.grid(row= i, column=9)
    RD_PKey_N10 = tk.Radiobutton(CreateTabFrame1, text="NO", variable=A10PK, value='n', indicatoron=0)
    RD_PKey_N10.grid(row= i, column=10 )
    lbl_5_10 = Label(CreateTabFrame1, text=" ", font=('times new roman', 22), bd=18)
    lbl_5_10.grid(row= i , column=11)    
    RD_FKey_Y10 = tk.Radiobutton(CreateTabFrame1, text="YES", variable=A10FK, value='y', indicatoron=0)
    RD_FKey_Y10.grid(row= i, column= 12)
    RD_FKey_N10= tk.Radiobutton(CreateTabFrame1, text="NO", variable=A10FK, value='n', indicatoron=0)
    RD_FKey_N10.grid(row= i, column=13 )
    


    # put the frame in the canvas
    canvas.create_window(0, 0, anchor='n', window=CreateTabFrame1)
    # make sure everything is displayed before configuring the scrollregion
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scroll_y.set)
    canvas.pack(fill='both', expand=True, side= 'left' , anchor= 'n' , pady = 5, padx = 5)
    scroll_y.pack(fill="y" , side = "right" )#, expand = TRUE)


    #=================================================================Delete Table Form ==============================================================================================


def InsertTupleForm():
    global InsertTupFrame, InsertTupFrame0 ,  lbl_result_IU , TbName , btn_TBD , btn_TBS
    InsertTupFrame = Frame(root)
    InsertTupFrame.pack(fill = "both" , expand = True , anchor = 'c', pady =40 , padx = 40)
    InsertTupFrame0 = Frame(InsertTupFrame)
    InsertTupFrame0.pack(side=TOP, pady=20 , anchor = 'c')
    lbl_header = Label(InsertTupFrame0 , text = "          Insert Tuple          ", font=('helvetica 16 bold italic', 26), bd=22 ,bg= "light blue")
    lbl_header.grid(row = 0,columnspan =2)
    Label(InsertTupFrame0, text="     ").grid(row = 1)
    lbl_Back = Label(InsertTupFrame0, text="BACK", fg="brown4",cursor="hand2", font=('algerian', 12,"bold underline"))
    lbl_Back.grid(row=0, sticky=W)
    lbl_Back.bind('<Button-1>', Toggle_FromInsertTup_ToNaviagation)
    '''btn_TBD = Button(DeleteTabFrame0, text="SELECT TABLE",font=("times new roman",18),bg="green",fg="white",bd=5,activebackground="seagreen1",cursor="hand2", width=35,
                                command= lambda : Tb_ShowD(DeleteTabFrame0) )
    btn_TBD.grid(row=1, column =0, pady=20)'''
    Label(InsertTupFrame0, text="SELECT TABLE NAME:").grid(row = 2,column=0)
    global btn_TBD 
    lbl_result_IU = Label(DeleteTabFrame0, text="", font=('times new roman', 18),fg="red")
    lbl_result_IU.grid(row=3, column = 2 )
    TbName = ttk.Combobox(InsertTupFrame0, textvariable = TABLENAMEDT ) 
    TbName['values'] = DropDownList()
    TbName.grid( row = 2, column = 1) 
    TbName.current() 
    btn_TBS = Button(InsertTupFrame0, text="SHOW",font=("times new roman",18),bg="green",fg="white",bd=2,activebackground="seagreen1",cursor="hand2", width=10,command= ViewDataTAB)
    btn_TBS.grid(row=4 ,column =1, pady=20)




    
    
    
  
 

# =======================================Toggling(Routing) Of Screens=======================================
def Toggle_FromRegister_ToLogin(event=None):
    status = 0
    menubar(status)
    RegisterFrame.destroy()
    LoginForm()


def Toggle_FromLogin_ToRegister(event=None):
    status = 0
    menubar(status)
    LoginFrame.destroy()
    RegisterForm()


def Toggle_FromLogin_ToForgetPass(event=None):
    status = 0
    menubar(status)
    LoginFrame.destroy()
    ForgetPasswordForm()


def Toggle_FromForgetPass_ToLogin(event=None):
    status = 0
    menubar(status)
    ForgetPasswordFrame.destroy()
    LoginForm()
    
def Toggle_FromNavigation_ToLogin(event=None):
    status = 0
    menubar(status)
    NavigationFrame.destroy()
    LoginForm()

def Toggle_FromLogin_ToNavigation(event=None):
    status = 1
    menubar(status)
    LoginFrame.destroy()
    NavigationForm()

def Toggle_FromNavigation_ToChangePass(event=None):
    NavigationFrame.destroy()
    ChangePassForm()

def Toggle_FromNavigation_ToCreateTab(event=None):
    NavigationFrame.destroy()
    CreateTabForm()

def Toggle_FromNavigation_ToViewTab(event=None):
    NavigationFrame.destroy()
    NavigationForm()

def Toggle_FromNavigation_ToDeleteTab(event=None):
    NavigationFrame.destroy()
    DeleteTableForm()

def Toggle_FromNavigation_ToUpdateTab(event=None):
    NavigationFrame.destroy()
    UpdateTableForm()

def  Toggle_FromEditTab_ToNaigationTab(event=None):
    UpdateTabFrame.destroy()
    NavigationForm()

def Toggle_FromChangePass_ToNaviagtion(event=None):
    ChangePassFrame.destroy()
    NavigationForm()    

def Toggle_FromCreateTab_ToNaviagtion(event=None):
    CreateTabFrame.destroy()
    NavigationForm() 

def Toggle_FromUpdateTab_ToNaviagation(event=None):
    UpdateTabFrame.destroy()
    NavigationForm()

def Toggle_FromDeleteTab_ToNaviagation(event=None):
    DeleteTabFrame.destroy()
    NavigationForm()


# =======================================Register Method=======================================
def Register():
    username_demo = USERNAME.get()
    password_demo = PASSWORD.get()
    firstname = FIRSTNAME.get()
    lastname = LASTNAME.get()
    cpass = CPASSWORD.get()
    username = encrypt(username_demo)
    password = encrypt(password_demo)
    captcha = CAPTCHA.get()
 
    Database()
    if username == "" or password == "" or firstname == "" or lastname == "" or captcha == "":
        lbl_result2.config(text="Please complete the required field !", fg="red")
        
    elif RegisterFrame.var.get()==0:
        lbl_result2.config(text="Please Agree The Terms & Condition's", fg="red")
            
    elif password_demo != cpass :
        lbl_result2.config(text="Password Does Not Match!", fg="red")
        
    else:
        if not check_mail(username_demo):
            lbl_result2.config(text="Invalid E-mail !", fg="red")

        elif not check_password(password_demo):
            lbl_result2.config(text="Ivalid Password[A-Z,a-z,0-9,!@#$%^&*]", fg="red")

        elif not (CAPTCHA.get() == get_image()):
            lbl_result2.config(text="Invalid CAPTCHA!", fg="red")
            regenerate_image_captcha()
        
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (username,))
            if cursor.fetchone() is not None:
                lbl_result2.config(text="Username is already taken", fg="red")
            else:
                cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)",
                               (str(username), str(password), str(firstname), str(lastname)))
                conn.commit()
                lbl_result2.config(text="Successfully Created!", fg="black")
                regenerate_image_captcha()
            cursor.close()
            conn.close()

        USERNAME.set("")
        PASSWORD.set("")
        FIRSTNAME.set("")
        LASTNAME.set("")
        CAPTCHA.set("")
        CPASSWORD.set("")
        RegisterFrame.var.set(0)
       


# =======================================Login Method=======================================
def Login():
    username_demo = USERNAME.get()
    password_demo = PASSWORD.get()
    username = encrypt(username_demo)
    password = encrypt(password_demo)
    captcha = CAPTCHA.get()
    Database()
    if username == "" or password == "" or captcha == "":
        lbl_result1.config(text="Please complete the required field !", fg="red")

    elif not CAPTCHA.get()==get_image():
        lbl_result1.config(text="Invalid CAPTCHA!", fg="red")
        regenerate_image_captcha_log()


    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",
                       (username, password))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You LoggedIn Successfully ", fg="blue")
            Toggle_FromLogin_ToNavigation()
            USERNAME.set("")
            PASSWORD.set("")
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
            CAPTCHA.set("")
            regenerate_image_captcha_log()
        conn.commit()
        cursor.close()
        conn.close()
    USERNAME.set("")
    PASSWORD.set("")
    CAPTCHA.set("")


# =======================================Forget Password Method=======================================
def ForgetPassword():
    username_demo = USERNAME.get()
    username_info = encrypt(username_demo)
    Database()
    if username_info == "":
        lbl_result3.config(text="Please complete the required field !", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? ", (username_info,))

        if cursor.fetchone() is not None:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("databaseproject2000@gmail.com", "database@2000")
            password = get_random_password_string(8)
            message = '''
            Hello,
            Dear Sir/Mam
            We wanted to let you know that your OurSQL password was reset.
            Please do not reply to this email with your password. We will never ask for your password, and we strongly discourage you from sharing it with anyone.
            Your Password Is : '''
            final_msg = message + password
            server.sendmail("databaseproject2000@gmail.com", username_demo, final_msg)
            server.quit()
            password_updater(username_info, password)
            lbl_result3.config(text="Email Sent Successfully", fg="blue")

        else:
            lbl_result3.config(text="Invalid Username ", fg="red")

        USERNAME.set("")
        cursor.close()
        conn.commit()
        conn.close()
        

def password_updater(username_info, password_info):
    Database()
    password_demo = encrypt(password_info)
    cursor.execute("UPDATE `member` SET `password` = ? WHERE `username` = ? ",
                   (password_demo, username_info))


def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

# =======================================Change Password Method=======================================      
def ChangePassword():
    UserName = USERNAME.get()
    OldPass = OLDPASS.get()
    NewPass = NEWPASSWORD.get()
    ConfirmPass = CONNEWPASSWORD.get()
    UserNameInfo = encrypt(UserName)
    OldPassInfo = encrypt(OldPass)
    NewPassInfo = encrypt(NewPass)

    Database()
    if OldPass == "" or NewPass == "" or ConfirmPass == "":
        lbl_result5.config(text="Please complete the required field !", fg="red")

    elif NewPass != ConfirmPass :
        lbl_result5.config(text="Password Don't Match !", fg="red")

    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ? ", (UserNameInfo,OldPassInfo))

        if cursor.fetchone() is not None:
            cursor.execute("UPDATE `member` SET `password` = ? WHERE `username` = ? ",
                   (NewPassInfo,UserNameInfo))
            lbl_result5.config(text="Password Changed Successfully", fg="blue")

        else:
            lbl_result5.config(text="Invalid Username ", fg="red")

        #UserNameInfo.set("")
        #OldPassInfo.set("")
        #NewPassInfo.set("")
        #ConfirmPass.set("")
        USERNAME.set("")
        OLDPASS.set("")
        NEWPASSWORD.set("")
        CONNEWPASSWORD.set("")
        cursor.close()
        conn.commit()
        conn.close()


#================================================Crete Table Backend Method=============================================================

def CreateTable(event):
    if  TABLENAME.get() == "" and EXISTTABLENAME.get() == "":   #ExistTab.current()
        lbl_result_CT.config(text="Please Enter Or Select Table Name !", fg="red")
        #ExistingTable(EXISTTABLENAME.get()) if not EXISTTABLENAME.get() == "" else  NewTable(TABLENAME.get()) 

    #elif   TABLENAME.get() != "" and  EXISTTABLENAME.get() != "":
        #lbl_result_CT.config(text="Can't Select Both !", fg="red")
    
    else :
        if (TABLENAME.get() == ""):
            ExistingTable(  EXISTTABLENAME.get() )
        else :
            NewTable(TABLENAME.get())



def ExistingTable(table_name):
    Database()
    value_msg = ValueListFunction()
    msg = f"ALTER TABLE {table_name} ADD ({value_msg})"
    cursor.execute(msg)
    conn.commit()
    conn.close()

    

def NewTable(table_name):
    Database()
    value_msg = ValueListFunction()
    msg = f"CREATE TABLE {table_name} ({value_msg})"
    print(msg)
    cursor.execute(msg)
    conn.commit()
    lbl_result_CT.config(text="Successfully Created the table !", fg="red")
    conn.close()
    clearall()

def ValueListFunction():
    global value_msg 
    value_msg = []
    if A1NAME.get() != "" or A1DTYPE.get() != "" or A1DLENGTH.get() != "" or A1NNULL.get() != "" or A1PK.get() != "" or A1FK.get() != "" :
        Atr1()

    if A2NAME.get() != "" or A2DTYPE.get() != "" or A2DLENGTH.get() != "" or A2NNULL.get() != "" or A2PK.get() != "" or A2FK.get() != "" :
        Atr2()
    
    if  A3NAME.get() != "" or A3DTYPE.get() != "" or A3DLENGTH.get() != "" or A3NNULL.get() != "" or A3PK.get() != "" or A3FK.get() != "" :
        Atr3()
    
    if A4NAME.get() != "" or A4DTYPE.get() != "" or A4DLENGTH.get() != "" or A4NNULL.get() != "" or A4PK.get() != "" or A4FK.get() != "" :
        Atr4()
    
    if A5NAME.get() != "" or A5DTYPE.get() != "" or A5DLENGTH.get() != "" or A5NNULL.get() != "" or A5PK.get() != "" or A5FK.get() != "" :
        Atr5()
    
    if A6NAME.get() != "" or A6DTYPE.get() != "" or A6DLENGTH.get() != "" or A6NNULL.get() != "" or A6PK.get() != "" or A6FK.get() != "" :
        Atr6()

    if A7NAME.get() != "" or A7DTYPE.get() != "" or A7DLENGTH.get() != "" or A7NNULL.get() != "" or A7PK.get() != "" or A7FK.get() != "" :
        Atr7()
    
    if A8NAME.get() != "" or A8DTYPE.get() != "" or A8DLENGTH.get() != "" or A8NNULL.get() != "" or A8PK.get() != "" or A8FK.get() != "" :
        Atr8()

    if A9NAME.get() != "" or A9DTYPE.get() != "" or A9DLENGTH.get() != "" or A9NNULL.get() != "" or A9PK.get() != "" or A9FK.get() != "" :
        Atr9()
    
    if A10NAME.get() != "" or A10DTYPE.get() != "" or A10DLENGTH.get() != "" or A10NNULL.get() != "" or A10PK.get() != "" or A10FK.get() != "" :
       Atr10()
    
    final_Value_msg = "".join(value_msg)
    return final_Value_msg

        

def Atr1():
    if A1NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A1PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A1FK.get() == "y":
        FkeyTable()
        chk_fk = f"FOREIGN KEY ({A1NAME.get()}) REFERENCES {FKEYTABLE.get()}({FKEYCOLUMN.get()})" 
 
    else:
        chk_fk = ""

    msg1 = f"{A1NAME.get()} {A1DTYPE.get()}({ A1DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg1)
    #delete_screen()

def Atr2():
    if A2NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A2PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A2FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A2NAME.get()})" 
    else:
        chk_fk = ""

    msg2 = f",{A2NAME.get()} {A2DTYPE.get()}({ A2DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg2)
    #delete_screen()

def Atr3():
    if A3NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A3PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A3FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A3NAME.get()})" 
    else:
        chk_fk = ""

    msg3 = f",{A3NAME.get()} {A3DTYPE.get()}({ A3DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg3)
    #delete_screen()

def Atr4():
    if A4NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A4PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A4FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A4NAME.get()})" 
    else:
        chk_fk = ""

    msg4 = f",{A4NAME.get()} {A4DTYPE.get()}({ A4DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg4)
    #delete_screen()

def Atr5():
    if A5NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A5PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A5FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A5NAME.get()})" 
    else:
        chk_fk = ""

    msg5 = f",{A5NAME.get()} {A5DTYPE.get()}({ A5DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg5)
    #delete_screen()

def Atr6():
    if A6NNULL.get() == "y":
        chk_nn = "NOT NULL"

    else:
        chk_nn = ""

    if A6PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A6FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A6NAME.get()})" 
    else:
        chk_fk = ""

    msg6 = f",{A6NAME.get()} {A6DTYPE.get()}({ A6DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg6)
    #delete_screen()

def Atr7():
    if A7NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A7PK.get() == "y":
        chk_pk ="PRIMARY KEY"
    else:
        chk_pk = ""

    if A7FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A7NAME.get()})" 
    else:
        chk_fk = ""

    msg7 = f",{A7NAME.get()} {A7DTYPE.get()}({ A7DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg7)
    #delete_screen()

def Atr8():
    if A8NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A8PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A8FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A8NAME.get()})" 
    else:
        chk_fk = ""

    msg8 = f",{A8NAME.get()} {A8DTYPE.get()}({ A8DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg8)
    #delete_screen()

def Atr9():
    if A9NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A9PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A9FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A9NAME.get()})" 
    else:
        chk_fk = ""

    msg9 = f",{A9NAME.get()} {A9DTYPE.get()}({ A9DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg9)
    #delete_screen()

def Atr10():
    if A10NNULL.get() == "y":
        chk_nn = "NOT NULL"
    else:
        chk_nn = ""

    if A10PK.get() == "y":
        chk_pk = "PRIMARY KEY"
    else:
        chk_pk = ""

    if A10FK.get() == "y":
        chk_fk  =  f"FOREIGN KEY({A10NAME.get()})" 
    else:
        chk_fk = ""

    msg10 = f",{A10NAME.get()} {A10DTYPE.get()}({ A10DLENGTH.get()}) {chk_nn} {chk_pk} {chk_fk}"
    value_msg.append(msg10)
    #delete_screen()

def clearall():
    A1NAME.set("") ; A1DTYPE.set("") ; A1DLENGTH.set("") ; A1NNULL.set("") ; A1PK.set("") ; A1FK.set("")
    A2NAME.set("") ; A2DTYPE.set("") ; A2DLENGTH.set("") ; A2NNULL.set("") ; A2PK.set("") ; A2FK.set("")
    A3NAME.set("") ; A3DTYPE.set("") ; A3DLENGTH.set("") ; A3NNULL.set("") ; A3PK.set("") ; A3FK.set("")
    A4NAME.set("") ; A4DTYPE.set("") ; A4DLENGTH.set("") ; A4NNULL.set("") ; A4PK.set("") ; A4FK.set("")
    A5NAME.set("") ; A5DTYPE.set("") ; A5DLENGTH.set("") ; A5NNULL.set("") ; A5PK.set("") ; A5FK.set("")
    A6NAME.set("") ; A6DTYPE.set("") ; A6DLENGTH.set("") ; A6NNULL.set("") ; A6PK.set("") ; A6FK.set("")
    A7NAME.set("") ; A7DTYPE.set("") ; A7DLENGTH.set("") ; A7NNULL.set("") ; A7PK.set("") ; A7FK.set("")
    A8NAME.set("") ; A8DTYPE.set("") ; A8DLENGTH.set("") ; A8NNULL.set("") ; A8PK.set("") ; A8FK.set("")
    A9NAME.set("") ; A9DTYPE.set("") ; A9DLENGTH.set("") ; A9NNULL.set("") ; A9PK.set("") ; A9FK.set("")    
    A10NAME.set("") ; A10DTYPE.set("") ; A10DLENGTH.set("") ; A10NNULL.set("") ; A10PK.set("") ; A10FK.set("")
    TABLENAME.set("")
    EXISTTABLENAME.set("")
 



# =======================================Validating Methods=======================================
def check_mail(email_info):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    var = True if (re.search(regex, email_info)) else False
    return var


def check_password(password_info):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pattern = re.compile(reg)
    match = re.search(pattern, password_info)
    var = True if match else False
    return var

def generate_captcha():
    data_set = list(string.ascii_letters+string.digits)
    s = ""
    for i in range(6):
        a = random.choice(data_set)
        s = s+a
        data_set.remove(a)

    global image_captcha
    image_captcha = s
    return s



def get_image():
    return image_captcha

def generate_first_image():
    global img,im,imgtk,show_img
    img = ImageCaptcha()

    s = generate_captcha()
    print(s)

    value = img.generate(s)
    img.write(s,"cap.png")
    img = cv2.imread('cap.png')
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image = im)
    show_img =Label(RegisterFrame, image = imgtk).grid(row =8)

def regenerate_image_captcha():
    global img,im,imgtk,show_img
    img = ImageCaptcha()
    s = generate_captcha()
    print(s)
    value = img.generate(s)
    img.write(s,"cap.png")
    img = cv2.imread('cap.png')
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image = im)
    show_img =Label(RegisterFrame, image = imgtk).grid(row=8)

def regenerate_image_captcha_log():
    global img,im,imgtk,show_img
    img = ImageCaptcha()
    s = generate_captcha()
    print(s)
    value = img.generate(s)
    img.write(s,"cap.png")
    img = cv2.imread('cap.png')
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image = im)
    show_img =Label(LoginFrame, image = imgtk).grid(row=3)

def generate_first_image_log():
    global img,im,imgtk,show_img
    img = ImageCaptcha()

    s = generate_captcha()
    print(s)

    value = img.generate(s)
    img.write(s,"cap.png")
    img = cv2.imread('cap.png')
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image = im)
    show_img =Label(LoginFrame, image = imgtk).grid(row =3)

# Function for existing table which gives the list of existing names of the table
def DropDownList():
   global final_list 
   final_list = []
   Database()
   cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
   list1 = cursor.fetchall()
   for i in list1 :
      final_list.append(i[0])
   return final_list




LoginForm()
#NavigationForm()




# ========================================MENUBAR WIDGETS==================================
def menubar(status1):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu0 = Menu(menubar, tearoff=0)
    filemenu1 = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)

    
    filemenu.add_command(label="Exit", command=Exit)
    menubar.add_cascade(label="File", font=("ALGERIAN",20),menu=filemenu)
    if status1 == 1:
        filemenu.add_command(label="Change Password" , command=Toggle_FromNavigation_ToChangePass)
        filemenu0.add_command(label="Logout" , command=Toggle_FromNavigation_ToLogin)
        filemenu1.add_command(label="1.Create Table" , command = Toggle_FromNavigation_ToCreateTab)
        filemenu1.add_command(label="2.Update Table" , command = Toggle_FromNavigation_ToUpdateTab)
        filemenu1.add_command(label="3.Drop Table"   , command = Toggle_FromNavigation_ToDeleteTab)
        filemenu1.add_command(label="4.View Table")
        filemenu1.add_command(label=" Structure")
        filemenu2.add_command(label="1.Insert Tuple")
        filemenu2.add_command(label="2.Update Tuple")
        filemenu2.add_command(label="3.Delete Tuple")
        filemenu2.add_command(label="4.View Tuple")
        filemenu2.add_command(label=" Data")
        filemenu3.add_command(label="See Info",command = BasicInformation)
        menubar.add_cascade(label="Logout", font=("ALGERIAN",20),menu=filemenu0)
        menubar.add_cascade(label="DML", font=("ALGERIAN",20),menu=filemenu2)
        menubar.add_cascade(label="DDL", font=("ALGERIAN",20),menu=filemenu1)
        menubar.add_cascade(label="Info", font=("ALGERIAN",20),menu=filemenu3)
    root.config(menu=menubar)

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()

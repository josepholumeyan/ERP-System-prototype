import tkinter as tk
from tkinter import ttk

import sqlite3
import json 
conn=sqlite3.connect("main.db")
conn.row_factory=sqlite3.Row
cursor=conn.cursor()

root=tk.Tk()
root.title("Buttons")
root.geometry("300x200")
style=ttk.Style()
style.theme_use("clam")

cursor.execute("""
CREATE TABLE IF  NOT  EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               value REAL,
               other TEXT--will store dict as json string
)
""")
cursor.execute("""
CREATE TABLE IF  NOT  EXISTS workers(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Name TEXT,
               Level INTEGER,
               Gender TEXT,
               Age  INTEGER,
               Department TEXT,
               Debt REAL,
               Salary REAL
)
""")

info1=[
        ("equity",0.00,""),
        ("total_income",0.00,""),
        ("total_expenditure",0.00,""),
        ("Password",0.00,""),
    ]
for title,value,other in info1:
    cursor.execute("SELECT COUNT(*) FROM users WHERE title=?",(title,))
    if  cursor.fetchone()[0]==0:
        cursor.execute("INSERT INTO users (title,value,other)VALUES(?,?,?)",(title, value,other))
        conn.commit()
    
cursor.execute("SELECT value FROM users WHERE title=? ",("equity",))
equity=cursor.fetchone()[0]
cursor.execute("SELECT value FROM users WHERE title=? ",("total_income",))
total_income=cursor.fetchone()[0]
cursor.execute("SELECT value FROM users WHERE title=? ",("total_expenditure",))
total_expenditure=cursor.fetchone()[0]
cursor.execute("SELECT value FROM users WHERE title=? ",("Password",))
password=cursor.fetchone()[0]



# #Button list
# home=ttk.Button#links to the homepage(welcome function)
# back=ttk.Button#take the user to the previous page
#close=ttk.button#saves updates and prompts user to restart or exit
#exit-ttk.button#exits the user from the program
#saveR=ttk.button#restart the code after saving
#deletew=ttk.button# linka worker to the delete one worker function
#deleteallworkersttk.button#links worker to delete all workers function
# checkE=ttk.Button#links to the check equity function
# checkW=ttk.Button#links to the workers list function
# checkti=ttk.Button#links to the total income function
# checkte=ttk.Button#links to the total expenditure function
# updatei=ttk.Button#links to the  update income function
# updateE=ttk.Button#links to  the update expenditure function
# addnew=ttk.Button#links to add new employee function
# updatew=ttk.Button#links to worker update function
# updateD=ttk.Button#links to the update debt function
# updatede=ttk.Button#links to the update department function
# updateSa=ttk.Button#links to the update salary function
# updatena=ttk.Button#links to the update name function
# updatele=ttk.Button#links to the update  level function




def welcome():#Home page 
    print("Mr. John and Sons Accountacy firm\nFelele,Ibadan\nWhat do you want to do?")
    global checkE
    checkE=ttk.Button(root,text="Check Equity",command=check_equity)
    checkE.pack(side="left",pady=20)
    global checkW
    checkW=ttk.Button(root,text="Check Workers Information",command=worker_information)
    checkW.pack(side="left",pady=20)
    

def check_equity():#displays the company's current equity and prompts user to check total income&expenditure
    #Clears the Former Buttons
    checkE.pack_forget()
    checkW.pack_forget()
    global back
    back=ttk.Button(root,text="Back",command=welcome)
    back.pack_forget()
    back.pack(pady=20)#take the user to the Home page
    global home
    home=ttk.Button(root,text="HOME",command=welcome)
    home.pack(pady=20)#take the user to the previous page
    global close
    close=ttk.Button(root,text="close",command=save)
    close.pack(pady=20)
    if passwordver(): 
        print("The cuurent Equity is",equity)
        #Add buttons for furthher directory
        global checkti
        checkti=ttk.Button(root,text="Check Total Income",command=check_total_income)
        checkti.pack(side="left",pady=20)
        global checkte
        checkte=ttk.Button(root,text="Check Total Expenditure",command=check_total_expenditure)
        checkte.pack(side="left",pady=20)


def check_total_income():#displays the gross income and prompts user to update income
    checkti.pack_forget()
    checkte.pack_forget()
    global updatei
    updatei=ttk.Button(root,text="Update Income",command=update_income)
    updatei.pack(pady=20)
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=check_equity)
    back.pack(pady=20)
    print("The Total Income so far is",total_income)


def check_total_expenditure():#displays the total expenditure prompts user to update total expenditure
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=check_equity)
    back.pack(pady=20)
    checkti.pack_forget()
    checkte.pack_forget()
    print("The Total Expenditure so far is",total_expenditure)
    global updatee 
    updatee=ttk.Button(root,text="Update Expenditure",command=update_expenditure)
    updatee.pack(pady=20)

def update_income():#updates the total income and reflects the changes accordinly in the comapny's equity
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=check_total_income)
    back.pack(pady=20)
    updatei.pack_forget()
    while True:
        try:
            increament=int(input("Input the recent income"))
            break
        except ValueError:
            print("Enter a valid number")
    if passwordver():
        global total_income
        total_income+=increament
        global equity
        equity+=increament
        print("Succesful Gross income is now",total_income)


def update_expenditure():#updates the total expenditure and reflects changes accordinly in the company's equity
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=check_total_expenditure)
    back.pack(pady=20)
    updatee.pack_forget()
    while True:
        try:
            increament=int(input("Input the recent Expenditure"))
            break
        except ValueError:
            print("Enter a valid number")
    if passwordver():   
        global total_expenditure
        total_expenditure+=increament
        global equity
        equity-=increament
        print("Succesful Gross expenditure is now",total_expenditure)


def worker_information():#displays the complete list of workers and prompts the user to eihter add new workers updateworker information or delete worker data
    #Clears the Former Buttons
    checkE.pack_forget()
    checkW.pack_forget()
    global home
    home=ttk.Button(root,text="HOME",command=welcome)
    home.pack(pady=20)#take the user to the previous page
    global back
    back=ttk.Button(root,text="Back",command=welcome)
    back.pack_forget()
    back.pack(pady=20)#take the user to the previous page
    global close
    close=ttk.Button(root,text="close",command=save)
    close.pack(pady=20)

    cursor.execute("SELECT COUNT(*) FROM workers")
    if  cursor.fetchone()[0]==0:
        print("There are no workers add new employees")
    cursor.execute("SELECT * FROM workers")
    rows=cursor.fetchall()
    col_names=[description[0]for description in cursor.description]
    print("|".join(col_names))
    for row in rows:
        print("|".join(str(row[col])for col in col_names))
    global addnew
    addnew=ttk.Button(root,text="Add new Employee",command=new_employee)
    addnew.pack(pady=30)
    global updatew
    updatew=ttk.Button(root,text="update worker information",command=worker_update)
    updatew.pack(pady=20)
    global deletew
    deletew=ttk.Button(root,text="Delete worker information",command=deleteworker)
    deletew.pack(side="top",anchor="ne",pady=10)
    global deleteallworkers
    deleteallworkers=ttk.Button(root,text="Delete all worker information",command=deleteallworker)
    deleteallworkers.pack(side="top",anchor="ne",pady=10)


def new_employee():#adds a new worker into the database and sets his/her salary according to their level,prompts user to update worker data
    addnew.pack_forget()
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=worker_information)
    back.pack(pady=20)#take the user to the previous page
    global name
    name=input("Name of Employee")
    global gender
    gender=input("Male or Female")
    while  True:
        global age
        age=int(input("How old is the employee"))
        if  age >70 or age <18:
            print("worker has to be betweeen age 18-70")
            continue    
        break
    while  True:
        global level
        level=int(input("What level is he/she"))
        if  level >3 or level <1:
            print("level has  to be between 1-3")
            continue
        elif level==1:
            global salary
            salary=50000
            break
        elif level==2:
            salary=75000
            break
        elif level==3:
            salary=100000
            break
        else:
            print("Enter valid input")
            continue
    global department
    department=input("What department is he or she in")
    if passwordver():
        cursor.execute("INSERT INTO workers(Name,Gender,Age,Level,Salary,Department)VALUES(?,?,?,?,?,?)",(name,gender,age,level,salary,department,))
        conn.commit()
        print("sucessful")
        global updatew
        updatew=ttk.Button(root,text="update worker information",command=worker_update)
        updatew.pack(pady=20)


def worker_update():#selects the worker that user wants to update his/her information prompts user to choose what to update debt,department,name,salary,level
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=new_employee)
    back.pack(pady=20)#take the user to the previous page
    updatew.pack_forget()
    global identity
    identity=int(input("Enter id of the worker you wish to select"))
    cursor.execute("SELECT * FROM workers WHERE id =?",(identity,))
    rows=cursor.fetchall()
    col_names=[description[0]for description in cursor.description]
    print("|".join(col_names))
    for row in rows:
        print("|".join(str(row[col])for col in col_names))
    print("what do you want to edit ")
    global updateD
    updateD=ttk.Button(root,text="Update Debt",command=lambda:update_debt(identity))
    updateD.pack(pady=20)
    global updatede
    updatede=ttk.Button(root,text="Update Department",command=lambda:update_department(identity))
    updatede.pack(pady=20)
    global updatena
    updatena=ttk.Button(root,text="Update Name",command=lambda:update_name(identity))
    updatena.pack(pady=20)
    global updateSa
    updateSa=ttk.Button(root,text="Update Salary",command=lambda:update_salary(identity))
    updateSa.pack(pady=20)
    global updatele
    updatele=ttk.Button(root,text="Update Level",command=lambda:update_level(identity))
    updatele.pack(pady=20)
#create 5 buttons leading to the 5 functions below using the identity variable as arguments to choose and change infomation of a specific worker

def update_debt(a):#update the selected workers debt to the database and then reflect the changes in the company's total expenditure and eqiuty(like he/she took a worker loan)
    updateD.pack_forget()
    updatede.pack_forget()
    updatena.pack_forget()
    updateSa.pack_forget()
    updatele.pack_forget()
    global updatew
    updatew=ttk.Button(root,text="update worker information",command=worker_update)
    updatew.pack(pady=20)
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=new_employee)
    back.pack(pady=20)#take the user to the previous page
    increament=int(input("Enter latest debt incurred"))
    time_period=int(input("In how many months is he or she pay it back"))
    salary_deduct=increament/time_period
    cursor.execute("SELECT Debt FROM workers WHERE id=?",(a,))
    Debt=cursor.fetchone()[0]
    if Debt is None:
        Debt=increament
    else:
        Debt+=increament
    cursor.execute("SELECT Salary FROM workers WHERE id=?",(a,))
    salary=cursor.fetchone()[0]
    salary-=salary_deduct
    if passwordver():   
        cursor.execute("UPDATE workers SET Salary=?,Debt=? WHERE id=?",(salary,Debt,a,))
        conn.commit()
        global equity
        equity-=increament
        global total_expenditure
        total_expenditure+=increament
        print("sucessful")
    #update debt as well as workers next salary based on how long he or she wishes to take to repay the loan
    #also updates comapny equity and total expenditure


def update_name(a):#updates the workers name to the database
    updateD.pack_forget()
    updatede.pack_forget()
    updatena.pack_forget()
    updateSa.pack_forget()
    updatele.pack_forget()
    global updatew
    updatew=ttk.Button(root,text="update worker information",command=worker_update)
    updatew.pack(pady=20)
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=new_employee)
    back.pack(pady=20)#take the user to the previous page
    if passwordver():   
        new_name=input("Enter the new name")
        cursor.execute("UPDATE workers SET Name=? WHERE id=?",(new_name,a,))
        conn.commit()
        print("sucessful")


def update_level(a):#updates the workers level to the database,the corresponding increase in salary wont be done automatically has to be done by user manually
    updateD.pack_forget()
    updatede.pack_forget()
    updatena.pack_forget()
    updateSa.pack_forget()
    updatele.pack_forget()
    global updatew
    updatew=ttk.Button(root,text="update worker information",command=worker_update)
    updatew.pack(pady=20)
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=new_employee)
    back.pack(pady=20)#take the user to the previous page
    new_level=int(input("Enter the new Level 1-3"))
    if passwordver():   
        cursor.execute("UPDATE workers SET Name=? WHERE id=?",(new_level,a,))
        conn.commit()


def update_salary(a):#updates the workers salary to the database
    updateD.pack_forget()
    updatede.pack_forget()
    updatena.pack_forget()
    updateSa.pack_forget()
    updatele.pack_forget()
    global updatew
    updatew=ttk.Button(root,text="update worker information",command=worker_update)
    updatew.pack(pady=20)
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=new_employee)
    back.pack(pady=20)#take the user to the previous page
    increament=int(input("How much is the raise"))
    if passwordver():   
        cursor.execute("SELECT Salary FROM workers WHERE id=?",(a,))
        salary=cursor.fetchone()
        salary=+increament
        cursor.execute("UPDATE workers SET Salary=? WHERE id=?",(salary,a,))
        conn.commit()
        print("sucessful")


def update_department(a):#updates the department of the worker to the database 
    updateD.pack_forget()
    updatede.pack_forget()
    updatena.pack_forget()
    updateSa.pack_forget()
    updatele.pack_forget()
    global updatew
    updatew=ttk.Button(root,text="update worker information",command=worker_update)
    updatew.pack(pady=20)
    global back
    back.pack_forget()
    back=ttk.Button(root,text="Back",command=new_employee)
    back.pack(pady=20)#take the user to the previous page
    new_department=input("Enter the new department")
    if passwordver():   
        cursor.execute("UPDATE workers SET Name=? WHERE id=?",(new_department,a,))
        conn.commit()
        print("sucessful")


def passwordver():#verfies the accuracy of password inputed and prompts user to create on if there is none 
    while True:
        global password
        if password==0:
            new_password()
        else:
            while True:
                try:
                    while True:
                        global passwordt
                        passwordt=int(input("enter pin to proceed"))
                        if len(str(passwordt))==4:
                            break
                        else:
                            print("password has to be 4 digits")
                            continue
                    break
                except ValueError:
                    print("enter a valid 4 digit code")
        if passwordt==password:
            print("correct")
            break
        else:
            print("password incorrect")
            continue
    return True

def new_password():#Creates a new password 
        print("No password set enter preffered password")
        while True:
            try:
                while True:
                    global password
                    password=int(input("enter a 4 digit password"))
                    if len(str(password))==4:
                        passwordver()
                        break
                    else:
                        print("password has to be 4 digits")
                        continue
                break
            except ValueError:
                print("enter a valid 4 digit code")


def deleteworker():# deletes data of a specific worker in the databse
    global identity
    identity=int(input("Enter id of the worker you wish to select"))
    cursor.execute("SELECT * FROM workers WHERE id =?",(identity,))
    rows=cursor.fetchall()
    col_names=[description[0]for description in cursor.description]
    print("|".join(col_names))
    for row in rows:
        print("|".join(str(row[col])for col in col_names))
    print("enter pin to delete")
    if passwordver():
        cursor.execute("DELETE FROM workers WHERE id=?",(identity,))
        conn.commit()
        print("sucessful")


def deleteallworker():#deletes data of all workers in the database
    print("enter pin to delete all workers")
    if passwordver():
        cursor.execute("DELETE FROM workers")
        conn.commit()
        print("sucessful")


def save():
#update all information before  closing the code
    cursor.execute("UPDATE users SET value=? WHERE title=?",(equity,"equity",))
    conn.commit()
    cursor.execute("UPDATE users SET value=? WHERE title=?",(total_income,"total_income",))
    conn.commit()
    cursor.execute("UPDATE users SET value=? WHERE title=?",(total_expenditure,"total_expenditure",))
    conn.commit()
    cursor.execute("UPDATE users SET value=? WHERE title=?",(password,"Password",))
    conn.commit()
    print("Want to exit or just save and restart")
    global saveR
    saveR=ttk.Button(root,text="Save and Restart",command=welcome)
    saveR.pack(pady=20)
    global exit 
    exit= ttk.Button(root,text="save and exit",command=exit)
    exit.pack(pady=20)
    print("Saved sucessfully")

welcome()
root.mainloop()
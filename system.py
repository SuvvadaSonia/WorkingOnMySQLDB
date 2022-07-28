"""
Description: By using python, working on MySQL and performing operations 
of Insert, Update, Delete and Fetch.
Author: Sonia Suvvada
Position: Junior Software Engineer

"""

from functions import is_int_or_not,is_phno_or_not,is_string_or_not 

import mysql.connector
con = mysql.connector.connect(host="localhost", user="root",password="Jagson@5355" ,database="tessrac")

cur = con.cursor()

clientInput = input("What query you want to execute? ")

filename = "ids.txt" 

if clientInput == "insert":
    n = input("Enter employee name: ")
    i = input("Enter employee ID: ")
    p = input("Enter employee phone number: ")
    if is_int_or_not(i) and is_phno_or_not(p):
        i = int(i)
        query = "Insert into employee values ('{}',{},{})".format(n,i,p)
        cur.execute(query)
        con.commit()
        print("Row inserted successfully")
        with open(filename,'a') as file:
            file.write("\n {}".format(i))
    else:
        print("Please enter valid employee ID or Valid phone number")
elif clientInput == "update":
    id = int(input("For which employee you want to update? empID: "))
    up = input("Which field you want to change, employeeName or empId or phoneNumber: ")
    if up == "phoneNumber":
        res = input("Updated phone number: ")
        if is_phno_or_not(res):
            query = "Update employee set {}='{}' where empId = {}".format(up,res,id)
            cur.execute(query)
            con.commit()
            print("Phone number Updated successfully")
        else:
            print("Enter valid phone number")
    else:
        res = input("Updated value: ")
        query = "Update employee set {}='{}' where empId = {}".format(up,res,id)
        cur.execute(query)
        con.commit()
        print("Row Updated successfully")
elif clientInput == "delete":
    id = int(input("Whom do you want to delete? empId: "))
    query = "Delete from employee where empId = {}".format(id)
    cur.execute(query)
    con.commit()
    print("Row Deleted successfully")
elif clientInput == "fetch":
    req = input("Whose data do you want to fetch? all or some: ")
    if req == "some":
        id = int(input("Whose data do you want to fetch? empId: "))
        query = "select * from employee where empId={}".format(id)
        cur.execute(query)
        output = cur.fetchall()
        print(output)
        print("Data fetched successfully")
    elif req == "all":
        query = "select * from employee"
        cur.execute(query)
        output = cur.fetchall()
        print(output)
        print("Data fetched successfully")
        
    
    
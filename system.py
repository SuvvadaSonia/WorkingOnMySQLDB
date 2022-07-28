"""
Description: By using python, working on MySQL and performing operations 
of Insert, Update, Delete and Fetch.
Author: Sonia Suvvada
Position: Junior Software Engineer

"""

# importing the validations from other file
from functions import is_int_or_not,is_phno_or_not,is_string_or_not 

import mysql.connector # import mysql connector

# connect to root mysql dbms
con = mysql.connector.connect(host="localhost", user="root",password="Jagson@5355" ,database="tessrac")

cur = con.cursor() # cursor function for row by row processing of result

clientInput = input("What query you want to execute? ") # takes input from user

filename = "ids.txt"  # initiate the filename to store the ids which are created when inserting

# if clientInput request is insert, then given values by client will store in communication table
if clientInput == "insert":
    n = input("Enter employee name: ")
    i = input("Enter employee ID: ")
    p = input("Enter employee phone number: ")
    if is_int_or_not(i) and is_phno_or_not(p):
        i = int(i)
        query = "Insert into employee values ('{}',{},{})".format(n,i,p)
        cur.execute(query) # executes the query
        con.commit() # commits the changes after query
        print("Row inserted successfully")
        # the ids will store in ids.txt
        with open(filename,'a') as file:
            file.write("\n {}".format(i))
    else:
        print("Please enter valid employee ID or Valid phone number")
# if clientInput request is update, the given values by user will be updated
elif clientInput == "update":
    id = int(input("For which employee you want to update? empID: "))
    up = input("Which field you want to change, employeeName or empId or phoneNumber: ")
    if up == "phoneNumber":
        res = input("Updated phone number: ")
        if is_phno_or_not(res):
            query = "Update employee set {}='{}' where empId = {}".format(up,res,id)
            cur.execute(query) # executes the query
            con.commit() # commits the changes after query
            print("Phone number Updated successfully")
        else:
            print("Enter valid phone number")
    else:
        res = input("Updated value: ")
        query = "Update employee set {}='{}' where empId = {}".format(up,res,id)
        cur.execute(query) # executes the query
        con.commit() # commits the changes after query
        print("Row Updated successfully")
# if clientInput request is delete, the given id by user will be deleted
elif clientInput == "delete":
    id = int(input("Whom do you want to delete? empId: "))
    query = "Delete from employee where empId = {}".format(id)
    cur.execute(query) # executes the query
    con.commit() # commits the changes after query
    print("Row Deleted successfully")
# if clientInput request is fetch, the given id by user, those respective details will be fetched
elif clientInput == "fetch":
    req = input("Whose data do you want to fetch? all or some: ")
    if req == "some":
        id = int(input("Whose data do you want to fetch? empId: "))
        query = "select * from employee where empId={}".format(id)
        cur.execute(query) # executes the query
        output = cur.fetchall() # fetches all the data 
        print(output)
        print("Data fetched successfully")
    elif req == "all":
        query = "select * from employee"
        cur.execute(query) # executes the query
        output = cur.fetchall() # fetches all the data 
        print(output)
        print("Data fetched successfully")
        
    
    
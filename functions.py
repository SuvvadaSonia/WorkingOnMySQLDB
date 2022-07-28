"""
Description: By using python, working on MySQL and performing operations 
of Insert, Update, Delete and Fetch.
Author: Sonia Suvvada
Position: Junior Software Engineer

"""

def is_int_or_not(n):
    return (n.isdigit())

def is_phno_or_not(n):
    if len(str(n)) == 10:
        return (True)
    else:
        return (False)

def is_string_or_not(n):
    if n.isdigit():
        return (False)
    else:
        return (True)
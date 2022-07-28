"""
Description: By using python, working on MySQL and performing operations 
of Insert, Update, Delete and Fetch.
Author: Sonia Suvvada
Position: Junior Software Engineer

"""

# function to validate given input is number or not
def is_int_or_not(n):
    return (n.isdigit())

# function to validate given input is phone number or not
def is_phno_or_not(n):
    if len(str(n)) == 10:
        return (True)
    else:
        return (False)

# function to validate given input is string or not
def is_string_or_not(n):
    if n.isdigit():
        return (False)
    else:
        return (True)
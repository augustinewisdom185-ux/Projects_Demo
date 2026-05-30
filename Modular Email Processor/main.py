"""Combining all the 4 types of functions to make a program that is:
(Action,Orchastrated,Validation, and Transformation funtions.)"""

#(Action function)For writing into a file name  called sample in Document folder
import os

def write_log(message):
    home = os.path.expanduser("~")
    log = os.path.join(home, "Documents", "Sample.log")
    with open (log, "a")as file:
        file.write(message + "\n")

#(Transformation function)For cleanig and slipting emails into username and domain name
def clean_split(email):
    cln_email = email.strip().lower()
    username, domain = cln_email.split("@")
    return {"Username": username,
            "Domain": domain}

#(Validity function)Checking the validity of an email address and returns either a True or False
def check_email(email):
    return "@" in  email and "." in email #or num in email

#print(check_email(""))

#An Orchastrated funtion used to call other functions in order of performance
def processed_email(email):
    write_log("App started!!.")
    #write_log(clean_split(""))
    check_email(email)
    if not check_email(email):
        write_log(f"invalid Email received: {email}")
    else:
        cln_email = check_email(email)
        write_log(f"Processed Email: {cln_email}")
        
        write_log("App stopped.")

email = input("Enter your email: ")
#num = int(input("Enter 3 numbers here: "))
processed_email(email)

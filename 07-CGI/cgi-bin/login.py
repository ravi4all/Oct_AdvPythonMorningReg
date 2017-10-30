#!C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='pythonregistration', autocommit=True)

cursor = connection.cursor()

form = cgi.FieldStorage()

usermail = form.getvalue('usermail')
userPwd = form.getvalue('userpwd')

# usermail = "ravi@gmail.com"
# userpwd = "ravi1234"

# def login():
#     if username == userPwd:
#         return "Login Successfull " + username
#     else:
#         return "Login Failed"


def registerhtml(data):
    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>Welcome to python CGI</h1>
    <h2>Name is {}</h2>
    <h2>Email is {}</h2>
    <h2>Country is {}</h2>
    <h2>Gender is {}</h2>
    </body>
    </html>
    """.format(data[0], data[1], data[3], data[4]))

def loginUser():
    query = "SELECT * FROM users WHERE UserEmail = %s AND UserPwd = %s"

    cursor.execute(query, (usermail, userPwd))
    for data in cursor:
        pass

    registerhtml(data)

loginUser()

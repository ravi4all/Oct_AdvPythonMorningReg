#!C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

username = form.getvalue('userName')
userPwd = form.getvalue('userPwd')

# if username == "" and userPwd == "":
#     print("Welcome User")
# else:
#     print("Login Failed")

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
<h2>Hello {}</h2>
<h2>Password is {}</h2>
</body>
</html>
""".format(username, userPwd))

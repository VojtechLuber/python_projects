import smtplib, ssl

host = "smtp.gmail.com"
port = 465


username = "vojtaluber@gmail.com"
password = "scizomiprxnimgir"

reciever = "vojtaluber@gmail.com"
context = ssl.create_default_context()
message = """
Hi!
"""
with smtplib.SMTP_SSL(host, port, context= context) as server:
    server.login(username, password)
    server.sendmail(username,reciever,message)
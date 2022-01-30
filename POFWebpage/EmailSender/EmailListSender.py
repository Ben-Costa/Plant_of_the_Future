import ..POFWebpage.mgdb
import smtplib
from EmailSender.Email_Login import Email, pswd, suckersEmailList
from email.message import EmailMessage
import imghdr

files = ['adccb3e63c4afd53d2fba31f510ea302.jpeg']

Database = POFDB
subscribedEmails = Database.getAllEmails()

for Emails in subscribedEmails:

    print(Emails)

    msg = EmailMessage()
    msg['Subject'] = 'Wealthy Nigerian Prince'
    msg['From'] = Email
    msg['To'] = Emails
    msg.set_content('Plz send your bank info so I can sends 1 hundred million dallars')

    msg.add_alternative("""
<!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This is a scam!</h1>
            <a href="pof.com">LINKKKKKKKKKKKKKKKKK</a>
        <body>
    </html>    
    """, subtype = 'html')
    for file in files:
        #if file not an image
        #with open(file, 'rb') as image:
        #    file_data = image.read()
        #    file_type = imghdr.what(image.name)
        #    file_name = image.name
        
        #msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)

        with open(file, 'rb') as image:
            file_data = image.read()
            file_type = imghdr.what(image.name)
            file_name = image.name

        msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
        smpt.login(Email, pswd)
        smpt.send_message(msg)



#https://techwithtech.com/importerror-attempted-relative-import-with-no-known-parent-package/ did this as was unable to find the 
# POFWebpage package so had to change root directory
import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents [2]  
sys.path.append(str(package_root_directory)) 

import smtplib
from POFWebpage.mgdb import POFDB
from Email_Login import Email, pswd
from email.message import EmailMessage
import imghdr

#files = ['adccb3e63c4afd53d2fba31f510ea302.jpeg']

Database = POFDB()
subscribedEmails = Database.getAllEmails()

for Emails in subscribedEmails:

    print(Emails['_id'])

    msg = EmailMessage()
    msg['Subject'] = 'Wealthy Nigerian Prince'
    msg['From'] = Email
    msg['To'] = Emails['_id']
    msg.set_content('Plz send your bank info so I can sends 1 hundred million dallars')

    msg.add_alternative("""
<!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This is a scam!</h1>
            <h1 style="color:SlateGray;">This is a Test!</h1>
            <a href="pof.com">Stuff</a>
        <body>
    </html>

    """, subtype = 'html')
    #for file in files:
        #if file not an image
        #with open(file, 'rb') as image:
        #    file_data = image.read()
        #    file_type = imghdr.what(image.name)
        #    file_name = image.name
        
        #msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)

    #    with open(file, 'rb') as image:
    #        file_data = image.read()
    #        file_type = imghdr.what(image.name)
    #        file_name = image.name

    #    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
        smpt.login(Email, pswd)
        smpt.send_message(msg)



import smtplib
from email.message import EmailMessage

class mailsend():
    def __init__(self):
        self.msg = EmailMessage()
        self.msg['Subject'] = "Sales report testing"
        self.msg['From'] = 'siddharth.warwatkar@outlook.com'
        self.msg['To'] = 'siddevil938@gmail.com'
        self.msg.set_content("Report attached....")

        files = ['sales_reports.xml']

        for file in files:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name

            self.msg.add_attachment(file_data, maintype='application', subtype='octet-stream',filename=file_name)
    
    def msent(self):
        with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login('siddharth.warwatkar@outlook.com', 'Devil@931986')
            smtp.send_message(self.msg)
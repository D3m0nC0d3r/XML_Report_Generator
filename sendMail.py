import smtplib
from email.message import EmailMessage
import logging

logger = logging.getLogger("sm_Error.logs")
hdlr = logging.FileHandler("./Logs/sm_Error.logs")
formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formater)
logger.addHandler(hdlr)
logger.setLevel(logging.ERROR)


class mailsend():
    def __init__(self):
        try:
            self.msg = EmailMessage()
            self.msg['Subject'] = "Sales report testing"
            self.msg['From'] = 'sender mail'
            self.msg['To'] = 'receiver mail'
            self.msg.set_content("Report attached....")

            files = ['sales_reports.xml']

            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name

                self.msg.add_attachment(file_data, maintype='application', subtype='octet-stream',filename=file_name)
        except Exception as obj:
            print('Error occur while initializing the mail.')
            logger.error(obj)

    def msent(self):
        try:
            with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login('##your email', '##your password')
                smtp.send_message(self.msg)
        except Exception as obj:
            print('Error occur while sending mail.')
            logger.error(obj)
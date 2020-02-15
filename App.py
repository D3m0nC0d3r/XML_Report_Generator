from backend import connect as bend
from sendMail import mailsend
import logging

logs = logging.getLogger('debug.logs')
hdlr = logging.FileHandler("./Logs/debug.logs")
formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formater)
logs.addHandler(hdlr)
logs.setLevel(logging.DEBUG)

b = bend()
s = mailsend()
if __name__ == "__main__":
    b.xmlgenerate()
    logs.debug('xml generated')
    s.msent()
    logs.debug('mail sent')
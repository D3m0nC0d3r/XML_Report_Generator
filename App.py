from backend import connect as bend
from sendMail import mailsend

b = bend()
s = mailsend()
if __name__ == "__main__":
    b.xmlgenerate()
    s.msent()
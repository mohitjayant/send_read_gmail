import smtplib
import getpass

FROM=input("FROM : ")
TO=input("TO : ")


def send_mail(subject, msg):
    try:
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.login(FROM,getpass.getpass())
        message='Subject:{} \n\n {}'.format(subject,msg)
        s.sendmail(FROM, TO,message)
        s.quit()
        print("Successfully sent!")
        
    except:
        print("Unsuccessful!")
        
        
        
subject=input("Subject : ")
msg=input("Message : ")

send_mail(subject,msg)




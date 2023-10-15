import pywhatkit
import time
p = []
l = int(input("enter the limit"))
for i in range(l):
    x = input("Enter the mobile no: ")
    p.append(x)
#Store the events
event1 = "HACKATHON 2023 DECEMBER 15"
event2 = "WEBINAR NOVEMBER 16"


while True:
    for x in p:
        msg1 = "Don't forget the " + event1
        msg2 = "Dont forget the " + event2
        pywhatkit.sendwhatmsg_instantly(x, msg1, 15)
        pywhatkit.sendwhatmsg_instantly(x, msg2, 15)
    time.sleep(86400)




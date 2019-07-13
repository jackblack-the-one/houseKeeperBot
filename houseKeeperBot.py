### created by Felix Meusel 10.01.2019
## just to improve a random generated workflow
## everything has to be in the same folder. In general the 3 functions work the same I simply use a function to randomize it 

import smtplib
import datetime
import sys
import random
import os
from email.mime.text import MIMEText
from datetime import timedelta


Week = ["clean the kitchen", "clean the living-room", "clean the dorm", "tidy up", "garbage service for the whole week", "other things"] #here you can type in the weekly tasks which you'll get randomized then
eigtheendays = ["new bedsheets", "clean the fridge", "get out paper-garbage "] #here you can type in the every 3 week tasks which you'll get randomized then
sixmonths = ["clean the windows", "clean cabintes", "sort documents", "clean the oven"] #here you can type in the  tasks for every six months which you'll get randomized then

str3 = "" #defining strings globaly, just for error fixing  
str4 = ""
str5 = ""
str6 = ""
CurrentDate = ""
week = timedelta(days = 7) #define week

def checktime(): #first the system will start to count if it is time to send out a new email
	global CurrentDate
	global ExpectedDate
	dt = datetime.date.today()
	dt = datetime.datetime(dt.year, dt.month, dt.day)
	CurrentDate = dt
	print(CurrentDate)
	with open("TIME.txt", "r") as e: #I've created text files for the usage on a single PC to count and compare if actual date has passed 
		for line in e:
			if line != 0:
				break
	nextW = CurrentDate + week
	print(CurrentDate)
	ExpectedDate = line
	ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%d/%m/%Y") #define time to compare
	print(ExpectedDate)
	if CurrentDate > ExpectedDate:
	    print("Date missed")
	    TasksW()
	else:
		print("Date not missed")
		sys.exit()
	with open("TIME.txt", "w") as f:
		ne = nextW.strftime("%d/%m/%Y")
		f.write(ne)

	with open("TIME1.txt", "r+") as e:
		first_line = e.readline()
		int(first_line)
		if first_line != 0 or first_line ==0 and first_line  <3:
			counter = int(first_line)
			counter = counter +1
			if counter >2:
				print("except")
				Tasks_18()
				e.seek(0,0)
				e.write(str(0))

			else:
				print(counter)
				k =str(counter)
				first_line = str(first_line)
				c = e.readline().replace(first_line, k)
				print(c)
				e.seek(0, 0)
				e.write(k)


	with open("TIME2.txt", "r+") as e:
		first_line = e.readline()
		int(first_line)
		if first_line != 0 or first_line ==0 and first_line  <3:
			counter = int(first_line)
			counter = counter +1
			if counter >26:
				print("except")
				Tasks_6()
				e.seek(0,0)
				e.write(str(0))

			else:
				print(counter)
				k =str(counter)
				first_line = str(first_line)
				c = e.readline().replace(first_line, k)
				print(c)
				e.seek(0, 0)
				e.write(k)

def TasksW():
	with open("TIME.txt", "r") as e:
		global str1, str2
		if e != 0:
			sr = random.SystemRandom()
			random.shuffle(Week)
			person1 = (Week[:3])
			person2 = (Week[3:])
			str1 = ', '.join(str(e) for e in person1)
			str2 = ', '.join(str(e) for e in person2)
			return str1, str2

def Tasks_18():
	global str3, str4
	sr = random.SystemRandom()
	random.shuffle(eigtheendays)
	taskr = (eigtheendays[2:3])
	taskr2 = (eigtheendays[:2])
	str3 = ', '.join(str(e) for e in taskr)
	str4 = ', '.join(str(e) for e in taskr2)
	return str3, str4
def Tasks_6():
	global str5, str6
	sr = random.SystemRandom()
	random.shuffle(sixmonths)
	taskr3 = (sixmonths[:2])
	taskr4 = (sixmonths[2:4])
	str5 = ', '.join(str(e) for e in taskr3)
	str6 = ', '.join(str(e) for e in taskr4)
	return str5, str6

checktime()




 
msg1 = "Dear household, \n amazing another week has gone \n this time person1 has to " + str1 + " . Have fun. For person2 its "+ str2 + " also have a lot of fun. \n" 
msg2 = " Oh I forgot, is there a three week task? \n For person1 could be: " + str3 + " and " + str5 +"\n"
msg3 = "For person2 " + str4 + " and " + str6 + ". I wish you will come through this . \n Yours sincerly \n E.C. Housekeeper"
msg = msg1 + msg2 + msg3
wired = "\x0a"
replacements = " "
spaced_message = msg.replace(wired, replacements)
msg = spaced_message
SUBJECT = "tasks in the household"

msg = MIMEText(msg)
print(msg)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("hholder@xxx.com", "1234") #add a new email account to send the emails or use an existing one
server.sendmail("hholder@xxx.com", "person2@wxxxxxeb.com",msg.as_string(), SUBJECT) #add the person who shall recieve the email
server.sendmail("hholder@xxx.com", "person1xxxl@xxx.com", msg.as_string(), SUBJECT)
server.quit()
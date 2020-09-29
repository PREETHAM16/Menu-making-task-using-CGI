#!/usr/bin/python3
import cgi
import subprocess as sp
import webbrowser as wb

print("content-type:text/html")
print()


x=cgi.FieldStorage().getvalue("x")
print("Welcome TO My World<br/><br/>")
print("The "+x+" is :<br/>")
print()
if(x=="Date"):
	print(sp.getoutput("date"))
elif(x=="Calender"):
	print(sp.getoutput("cal"))
elif(x=="IP address"):
	print(sp.getoutput("ifconfig"))
elif(x=="Server"):
	print(sp.getoutput("whoami"))
elif(x=="Notepad"):
	print(sp.getoutput("gedit"))
elif(x=="Calender"):
	print(sp.getoutput("cal"))
elif(x=="Firefox"):
	print(wb.open("http://firefox.com"))
elif(x=="Chrome"):
	print(wb.open("http://google.com"))
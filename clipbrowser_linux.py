#clipbrowser (it pretends to be a browser but it just copies the url into your clipboard!)

import sys
import pyperclip #https://pypi.org/project/pyperclip/
from notifypy import Notify #remove this import and the functions to disable notifications https://pypi.org/project/notify-py/


def send_notif(text,title):
	notification = Notify()
	notification.title = title
	notification.message = text
	notification.application_name = "ClipBrowser"
	if(icon):
		notification.icon = icon_path
	if(sound):
		notification.audio = sound_path
	notification.send()

debug = 0 #enables some extra console printing stuff	

	
#close early if no input	
n = len(sys.argv)
if (n < 2):
		if(debug):
			print("no args\n")
			print(sys.executable)
		sys.exit(1) #close if no arguments are passed (it will always be 1 if no arguemnts are passed)

		
#set defaults
icon = 1
icon_path = "/home/shy/Desktop/ClipBrowser.png" #CHANGE ME!
sound = 1
sound_path = "/home/shy/Desktop/clipbrowser.wav" #CHANGE ME!
notifications = 1

if(debug):
	print("\nArgs:", end = " ")
	for i in range(1, n):
		print(sys.argv[i], end = " ")

#zomg actually copy stuff:		
pyperclip.copy(sys.argv[1]) #seriously the only line of code that does what the program is made for lmao
if(notifications):
	send_notif(sys.argv[1],"Copied") #remove to disable notifs
sys.exit(0)

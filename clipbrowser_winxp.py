#clipbrowser (it pretends to be a browser but it just copies the url into your clipboard!)


import sys
import pyperclip #https://pypi.org/project/pyperclip/
import winsound  #to play the sound in winxp since there is no notify-py
import winreg



debug = 0 #enables some extra console printing stuff	

	
#close early if no input	
n = len(sys.argv)
if (n < 2):
		if(debug):
			print("no args\n")
			print(sys.executable)
		sys.exit(1) #close if no arguments are passed (it will always be 1 if no arguemnts are passed)

		
#set defaults	(use this on systems without a registry)	
sound = 0
sound_path = "path_to_sound.wav"
notifications = 1

#windows reg check and load custom stuff
hive = winreg.HKEY_CURRENT_USER #sets the hive for ALL reg stuff program wide

try:
	sound_key = winreg.OpenKeyEx(hive, r"SOFTWARE\\ClipBrowser\\CustomSound\\")
except:
	sound_key = 0
	if(debug):
		print("custom sound not set up")	

if sound_key:
	keystore = winreg.QueryValueEx(sound_key, "Enabled")
	if(keystore[0]):
		sound = 1
		keystore = winreg.QueryValueEx(sound_key, "Sound_path")
		sound_path = keystore[0]
		winreg.CloseKey(sound_key)

	
#create windows reg keys when you type in INSTALL PATH (full path to exe)
if(n == 4):
	if((sys.argv[1] == "INSTALL") & (sys.argv[2] == "PATH")):
		print("Installing as default browser!\n") 

		
		SMI = winreg.OpenKeyEx(hive, r"SOFTWARE\\Clients\\StartMenuInternet\\")
		
		current_sub_key = winreg.CreateKey(SMI, "ClipBrowser")
		winreg.CloseKey(current_sub_key)
		
		current_sub_key = winreg.CreateKey(SMI, "ClipBrowser\\Capabilities\\")
		winreg.SetValueEx(current_sub_key, "ApplicationDescription", 0, winreg.REG_SZ, "Copies URLS to your clipboard")
		winreg.SetValueEx(current_sub_key, "ApplicationIcon", 0, winreg.REG_SZ, sys.argv[3]+",0")
		winreg.SetValueEx(current_sub_key, "ApplicationName", 0, winreg.REG_SZ, "ClipBrowser")
		winreg.CloseKey(current_sub_key)
		
		current_sub_key = winreg.CreateKey(SMI, "ClipBrowser\\Capabilities\\FileAssociations\\") #remove this part is you don't want actual html files to open using this software
		winreg.SetValueEx(current_sub_key, ".htm", 0, winreg.REG_SZ, "ClipBrowserHTML")
		winreg.SetValueEx(current_sub_key, ".html", 0, winreg.REG_SZ, "ClipBrowserHTML")
		winreg.SetValueEx(current_sub_key, ".shtml", 0, winreg.REG_SZ, "ClipBrowserHTML")
		winreg.SetValueEx(current_sub_key, ".xht", 0, winreg.REG_SZ, "ClipBrowserHTML")
		winreg.SetValueEx(current_sub_key, ".xhtml", 0, winreg.REG_SZ, "ClipBrowserHTML")
		winreg.CloseKey(current_sub_key)
		
		current_sub_key = winreg.CreateKey(SMI, "ClipBrowser\\Capabilities\\Startmenu\\")
		winreg.SetValueEx(current_sub_key, "StartMenuInternet", 0, winreg.REG_SZ, "ClipBrowser")
		winreg.CloseKey(current_sub_key)
		
		current_sub_key = winreg.CreateKey(SMI, "ClipBrowser\\Capabilities\\URLAssociations\\")
		winreg.SetValueEx(current_sub_key, "ftp", 0, winreg.REG_SZ, "ClipBrowserHTML")
		winreg.SetValueEx(current_sub_key, "http", 0, winreg.REG_SZ, "ClipBrowserHTML")
		winreg.SetValueEx(current_sub_key, "https", 0, winreg.REG_SZ, "ClipBrowserHTML")
		#add more here if you want to let it handle other URL types
		winreg.CloseKey(current_sub_key)
		
		current_sub_key = winreg.CreateKey(SMI, "ClipBrowser\\DefaultIcon\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, sys.argv[3]+",0")
		winreg.CloseKey(current_sub_key)
		
		current_sub_key = winreg.CreateKey(SMI, "ClipBrowser\\InstallInfo\\")
		#some commands have no actual function but it could be added in the future. the values are apparently required for the program to be listed in windows according to the MS site 
		winreg.SetValueEx(current_sub_key, "HideIconsCommand", 0, winreg.REG_SZ, "\""+sys.argv[3]+"\" INSTALL HIDEICONS")
		winreg.SetValueEx(current_sub_key, "IconsVisible", 0, winreg.REG_DWORD, 1)
		winreg.SetValueEx(current_sub_key, "ReinstallCommand", 0, winreg.REG_SZ, "\""+sys.argv[3]+"\" INSTALL ENABLE")
		winreg.SetValueEx(current_sub_key, "ShowIconsCommand", 0, winreg.REG_SZ, "\""+sys.argv[3]+"\" INSTALL SHOWICONS")
		winreg.CloseKey(current_sub_key)	
		
		current_sub_key = winreg.CreateKey(SMI, "ClipBrowser\\shell\\open\\command\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, "\""+sys.argv[3]+"\"")
		winreg.CloseKey(current_sub_key)	
		#end of SMI entries
		
		classes = winreg.OpenKeyEx(hive, r"SOFTWARE\\Classes\\")
		
		
		current_sub_key = winreg.CreateKey(classes, "ClipBrowserHTML")
		winreg.SetValueEx(current_sub_key, "FriendlyTypeName", 0, winreg.REG_SZ, "ClipBrowser")
		winreg.CloseKey(current_sub_key)
		
		current_sub_key = winreg.CreateKey(classes, "ClipBrowserHTML\\Application\\")
		winreg.SetValueEx(current_sub_key, "ApplicationCompany", 0, winreg.REG_SZ, "ShyStudios")
		winreg.SetValueEx(current_sub_key, "ApplicationDescription", 0, winreg.REG_SZ, "Copies URLS to your clipboard")
		winreg.SetValueEx(current_sub_key, "ApplicationIcon", 0, winreg.REG_SZ, sys.argv[3]+",0")
		winreg.SetValueEx(current_sub_key, "ApplicationName", 0, winreg.REG_SZ, "ClipBrowser")
		winreg.SetValueEx(current_sub_key, "FriendlyTypeName", 0, winreg.REG_SZ, "ClipBrowser")
		winreg.CloseKey(current_sub_key)
		
		current_sub_key = winreg.CreateKey(classes, "ClipBrowserHTML\\DefaultIcon\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, sys.argv[3]+",0")
		winreg.CloseKey(current_sub_key)
		
		#this is the ACTUAL command windows runs
		current_sub_key = winreg.CreateKey(classes, "ClipBrowserHTML\\shell\\open\\command\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, "\""+ sys.argv[3]+ "\"" + " \"%1\"")
		winreg.CloseKey(current_sub_key)

		current_sub_key = winreg.CreateKey(classes, "http\\shell\\open\\command\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, "\""+ sys.argv[3]+ "\"" + " \"%1\"")
		winreg.CloseKey(current_sub_key)


		current_sub_key = winreg.CreateKey(classes, "https\\shell\\open\\command\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, "\""+ sys.argv[3]+ "\"" + " \"%1\"")
		winreg.CloseKey(current_sub_key)

		#i cant figure out how to get the program listed in the actual winxp options list but these extra 2 commands DO work


		#end of class entries
		
		#enable notifications by default
		software = winreg.OpenKeyEx(hive, r"SOFTWARE\\")
		current_sub_key = winreg.CreateKey(software, "ClipBrowser\\")
		winreg.SetValueEx(current_sub_key, "Notifications", 0, winreg.REG_DWORD, 1)
		winreg.CloseKey(current_sub_key)
	
		#prob redundent
		winreg.CloseKey(software)
		winreg.CloseKey(classes)
		winreg.CloseKey(SMI)
		winreg.CloseKey(hive)

		sys.exit(0)
		
#clipbrowser.exe INSTALL NATIVEPY (PATH TO PYTHON.exe) (PATH TO clipbrowser.py)		
if(n == 5):
	if((sys.argv[1] == "INSTALL") & (sys.argv[2] == "NATIVEPY")):
		classes = winreg.OpenKeyEx(hive, r"SOFTWARE\\Classes\\")
		current_sub_key = winreg.CreateKey(classes, "ClipBrowserHTML\\shell\\open\\command\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, "\""+sys.argv[3] +"\" \""+ sys.argv[4]+ "\"" + " \"%1\"")
		winreg.CloseKey(current_sub_key)


		current_sub_key = winreg.CreateKey(classes, "http\\shell\\open\\command\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, "\""+sys.argv[3] +"\" \""+ sys.argv[4]+ "\"" + " \"%1\"")
		winreg.CloseKey(current_sub_key)

		current_sub_key = winreg.CreateKey(classes, "https\\shell\\open\\command\\")
		winreg.SetValueEx(current_sub_key, "", 0, winreg.REG_SZ, "\""+sys.argv[3] +"\" \""+ sys.argv[4]+ "\"" + " \"%1\"")
		winreg.CloseKey(current_sub_key)


		winreg.CloseKey(classes)
		winreg.CloseKey(hive)
		sys.exit(0)
#windows reg 	
if(n == 4):
	if((sys.argv[1] == "INSTALL") & (sys.argv[2] == "SOUND")):
		

		software = winreg.OpenKeyEx(hive, r"SOFTWARE\\")
		current_sub_key = winreg.CreateKey(software, "ClipBrowser\\CustomSound")
		winreg.SetValueEx(current_sub_key, "Enabled", 0, winreg.REG_DWORD, 1)
		winreg.SetValueEx(current_sub_key, "Sound_path", 0, winreg.REG_SZ, sys.argv[3])
		
		winreg.CloseKey(current_sub_key)
		winreg.CloseKey(software)
		winreg.CloseKey(hive)
		sys.exit(0)

	
#gotta get this file AFTER the install section
try:
	notification_key = winreg.OpenKeyEx(hive, r"SOFTWARE\\ClipBrowser\\")
except:
	notification_key = 0
	if(debug):
		print("You didn't run install dumass")	

if notification_key:
	keystore = winreg.QueryValueEx(notification_key, "Notifications")
	if(keystore[1]): #the 1 value will always be true if the value exists
		notifications = keystore[0]
		winreg.CloseKey(notification_key)		
	
winreg.CloseKey(hive) # closes it if it wasn't closed by the other things	
# total arguments

if(debug):
	print("\nArgs:", end = " ")
	for i in range(1, n):
		print(sys.argv[i], end = " ")

#zomg actually copy stuff:		
pyperclip.copy(sys.argv[1]) #seriously the only line of code that does what the program is made for lmao
if(notifications):
	if(sound):
		winsound.PlaySound(sound_path, winsound.SND_FILENAME)
sys.exit(0)
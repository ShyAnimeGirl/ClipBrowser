
![Logo](https://raw.githubusercontent.com/ShyAnimeGirl/ClipBrowser/V1.0.0/ClipBrowser.png)


# ClipBrowser

A VERY VERY Simple python script which copies a URL to your clipboard. It can play a cool little sound and show a notification! This is used in place of a web browser so when clicking links they simply get copied to your clipboard.

Why would you use this you may ask?
Personally I use multiple web browsers and when I click a link I want to select which one it opens in.
It is also useful as a way to not accidentally click on a malicious link, don’t think you would never do this IT CAN HAPPEN! 



## Features

- Cool notification sound (customizable)
- Cool notification Icon (customizable)


## Installation


### Win10

The vast majority of code in clipbrowser.py is related to modern windows registry entries to get the software to show up as a web browser choice in windows default “apps”.

Download the win10 release, extract the ClipBrowser folder somewhere you want the program to live (I use Program Files). Hopefully the .exe provided will work for your windows version, if it doesn’t you can always build it yourself or run it naively with python (see winxp). Open a powershell or command prompt in the installation folder and run the following commands (replace the actual path with your own):

```
.\ClipBrowser.exe INSTALL PATH "C:\Program Files\ClipBrowser\ClipBrowser.exe"
```
This will register ClipBrowser with the system as a browser. Navigate to your control panel, Apps, Default Apps, and hopefully you will be able to select ClipBrowser!

Optional:
```
.\ClipBrowser.exe INSTALL SOUND "C:\Program Files\ClipBrowser\clipbrowser.wav"
```    
Specifies the location of the notification sound.

 
```
.\ClipBrowser.exe INSTALL ICON "C:\Program Files\ClipBrowser\ClipBrowser.png"
```
Specifies the location of the notification icon.
 
 
```
.\ClipBrowser.exe INSTALL NATIVEPY "C:\Program Files\Python311\pythonw.exe" "C:\Program Files\ClipBrowser\clipbrowser.py"
```
ADVANCED, allows windows to run the python script directly instead of the EXE, you need python for this and all of the required modules (see linux instructions). Please note, you need to specify the path to pythonW not python or you will get a command prompt popping up every time you click a link. Also note you still need the .exe file as this is where windows gets the .html icons from.


### linux
Install the following modules:

Pyperclip
```
python3 -m pip install pyperclip
```
notify-py (not to be confused with notifypy)
```
python3 -m pip install notify-py
```

For linux users I’ve provided clipbrowser_linux.py which has the windows registry stuff removed.
Modify lines 33 and 35 to point to the correct path for the notification sound and icon.

Build this as a binary or run it from python directly, the first argument will be the text copied so you can test it simply by running:
```
python3 clipbrowser_linux.py test
```
“test” should now be in your clipboard

Set this as your default browser in the way you see fit. 

### WindowsXP
The clipbrowser_winxp.py file is modified to work with windows XP’s registry. 
I was unable to build a windows xp exe so my installation process is purely python based, but there may be an exe version in the future.

For now you will need a version of python and pip that works with xp. In my case I am using [this build of 3.8](https://msfn.org/board/topic/183741-python-3813-for-windows-xp-sp3/?do=findComment&comment=1240896). 

You will also need to install the pyperclip module, the notify-py module is NOT used on XP!

Place clipbrowser_winxp.py and clipbrowser.wav (if you want) somewhere it can live (in my example here C:\clipbrowser).

Navigate to your clipbrowser folder in a command prompt and run the following commands:
```
c:\Python38\python.exe clipbrowser_winxp.py INSTALL PATH C:\clipbrowser\clipbrowser_winxp.py
```
```
c:\Python38\python.exe clipbrowser_winxp.py INSTALL NATIVEPY C:\Python38\pythonw.exe C:\clipbrowser\clipbrowser_winxp.py
```
On XP these commands will automatically set ClipBrowser as the default url handler, it does NOT currently work with .html files, you need to manually specially that in the folder options control panel under the file types tab.

Optional to enable sound:
```
c:\Python38\python.exe clipbrowser_winxp.py INSTALL SOUND C:\clipbrowser\clipbrowser.wav
```
On xp there are no desktop notifications but the sound can still be played, if you want this functionality in the main windows version you will need to import winsound and replace the final send_notif with winsound.PlaySound(sound_path, winsound.SND_FILENAME)
On linux you can get this functionality in many ways however it seems the most popular method, the playsound module, does not play nice with pyperclip so if you want this then figure it out some other way, there are a zillion modules that let you play a wav in linux. 

### MacOS
I tried for hours to get the compiled .app working the way it should but it never worked, the script can run and will work fine on its own but once compiled into a .app it stops working and I can’t figure out why. Maybe you can or maybe you want to set up something else like an apple script that runs the python script directly. You will likely need [defaultbrowser](https://github.com/kerma/defaultbrowser) and some plst settings to get osx to open things using the script. The macos folder contains the MacOS icon and my pyinstaller spec file.

## Authors
- [Shy](http://shystudios.us/about.html) (Concept, Programming, and Sound)
- [Gunther](http://shystudios.us/about.html) (Icon)

# Ashoka Autolog
GNU General Public License v3.0

Note: You must have Microsoft Edge installed. If you download and run just 'Ashoka Autologin.py', make sure you've installed selenium, and have the Microsoft Edge webdriver in a folder C:\\Ashoka Autolog\
You can download the webdriver from here: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

The installer has both the webdriver and a standalone instance of python, with selenium installed.

Ashoka Autolog v1.0

author: quagzlor
email: quagzlor.d@gmail.com

CAUTION: Your details are saved in plaintext. Anyone can open the file and read them. This is a program meant for convenience.

Link to installer (hosted on sourceforge): https://sourceforge.net/projects/ashoka-autolog/

When the program starts, a python command line window will open. DO NOT CLOSE THIS, else the program will end as well.

To start this program, just double click 'Ashoka Autologin.py'. If you've already entered your username etc, you don't have to enter them again.

Instructions for use:

1. Launch 'Ashoka Autologin.py'
2. Fill in your username and password.
3. Fill in how many hours you want between log-ins (the server logs you out every 12 hours, recommend setting time as 11)
4. Chill

In case your login details change:

1. Open Autologin_data.txt
2. Line 1 has your username
   Line 2 has your password
   Line 3 has your log-in delay
3. Change whatever you need to, and save the file.

Thanks to: Stack Overflow, Selenium, Winpython (for the standalone python) and Inno Setup (for the setup executable)

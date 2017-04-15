# v0.1 of Ashoka Autologin
#This project is covered under GNU GPLv3 licence
import urllib
login_page=""
username=""
password=""
time_delay=0
test_page="https://www.google.com"

if username and password and login_page == "":
    print "What is the login link?"
    login_page=raw_input()
    print "What is the username?"
    username=raw_input()
    print "What is the password?"
    password=raw_input()
    print "After how many hours do you want to log in again?"
    time_delay=input()

    file_object= open("Autologin_Data.txt","w")

with urllib.request.urlopen(login_page)
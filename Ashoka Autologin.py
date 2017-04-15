# v0.1 of Ashoka Autologin
#This project is covered under GNU GPLv3 licence
import urllib
import urllib2
import os.path
import mechanize

login_page="http://10.1.0.100:8090/"
password=""
time_delay=""
test_page="https://www.google.com"
r=""

br=mechanize.Browser()

if os.path.isfile("Autologin_Data.txt")!=True:
    print "What is the username?"
    username=raw_input()
    print "What is the password?"
    password=raw_input()
    print "After how many hours do you want to log in again?"
    time_delay=raw_input()


    save_file= open("Autologin_Data.txt","w")
    save_file.write(username+'\n')
    save_file.write(password+'\n')
    save_file.write(time_delay)
    save_file.close()

save_file=open("Autologin_Data.txt","r")
username=save_file.readline()
password=save_file.readline()
time_delay=save_file.readline()
save_file.close()

login_data=urllib.urlencode({'username':username,
                             'password':password})

br.open(login_page,login_data)

br.click(btnSubmit)

# -*- coding: utf-8 -*-
import sys
import requests
import json
from bs4 import BeautifulSoup
# fbxWelcomeBoxName

base_url = "http://graph.facebook.com/"
re = raw_input("Does your profile has a username? (y/n): ")
if re == 'y':
    user_name = raw_input("Enter your Facebook username: ")
    url = base_url + user_name
    response = requests.get(url);
    profile_id = json.loads(response.content)["id"]
elif re == 'n':
    profile_id = raw_input("Enter your Facebook Profile ID: ")
else:
    print "Invalid Response. Try again!"
    sys.exit()

num = int(raw_input("How many neighbours would you like to find out? (Max 20) "))
if num > 20:
    print "Your desires are too high! Sorry!"
else:
    i=0
    temp = int(profile_id)
    while i<num:
        temp += 1
        fb_url = "https://www.facebook.com/profile.php?id=" + str(temp)
        r = requests.get(fb_url)
        html = r.content
        soup = BeautifulSoup(html)
        name = soup.title.string.split(" | ")
        name = name[0]
        if name != "Profile Unavailable" and name != "Content Not Found" and name.encode('utf-8') != "सामग्री नहीं मिली":
            print name.encode('utf-8'), "https://www.facebook.com/profile.php?id="+str(temp)
            i+=1

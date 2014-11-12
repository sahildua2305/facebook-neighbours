# -*- coding: utf-8 -*-
import sys
import requests
import json
from bs4 import BeautifulSoup

re = raw_input("Does your profile has a username? (y/n): ")
if re == 'y':
    # Make a graph HTTP call to get facebook profile ID corresponding to the username
    base_url = "http://graph.facebook.com/"
    user_name = raw_input("Enter your Facebook username: ")
    url = base_url + user_name
    response = requests.get(url);
    profile_id = json.loads(response.content)["id"]
elif re == 'n':
    # Directly get profile ID from user input
    profile_id = raw_input("Enter your Facebook Profile ID: ")
else:
    # Invalid response except y/n
    print "Invalid Response. Try again!"
    sys.exit()

# Ask for number of neighbours user will like to see
num = int(raw_input("How many neighbours would you like to find out? (Max 20) "))
if num > 20:
    print "Your desires are too high! Sorry!"
else:
    # Initialization of counter variable(count)
    count = 0
    # Store the profile ID in a temp variable which will be set(incremented) again and again
    temp = int(profile_id)
    while count < num:
        temp += 1
        fb_url = "https://www.facebook.com/profile.php?id=" + str(temp)
        # Make HTTP call with every value of profile ID(temp)
        r = requests.get(fb_url)
        html = r.content
        soup = BeautifulSoup(html)
        # Get name from title of the page(the easiest method to get name from the page)
        name = soup.title.string.split(" | ")
        name = name[0]
        # Error handling
        if name != "Profile Unavailable" and name != "Content Not Found" and name.encode('utf-8') != "सामग्री नहीं मिली":
            print name.encode('utf-8'), "https://www.facebook.com/profile.php?id="+str(temp)
            count += 1 # Increment counter variable(count)

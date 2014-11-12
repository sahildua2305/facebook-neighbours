import urllib2
from bs4 import BeautifulSoup
# fbxWelcomeBoxName

base_url = "https://www.facebook.com/profile.php?id="
profile_id = raw_input("Enter your Facebook profile ID: ")

url = base_url + profile_id

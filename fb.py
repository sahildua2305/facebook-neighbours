import urllib2
import requests
import json
from bs4 import BeautifulSoup
# fbxWelcomeBoxName

base_url = "http://graph.facebook.com/"
#user_name = raw_input("Enter your Facebook username: ")

user_name = "iamsahildua"
url = base_url + user_name

response = requests.get(url);
profile_id = json.loads(response.content)["id"]
print profile_id

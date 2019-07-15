import requests
import json
import os
import win_unicode_console
import random

win_unicode_console.enable()

# I'm using proxies to interact with Instagram just in case
def GetProxies():
    proxies = []
    list = requests.get("https://www.proxy-list.download/api/v1/get?type=https&anon=elite")
    for line in list.content.splitlines():
        proxy = {"https": line.decode(), "http": line.decode()}
        proxies.append(proxy)
    random.shuffle(proxies)
    return proxies

def InstaSearch(term):
    proxies = GetProxies()
    results = "N/A"
    for proxy in proxies:
        try:
            results = requests.get("https://www.instagram.com/web/search/topsearch/?context=blended&query={}&rank_token=0.6841947012676349&include_reel=true".format(term), proxies=proxy)
            return results.json()
        except Exception as e:

            # these are public proxies, they tend to fail
            print(type(e))

            # if I'm getting something back and it isn't json I want to see that
            if type(e) == json.decoder.JSONDecodeError:
                print(results)

results = InstaSearch(input("Enter Instagram search term:"))

for user in results["users"]:
    username = user["user"]["username"]
    realName = user["user"]["full_name"]
    print("{} ({})".format(username, realName))
import requests
import bs4
from bs4 import BeautifulSoup

def getCurrFlow(ip):
    res = requests.get('https://netflow.dorm.ccu.edu.tw/flows/'+ ip)
    res.encodeing = "utf8"
    return BeautifulSoup(res.text, 'html.parser').find_all('font')[0].text
    
if __name__ == "__main__":
    targetIP = input("IP: ")
    print(getCurrFlow(targetIP))

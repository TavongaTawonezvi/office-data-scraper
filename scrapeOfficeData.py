from bs4 import BeautifulSoup
import requests

tags = ""
r = requests.get("pageURL").text
with open("mashable_office.html", "r",encoding="utf=8") as f:
    soup = BeautifulSoup(f, "html.parser")

    tags = soup.find("article")
with open("the_office.txt", "a") as officeFile:
    for p in tags.select("p"):
        officeFile.write(p.text + "\n")
        


    

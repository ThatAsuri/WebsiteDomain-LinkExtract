import requests
from bs4 import BeautifulSoup
import re
urls = []

main_url = input("Give me URL in this format - https://example.com: ")
link = requests.get(main_url)
  
all_links = BeautifulSoup(link.text, "html.parser")

for httpys in all_links.find_all("a", attrs={"href": re.compile("^http")}):
    print(httpys.get("href"))
    urls.append(httpys.get("href"))
    
# Remove duplicates
urls = list(dict.fromkeys(urls))

file = open("extracted_links.txt", "w")
for url in urls:
    file.writelines(url + "\n")
file.close()







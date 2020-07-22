import requests as rq
from bs4 import BeautifulSoup
import os

r1   = rq.get("https://www.pexels.com/@amritphotos")
soup = BeautifulSoup(r1.text,"html.parser")

links = []

x = soup.select('img[src^="https://images.pexels.com/photos"]')

for img in x:
    links.append(img['src'])

#for l in links:
#    print(l)

os.mkdir('amrit_photos')
i = 1

for index,img_link in enumerate(links):
    if i<=10:
        img_data = rq.get(img_link).content
        with open("amrit_photos/"+str(index+1)+'.jpeg','wb+') as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break

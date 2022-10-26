import requests as req
import os, bs4
import json


base_url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
entered_num = input("Input the comic number ")
base_url += entered_num
print('Downloading image from %s...' % base_url)
res = req.get(base_url)
soup = bs4.BeautifulSoup(res.text,"html.parser")
comic_elem = soup.select('#comic img')
comic_url = 'http:' + comic_elem[0].get('src')

res = req.get(comic_url)

imageFile = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
for chunk in res.iter_content(1):
	imageFile.write(chunk)
imageFile.close()
print('Downloaded the image file')

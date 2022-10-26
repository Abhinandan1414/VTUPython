import requests as req
import os, bs4
import json


base_url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
entered_num = input("Input the comic number example 1414: ")
base_url += entered_num
print('Downloading image from location ----' ,base_url)
res = req.get(base_url)
soup = bs4.BeautifulSoup(res.text,"html.parser")
comic_elem = soup.select('#comic img')
comic_url = 'http:' + comic_elem[0].get('src')
print("comic_url is: "+comic_url)

res = req.get(comic_url)

image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
for data_chunk in res.iter_content():
	image_file.write(data_chunk)
image_file.close()
print('Downloaded the image file to location',os.path.join('xkcd'),"File name is",os.path.basename(comic_url))

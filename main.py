import requests
import json
from bs4 import BeautifulSoup

res = requests.get('http://digitalinnovation.one/blog/')
res.encoding ='utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find(class_="pagination").find_all('a')

all_pages = []
for link in links:
    page = requests.get(link.get('href'))
    all_pages.append(BeautifulSoup(page.text, 'html.parser'))

all_post = []
for posts in all_pages:
    posts = soup.find_all(class_="post")
    for post in posts:
        info = post.find(class = "post-content")
        title = info.h2.text
        preview = info.p.text
        author = info.find(class_="post-author").text
        time = info.find(class_="post-date")['datetime']
        all_post.append({
            'title': title,
            'preview': preview,
            'author': author,
            'time': time
        })

print(all_post)
with open('post.json', 'w') as json_file:
    json.dump(all_post, json_file, ident=3, ensure_ascii=False)
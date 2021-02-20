from bs4 import BeautifulSoup
# Can use 'lxml' instead 'html.parser
# import lxml

with open('website.html',encoding='utf-8') as file:
    content = file.read()
    
soup = BeautifulSoup(content,'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)
# print(soup.li)
# print(soup.prettify())

anchor_tags = soup.find_all(name='a')
# print(anchor_tags)
# for tag in anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
heading = soup.find(name='h3', class_='default')

url = soup.select_one(selector='h3 a')
name = soup.select_one(selector='#name')
# select returns a list

print(name) 
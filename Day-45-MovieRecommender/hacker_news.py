import requests
from bs4 import BeautifulSoup

hacker_news = "https://news.ycombinator.com/"

response = requests.get(hacker_news).text
soup = BeautifulSoup(response, 'html.parser')

articles = soup.find_all(name='a', class_='storylink')
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)
article_upvotes = [score.getText().split(' ')[0] for score in soup.find_all(name='span', class_='score')]
max_value = max(article_upvotes)
max_value_index = article_upvotes.index(max_value)
print(article_texts[max_value_index])
print(article_links[max_value_index])
print(article_upvotes[max_value_index])
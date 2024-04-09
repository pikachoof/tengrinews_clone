from bs4 import BeautifulSoup as BS
from bs4 import NavigableString as NS
import requests

def fetch_articles(page, article_list_name, base_url):
    articles_list = page.find(class_='article_list_name').children
    articles = []
    for item in articles_list:
        if not isinstance(item, NS):
            article = {}
            article['href'] = base_url + item.a['href']
            article['img_src'] = base_url + item.picture.source['srcset']
            article['announce'] = item.find(class_='content_main_item_announce').text
            article['title'] = item.find(class_='content_main_item_title').text
            articles.append(article)

    return articles



def print_articles(articles):
    for article in articles:
        print(article)
    pass


def fetch_page(url):
    page = requests.get(url, stream=False, timeout=3)
    page = BS(page.content, 'html.parser')
    return page


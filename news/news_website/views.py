from django.shortcuts import render
from django.http import HttpResponse
from . import fetch

# Create your views here.
def index(request):
    page_number = 1
    if request.method == "POST":
        page_number = request.form['page_number']

    url = 'https://tengrinews.kz/news'
    news = fetch.fetch_page(url + 'page/{}'.format(page_number))
    articles = fetch.fetch_articles(news, 'content_main', url)
    context = {
            'articles' : articles,
    }
    return render(request, 'templates/index.html', context)
    

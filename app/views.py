from django.shortcuts import render
from newscatcherapi import NewsCatcherApiClient
import requests

def index(request):
    try:
        newscatcherapi = NewsCatcherApiClient(x_api_key='j9eDrL_PjAatxMYJu9Tox0xANBQYmGePDDArY7aO4mQ')

        all_articles = newscatcherapi.get_search(q='Elon Musk',
                                                lang='en',
                                                countries='CA',
                                                page_size=100)
        print(all_articles['articles'])

        context = {
            "all_articles" : all_articles['articles'][:2],
        }
        return render(request, 'index.html', context)   
    except:
        pass

    return render(request, 'index.html')   



def other(request):
    url = 'https://api.worldnewsapi.com/search-news'
    parameters = {
    'text': 'Bamboo Development', # query phrase
    'sort': 'publish-time',  # maximum is 100
    'api-key': 'aaa245439f6e4d2093fa3e4235bb8459',  # your own API key
    'source-countries' : 'in'
}
    response = requests.get(url, params=parameters)
    news_list = response.json()
    try:
        context = {
            'news_list' : list(news_list['news'][:2]),
        }
        return render(request, 'news.html', context)
    except:
        pass
       
    return render(request, 'news.html')


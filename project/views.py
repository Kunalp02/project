from django.shortcuts import render
from newscatcherapi import NewsCatcherApiClient


def index(request):

    newscatcherapi = NewsCatcherApiClient(x_api_key='Api_key')

    all_articles = newscatcherapi.get_search(q='Elon Musk',
                                            lang='en',
                                            countries='CA',
                                            page_size=100)
    print(all_articles['articles'])

    context = {
        "all_articles" : all_articles['articles'][:2],
    }
    return render(request, 'index.html', context)   
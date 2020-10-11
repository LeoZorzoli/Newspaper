from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import User
from datetime import date




import requests

today = date.today()

response_temp = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=-32.03&lon=-60.31&appid=969c8c1c061df85848b351e72bf74e51")
geodata = response_temp.json()

response_covid = requests.get('https://api.covid19api.com/dayone/country/argentina')
covid = response_covid.json()

temp = int(geodata['main']['temp'] - 273.15)
img = geodata['weather'][0]['icon']
description = geodata['weather'][0]['description']

total_covid = covid[len(covid) - 1]['Active']

class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class': "input form-control col-lg-8 col-sm-12 col-xs-12"}))

# Create your views here.
def index(request):

    '''APINEWS PRINCIPAL 3 ARG NEWS'''
    url = ('http://newsapi.org/v2/top-headlines?'
            'country=ca&'
            'pageSize=3&'
            'sortBy=popularity&'
            'apiKey=4f2554546ddf475e93b9d5cb8c2f1952')
    response = requests.get(url)
    apiNewsPrincipal = response.json()

    '''APINEWS BBC PRINCIPAL'''
    url = ('http://newsapi.org/v2/top-headlines?'
        'sources=bbc-news&'
        'pageSize=3&'
        'apiKey=4f2554546ddf475e93b9d5cb8c2f1952')
    response = requests.get(url)
    apiNewsBBC = response.json()

    '''APINEWS WORLD RECENT'''
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=4f2554546ddf475e93b9d5cb8c2f1952')
    response = requests.get(url)
    apiNewsWorld = response.json()

    '''APINEWS INGLATERRA RECENT'''
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=in&'
        'pageSize=4&'
        'apiKey=4f2554546ddf475e93b9d5cb8c2f1952')
    response = requests.get(url)
    apiNewsInglaterra = response.json()

    if request.method == 'GET':
        context = {
            'today': today,
            'geodata': geodata,
            'temp': temp,
            'img': img,
            'description': description,
            'total_covid': total_covid,
            'apiNewsPrincipal': apiNewsPrincipal,
            'apiNewsBBC': apiNewsBBC,
            'apiNewsWorld': apiNewsWorld,
            'apiNewsInglaterra': apiNewsInglaterra,
            'form': Search()
        }

        return render(request, "newspaper/index.html", context)
    else:
        form = Search(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            '''APINEWS SEARCH NEW'''
            url = ('https://newsapi.org/v2/everything?'
                f'q={item}&'
                'apiKey=4f2554546ddf475e93b9d5cb8c2f1952')
            response = requests.get(url)
            apiNewsSearched = response.json()

            context = {
                'apiNewsSearched': apiNewsSearched,
                'today': today,
                'form': Search()
            }

            if not apiNewsSearched: 
                return render(request, "newspaper/search.html", {'message': 'No match to your search', 'today': today, "form":Search()})

            else:
                return render(request, "newspaper/search.html", context)
        else:
            return render(request, "encyclopedia/index.html", {"form": form})


def category(request, category):

    '''APINEWS CATEGORY'''
    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        f'category={category}&'
        'apiKey=4f2554546ddf475e93b9d5cb8c2f1952')
    response = requests.get(url)
    apiNewsCategory = response.json()

    print(len(apiNewsCategory))

    if len(apiNewsCategory['articles']) == 0:
        context = {
            'message': "OOPS! It looks like this category doesn't exist.",
            'today': today,
            'geodata': geodata,
            'temp': temp,
            'img': img,
            'description': description,
            'form': Search()
        }
        return render(request, "newspaper/error.html", context)

    context = {
        'today': today,
        'geodata': geodata,
        'temp': temp,
        'img': img,
        'description': description,
        'apiNewsCategory': apiNewsCategory,
        'form': Search()
    }

    return render(request, "newspaper/category.html", context)

def allnews(request):

    '''APINEWS ALLNEWS'''
    url = ('https://newsapi.org/v2/top-headlines?'
        'sortBy=popularity&'
        'language=en&'
        'pageSize=50&'
        'apiKey=4f2554546ddf475e93b9d5cb8c2f1952')

    response = requests.get(url)
    apiAllNews = response.json()

    context = {
        'apiAllNews': apiAllNews,
        'today': today,
        'form': Search()
    }

    return render(request, "newspaper/allnews.html", context)

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']

        message = Message.objects.create(first_name=first_name, last_name=last_name, email=email, message=message)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "newspaper/contact.html", {"today": today})
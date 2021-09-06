from news.models import Article
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/todays-news.html', {"date": date, "news" : news })

def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day = days[day_number]
    return day

def past_days_news(request, past_date):

    try:
        # convert data from string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
        print("heey",date)
    except ValueError:
        raise Http404()

    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news" : news})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html', {"message": message, "articles": searched_articles})

    else: 

        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {"message": message})
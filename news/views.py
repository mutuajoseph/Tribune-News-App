from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/todays-news.html', {"date": date,})

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

    return render(request, 'all-news/past-news.html', {"date": date})
import random
import requests
from django.shortcuts import render, redirect
from datetime import datetime
from .models import UserData

API_KEY = '120f454ec0eb2cf5575d80307b6ae4e9'

def get_weather(city="Ahmedabad"):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)

    if weather_response.status_code == 200:
        current_weather = weather_response.json()
    else:
        current_weather = None

    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()
    else:
        forecast_data = None

    return current_weather, forecast_data

def home(request):
    quotes = [
        "The sun is shining, and so is your smile!",
        "Weather is what you expect, climate is what you get.",
        "There's no such thing as bad weather, only inappropriate clothing.",
        "The weather is a great metaphor for life—sometimes it's sunny, sometimes it's stormy.",
        "There is no such thing as bad weather, only inappropriate clothing.",
        "Some people feel the rain; others just get wet.",
        "The sun is a daily reminder that we too can rise again from the darkness, that we too can shine our own light.",
        "A change in the weather is sufficient to recreate the world and ourselves.",
        "If you want to see the sunshine, you have to weather the storm",
        "In the midst of winter, I found there was, within me, an invincible summer.",
        "There's no such thing as bad weather, just bad clothes.",
        "The rain is a blessing. It's nature's way of nourishing the earth.",
      ]
    current_quotes = random.sample(quotes, 3) 
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    weather_data, forecast_data = get_weather()  

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        UserData.objects.create(name=name, email=email)
        return redirect('submissions')

    context = {
        'current_time': current_time,
        'current_quotes': current_quotes,
        'weather_data': weather_data,
        'forecast_data': forecast_data,
    }
    
    return render(request, 'Index.html', context)

def submissions(request):
    all_submissions = UserData.objects.all()
    return render(request, 'submissions.html', {'submissions': all_submissions})




from django.shortcuts import render, redirect
from .models import Cities
import requests

def weather_app(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4a458b93357cb3b01d7d08cd32aed91d'
    weather_data = []
    cities_list = Cities.objects.all()

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            add_city = Cities.objects.create(city=city)
            add_city.save()
            return redirect('/')

    for city in cities_list:
        get_weather = requests.get(url.format(city.city)).json()

        if get_weather.get('cod') == 200:  # Check for a valid response
            weather = {
                'city': city.city,
                'temp': get_weather['main']['temp'],
                'desc': get_weather['weather'][0]['description'],
                'icon': get_weather['weather'][0]['icon']
            }
            weather_data.append(weather)
        else:
            print(f"Error fetching weather data for {city.city}: {get_weather.get('message')}")

    context = {'weather_data': weather_data}
    return render(request, 'weather/weather_page.html', context)

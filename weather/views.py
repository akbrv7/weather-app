from django.shortcuts import render
import requests

def weather_veiw(request):
    api_key = '47c0fac0ea4d502eeb3bde192957445e'
    city = request.GET.get('city', 'Navoiy')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    weather_data = response.json()

    context = {
        'city': city,
        "temperature": weather_data['main']['temp'],
        "description": weather_data['weather'][0]['description'],
        "icon": weather_data['weather'][0]['icon']
    }

    return render(request, 'weather/weather.html', context)
# def gwd(city):
#     api_key = '47c0fac0ea4d502eeb3bde192957445e'
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None
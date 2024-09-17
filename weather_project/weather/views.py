from django.shortcuts import render
import requests
from django.core.cache import cache

def home(request):

    api_key = "<type_key_here>"
    city = request.GET.get('city', 'Hyderabad')  
    country = request.GET.get('country', 'India')  
    
    cache_key = f"{city}_{country}_weather"
    cached_data = cache.get(cache_key)

    if cached_data:
        print(f"Cache hit for {city}, {country}.")
        payload = cached_data
    
    else:
        print(f"Cache miss for {city}, {country}. Fetching new data...") 
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={api_key}"
        data = requests.get(url).json()

        if data.get('cod') != 200:
            payload = {
                "error": "City not found. Please try again."
            }
        else:
            payload = {
                "city": data["name"],
                "weather": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "temperature": {
                    "kelvin": data["main"]["temp"],
                    "celsius": data["main"]["temp"] - 273.15
                },
                "pressure": data["main"]["pressure"],
                "humidity": data["main"]["humidity"]
            }
            cache.set(cache_key, payload, timeout=3600)

    context = {'data':payload}
    print(payload)
    return render(request, "weather/home.html", context)
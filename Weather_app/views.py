from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import requests 

# Create your views here.
def home(request):
    city = request.GET.get("city","Sialkot")
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a30d8727eb51710600c308a1b6ba916b'
    data = requests.get(url).json()
    
    payload = { 
    'city':data['name'], 
    'weather' : data['weather'][0]['main'] , 
    'icon': data['weather'][0]['icon'],
    'kelvin_temperature': data['main']['temp'], 
    'celcius_temperature': int(data['main']['temp'] - 273),
    'pressure': data['main']['pressure'], 
    'humidity': data['main']['humidity'],
    'description' : data['weather'][0]['description']
    }

    context = {'data': payload}
    print(context)

    return render(request,'home.html', context)

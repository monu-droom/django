from django.shortcuts import render, redirect
import requests

# Create your views here.

def get_weather(request):
    cities = [
        "Delhi", "Mumbai", "Kolkāta", "Bangalore", "Chennai", "Hyderābād", "Pune", "Ahmedabad",
        "Sūrat", "Lucknow", "Jaipur", "Kanpur", "Mirzāpur", "Nāgpur", "Ghāziābād", "Supaul",
        "Vadodara", "Rājkot", "Vishākhapatnam", "Indore", "Thāne", "Bhopāl", "Pimpri-Chinchwad",
        "Patna", "Bilāspur", "Ludhiāna", "Āgra", "Madurai", "Jamshedpur", "Prayagraj", "Nāsik",
        "Farīdābād", "Meerut", "Jabalpur", "Kalyān", "Vasai-Virar", "Najafgarh", "Vārānasi",
        "Srīnagar", "Aurangābād", "Dhanbād", "Amritsar", "Alīgarh", "Guwāhāti", "Hāora", "Rānchi",
        "Gwalior", "Chandīgarh", "Haldwāni", "Vijayavāda", "Jodhpur", "Raipur", "Kota", "Bareilly"
    ]
    return render(request, 'weather.html', {'cities': cities})


def fetch_weather(request):
    response_dict = {}
    API_KEY = '741a82c392f0201594fe22d664b1b5bd'
    if request.method == 'POST':
        city = request.POST['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()
        if response['cod'] == 200:
            response_dict = {
                'city': response['name'],
                'temp' : response['main']['temp'],
                'weather': response['weather'][0]['main'],
                'feels_like' : response['main']['feels_like']
            }
        print(response_dict)       
        return render(request, 'weather_result.html', {'response_dict' : response_dict})
    else:
        print('Whoops! wrong request')
    return redirect('get_weather')
    
from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    data = {}
    city = ''
    if request.method == 'POST':
        city = request.POST['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=3d010b7bcbb634e9b67130fe041e6f27'
        try:
            res = urllib.request.urlopen(url).read()
            json_data = json.loads(res)
            if str(json_data.get('cod')) == '200':
                data = {
                    "country_code": str(json_data['sys']['country']),
                    "coordinate": ' ('+ str(json_data['coord']['lon']) + ' , ' +
                    str(json_data['coord']['lat']) + ')',
                    "temp": str(json_data['main']['temp']),
                    "pressure": str(json_data['main']['pressure']),
                    "humidity": str(json_data['main']['humidity']),
                    "description": str(json_data['weather'][0]['description']),
                }
            else:
                city = ''
        except Exception:
            city = 'City not found!'
            data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
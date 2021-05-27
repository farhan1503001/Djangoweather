from django.shortcuts import render

# Create your views here.
def home(request):
    import json 
    import requests
    if request.method=='POST':
        cityname=request.POST['cityname']
        weather_url='https://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid=dbcff67f1bebd11657e002b3e177ff5b'
        #key=dbcff67f1bebd11657e002b3e177ff5b
        try:
            dataset=requests.get(weather_url)
            api=json.loads(dataset.content)
            long=api['coord']['lon']
            lat=api['coord']['lat']
            celcius_temp=round(api['main']['temp']-273.00,3)
            curr_feel=round(api['main']['feels_like']-273.00,3)
            try:
                poldata=requests.get('http://api.openweathermap.org/data/2.5/air_pollution?lat='+str(lat)+'&lon='+str(long)+'&appid=dbcff67f1bebd11657e002b3e177ff5b')
                polindex=json.loads(poldata.content)
                if polindex['list'][0]['main']['aqi']<=3:
                    color='low'
                    desc='DAQI Index within range 1-3 indicates low air pollution'
                elif polindex['list'][0]['main']['aqi']>=4 & polindex['list'][0]['main']['aqi']<=6:
                    color='moderate'
                    desc='DAQI Index within range 4-7 indicates air pollution of moderate level'
                elif polindex['list'][0]['main']['aqi']<=3 & polindex['list'][0]['main']['aqi']<=9:
                    color='high'
                    desc='DAQI Index within range 7-9 indicates high air pollution'
                else:
                    color='veryhigh'
                    desc='DAQI Index of value 10 indicates high air pollution'

            except Exception as e1:
                polindex='Pollution Data Error'
        except Exception as e:
            api='Error..'
        return render(request,'home.html',{'api':api,'pol':polindex,'apitemp':celcius_temp,
        'feels_like':curr_feel,'description_color':color,'description':desc})
    else:
        weather_url='https://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=dbcff67f1bebd11657e002b3e177ff5b'
        #key=dbcff67f1bebd11657e002b3e177ff5b
        try:
            dataset=requests.get(weather_url)
            api=json.loads(dataset.content)
            long=api['coord']['lon']
            lat=api['coord']['lat']
            celcius_temp=round(api['main']['temp']-273.00,3)
            curr_feel=round(api['main']['feels_like']-273.00,3)
            try:
                poldata=requests.get('http://api.openweathermap.org/data/2.5/air_pollution?lat='+str(lat)+'&lon='+str(long)+'&appid=dbcff67f1bebd11657e002b3e177ff5b')
                polindex=json.loads(poldata.content)
                if polindex['list'][0]['main']['aqi']<=3:
                    color='low'
                    desc='DAQI Index within range 1-3 indicates low air pollution'
                elif polindex['list'][0]['main']['aqi']>=4 & polindex['list'][0]['main']['aqi']<=6:
                    color='moderate'
                    desc='DAQI Index within range 4-7 indicates air pollution of moderate level'
                elif polindex['list'][0]['main']['aqi']<=3 & polindex['list'][0]['main']['aqi']<=9:
                    color='high'
                    desc='DAQI Index within range 7-9 indicates high air pollution'
                else:
                    color='veryhigh'
                    desc='DAQI Index of value 10 indicates high air pollution'

            except Exception as e1:
                polindex='Pollution Data Error'
        except Exception as e:
            api='Error..'
        return render(request,'home.html',{'api':api,'pol':polindex,'apitemp':celcius_temp,
        'feels_like':curr_feel,'description_color':color,'description':desc})
def about(request):
    return render(request,'about.html',{})

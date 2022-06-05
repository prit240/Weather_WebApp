#make a virtual envirnment and install all the module 
#import the flask module
from flask import Flask,render_template,request
import requests

app = Flask(__name__)

#make a route and render all the html templates in this route
@app.route('/', methods=["GET", "POST"])
def index():
    weatherData = ''
    error = 0
    cityNname = ''
    if request.method == "POST":
        cityNname = request.form.get("cityName")
        if cityNname:
            weatherApiKey = 'bb25b11cb84453798ec30423ea03638f'
            url = "https://api.openweathermap.org/data/2.5/weather?q="+cityNname+"&appid=" + weatherApiKey 
            weatherData = requests.get(url).json()
        else:
            error = 1


    return render_template('index.html',data = weatherData, cityNname = cityNname, error = error)
     
        #take a variable to show the json data
        #r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=bb25b11cb84453798ec30423ea03638f')

        #read the json object
        #json_object = r.json()
        #print(json_object)
        #take some attributes like temperature,humidity,pressure of this 
        #temperature = int(json_object["main"]["temp"]) #this temparetuure in kelvin
        #humidity = int(r.json()['main']['humidity'])
        #pressure = int(r.json()['main']['pressure'])
        #wind = int(r.json()['wind']['speed'])

        #atlast just pass the variables
        #condition = r.json()['weather'][0]['main']
        #desc = r.json()['weather'][0]['description']
        
        #return render_template('index.html',data=data)
    #else:
        #return render_template('index.html',data=data) 


if __name__ == "__main__":
    #app.run(debug=True)
    app.run()
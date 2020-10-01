import requests
from tkinter import *

def weather():
	city = city_listbox.get()
	url = "https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02".format(city)
	res = requests.get(url)
	output = res.json()

	weather_status = output['weather'][0]['description']
	temperature = output['main']['temp']
	humidity = output['main']['humidity']
	windspeed = output['wind']['speed']

	weatherstatus_lable.configure(text="Weather :" + str(weather_status))
	temp_label.configure(text="Temperature :" + str(temperature))
	humidity_label.configure(text="Humidity Level :" + str(humidity))
	windspeed_label.configure(text="Wind Speed :" + str(windspeed))


root=Tk()
root.geometry("390x360")
root.title("Weather Of The India")
root.config(background="powderblue")

city_list = ["Delhi","Mumbai","Pune","Nagpur","Jaisalmer","Shimla","Banglore","Wardha","Hydrabad","Ahemdabad","Kolkata","Chennai","Jaipur","Lucknow","Patna","Raipur"]


city_listbox = StringVar(root)
city_listbox.set("Select The City")
option = OptionMenu(root,city_listbox,*city_list)

option.grid(row=2,column=2,padx=150,pady=10)

button1 = Button(root,text="Select",width=15,fg="black",background="white",bd=2,command=weather)
button1.grid(row=5,column=2,padx=150)

weatherstatus_lable = Label(root,font=("arial",20,"bold"),fg="black",background="powderblue")
weatherstatus_lable.grid(row=12,column=2)

temp_label = Label(root,font=("arial",20,"bold"),fg="black",background="powderblue")
temp_label.grid(row=16,column=2)

humidity_label = Label(root,font=("arial",20,"bold"),fg="black",background="powderblue")
humidity_label.grid(row=20,column=2)

windspeed_label = Label(root,font=("arial",20,"bold"),fg="black",background="powderblue")
windspeed_label.grid(row=24,column=2)





root.mainloop()

import requests
API_KEY="dc14b34e3ad881e0d6cbed6aa713fe36"
def get_data(place,days,type):

    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()

    filter_data = data["list"]

    filter_data = filter_data[:days * 8]
    time=[]
    [time.append(item["dt_txt"]) for item in filter_data]
    if type=="Temperature":
        final_data=[item["main"]["temp"]/10 for item in filter_data]
        return final_data,time

    if type=="Sky":
        final_data=[item["weather"][0]["main"] for item in filter_data]
        return final_data,time







if __name__=="__main__":
  t,d=get_data("London",3,"Sky")
  print(t)
  print(d)
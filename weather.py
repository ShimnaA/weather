import requests
from bs4 import BeautifulSoup
import pandas as pd

class WeatherForcast:
    def __init__(self):
        self.base_url = "https://forecast.weather.gov/MapClick.php?lat=34.052230000000066&lon=-118.24367999999998"

    def getdetails(self):
        page = requests.get(self.base_url)
        soup = BeautifulSoup(page.content, "html.parser")

        forecast_elems = soup.find_all("li", class_="forecast-tombstone")
        period_list = [item.find(class_="period-name").get_text() for item in forecast_elems]
        desc_list = [item.find(class_="short-desc").get_text() for item in forecast_elems]
        temperature_list = [item.find(class_='temp').get_text() for item in forecast_elems]
        weather_data = pd.DataFrame(
            {
                "Period": period_list,
                "Description": desc_list,
                "Temperature": temperature_list
            })
        print(weather_data)
        weather_data.to_csv("forecastdetails.csv")

    def forecast(self):
        self.getdetails()


if __name__ == '__main__':
    weather = WeatherForcast()
    weather.forecast()

import requests
from dateutil.parser import parse


class YahooWeatherForecast:

    def get(self, city):
        url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in" \
              "%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22'{" \
              "}'%22)%20and%20u%20%3D%20%22c%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys" \
            .format(city)
        data = requests.get(url).json
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": day_data["high"]
            })
        return forecast


class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or YahooWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)


def _main():
    city_info = CityInfo("Moskow")
    forecast = city_info.weather_forecast()
    print(forecast)


# if __name__ = "_main_"
#     _main()

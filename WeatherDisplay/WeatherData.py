def degrees_to_direction(degrees: float):
    if degrees >= 348.75 or degrees < 11.25:
        return 'O'
    elif 11.25 <= degrees < 33.75:
        return 'OSO'
    elif 33.75 <= degrees < 56.25:
        return 'SO'
    elif 56.25 <= degrees < 78.75:
        return 'SSO'
    elif 78.75 <= degrees < 101.25:
        return 'S'
    elif 101.25 <= degrees < 123.75:
        return 'SSW'
    elif 123.75 <= degrees < 146.25:
        return 'SW'
    elif 146.25 <= degrees < 168.75:
        return 'WSW'
    elif 168.75 <= degrees < 191.25:
        return 'W'
    elif 191.25 <= degrees < 213.75:
        return 'WNW'
    elif 213.75 <= degrees < 236.25:
        return 'NW'
    elif 236.25 <= degrees < 258.75:
        return 'NNW'
    elif 258.75 <= degrees < 281.25:
        return 'N'
    elif 281.25 <= degrees < 303.75:
        return 'NNO'
    elif 303.75 <= degrees < 326.25:
        return 'NO'
    else:
        return 'ONO'


ROUND_DIGITS = 1


class WeatherData:

    def __init__(self, weather_data_raw: str):
        weather_data = weather_data_raw.split('|')
        self._wind_speed = float(weather_data[1])
        self._wind_gust = float(weather_data[2])
        self._wind_dir = float(weather_data[3])
        self._rain = float(weather_data[4])
        self._ground_temp = float(weather_data[5])
        self._air_temp = float(weather_data[6])
        self._air_pressure = float(weather_data[7])
        self._air_humidity = float(weather_data[8])
        self._air_quality = float(weather_data[9])

    @property
    def wind_speed(self):
        return round(self._wind_speed, ROUND_DIGITS)

    @property
    def wind_gust(self):
        return round(self._wind_gust, ROUND_DIGITS)

    @property
    def wind_dir(self):
        return degrees_to_direction(round(self._wind_dir, ROUND_DIGITS))

    @property
    def rain(self):
        return round(self._rain, ROUND_DIGITS)

    @property
    def ground_temp(self):
        return round(self._ground_temp, ROUND_DIGITS)

    @property
    def air_temp(self):
        return round(self._air_temp, ROUND_DIGITS)

    @property
    def air_pressure(self):
        return round(self._air_pressure, ROUND_DIGITS)

    @property
    def air_humidity(self):
        return round(self._air_humidity, ROUND_DIGITS)

    @property
    def air_quality(self):
        return round(self._air_quality, ROUND_DIGITS)

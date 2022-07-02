from gpiozero import Button
from WeatherSocketClient import send_data, send_log

import math
import time
import datetime
import statistics
import wind_direction_byo
import board
import busio
import adafruit_bme680
import ds18b20_therm
import gc

RADIUS_CM = 9.0
WIND_INTERVAL = 5
ADJUSTMENT = 1.18
CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600
BUCKET_SIZE = 0.2794
TOTAL_INTERVAL = 60

rain_count = 0
wind_count = 0
store_speeds = []
store_directions = []

def spin():
    global wind_count
    wind_count = wind_count + 1
    
def calculate_speed(time_sec):
    global wind_count
    
    circumference_cm = (2.0 * math.pi) * RADIUS_CM
    dist_km = (circumference_cm * wind_count) / CM_IN_A_KM
    
    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * SECS_IN_AN_HOUR
    final_speed = km_per_hour * ADJUSTMENT
    
    return final_speed

def bucket_tipped():
    global rain_count
    rain_count = rain_count + 1

def reset_rainfall():
    global rain_count
    rain_count = 0

def reset_wind():
    global wind_count
    wind_count = 0
    
i2c = busio.I2C(board.SCL, board.SDA)
tphg_sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

temp_probe = ds18b20_therm.DS18B20()

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin

rain_sensor = Button(6)
rain_sensor.when_pressed = bucket_tipped

while True:
    start_time = time.time()
    
    while time.time() - start_time <= TOTAL_INTERVAL:
        wind_start_time = time.time()
        reset_wind()
        
        wind_direction = wind_direction_byo.get_dir_value(WIND_INTERVAL)
        store_directions.append(wind_direction)

        wind_speed = calculate_speed(WIND_INTERVAL)
        store_speeds.append(wind_speed)
        
    wind_average = wind_direction_byo.get_average(store_directions)
    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    
    rainfall = rain_count * BUCKET_SIZE
    reset_rainfall()
    
    store_speeds = []
    store_directions = []
    
    ground_tem = temp_probe.read_temp()
    humidity = tphg_sensor.humidity
    pressure = tphg_sensor.pressure
    temperature = tphg_sensor.temperature
    gas = tphg_sensor.gas
    
    timestamp = str(datetime.datetime.now())

    weather_data = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(timestamp, wind_speed, wind_gust, wind_average, rainfall, ground_tem, temperature, pressure, humidity, gas)
    send_log()
    send_data(weather_data, False)
    
    gc.collect(generation=0)

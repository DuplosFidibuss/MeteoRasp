import sys
import time

from WeatherDisplay import *

data = "0|0|0|0|0|0|0|0|0|0"
weather_data = WeatherData(data)

surf, font = init_display()
update_display(surf, font, weather_data)

while True:
    event = pygame.event.wait()
    if event.type == KEYDOWN or event.type == QUIT:
        close_display()
        sys.exit()
    time.sleep(0.05)

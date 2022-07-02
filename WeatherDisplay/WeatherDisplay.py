import pygame
from pygame import font, Surface
from pygame.locals import *
from WeatherData import WeatherData


WHITE = (190, 190, 230)
BLACK = (0, 0, 0)
(B, H) = (800, 480)


def init_display():
    pygame.init()
    surf = pygame.display.set_mode((B, H), 0, 32)
    pygame.display.set_caption('Wetter')
    font = pygame.font.SysFont('FreeSerif.ttf', 40)
    surf.fill(WHITE)
    pygame.display.update()
    return surf, font


def update_display(surf: Surface, font: font.SysFont, data: WeatherData):
    image = pygame.image.load(r'Pictures\wind_edited_small.png')
    surf.blit(image, (62, 10))
    wind_speed = font.render('{} km/h'.format(data.wind_speed), True, BLACK)
    surf.blit(wind_speed, (62, 120))

    image = pygame.image.load(r'Pictures\wind_edited_small.png')
    surf.blit(image, (328, 10))
    max_str = font.render('max', True, BLACK)
    surf.blit(max_str, (420, 85))
    wind_gust = font.render('{} km/h'.format(data.wind_gust), True, BLACK)
    surf.blit(wind_gust, (328, 120))

    image = pygame.image.load(r'Pictures\wind_rose_edited_small_1.png')
    surf.blit(image, (595, 10))
    wind_dir = font.render('{}'.format(data.wind_dir), True, BLACK)
    surf.blit(wind_dir, (595, 120))

    image = pygame.image.load(r'Pictures\rain_small.png')
    surf.blit(image, (62, 170))
    rain = font.render('{} mm'.format(data.rain), True, BLACK)
    surf.blit(rain, (62, 280))

    image = pygame.image.load(r'Pictures\ground_edited_small.png')
    surf.blit(image, (328, 244))
    image = pygame.image.load(r'Pictures\ground_temperature_edited_small.png')
    surf.blit(image, (388, 170))
    ground_temp = font.render('{} °C'.format(data.ground_temp), True, BLACK)
    surf.blit(ground_temp, (328, 280))

    image = pygame.image.load(r'Pictures\temperature_edited_small.png')
    surf.blit(image, (595, 170))
    air_temp = font.render('{} °C'.format(data.air_temp), True, BLACK)
    surf.blit(air_temp, (595, 280))

    image = pygame.image.load(r'Pictures\barometer_edited_small.png')
    surf.blit(image, (62, 330))
    pressure = font.render('{} mbar'.format(data.air_pressure), True, BLACK)
    surf.blit(pressure, (62, 440))

    image = pygame.image.load(r'Pictures\humidity_edited_small.png')
    surf.blit(image, (328, 330))
    humidity = font.render('{} %'.format(data.air_humidity), True, BLACK)
    surf.blit(humidity, (328, 440))

    image = pygame.image.load(r'Pictures\co2_edited_small.png')
    surf.blit(image, (595, 330))
    quality = font.render('{}'.format(data.air_quality), True, BLACK)
    surf.blit(quality, (595, 440))

    pygame.display.update()


def close_display():
    pygame.quit()

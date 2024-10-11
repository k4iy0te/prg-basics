###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = input('Enter the km/h: ')
speed_kmh = int(speed_kmh)
speed_ms = speed_kmh * 1000 / 3600
print(speed_kmh, "km/h = ", speed_ms, "m/s")
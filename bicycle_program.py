# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This main program will create a bicycle object

from bicycle import *

# create an instance of a bicycle
bike1 = Bicycle()
bike2 = Bicycle()

print(bike1.current_state())
bike1.set_cadence(120)
print('Cadence: ' + str(bike1.get_cadence()))
bike1.set_gear(4)
print('Gear: ' + str(bike1.get_gear()))
print(bike1.current_state())

print(bike2.current_state())
bike2.set_cadence(50)
print('Cadence: ' + str(bike2.get_cadence()))
bike2.set_gear(6)
print('Gear: ' + str(bike2.get_gear()))
print(bike2.current_state())

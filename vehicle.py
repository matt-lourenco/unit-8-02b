# Created on 22 Nov 2016
# Created by: Matthew Lourenco
# This is a class that defines a generic vehicle
# Edited on: 28 Nov 2016
# Fixed bug that prevents it from working in python 2.7

class Vehicle:
    #This is a class that creates a generic vehicle
    
    def __init__(self):
        #private fields
        
        self.__license_plate_number = 'AAAA000'
        self.__colour = 'white'
        self.__number_of_doors = 4
        self.__speed = 0
        self.__maximum_speed = 200
        self.__minimum_speed = -30
        self.__number_of_wheels = 4
        self.__number_of_tires = 4
    
    # properties
    
    def get_license_plate_number(self):
        #get the license plate number property
        return self.__license_plate_number
    
    def set_license_plate_number(self, new_license_plate_number):
        #set the license plate number property
        self.__license_plate_number = new_license_plate_number
    
    def get_colour(self):
        #get the colour property
        return self.__colour
    
    def set_colour(self, new_colour):
        #set the colour property
        self.__colour = new_colour
    
    def get_number_of_doors(self):
        #get the number of doors property
        return self.__number_of_doors
    
    def get_speed(self):
        #get the speed property
        return self.__speed
    
    def get_maximum_speed(self):
        #get the maximum speed property
        return self.__maximum_speed
    
    def get_minimum_speed(self):
        #get the minimum speed property
        return self.__minimum_speed
    
    def get_number_of_wheels(self):
        #get the number of wheels
        return self.__number_of_wheels
    
    def get_number_of_tires(self):
        #get the number of tires
        return self.__number_of_tires
    #public methods
    def accelerate(self, speed_increase):
        #increases the speed
        
        #if speed is less than max speed increase speed but do not increase over max speed
        if self.__speed < self.__maximum_speed:
            self.__speed = self.__speed + speed_increase
            if self.__speed > self.__maximum_speed:
                self.__speed = self.__maximum_speed
        else:
            print('Can not increase speed past maximum speed.')
    
    def brake(self, speed_decrease):
        #decreases the speed
        
        #if speed is greater than min speed decrease speed but do not decrease below min speed
        if self.__speed > self.__minimum_speed:
            self.__speed = self.__speed - speed_decrease
            if self.__speed < self.__minimum_speed:
                self.__speed = self.__minimum_speed
        else:
            print('Can not decrease speed below maximum reverse speed.')

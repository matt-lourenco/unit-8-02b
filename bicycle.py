# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This class is used to define a bicycle object
# Edited by: Matthew Lourenco
# Edited to make the properties visible and some changeable

class Bicycle:
    # this class defines a bicycle

    # class variable shared by all instances
            

    def __init__(self):
        # private fields

        self.__cadence = 0
        self.__speed = 0
        self.__gear = 1

        # public properties
        self.some_property = None
    
    # properties
    def get_cadence(self):
        #get the cadence property
        return self.__cadence
    
    def set_cadence(self, new_cadence):
        #set the cadence property
        self.__cadence = new_cadence
    
    def get_speed(self):
        #get the speed property
        return self.__speed
    
    def get_gear(self):
        #get the gear property
        return self.__gear
    
    def set_gear(self, new_gear):
        #set the gear property
        self.__gear = new_gear
    
    # public methods
    def speed_up(self, speed_increase):
        #increase the current speed by value passed in

        self.__speed = self.__speed + speed_increase

    def apply_brakes(self, speed_decrease):
        # decrease the current speed by value passed in
        
        self.__speed = self.__speed - speed_decrease

    def current_state(self):
        # returns the current state of the bicycle as a string 
        
        # this varaible is local to this method
        return_string = 'Cadence: ' + str(self.__cadence) + ' Speed: ' + str(self.__speed) + ' Gear: ' + str(self.__gear)
        
        return return_string           

import abc
import time

class Rover(abc.ABC):
	def __init__(self, _x, _y, maxx, maxy, charge): 
		#puts the rover at initial location if free else throws exception, sets the max charge capacity
		#Create and set the variables needed for the class
		if _x < 0 or _x > maxx : raise Exception("Invalid initial x coordinates")
		if _y < 0 or _y > maxy : raise Exception("Invalid initial y coordinates")
		self.ttc = charge
		self.x = _x
		self.y = _y
		self.maxx = maxx 
		self.maxy = maxy
		self.isactive = True
		self.trip_distance = 0
		self.total_distance = 0
		self.charge_left = self.ttc // 5

	@abc.abstractmethod
	def navigate(self, inp):
		#function that helps to navigate the rover, will be overriden by derived classes
		pass
		
	def get_id(self):
		#function which returns the rover id which is an integer
		pass
		
	def get_charge_left(self):
		#returns how much distance units rover can travel
		pass
		
	def trip_distance(self):
		#returns the latest trip distance that was travelled
		pass
		
	def total_distance(self):
		#totally how many units covered by the rover - radial in case of drone
		pass

	def charge_rover(self):
	#takes n seconds to solar charge which gives capacity to travel n//5 units, e.g. 10 secs of charge gives 2 units of travel
	#This n value is the charging capacity that gets specified in the constructor
		pass
		
	def get_location(self):
		#gets current location coordinates
		pass
		
	def is_active(self):
		#True (if charge available) /False (if no charge or is on charge)
		pass

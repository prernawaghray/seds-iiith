import MarsLand
import time

plateau = MarsLand.MarsLand(10,10,6,5)
plateau.addMarsRover(2,3,15)  #adds a land rover with id say, 1001 at 2,3 with charge capacity of 15 seconds
try:
    plateau.addMarsRover(2,3,100) #should throw error since already rover present in same coordinates
except Exception as e:
    print(e)
plateau.addMarsRover(4,4,100) #adds a land rover with id say 1002 at 4,4 with charge capacity of 100 seconds
try:
    plateau.addMarsDrone(2,3,100) #should throw error since already rover present in same coordinates
except Exception as e:
    print(e)
plateau.addMarsDrone(5,5,70)  #adds a land rover with id say 2001 at 5,5 with charge capacity of 70 seconds
plateau.showMap()
id1 = list(plateau.land_rover.keys())[0] #change the index value accordingly to access land_rovers
try :
    plateau.land_rover[id1].navigate("rrF",plateau.taken_coords) #Moves from 2,3 to 3,3 to 4,3 and returns Failure since 4,4 is already occupied
except Exception as e:
    print(e)
plateau.showMap()
print(plateau.land_rover[id1].get_location()) #returns 4,3 since that was the last place of rover 1001
print(plateau.land_rover[id1].get_charge_left()) #returns 1 since 2 units rover has moved
try:
    plateau.land_rover[id1].navigate("$",plateau.taken_coords) #Throws exception since $ is not from navigation options : L/l, R/r, B/b, F/f
except Exception as e:
    print(e)
plateau.land_rover[id1].navigate("B",plateau.taken_coords) #Moves from 4,3 to 4,2
print(plateau.land_rover[id1].get_charge_left()) #returns 0 since 1 unit the rover has moved
plateau.land_rover[id1].charge_rover() #suspends this rover functionality for 15 seconds to charge up
print(plateau.land_rover[id1].is_active()) #False
time.sleep(15)
print(plateau.land_rover[id1].is_active()) #True
id2 = list(plateau.drones.keys())[0]

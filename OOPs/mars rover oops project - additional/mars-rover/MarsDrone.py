from Rover import Rover
class MarsDrone(Rover):
    def navigate(self, dest_x, dest_y):
        #flys to the location/nearest coordinate specified.
        # Nearest here means any empty spot in the 3/5/8 directions around the destination coordinates
        # in case no coordinate is free it returns failure. Works only when charge is available on the rover
        # gives update about the charging needed.
        dist = ((self.x - dest_x)*(self.x - dest_x) + (self.y - dest_y)*(self.x - dest_x))**0.5
        dist = int(dist)
        if dist > self.get_charge_left() : raise Exception('No charge left on the rover')
        self.x, self.y = dest_x, dest_y
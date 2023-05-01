import MarsRover
import MarsDrone

class Point:
    def __init__(self):
        #class meant to create points in 2D plane
        self.is_occupied = '_' #indicates that the point is empty, can be later set to 'L' or 'D'
        self.rover = None #can be set to Land or Drone object id upon adding the rover to this location
    
class MarsLand:
    def __init__(self,rows,columns, max_landrovers, max_drones):
        #sets up the 2D plane of rows x columns Points and puts a cap on each of the rover
        if rows <= 0 or columns <= 0 : raise Exception("Invalid rows and/or columns value")
        if max_drones < 0 or max_landrovers < 0 : raise Exception("Invalid count of rovers")
        if max_landrovers > rows * columns : raise Exception("Cannot have more rovers than number of coordinates")
        if max_drones > rows * columns : raise Exception("Cannot have more rovers than number of coordinates")
        if (max_landrovers + max_drones) > rows * columns : raise Exception("Cannot have more rovers than number of coordinates")
        self.points = [[Point() for _ in range(columns)] for _ in range(rows)] #creates a list of list of points
        self.land_rover = {} #stores the dictionary of id:land_rover created
        self.drones = {} #stores the dictionary of id:drones created
        self.taken_coords = []
        self.rows = rows
        self.columns = columns
        self.max_drones = max_drones
        self.max_landrovers = max_landrovers
		
    def addMarsRover(self, _x, _y, c):
        #adds a land rover at the given coordinates, throws exception if cap is reached
        if self.max_landrovers == 0 : raise Exception('Total land rover quota reached')
        if _x > self.rows or _y > self.columns : raise Exception('coordinates are beyond range')
        if self.points[_x][_y].is_occupied != '_' : raise Exception('Rover already present in the given location')
        self.points[_x][_y].is_occupied = 'L'
        self.points[_x][_y].rover = MarsRover.MarsRover(_x,_y, self.rows, self.columns, c)
        self.land_rover[id(self.points[_x][_y].rover)] = self.points[_x][_y].rover
        self.max_landrovers -= 1
        self.taken_coords.append((_x,_y))
	
    def addMarsDrone(self, _x, _y, c):
        #adds a drone at the given coordinates, throws exception if cap is reached
        if self.max_drones == 0 : raise Exception('Total drone quota reached')
        if _x > self.rows or _y > self.columns : raise Exception('coordinates are beyond range')
        if self.points[_x][_y].is_occupied != '_' : raise Exception('Rover already present in the given location')
        self.points[_x][_y].is_occupied = 'D'
        self.points[_x][_y].rover = MarsDrone.MarsDrone(_x,_y, self.rows, self.columns, c)
        self.drones[id(self.points[_x][_y].rover)] = self.points[_x][_y].rover
        self.max_drones -= 1
        self.taken_coords.append((_x,_y))

    def removeRover(self,_x,_y):
        #deletes the rover on the surface, updates the count of rovers accordingly
        if self.points[_x][_y].is_occupied == '_' : raise Exception('No rover at the given location')
        if self.points[_x][_y].is_occupied == 'L' :
            self.land_rover.pop(id(self.points[_x][_y].rover))
            del(self.points[_x][_y].rover)
            self.max_landrovers += 1
            self.points[_x][_y].is_occupied = '_'
            self.taken_coords.remove((_x,_y))
        if self.points[_x][_y].is_occupied == 'D' :
            self.drones.pop(id(self.points[_x][_y].rover))
            del(self.points[_x][_y].rover)
            self.max_drones += 1
            self.points[_x][_y].is_occupied = '_'
            self.taken_coords.remove((_x,_y))
    
    def find_nearest(self,x,y):
        if x-1 >=0 and self.points[x-1][y].is_occupied == '_': return (x-1,y)
        elif x+1 < self.rows and self.points[x+1][y].is_occupied == '_': return (x+1,y)
        elif y-1 >=0 and self.points[x][y-1].is_occupied == '_': return (x,y-1)
        elif y+1 >=self.columns and self.points[x][y+1].is_occupied == '_': return (x,y+1)
        elif x-1 >=0 and y-1>=0 and self.points[x-1][y-1].is_occupied == '_': return (x-1,y-1)
        elif x-1 >=0 and y+1 < self.columns and self.points[x+1][y].is_occupied == '_': return (x-1,y+1)
        elif y-1 >=0 and x+1 < self.rows and self.points[x][y-1].is_occupied == '_': return (x+1,y-1)
        elif y+1 < self.columns and x+1 < self.rows and self.points[x][y+1].is_occupied == '_': return (x+1,y+1)
        else: raise Exception('All nearest locations occupied')

    def showMap(self):
        #prints an ascii art of 2D plane marking L and D for land and drone rovers and X for empty space
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.points[i][j].is_occupied + ' ', end='')
            print('')
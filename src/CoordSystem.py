from graphics import *


#unused coordinate system that i might try to finish
class CoordSystem:
    def __init__(self, x, y):
        #indices match each other
        self.locations = []
        self.colors = []
        self.win = GraphWin('Evolution Simulation', 800, 800)
        self.win.setCoords(0, 0, x, y)
    
    def draw(self, coord, color):
        '''
        Inputs:
            coord([x, y]): location of draw
            color:([r, g, b]): color values for the specific location
        '''
        self.locations.append(coord)
        self.colors.append(color)

    def view(self):
        print('locations: ', self.locations)
        print('colors: ', self.colors)

    def checkUserKeyClose(self):
        #closes if user presses any key
        keyString = self.win.checkKey()
        if keyString == '':
            return False
        else:
            return True

    def close(self):
        self.win.close()


        


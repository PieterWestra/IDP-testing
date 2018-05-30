from leg import Leg


class Robot:


    def __init__(self, numlegs, legjoints):
        self.legs = [Leg(i, legjoints) for i in range(numlegs)]


    def printlegs(self):
        print( [l.servos for l in self.legs] )


    def walk(self, numsteps):
        for l in self.legs:
            l.reset()

        for _ in range(numsteps):
            for l in self.legs:
                l.step()

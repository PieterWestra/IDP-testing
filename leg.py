import sys, traceback
import time

import ax12


class Leg:


    def __init__(self, legnum, numservos):
        self.servos = [legnum*numservos+i+1 for i in range(3)]
        self.direction = legnum % 2


    def moveservo(self, servo_idx, angle, speed):
        try:
            ax12.Ax12.moveSpeed(servo_idx, angle, speed)
        except:
            print("\nCould not move Servo " + str(self.servos[servo_idx]))
            traceback.print_exc(file=sys.stdout)


    def moverelative(self, servo_idx, angle, speed):
        # move servos relative to their current rotation
        # direction decided by robot side
        side = -1 if self.servos[servo_idx] in [10, 13, 16] else 1

        current_angle = ax12.Ax12().readPosition()
        self.moveservo(servo_idx, current_angle + angle * side, speed)




# <editor-fold>
    def step(self):
        if self.direction == 1:
            self.moveservo(1, 150, 200)
            self.moveservo(2, 150, 200)
            time.sleep(0.2)

            self.moveservo(0, 550, 200)
            self.moveservo(1, 400, 200)
            self.moveservo(2, 300, 200)
            self.direction = 0
        elif self.direction == 0:
            self.moveservo(0, 150, 200)
            self.moveservo(1, 400, 200)
            self.moveservo(2, 300, 200)
            self.direction = 1
# </editor-fold>


    def reset(self):
        self.moveservo(0, 350, 200)
        self.moveservo(1, 400, 200)
        self.moveservo(2, 300, 200)

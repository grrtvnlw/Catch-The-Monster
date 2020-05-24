import pyglet
from pyglet.window import key
from . import physicalobject, resources
from . import util

from random import randint

class Goblin(physicalobject.PhysicalObject):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.goblin_image, *args, **kwargs)

        self.counter = 0
        self.change_at = randint(50,100)
        self.randomize()
        self.name = "Goblin"

    def update(self, dt):
        # Do all the normal physics stuff
        super().update(dt)
        # self.velocity_x = 0
        # self.velocity_y = 0
        self.counter += 1
        if self.counter >= self.change_at:
            self.counter = 0

            # The randomize() function alters
            # the current velocity of the monster.
            self.randomize()

    def randomize(self):
        self.velocity_x = randint(200, 300)
        self.velocity_y = randint(200, 300)
        
        # This expression means: there is a 50%
        # chance we will change our horizontal direction.
        if randint(0, 100) > 40:
            self.velocity_x *= -1
            
        # This expression means: there is a 50%
        # chance we will change our vertical direction.
        if randint(0, 100) > 40:
            self.velocity_y *= -1        

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        super().delete()

    def handle_collision_with(self, other_object):
        self.dead = False
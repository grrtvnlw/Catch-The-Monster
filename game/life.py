import pyglet
from pyglet.window import key
from . import physicalobject, resources

from random import randint

class Life(physicalobject.PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.life_image, *args, **kwargs)

        self.counter = 0
        self.change_at = randint(50,100)
        self.randomize()
        self.name = "life"

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
        self.velocity_x = randint(50, 100)
        self.velocity_y = randint(50, 100)
        
        # This expression means: there is a 50%
        # chance we will change our horizontal direction.
        if randint(0, 100) > 60:
            self.velocity_x *= -1
            
        # This expression means: there is a 50%
        # chance we will change our vertical direction.
        if randint(0, 100) > 60:
            self.velocity_y *= -1        

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        super().delete()

    def handle_collision_with(self, other_object):
        if other_object.name == "Joe":
            self.dead = True
        else:
            self.dead = False

import pyglet
from pyglet.window import key
from . import physicalobject, resources


class Player(physicalobject.PhysicalObject):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)

        # How fast can the player move?
        self.speed = 600

        # Let pyglet handle keyboard events for us
        self.key_handler = key.KeyStateHandler()

        self.name = "Joe"

        self.lives = 9

        self.score = 0

    def update(self, dt):
        # Do all the normal physics stuff
        super().update(dt)

        # When no keys are pressed, don't
        # move the player
        self.velocity_x = 0
        self.velocity_y = 0

        # When we press keys, modify the current
        # velocity of the player
        if self.key_handler[key.LEFT]:
            self.velocity_x = -self.speed
        if self.key_handler[key.RIGHT]:
            self.velocity_x = self.speed
        if self.key_handler[key.UP]:
            self.velocity_y = self.speed
        if self.key_handler[key.DOWN]:
            self.velocity_y = -self.speed

    def delete(self):
       # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        super().delete()

    def handle_collision_with(self, other_object):
        if other_object.name == "Goblin":
            self.dead = True
        elif other_object.name == "Monster":
            self.dead = False
        elif other_object.name == "life":
            self.dead = False
    
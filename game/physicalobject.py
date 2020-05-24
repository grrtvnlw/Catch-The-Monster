import pyglet
from . import util

from config import WIDTH, HEIGHT

class PhysicalObject(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # In addition to position, we have velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0

        # And a flag to remove this object from the game_object list
        self.dead = False
        self.new_objects = [] 

    def update(self, dt):
        """This method should be called every frame."""

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Wrap around the screen if necessary
        self.check_bounds()

    def check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior"""
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = WIDTH + self.image.width / 2
        max_y = HEIGHT + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        if self.y < min_y:
            self.y = max_y
        if self.x > max_x:
            self.x = min_x
        if self.y > max_y:
            self.y = min_y

    def collides_with(self, other_object):
        """Determine if this object collides with another"""

        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        collision_distance = self.image.width / 1.5 + other_object.image.width / 1.5

        # Get distance using position tuples
        actual_distance = util.distance(self.position, other_object.position)

        return (actual_distance <= collision_distance)


from pyglet.event import EventDispatcher

from classes.Module import Module


class Collider(Module):
    def __init__(self):
        self.dispatcher = EventDispatcher()
        self.collisions_list

    def on_collision(self):
        pass


from pyglet.event import EventDispatcher

from classes.Module import Module


class CollisionManager(Module):
    def update(self, dt):
        colliders = [obj.find_modules("ColliderGroup") for obj in self.object.group.game.objects]


class ColliderGroup(Module):
    def __init__(self, g_object, *args, **kwargs):
        super().__init__(g_object, *args, **kwargs)
        self.group = []


class Collider(Module):
    def __init__(self, g_object, *args, **kwargs):
        super().__init__(g_object, *args, **kwargs)
        self.dispatcher = EventDispatcher()
        self.collisions_list = {}

    def collision_check(self, other):
        pass
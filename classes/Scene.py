from pyglet.math import Vec2


class SceneObject:
    def __init__(self):
        self.


class Scene:
    def __init__(self, resources: str = "../base_resources"):
        self.objects = []
        self.batches = {}
        self.global_params = {"camera_pos": Vec2}

    def add_global(self, key: str, value):
        if key in self.global_params.keys:
            return False
        else:
            self.global_params[key] = value

    def add_object(self):
        pass

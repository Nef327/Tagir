import pyglet as pg
from pyglet.math import Mat4


class Game:
    def __init__(self, resources: str = "../base_resources"):
        pg.resource.location = [resources]
        self.window = pg.window.Window()
        self.camera_pos = pg.math.Vec3(self.window.view[0], self.window.view[5], self.window.view[10])
        self.scale: int = 1

        self.objects = []
        self.batches = {}
        self.global_params = {}

        @self.window.event
        def on_draw():
            self.window.clear()
            for batch in self.batches.values():
                batch: pg.graphics.Batch
                batch.draw()

    def add_object(self, object: pg.sprite.Sprite):
        self.objects.append((object))

    def get_batches(self):
        return tuple(self.batches.keys())

    def get_batch(self, batch_name):
        return self.batches[batch_name]

    def add_batch(self, batch: pg.graphics.Batch, batch_name: str):
        if batch_name not in self.batches.keys():
            self.batches[batch_name] = batch;
        else:
            print(f"DEBUG: Batch with name: {batch_name} already exists.")

    def change_camera_pos(self, x: float = 0, y: float = 0, z: float = 0):
        self.camera_pos += pg.math.Vec3(x, y, z)
        self.window.view += self.window.view.translate(pg.math.Vec3(x, y, z))

    def set_camera_pos(self, x: float = 0, y: float = 0, z: float = 0):
        self.camera_pos = pg.math.Vec3(x, y, z)
        self.window.view = self.window.view.translate(pg.math.Vec3(x, y, z))

    def add_scale(self, n):
        self.scale *= n
        self.window.view = self.window.view.scale(n)

    def set_scale(self, n):
        self.window.view = self.window.view.scale(1 / self.scale)
        self.scale = n

    def scale_to_default(self):
        self.window.view = self.window.view.scale(1 / self.scale)
        self.scale = 1







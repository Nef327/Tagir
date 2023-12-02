import pyglet as pg
from classes.CameraGroup import CenteredCameraGroup


class Game:
    def __init__(self, resources: str = "../base_resources"):
        pg.resource.path = [resources]
        self.window = pg.window.Window()

        self.camera = CenteredCameraGroup(self.window, self, 0, 0)

        self.objects = []
        self.batches = {}
        self.global_params = {}

        @self.window.event
        def on_draw():
            self.window.clear()
            for batch in self.batches.values():
                batch: pg.graphics.Batch
                batch.draw()

    def add_object(self, object: pg.sprite.Sprite, camera=None):
        if camera is None:
            camera = self.camera
        object.group = camera
        self.objects.append(object)

    def get_batches(self):
        return tuple(self.batches.keys())

    def get_batch(self, batch_name):
        return self.batches[batch_name]

    def add_batch(self, batch: pg.graphics.Batch, batch_name: str):
        if batch_name not in self.batches.keys():
            self.batches[batch_name] = batch
        else:
            print(f"DEBUG: Batch with name: {batch_name} already exists.")

    def change_camera_pos(self, x: float = 0, y: float = 0):
        self.camera.position += pg.math.Vec2(x, y)

    def set_camera_pos(self, x: float = 0, y: float = 0, z: float = 0):
        self.camera.position = pg.math.Vec2(x, y)

    def add_scale(self, n):
        self.camera.zoom += n

    def multiply_scale(self, n):
        self.camera.zoom *= n

    def set_scale(self, n):
        self.camera.zoom = n

    def scale_to_default(self):
        self.camera.zoom = 1

    def update(self, dt: float):
        for object in self.objects:
            object.update_modules(dt)
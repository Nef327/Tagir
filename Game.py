import pyglet as pg


class Game:
    def __init__(self):
        self.window = pg.window.Window()
        self.camera_pos = pg.math.Vec3(self.window.view[0], self.window.view[5], self.window.view[10])
        self.camera_scale = pg.math.Vec3(self.window.view[0], self.window.view[5], self.window.view[10])

        self.objects = []
        self.global_params = {}

    def change_camera_pos(self, x: float, y: float, z: float):
        self.window.view.translate(pg.math.Vec3(x, y, z))


    def change_

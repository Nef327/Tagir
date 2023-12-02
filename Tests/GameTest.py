import pyglet as pg
from pyglet.window import key
from classes.Game import Game

game = Game()
da_batch = pg.graphics.Batch()
game.add_batch(da_batch, "foreground")
game.add_object(pg.sprite.Sprite(pg.resource.image("images/circle.png"), 0, 0, batch=da_batch))
game.add_object(pg.sprite.Sprite(pg.resource.image("images/circle.png"), 1200, 0, batch=da_batch))

scrolling_speed: float = 2000
keys = pg.window.key.KeyStateHandler()
game.window.push_handlers(keys)


def update(delta):
    if keys[key.UP]:
        game.change_camera_pos(0, scrolling_speed * delta)
    if keys[key.DOWN]:
        game.change_camera_pos(0, -scrolling_speed * delta)
    if keys[key.RIGHT]:
        game.change_camera_pos(scrolling_speed * delta)
    if keys[key.LEFT]:
        game.change_camera_pos(-scrolling_speed * delta)
    if keys[key.SPACE]:
        game.set_camera_pos()


@game.window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    scroll_y /= 1.2
    if scroll_y < 0:
        scroll_y = 1 / abs(scroll_y)
    game.multiply_scale(scroll_y)
    if game.camera.zoom < 0.1:
        game.set_scale(0.1)


pg.clock.schedule_interval(update, 1 / 60)
# k = Mat4((0.5, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0.5, 0, *(0, 0, 0), 1))
# print(k @ Mat4((1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, *(100, 100, 100), 1)))
pg.app.run(interval=1/60)

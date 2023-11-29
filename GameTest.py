import pyglet as pg
from pyglet.window import key
from Game import Game
from pyglet.math import Mat4

game = Game()
da_batch = pg.graphics.Batch()
game.add_batch(da_batch, "foreground")
game.add_object(pg.sprite.Sprite(pg.resource.image("images/circle.png"), 0, 0, batch=da_batch))
game.add_object(pg.sprite.Sprite(pg.resource.image("images/circle.png"), 1200, 0, batch=da_batch))

scrolling_speed: float = -400
keys = pg.window.key.KeyStateHandler()
game.window.push_handlers(keys)


def update(delta):
    if keys[key.UP]:
        game.change_camera_pos(0, scrolling_speed * delta, 0)
    if keys[key.DOWN]:
        game.change_camera_pos(0, -scrolling_speed * delta, 0)
    if keys[key.RIGHT]:
        game.change_camera_pos(scrolling_speed * delta)
    if keys[key.LEFT]:
        game.change_camera_pos(-scrolling_speed * delta)
    if keys[key.SPACE]:
        game.set_camera_pos()


@game.window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    delta_scale = game.scale
    scroll_y /= 1.2
    if scroll_y < 0:
        scroll_y = 1 / abs(scroll_y)
    game.multiply_scale(scroll_y)
    if game.scale < 0.1:
        game.set_scale(0.1)
    delta_scale -= game.scale
    width, height = game.window.width, game.window.height
    w_point = (0, 0)
    w_point = (w_point[0] + x / width, w_point[1] + y / height)
    game.change_camera_pos(width * delta_scale * w_point[0], height * delta_scale * w_point[1])
    print(game.camera_pos)
    print(game.window.view)


pg.clock.schedule_interval(update, 1 / 60)
# k = Mat4((0.5, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0.5, 0, *(0, 0, 0), 1))
# print(k @ Mat4((1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, *(100, 100, 100), 1)))
pg.app.run(interval=1/60)

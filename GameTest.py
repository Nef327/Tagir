import pyglet as pg
from Game import Game


game = Game()
da_batch = pg.graphics.Batch()
game.add_batch(da_batch, "foreground")
game.add_object(pg.sprite.Sprite(pg.resource.image("/images/circle.png"), 400, 300, batch=da_batch))
pg.app.run()



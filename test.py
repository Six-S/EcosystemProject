import pyglet

import random
#*args is super dope

window = pyglet.window.Window()

class Enviornment():

    def __init__(self):
        print ('[INFO] Building enviornment.')
        self.set_water()

    def set_water(self):
        nums = []

        for x in range(8):
            nums.append(random.randint(50, 250))

        return pyglet.graphics.vertex_list(4,
            ('v2i', (nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7])),
            ('c3B', (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255)))


# quad = pyglet.graphics.vertex_list(4,
#             ('v2i', (10, 10, 30, 10, 30, 30, 10, 30)),
#             ('c3B', (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255)))


# ---------------------> EVENT LISTENERS <------------------------ #


if __name__ in '__main__':

    e = Enviornment()
    speed = 10
    square = quad = pyglet.graphics.vertex_list(4,
            ('v2i', (10, 10, 30, 10, 30, 30, 10, 30)),
            ('c3B', (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)))

    @window.event
    def on_draw():
        window.clear()

        print ('!!!!!!!!!!!!')

        quad = e.set_water()
        quad.draw(pyglet.gl.GL_QUADS)

    @window.event
    def on_key_press(symbol, modifiers):

        if symbol == pyglet.window.key.Q:
            print ('[INFO] Exiting enviornment. Goodbye.')
            exit(0)
        elif

    pyglet.app.run()
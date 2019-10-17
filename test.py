import pyglet

#*args is super dope

window = pyglet.window.Window()

env = pyglet.graphics.Batch()

quad = pyglet.graphics.vertex_list(4,
    ('v2i', (10, 10, 30, 10, 30, 30, 10, 30)),
    ('c3B', (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255)))

@window.event
def on_draw():
    window.clear()
    quad.draw(pyglet.gl.GL_QUADS)

if __name__ == "__main__":
    pyglet.app.run()


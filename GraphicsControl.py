import pyglet

window = pyglet.window.Window()

header = pyglet.text.Label('EcoSystem',
                        font_name='Times New Roman',
                        font_size=20,
                        x=300, y=450,
                        anchor_x='center', anchor_y='center')

label = pyglet.text.Label('Hello world',
                        font_name='Times New Roman',
                        font_size=12,
                        x=550, y=25,
                        anchor_x='center', anchor_y='center')

@window.event
def on_key_press(symbol, modifiers):
    print 'we out here.', symbol

@window.event
def on_draw():
    window.clear()
    label.draw()
    header.draw()

pyglet.app.run()
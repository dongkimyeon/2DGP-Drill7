from pico2d import *
import random


class Grass:
    pass
class Boy:
    pass
class Zombie:
    pass
class Ball:
    pass

def reset_world():
    global running
    running = True

def update_world():
    pass

def render_world():
    pass

def handle_events():
    pass



open_canvas()
reset_world()

# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code
close_canvas()



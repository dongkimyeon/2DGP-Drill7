from pico2d import *
import random


gameobjs = []
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    pass
class Zombie:
    def __init__(self):
        self.x, self.y = 100, 300
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_hight = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_hight, self.x, self.y)

class Ball:
    pass

def reset_world():
    global running
    global gameobjs
    running = True
    newGrass = Grass()
    gameobjs.append(newGrass)

    newZombie = Zombie()
    gameobjs.append(newZombie)

    team = [Boy() for i in range(10)]
    gameobjs += team


def update_world():
    for obj in gameobjs:
        obj.update()


def render_world():
    clear_canvas()
    for obj in gameobjs:
        obj.draw()
    update_canvas()

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



import math
import random
import arcade


WIDTH = 1280
HEIGHT = 700
a_press = False
d_press = False
w_press = False
s_press = False
x = 300
y = 200
zombie_x = []
zombie_y = []

for zombie in range(10):
    x1 = random.randrange(0 - 100, 0)
    y1 = random.randrange(0, HEIGHT - 70)
    zombie_x.append(x1)
    zombie_y.append(y1)


def update(delta_time):
    global a_press
    global d_press
    global w_press
    global s_press
    global y
    global x
    global x1
    global y1
    if w_press is True:
        y += 3
    if s_press is True:
        y -= 3

    if a_press is True:
        x -= 3

    if d_press is True:
        x += 3

    for bullet in bullet_list:
        bullet[0] -= 15
        bullet[1] += 0

    x1 += 3
    y1 += 0




def on_draw():
    arcade.start_render()
    global x
    global y
    global x1
    global y1
    arcade.draw_xywh_rectangle_filled(x-15, y+40, 30, 5, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x, y, 30, 60, arcade.color.YELLOW)
    arcade.draw_circle_filled(x+14, y+80, 20, arcade.color.YELLOW)

    for bullet in bullet_list:
        arcade.draw_circle_filled(bullet[0]-15, bullet[1]+40, 3, arcade.color.BLACK)

    for zombie in range(10):
        arcade.draw_xywh_rectangle_filled(x1, y1, 30, 60, arcade.color.YELLOW)
        arcade.draw_circle_filled(x1 + 14, y1 + 80, 20, arcade.color.YELLOW)


def on_key_press(key, modifiers):
    global y
    global x
    global w_press
    global s_press
    global d_press
    global a_press
    if key == arcade.key.W:
        w_press = True

    if key == arcade.key.S:
        s_press = True

    if key == arcade.key.A:
        a_press = True

    if key == arcade.key.D:
        d_press = True

    if key == arcade.key.SPACE:
        bullet_list.append([x,y])


def on_key_release(key, modifiers):
    global w_press
    global s_press
    global a_press
    global d_press
    if key == arcade.key.W:
        w_press = False

    if key == arcade.key.S:
        s_press = False

    if key == arcade.key.A:
        a_press = False

    if key == arcade.key.D:
        d_press = False

def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60 )

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    global bullet_list
    bullet_list = []

    global zombie_list
    zombie_list = []
    arcade.run()


if __name__ == '__main__':
    setup()
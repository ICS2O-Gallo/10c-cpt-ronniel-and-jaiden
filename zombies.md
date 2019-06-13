import arcade
import random


WIDTH = 640
HEIGHT = 480


zombie_x = [0-10]
zombie_y = [0]

zombie_1 = [zombie_x[0], zombie_y[0], 50, 30, arcade.color.GREEN]

def update(delta_time):
    global i

    for i in range(len(zombie_x)):
        zombie_x[i] += 10

    if zombie_x[i] <= 0:
        zombie_y[0] = random.randrange(0, HEIGHT)






def on_draw():
    arcade.start_render()

    draw_zombie(zombie_x[0], zombie_y[0])
    draw_zombie(zombie_x[0], zombie_y[0])



def on_key_press(key, modifiers):
    pass



def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass

def draw_zombie(x, y, zombie):
    arcade.draw_rectangle_filled(x, y, 30, 60, arcade.color.YELLOW)
    arcade.draw_circle_filled(x, y + 50, 20, arcade.color.YELLOW)


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()








if __name__ == '__main__':
    setup()

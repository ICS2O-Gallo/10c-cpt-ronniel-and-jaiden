import arcade
import random


WIDTH = 640
HEIGHT = 480


zom_x = 0
zom_y = 1
zom_width = 2
zom_height = 3
zom_color = 4

zombie_1 = [100, 100, 30, 50, arcade.color.GREEN]

def update(delta_time):
    pass






def on_draw():
    arcade.start_render()
    draw_zombie(zombie_1)




def on_key_press(key, modifiers):
    pass



def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass

def draw_zombie(zombie):
    arcade.draw_rectangle_filled(zombie[zom_x],
                                 zombie[zom_y],
                                 zombie[zom_width],
                                 zombie[zom_height],
                                 zombie[zom_color])


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
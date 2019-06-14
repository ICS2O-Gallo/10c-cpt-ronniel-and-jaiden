import arcade
import random


WIDTH = 640
HEIGHT = 480


zom_x = 0
zom_y = 1
zom_width = 2
zom_height = 3
zom_color_body = 4

i = random.randrange(30, HEIGHT-30)



zombie_1_body = [, i, 30, 50, arcade.color.GREEN]
zombie_1_head = [zombie_1_body[0], zombie_1_body[1] + 36, 20, 20, arcade.color.GREEN]

zombie_2_body = [rand, i, 30, 50, arcade.color.GREEN]
zombie_2_head = [zombie_2_body[0], zombie_2_body[1] + 36, 20, 20, arcade.color.GREEN]

zombie_3_body = [rand, i, 30, 50, arcade.color.GREEN]
zombie_3_head = [zombie_3_body[0], zombie_3_body[1] + 36, 20, 20, arcade.color.GREEN]

zombie_4_body = [rand, i, 30, 50, arcade.color.GREEN]
zombie_4_head = [zombie_4_body[0], zombie_4_body[1] + 36, 20, 20, arcade.color.GREEN]

zombie_5_body = [rand, i, 30, 50, arcade.color.GREEN]
zombie_5_head = [zombie_5_body[0], zombie_5_body[1] + 36, 20, 20, arcade.color.GREEN]

zombie_6_body = [rand, i, 30, 50, arcade.color.GREEN]
zombie_6_head = [zombie_6_body[0], zombie_6_body[1] + 36, 20, 20, arcade.color.GREEN]



def update(delta_time):
   pass




def on_draw():
    arcade.start_render()

    draw_zombie(zombie_1_body)
    draw_zombie(zombie_1_head)

    draw_zombie(zombie_2_body)
    draw_zombie(zombie_2_head)

    draw_zombie(zombie_3_body)
    draw_zombie(zombie_3_head)

    draw_zombie(zombie_4_body)
    draw_zombie(zombie_4_head)

    draw_zombie(zombie_5_body)
    draw_zombie(zombie_5_head)

    draw_zombie(zombie_6_body)
    draw_zombie(zombie_6_head)




def on_key_press(key, modifiers):
    pass



def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass

def draw_zombie(zombie):





    # body
    arcade.draw_rectangle_filled(zombie[zom_x],
                                 zombie[zom_y],
                                 zombie[zom_width],
                                 zombie[zom_height],
                                 zombie[zom_color_body])
    # head
    arcade.draw_rectangle_filled(zombie[zom_x],
                                 zombie[zom_y],
                                 zombie[zom_width],
                                 zombie[zom_height],
                                 zombie[zom_color_body])





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

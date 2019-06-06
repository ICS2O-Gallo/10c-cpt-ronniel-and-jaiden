import arcade


WIDTH = 640
HEIGHT = 480


movement = [200]
D = False
A = False

barricade = [320, 0, 5, 960, arcade.color.WHITE_SMOKE]

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


def update(delta_time):
    global D
    global A

    if D == True:
        movement[0] += 3

    if A == True:
        movement[0] -= 3


    if movement[0] >= barricade[0]:
        movement[0] -= 3







def on_draw():
    arcade.draw_rectangle_filled(movement[0], 240, 30, 30, arcade.color.BLUE)
    arcade.draw_rectangle_filled(barricade[0], barricade[1], barricade[2], barricade[3], barricade[4])



def on_key_press(key, modifiers):
    global D
    global A

    if key == arcade.key.D:
        D = True
    if key == arcade.key.A:
        A = True

def on_key_release(key, modifiers):
    global D
    global A
    if key == arcade.key.D:
        D = False
    if key == arcade.key.A:
        A = False


def on_mouse_press(x, y, button, modifiers):
    pass








if __name__ == '__main__':
    setup()
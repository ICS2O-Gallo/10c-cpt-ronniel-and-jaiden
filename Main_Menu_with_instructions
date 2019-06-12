# 10c-cpt-ronniel-and-jaiden
10c-cpt-ronniel-and-jaiden created by GitHub Classroom

import arcade


WIDTH = 1280
HEIGHT = 700

current_screen = "menu"

BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6


button1 = [WIDTH / 4 + 135, HEIGHT / 2 + 50, 355, 50, False, arcade.color.BLACK, arcade.color.BLACK]
button2 = [WIDTH / 4 + 135, HEIGHT / 3 + 45, 360, 55, False, arcade.color.BLACK, arcade.color.BLACK]


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...

    if current_screen == "menu":

        draw_button(button1)
        draw_button(button2)

        arcade.draw_text("BIOHAZARD:", WIDTH / 4 - 100, HEIGHT - 110, arcade.color.LIGHT_GREEN, 100)
        arcade.draw_text("M-VIRUS", WIDTH / 4 + 100, HEIGHT - 200, arcade.color.LIGHT_GREEN, 75)
        arcade.draw_text("Play Game", WIDTH / 4 + 135, HEIGHT / 2 + 50, arcade.color.RED_DEVIL, 50)
        arcade.draw_text("Intructions", WIDTH / 4 + 135, HEIGHT / 3 + 50, arcade.color.RED_DEVIL, 50)
        arcade.draw_text("Quit Game", WIDTH / 4 + 135, HEIGHT / 3 - 50, arcade.color.RED_DEVIL, 50)

    elif current_screen == "instructions":
        arcade.draw_text("Instructions", WIDTH / 3 - 100, HEIGHT - 150, arcade.color.RED, 100)

        # Movement and reload
        arcade.draw_text("Movement", 180, 470, arcade.color.ORANGE, 40)
        arcade.draw_text("W", 275, 400, arcade.color.ORANGE, 40)
        arcade.draw_text("S", 285, 325, arcade.color.ORANGE, 40)
        arcade.draw_text("A", 225, 325, arcade.color.ORANGE, 40)
        arcade.draw_text("D", 340, 325, arcade.color.ORANGE, 40)
        arcade.draw_text("R", 390, 400, arcade.color.BLUE_GRAY, 40)
        arcade.draw_text("Reload", 420, 355, arcade.color.BLUE_GRAY, 30)

        # Shooting
        arcade.draw_ellipse_filled(950, 300, 150, 200, arcade.color.AERO_BLUE)
        arcade.draw_rectangle_filled(950, 360, 290, 10, arcade.color.DARK_RASPBERRY)
        arcade.draw_rectangle_filled(948, 430, 10, 140, arcade.color.DARK_RASPBERRY)
        arcade.draw_text("Shoot", 700, 480, arcade.color.AFRICAN_VIOLET, 30)
        arcade.draw_rectangle_filled(790, 450, 75, 5, arcade.color.AFRICAN_VIOLET, 140)
        arcade.draw_text("MOUSE", 914, 275, arcade.color.BLUE, 15)

        # button
        arcade.draw_text("Main Menu", 80, 75, arcade.color.RED, 50)




def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):

    if mouse_hover(x, y, button1):
        button1[BTN_IS_CLICKED] = True

    if mouse_hover(x, y, button2):
        button2[BTN_IS_CLICKED] = True


def on_mouse_release(x, y, button, modifiers):
    global current_screen

    button1[BTN_IS_CLICKED] = False
    button2[BTN_IS_CLICKED] = False

    if button2[BTN_IS_CLICKED] == False and mouse_hover(x,y, button2) == True:
        current_screen = "instructions"




def mouse_hover(x, y, button) -> bool:
    if (x > button[BTN_X] and x < button[BTN_X] + button[BTN_WIDTH] and
            y > button[BTN_Y] and y < button[BTN_Y] + button[BTN_HEIGHT]):
        return True
    else:
        return False


def draw_button(button):
    # Select the appropriate color to draw with
    if button[BTN_IS_CLICKED]:
        color = button[BTN_CLICKED_COLOR]
    else:
        color = button[BTN_COLOR]

    # Draw button1
    arcade.draw_xywh_rectangle_filled(button[BTN_X],
                                      button[BTN_Y],
                                      button[BTN_WIDTH],
                                      button[BTN_HEIGHT],
                                      color)



if __name__ == '__main__':
    setup()

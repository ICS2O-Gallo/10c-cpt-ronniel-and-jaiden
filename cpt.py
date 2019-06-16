import arcade
import sys
import random

WIDTH = 1280
HEIGHT = 700

current_screen = "menu"

# Button Map
BTN_X = 0
BTN_Y = 1
BTN_WIDTH = 2
BTN_HEIGHT = 3
BTN_IS_CLICKED = 4
BTN_COLOR = 5
BTN_CLICKED_COLOR = 6


button1 = [WIDTH / 4 + 135, HEIGHT / 2 + 50, 275, 50, False, arcade.color.BLACK, arcade.color.BLACK]
button2 = [WIDTH / 4 + 135, HEIGHT / 3 + 45, 360, 55, False, arcade.color.BLACK, arcade.color.BLACK]
button3 = [WIDTH / 4 + 135, HEIGHT / 3 - 53, 360, 55, False, arcade.color.BLACK, arcade.color.BLACK]
button4 = [85, 75, 355, 50, False, arcade.color.BLACK, arcade.color.BLACK]
button5 = [WIDTH / 4 + 135, HEIGHT / 3 - 53, 305, 55, False, arcade.color.RED_VIOLET, arcade.color.RED_DEVIL]

#             x      y     width height     color
barricade = [1000, HEIGHT/2, 10, 960, arcade.color.WHITE_SMOKE]
barricade_hp = 1



a_press = False
d_press = False
w_press = False
s_press = False

# starting point of scientist(player)
sci_x = 1100
sci_y = 200

zombie_x_1 = []
zombie_y_1 = []

zombie_x_2 = []
zombie_y_2 = []


# starting point of zombie_1
for zombie_1 in range(10):
    zom_x_1 = random.randrange(0 - 100, 0)
    zom_y_1 = random.randrange(0, HEIGHT - 70)
    zombie_x_1.append(zom_x_1)
    zombie_y_1.append(zom_y_1)

# starting point of zombie_2
for zombie_2 in range(10):
    zom_x_2 = random.randrange(0 - 100, 0)
    zom_y_2 = random.randrange(0, HEIGHT - 70)
    zombie_x_2.append(zom_x_1)
    zombie_y_2.append(zom_y_1)



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

    #bullet creation
    global bullet_list
    bullet_list = []


    arcade.run()

    arcade.run()



def update(delta_time):
    global a_press
    global d_press
    global w_press
    global s_press
    global sci_y
    global sci_x
    global zom_x_1
    global zom_y_1
    global zom_x_2
    global zom_y_2
    global barricade_hp
    global current_screen

# movement of scientist(player)
    if w_press is True:
        sci_y += 7
    if s_press is True:
        sci_y -= 7

    if a_press is True:
        sci_x -= 7

    if d_press is True:
        sci_x += 7

# bullet movement
    for bullet in bullet_list:
        bullet[0] -= 50
        bullet[1] += 0

# scientist collision
    if sci_x <= barricade[0]:
        sci_x += 5

    if sci_x + 20 >= WIDTH:
        sci_x -= 7

    elif sci_y + 50 >= HEIGHT:
        sci_y -= 7
    elif sci_y <= 0:
        sci_y += 7


    #zombie movement
    if current_screen == "Game":
        zom_x_1 += 10
        zom_y_1 += 0

    else:
        zom_x_1 += 0
        zom_y_1 += 0

    if current_screen == "Game":
        zom_x_2 += 10
        zom_y_2 += 0

    else:
        zom_x_2 += 0
        zom_y_2 += 0

    if zom_x_1 >= barricade[0] - 32:
        zom_x_1 -= 10
        barricade_hp -= 5

    #zombie collision
    if zom_x_2 >= barricade[0] - 32:
        zom_x_2 -= 10
        barricade_hp -= 1

    # game over conditions
    if barricade_hp <= 0:
        current_screen = "game_over"




def on_draw():
    arcade.start_render()
    # Draw in here...
    global current_screen,barricade_hp

    # main menu
    if current_screen == "menu":
        arcade.set_background_color(arcade.color.BLACK)
        barricade_hp = 500

        #buttons
        draw_button(button1)
        draw_button(button2)
        draw_button(button3)
        # Titile
        arcade.draw_text("BIOHAZARD:", WIDTH / 4 - 50, HEIGHT - 110, arcade.color.LIGHT_GREEN, 100)
        arcade.draw_text("M-VIRUS", WIDTH / 4 + 100, HEIGHT - 200, arcade.color.LIGHT_GREEN, 75)
        # options
        arcade.draw_text("Play Game", WIDTH / 4 + 135, HEIGHT / 2 + 50, arcade.color.RED_DEVIL, 50)
        arcade.draw_text("Intructions", WIDTH / 4 + 135, HEIGHT / 3 + 50, arcade.color.RED_DEVIL, 50)
        arcade.draw_text("Quit Game", WIDTH / 4 + 135, HEIGHT / 3 - 50, arcade.color.RED_DEVIL, 50)

    elif current_screen == "instructions":
        arcade.set_background_color(arcade.color.BLACK)
        # Title
        arcade.draw_text("Instructions", WIDTH / 3 - 100, HEIGHT - 150, arcade.color.RED, 100)

        # Movement and reload
        arcade.draw_text("Movement", 180, 470, arcade.color.ORANGE, 40)
        arcade.draw_text("W", 275, 400, arcade.color.ORANGE, 40)
        arcade.draw_text("S", 285, 325, arcade.color.ORANGE, 40)
        arcade.draw_text("A", 225, 325, arcade.color.ORANGE, 40)
        arcade.draw_text("D", 340, 325, arcade.color.ORANGE, 40)


        # Shooting
        arcade.draw_text("Shooting", 850, HEIGHT/2 + 30, arcade.color.BLUE, 40)
        arcade.draw_rectangle_filled(960, HEIGHT/2, 400, 40, arcade.color.BLUE_GRAY)
        arcade.draw_text("Space Bar", 920, HEIGHT/2 - 10, arcade.color.BLUE, 20)

        # button
        draw_button(button4)
        arcade.draw_text("Main Menu", 80, 75, arcade.color.RED, 50)

    elif current_screen == "Game":
        arcade.set_background_color(arcade.color.BLACK)
        global sci_x
        global sci_y
        global zom_x_1
        global zom_y_1
        global zom_x_2
        global zom_y_2

        # scientist
        arcade.draw_xywh_rectangle_filled(sci_x - 15, sci_y + 40, 30, 5, arcade.color.RED)
        arcade.draw_xywh_rectangle_filled(sci_x, sci_y, 30, 60, arcade.color.YELLOW)
        arcade.draw_circle_filled(sci_x + 14, sci_y + 80, 20, arcade.color.YELLOW)

        # bullets and zombie respawn location
        for bullet in bullet_list:
            arcade.draw_circle_filled(bullet[0] - 15, bullet[1] + 40, 3, arcade.color.BLUE_GRAY)
            if zom_x_1 >= bullet[0] and zom_y_1 - 40 <= bullet[1] and zom_y_1 + 50 >= bullet[1]:
                del bullet_list[0]


                zom_x_1 = 0
                zom_y_1 = random.randrange(0, HEIGHT - 70)

            if zom_x_2 >= bullet[0] and zom_y_2 - 40 <= bullet[1] and zom_y_2 + 50 >= bullet[1]:
                del bullet_list[0]

                zom_x_2 = 0
                zom_y_2 = random.randrange(0, HEIGHT - 70)

            if bullet[0] <= 0:
                del bullet_list[0]

        # zombies
        for zombie in range(10):

            arcade.draw_xywh_rectangle_filled(zom_x_1, zom_y_1, 30, 60, arcade.color.GREEN)
            arcade.draw_rectangle_filled(zom_x_1 + 14, zom_y_1 + 80, 20, 20, arcade.color.GREEN)


            arcade.draw_xywh_rectangle_filled(zom_x_2, zom_y_2, 30, 60, arcade.color.GREEN)
            arcade.draw_rectangle_filled(zom_x_2 + 14, zom_y_2 + 80, 20, 20, arcade.color.GREEN)

        # barricade
        arcade.draw_rectangle_filled(barricade[0], barricade[1], barricade[2], barricade[3], barricade[4])



    elif current_screen == "game_over":
        arcade.set_background_color(arcade.color.RED_VIOLET)
        barricade_hp = 500
        # zombie starting point when game is finished
        zom_x_1 = 0
        zom_x_2 = 0

        # button
        draw_button(button5)

        # Why player lost
        arcade.draw_text("The Zombies have Broke the Barricade", 125, HEIGHT - 100, arcade.color.RED_DEVIL, 50)

        # option
        arcade.draw_text("Main Menu", WIDTH / 4 + 135, HEIGHT / 3 - 50, arcade.color.RED_DEVIL, 50)





def on_key_press(key, modifiers):
    global sci_y
    global sci_x
    global w_press
    global s_press
    global d_press
    global a_press

    # scientist movement and shooting
    if key == arcade.key.W:
        w_press = True

    if key == arcade.key.S:
        s_press = True

    if key == arcade.key.A:
        a_press = True

    if key == arcade.key.D:
        d_press = True

    if key == arcade.key.SPACE:
        bullet_list.append([sci_x, sci_y])


def on_key_release(key, modifiers):
    global w_press
    global s_press
    global a_press
    global d_press

    # scientist not moving
    if key == arcade.key.W:
        w_press = False

    if key == arcade.key.S:
        s_press = False

    if key == arcade.key.A:
        a_press = False

    if key == arcade.key.D:
        d_press = False


def on_mouse_press(x, y, button, modifiers):

    # buttons if clicked
    if mouse_hover(x, y, button1):
        button1[BTN_IS_CLICKED] = True

    if mouse_hover(x, y, button2):
        button2[BTN_IS_CLICKED] = True

    if mouse_hover(x, y, button3):
        button2[BTN_IS_CLICKED] = True

    if mouse_hover(x, y, button4):
        button4[BTN_IS_CLICKED] = True

    if mouse_hover(x, y, button5):
        button5[BTN_IS_CLICKED] = True


def on_mouse_release(x, y, button, modifiers):
    global current_screen

    button1[BTN_IS_CLICKED] = False
    button2[BTN_IS_CLICKED] = False
    button3[BTN_IS_CLICKED] = False
    button4[BTN_IS_CLICKED] = False
    button5[BTN_IS_CLICKED] = False

    # button going into game
    if button1[BTN_IS_CLICKED] == False and mouse_hover(x, y, button1) == True and current_screen == "menu":
        current_screen = "Game"

    # button going into instructions
    if button2[BTN_IS_CLICKED] == False and mouse_hover(x, y, button2) == True and current_screen == "menu":
        current_screen = "instructions"

    # button quiting game
    if button3[BTN_IS_CLICKED] == False and mouse_hover(x, y, button3) == True and current_screen == "menu":
        sys.exit()

    # button going from instructions to main menu
    if button4[BTN_IS_CLICKED] == False and mouse_hover(x, y, button4) == True and current_screen == "instructions":
        current_screen = "menu"

    # button going from game over screen to menu
    if button5[BTN_IS_CLICKED] == False and mouse_hover(x, y, button5) == True and current_screen == "game_over":
        current_screen = "menu"






# if mouse is over button or not
def mouse_hover(x, y, button) -> bool:
    if (x > button[BTN_X] and x < button[BTN_X] + button[BTN_WIDTH] and
            y > button[BTN_Y] and y < button[BTN_Y] + button[BTN_HEIGHT]):
        return True
    else:
        return False

# function for drawing buttons
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

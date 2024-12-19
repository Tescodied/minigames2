import pygame
import os
pygame.init()

W, H = 1000, 1000

win = pygame.display.set_mode((W, H))
pygame.display.set_caption("New original game")

def find_file_path(name):
    print(f"Full path : {os.path.abspath(name)}")


path = find_file_path("Road- sky and clouds horizontal 1.png")

def make_image(file_name, width, height):
    return pygame.transform.scale(pygame.image.load(f"{path}{file_name}").convert_alpha(), (width , height))

bg1 = make_image("Road- sky and clouds horizontal 1.png", W, H)
bg2 = make_image("Road- sky and clouds horizontal 2.png", W, H)
loading_bg = make_image("loading screen background.png", W, H)

curser = make_image("curser.png", 50, 50)

#pygame.transform.scale(pygame.image.load(f"{path}Road- sky and clouds horizontal 1.png"), (W , H)) 
#bg2 = pygame.transform.scale(pygame.image.load(f"{path}Road- sky and clouds horizontal 2.png"), (W , H))

mc_width, mc_height = 200, 200
mc = pygame.transform.scale(
    pygame.image.load(f"{path}main character.png").convert_alpha(), (mc_width, mc_height))

top_road, bot_road = H // 2.55 , H - H // 15

def start():
    clock = pygame.time.Clock()
    running = True
    pygame.mouse.set_visible(False)

    button_width, button_height = 300, 200 
    play_button = make_image("play button.png", button_width, button_height)
    outline = pygame.mask.from_surface(play_button)

    def check_hovering_button(mousex, mousey):
         return (buttonx <= mousex <= buttonx + button_width and buttony <= mousey <= buttony + button_height)

    while running:
        clock.tick(60)

        win.blit(loading_bg, (0,0))
        buttonx, buttony = W // 2 - play_button.get_width() // 2, H // 1.5 - play_button.get_height() / 2
        win.blit(play_button, (buttonx, buttony))

        mousex, mousey = pygame.mouse.get_pos()
        hovering = check_hovering_button(mousex, mousey)

        button_change = 1
        if hovering:
            button_change = 1.1
            
        play_button = pygame.transform.scale(play_button, (button_width * button_change, button_height * button_change))

        win.blit(curser, (mousex, mousey))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and hovering:
                running = False
                break


def main():
    running = True

    bg1_xcor, bg2_xcor = 0, W
    bg_speed = 5

    player_speed = 7
    player_x = W // 50
    player_y = (bot_road + top_road) // 2

    clock = pygame.time.Clock()

    start()

    while running:
        clock.tick(60)
        
        #BG
        if bg1_xcor < -W:
            bg1_xcor = W
        if bg2_xcor < -W:
            bg2_xcor = W

        bg1_xcor -= bg_speed
        bg2_xcor -= bg_speed
        
        win.blit(bg1, (bg1_xcor, 0))
        win.blit(bg2, (bg2_xcor, 0))

        #
        win.blit(mc, (player_x, player_y))

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] and player_y > top_road - mc_height:
            player_y -= player_speed
        if keys_pressed[pygame.K_DOWN] and player_y < bot_road - mc_height:
            player_y += player_speed

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()
    quit("Thanks for playing")
    

if __name__ == "__main__":
    main()

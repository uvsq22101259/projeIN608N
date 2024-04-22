import pygame
import sys
import abalone
import abalone_IA
import toolbox
import shared_data as sd

button_image = pygame.image.load("rouecrantee.png")
button_image = pygame.transform.scale(button_image, (150, 150))

# Permet de chnager la couleur de l'image
var = pygame.PixelArray(button_image)
var.replace((0, 0, 0), (255, 255, 255))
del var


def main_menu(SCREEN, BG):
    pygame.display.set_caption('Main Menu')

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = toolbox.get_font(
            sd.FONT_SIZE*2.2).render('Main Menu', 1, (255, 255, 255))
        MENU_RECT = MENU_TEXT.get_rect(
            center=(sd.WINDOW_SIZE[0]//2, sd.WINDOW_SIZE[1]//7.2))

        PLAY_Button = toolbox.Button(image=None, pos=(sd.WINDOW_SIZE[0]//2, sd.WINDOW_SIZE[1]//2.4), text_input="PLAY", font=toolbox.get_font(
            sd.FONT_SIZE*1.7), base_color="#d7fcd4", hovering_color="Green")

        Option_Button = toolbox.Button(image=button_image, pos=(sd.WINDOW_SIZE[0]//1.08, sd.WINDOW_SIZE[1]//1.16), text_input="", font=toolbox.get_font(
            sd.FONT_SIZE*1.7), base_color="#d7fcd4", hovering_color="Green")

        QUIT_Button = toolbox.Button(image=None, pos=(sd.WINDOW_SIZE[0]//2, sd.WINDOW_SIZE[1]//1.44), text_input="QUIT", font=toolbox.get_font(
            sd.FONT_SIZE*1.7), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for Button in [PLAY_Button, QUIT_Button, Option_Button]:
            Button.changeColor(MENU_MOUSE_POS)
            Button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_Button.checkForInput(MENU_MOUSE_POS):
                    play(SCREEN, BG)
                if Option_Button.checkForInput(MENU_MOUSE_POS):
                    option(SCREEN, BG)
                if QUIT_Button.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def option(SCREEN, BG):
    pygame.display.set_caption('Option')

    while True:
        OPTION_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTION_TEXT = toolbox.get_font(sd.FONT_SIZE).render(
            "Option", True, "White")
        OPTION_RECT = OPTION_TEXT.get_rect(
            center=(sd.WINDOW_SIZE[0]//2, sd.WINDOW_SIZE[1]//2.7))
        SCREEN.blit(OPTION_TEXT, OPTION_RECT)

        OPTION_BACK = toolbox.Button(image=None, pos=(sd.WINDOW_SIZE[0]//2, sd.WINDOW_SIZE[1]//1.5), text_input="BACK", font=toolbox.get_font(
            sd.FONT_SIZE), base_color="White", hovering_color="Green")

        OPTION_BACK.changeColor(OPTION_MOUSE_POS)
        OPTION_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTION_BACK.checkForInput(OPTION_MOUSE_POS):
                    main_menu(SCREEN, BG)

        pygame.display.update()


def play(SCREEN, BG):
    pygame.display.set_caption('Play')

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = toolbox.get_font(sd.FONT_SIZE).render(
            "Choose a gamemode :", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(
            center=(sd.WINDOW_SIZE[0]//2, sd.WINDOW_SIZE[1]//2.7))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        GAME_BUTTON = toolbox.Button(image=None, pos=(sd.WINDOW_SIZE[0]//3, sd.WINDOW_SIZE[1]//2), text_input="1 vs 1", font=toolbox.get_font(
            sd.FONT_SIZE), base_color="WHITE", hovering_color="Green")

        AI_GAME_BUTTON = toolbox.Button(image=None, pos=(sd.WINDOW_SIZE[0]//1.5, sd.WINDOW_SIZE[1]//2), text_input="1 vs AI", font=toolbox.get_font(
            sd.FONT_SIZE), base_color="WHITE", hovering_color="Green")

        PLAY_BACK = toolbox.Button(image=None, pos=(sd.WINDOW_SIZE[0]//2, sd.WINDOW_SIZE[1]//1.5), text_input="BACK", font=toolbox.get_font(
            sd.FONT_SIZE), base_color="White", hovering_color="Green")

        GAME_BUTTON.changeColor(PLAY_MOUSE_POS)
        GAME_BUTTON.update(SCREEN)

        AI_GAME_BUTTON.changeColor(PLAY_MOUSE_POS)
        AI_GAME_BUTTON.update(SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    abalone.game(SCREEN)
                if AI_GAME_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    abalone_IA.game_IA(SCREEN)
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu(SCREEN, BG)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode(sd.WINDOW_SIZE)
    BG = pygame.image.load('bg.png')
    pygame.display.set_caption('Game')
    main_menu(SCREEN, BG)

import pygame
import utils
import images
from constants import ILLUSIONS

def view(game):
    vw = game.vw
    vh = game.vh

    CARD_CLR = (200, 200, 205)
    CARD_HVR_CLR = (235, 235, 245)
    CARD_HVR_BORDER_CLR = (55, 55, 62)
    CARD_HVR_BORDER_WEIGHT = 3
    TEXT_COLOR = (0, 0, 0)
    CARD_W = int(vw(28.5))
    CARD_H = int(vh(45))
    CARD_GAP_X = vw(2)
    CARD_GAP_Y = vh(3)
    PAD_X = vw(5)
    PAD_Y = vh(3)
    CARD_PADDING = 16

    page = 0

    def draw():
        mouse_pos = pygame.mouse.get_pos()
        
        for i in list(range(0, 6)):
            if not page + i < len(ILLUSIONS):
                continue

            x = PAD_X + (CARD_W + CARD_GAP_X) * (i % 3)
            y = PAD_Y + (i // 3) * (CARD_H + CARD_GAP_Y)
            rect = pygame.Rect((x, y), (CARD_W, CARD_H))
            
            if rect.collidepoint(mouse_pos):
                hover_border_rect = rect.copy()
                hover_border_rect.x -= CARD_HVR_BORDER_WEIGHT
                hover_border_rect.y -= CARD_HVR_BORDER_WEIGHT
                hover_border_rect.w += CARD_HVR_BORDER_WEIGHT * 2
                hover_border_rect.h += CARD_HVR_BORDER_WEIGHT * 2

                pygame.draw.rect(game.gameDisplay, CARD_HVR_BORDER_CLR, hover_border_rect)
                pygame.draw.rect(game.gameDisplay, CARD_HVR_CLR, rect)
            else:
                pygame.draw.rect(game.gameDisplay, CARD_CLR, rect)

            img = utils.scale_image_contain(images.store[ILLUSIONS[page + i]]["1"], w=CARD_W - CARD_PADDING * 2, h=(CARD_H * 8) // 10)
            game.gameDisplay.blit(img, (x + CARD_PADDING, y + CARD_PADDING))

            txt = game.font.xl.render(utils.format_illusion_name(ILLUSIONS[page + i]), True, TEXT_COLOR)
            game.gameDisplay.blit(txt, (x + (CARD_W - txt.get_width()) // 2, y + (CARD_H * 88) // 100))

    def update():
        draw()

    game.update_function = update

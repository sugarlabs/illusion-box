import pygame
import utils
import images
from constants import ILLUSIONS
import illusion

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
    card_data = []
    mouse_down = False

    for i in list(range(0, 6)):
        if not page + i < len(ILLUSIONS):
            continue

        x = PAD_X + (CARD_W + CARD_GAP_X) * (i % 3)
        y = PAD_Y + (i // 3) * (CARD_H + CARD_GAP_Y)
        rect = pygame.Rect((x, y), (CARD_W, CARD_H))

        img = utils.scale_image_contain(images.store[ILLUSIONS[page + i]]["1"], w=CARD_W - CARD_PADDING * 2, h=(CARD_H * 8) // 10)
        txt = game.font.xl.render(utils.format_illusion_name(ILLUSIONS[page + i]), True, TEXT_COLOR)

        card_data.append({
            "rect": rect,
            "img": img,
            "txt": txt,
            "index": page + i
        })

    def handle_input(mouse_pos):
        for card in card_data:
            rect = card['rect']
            if rect.collidepoint(mouse_pos):
                return card
        return None

    def handle_card_click(mouse_pos, mouse_released):
        nonlocal mouse_down
        hovered_card = handle_input(mouse_pos)
        if hovered_card:
            if pygame.mouse.get_pressed()[0]:
                mouse_down = True
            elif mouse_released and mouse_down:
                mouse_down = False
                game.current_illusion = hovered_card["index"]
                game.set_screen(illusion.view)

    def draw():
        mouse_pos = pygame.mouse.get_pos()
        hovered_card = handle_input(mouse_pos)

        for card in card_data:
            rect = card['rect']
            if card == hovered_card:
                hover_border_rect = rect.copy()
                hover_border_rect.x -= CARD_HVR_BORDER_WEIGHT
                hover_border_rect.y -= CARD_HVR_BORDER_WEIGHT
                hover_border_rect.w += CARD_HVR_BORDER_WEIGHT * 2
                hover_border_rect.h += CARD_HVR_BORDER_WEIGHT * 2
                pygame.draw.rect(game.gameDisplay, CARD_HVR_BORDER_CLR, hover_border_rect)
                pygame.draw.rect(game.gameDisplay, CARD_HVR_CLR, rect)
            else:
                pygame.draw.rect(game.gameDisplay, CARD_CLR, rect)

            game.gameDisplay.blit(card["img"], (rect.x + CARD_PADDING, rect.y + CARD_PADDING))
            game.gameDisplay.blit(card["txt"], (rect.x + (CARD_W - card["txt"].get_width()) // 2, rect.y + (CARD_H * 88) // 100))

    def update():
        mouse_released = not pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        draw()
        handle_card_click(mouse_pos, mouse_released)

    game.update_function = update

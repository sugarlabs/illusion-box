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

    BTN_CLR = (150, 150, 150)
    BTN_HVR_CLR = (200, 200, 200)
    BTN_TEXT_COLOR = (255, 255, 255)

    page = 0
    card_data = []
    mouse_down = False

    left_btn_rect = pygame.Rect(6, vh(50), PAD_X - 6, vh(10))
    right_btn_rect = pygame.Rect(vw(100) - PAD_X, vh(50), PAD_X - 6, vh(10))
    left_text = game.font.lg.render("<", True, BTN_TEXT_COLOR)
    right_text = game.font.lg.render(">", True, BTN_TEXT_COLOR)

    def load_cards():
        nonlocal card_data
        card_data = []
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

    load_cards()

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

    def draw_buttons():
        left_hovered = left_btn_rect.collidepoint(pygame.mouse.get_pos())
        right_hovered = right_btn_rect.collidepoint(pygame.mouse.get_pos())

        if page > 0:
            pygame.draw.rect(game.gameDisplay, BTN_HVR_CLR if left_hovered else BTN_CLR, left_btn_rect)
            game.gameDisplay.blit(left_text, (left_btn_rect.centerx - left_text.get_width() // 2, left_btn_rect.centery - left_text.get_height() // 2))
        
        if page + 6 < len(ILLUSIONS):
            pygame.draw.rect(game.gameDisplay, BTN_HVR_CLR if right_hovered else BTN_CLR, right_btn_rect)
            game.gameDisplay.blit(right_text, (right_btn_rect.centerx - right_text.get_width() // 2, right_btn_rect.centery - right_text.get_height() // 2))


        return left_btn_rect, right_btn_rect

    def handle_pagination(mouse_pos, mouse_released):
        nonlocal page, mouse_down

        left_btn_rect, right_btn_rect = draw_buttons()

        if pygame.mouse.get_pressed()[0]:
            mouse_down = True

        if mouse_released and mouse_down:
            mouse_down = False

            if left_btn_rect.collidepoint(mouse_pos) and page > 0:
                page -= 6
                load_cards()
            elif right_btn_rect.collidepoint(mouse_pos) and page + 6 < len(ILLUSIONS):
                page += 6
                load_cards()

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
        mouse_pos = pygame.mouse.get_pos()
        mouse_released = not pygame.mouse.get_pressed()[0]

        draw()
        handle_card_click(mouse_pos, mouse_released)
        handle_pagination(mouse_pos, mouse_released)

    game.update_function = update

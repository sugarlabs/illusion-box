# Copyright (C) 2024 Spandan Barve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
import utils
import images
import showcase
from constants import ILLUSIONS


def view(game):
    vw = game.vw
    vh = game.vh
    illusion = game.current_illusion

    index = -1
    img = None
    label = None
    m_x = 0
    m_y = 0
    btm_txt = game.font.xl.render(
        "Press <Spacebar> to cycle through images and see the illusion",
        True,
        (0, 0, 0),
    )
    b_t_x = vw(50) - btm_txt.get_width() // 2

    BACK_BUTTON_RECT = pygame.Rect(vw(1), vh(1), vw(15), vh(8))
    BACK_BUTTON_COLOR = (200, 200, 200)
    BACK_BUTTON_HOVER_COLOR = (170, 170, 170)
    BACK_TEXT_COLOR = (0, 0, 0)
    BACK_TEXT = game.font.lg.render("Back", True, BACK_TEXT_COLOR)
    IMAGES_COUNT = len(images.store[ILLUSIONS[illusion]])
    back_txt_x = (
        BACK_BUTTON_RECT.x + (BACK_BUTTON_RECT.w - BACK_TEXT.get_width()) // 2
    )
    back_txt_y = (
        BACK_BUTTON_RECT.y + (BACK_BUTTON_RECT.h - BACK_TEXT.get_height()) // 2
    )

    mouse_pos = (0, 0)
    mouse_down = False

    def rotate_img():
        nonlocal img, label, m_x, m_y, index

        index = (index + 1) % IMAGES_COUNT

        if IMAGES_COUNT > 1:
            img = utils.scale_image_contain(
                images.store[ILLUSIONS[illusion]][f"{index + 1}"],
                w=vw(90),
                h=vh(75),
            )
        else:
            img = utils.scale_image_contain(
                images.store[ILLUSIONS[illusion]][f"{index + 1}"],
                w=vw(90),
                h=vh(85),
            )

        label = game.font.xxl.render(
            utils.format_illusion_name(ILLUSIONS[illusion]) + " Illusion",
            True,
            (0, 0, 0),
        )
        m_x = vw(50) - img.get_width() // 2
        m_y = vh(50) - img.get_height() // 2

    def draw_back_button():
        if BACK_BUTTON_RECT.collidepoint(mouse_pos):
            pygame.draw.rect(
                game.gameDisplay, BACK_BUTTON_HOVER_COLOR, BACK_BUTTON_RECT
            )
        else:
            pygame.draw.rect(game.gameDisplay,
                             BACK_BUTTON_COLOR,
                             BACK_BUTTON_RECT)

        game.gameDisplay.blit(BACK_TEXT, (back_txt_x, back_txt_y))

    def handle_back_button_click():
        nonlocal mouse_down

        if BACK_BUTTON_RECT.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                mouse_down = True
            elif mouse_down:
                mouse_down = False
                game.set_screen(showcase.view)

    def draw():
        nonlocal img, label, m_x, m_y, btm_txt, b_t_x

        game.gameDisplay.blit(img, (m_x, m_y))
        game.gameDisplay.blit(label, (vw(50) - label.get_width() // 2, vh(1)))
        if IMAGES_COUNT > 1:
            game.gameDisplay.blit(btm_txt, (b_t_x, vh(93)))

        draw_back_button()

    def update():
        nonlocal mouse_pos

        mouse_pos = pygame.mouse.get_pos()

        draw()
        handle_back_button_click()

        for event in game.events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    rotate_img()

    rotate_img()
    game.update_function = update

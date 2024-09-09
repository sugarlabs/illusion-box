import pygame
import utils
import images
from constants import ILLUSIONS

def view(game):
    vw = game.vw
    vh = game.vh
    illusion = game.current_illusion

    index = 0
    img = None
    label = None
    m_x = 0
    m_y = 0

    def rotate_img():
        nonlocal img, label, m_x, m_y

        img = utils.scale_image_contain(images[ILLUSIONS[illusion]][index + 1], w = vw(90), h = vh(90))
        label = game.font.xxl.render(utils.format_illusion_name(ILLUSIONS[illusion]), True, (0, 0, 0))
        m_x = vw(50) - img.get_width() // 2
        m_y = vh(50) - img.get_height() // 2


    def draw():
        nonlocal img, label, m_x, m_y

        if img is not None:
            game.gameDisplay.blit(img, (m_x, m_y))
            game.gameDisplay.blit(label, (vw(50) - label.get_width() // 2, vh(1)))


    def update():
        draw()

    game.update_function = update

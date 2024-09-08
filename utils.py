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


def scale_image_maintain_ratio(img, w=None, h=None):
    o_w, o_h = img.get_size()
    m_w, m_h = o_w, o_h

    if w is not None and h is None:
        m_h = w * (o_h / o_w)
        return pygame.transform.scale(img, (int(w), int(m_h)))

    if h is not None and w is None:
        m_w = h * (o_w / o_h)
        return pygame.transform.scale(img, (int(m_w), int(h)))

    if w is None and h is None:
        return img
    
def scale_image_contain(img, w, h):
    img_ratio = img.get_width() / img.get_height()
    target_ratio = w / h

    new_img = pygame.Surface((w, h), pygame.SRCALPHA)

    if img_ratio > target_ratio : 
        new_w = w
        new_h = int(w / img_ratio)
        sc_img = pygame.transform.scale(img, (new_w, new_h))
        new_img.blit(sc_img, (0, (h - new_h) // 2))
    else :
        new_h = h
        new_w = int(h * img_ratio)
        sc_img = pygame.transform.scale(img, (new_w, new_h))
        new_img.blit(sc_img, ((w - new_w) // 2, 0))

    return new_img


def array_has_no_none(arr):
    return all(element is not None for element in arr)

def format_illusion_name(name):
    return name.replace('_', ' ').title()

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


import os
import pygame
import constants

store = {}

def load():
    for ill in constants.ILLUSIONS:
        directory = f"images/{ill}"
        store[ill] = {}
        for filename in os.listdir(directory):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                file_path = os.path.join(directory, filename)
                try:
                    image = pygame.image.load(file_path)
                    base_filename = os.path.splitext(filename)[0]
                    store[ill][base_filename] = image
                except pygame.error as err:
                    print(f"Error loading image '{file_path}': {err}")
    return store
import pygame
from pygame.sprite import Sprite

from utils.constants import *
from utils.helpers import *


class Word(Sprite):
    def __init__(self, word, x, y):
        super(Word, self).__init__()
        self.letters = []
        self.index = 0
        for w in word:
            self.image = pygame.image.load(LETTERS_TRANSPARENTES[w]).convert_alpha()
            self.image = scale_image(self.image, 50)
            x += self.image.get_width() + 5
            letter_x = self.image.get_width() + x
            letter_y = y
            self.rect = self.image.get_rect(center=(letter_x, letter_y))
            self.letters.append(
                {
                    'index': self.index,
                    'image': self.image,
                    'rect': self.rect,
                    'letter': w,
                    'status': False
                }
            )
            self.index += 1

    def letter_found(self, letter):
        for let in self.letters:
            if let['letter'] == letter and not let['status']:
                let['status'] = True
                let['image'] = pygame.image.load(LETTERS[letter]).convert_alpha()
                let['image'] = scale_image(let['image'], 50)
                break

import pygame
import random

FOOD_SIZE = 20
colors = [(173, 235, 173), (255, 214, 153), (255, 204, 224), (255, 255, 179), (217, 179, 255), (204, 255, 255)]


class Food:

    def __init__(self, screen):

        self.rect = None
        self.screen = screen

        self.x = 0
        self.y = 0

        self.color = (255, 255, 255)

    def draw(self):

        self.rect = pygame.draw.rect(self.screen, self.color, [self.x, self.y, FOOD_SIZE, FOOD_SIZE])

    def update(self, snake_locations):
        self.__update_color()
        self.__update_location(snake_locations)

    def __update_location(self, snake_locations):
        self.y = random.randrange(0, self.screen.get_height(), 20)
        self.x = random.randrange(0, self.screen.get_width(), 20)

        if [loc for loc in snake_locations if loc[0] == self.x and loc[1] == self.y]:
            self.__update_location(snake_locations)

    def __update_color(self):
        i = random.randint(0, len(colors) - 1)
        self.color = colors[i]

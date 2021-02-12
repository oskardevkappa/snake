import pygame


SNAKE_COLOR = (255, 255, 255)
SNAKE_SIZE = 20
colors = [SNAKE_COLOR, (255, 179, 209), (214, 214, 245)]


class Snake:

    def __init__(self, screen, start_position):

        self.screen = screen

        self.length = 1

        self.xspeed = 0
        self.yspeed = 0

        self.x = start_position[0]
        self.y = start_position[1]

        self.last_locations = []

    def change_direction(self, direction):

        if direction == 'r':
            if not self.xspeed == -SNAKE_SIZE:
                self.yspeed = 0
                self.xspeed = SNAKE_SIZE

        if direction == 'l':
            if not self.xspeed == SNAKE_SIZE:
                self.yspeed = 0
                self.xspeed = -SNAKE_SIZE

        if direction == 'u':
            if not self.yspeed == SNAKE_SIZE:
                self.xspeed = 0
                self.yspeed = -SNAKE_SIZE

        if direction == 'd':
            if not self.yspeed == -SNAKE_SIZE:
                self.xspeed = 0
                self.yspeed = SNAKE_SIZE

    def draw(self):

        # drawing the snake2 head
        pygame.draw.rect(self.screen, colors[0], [self.x, self.y, SNAKE_SIZE, SNAKE_SIZE])

        # drawing the snake2 tail
        for loc in self.last_locations:
            pygame.draw.rect(self.screen, colors[0], [loc[0], loc[1], SNAKE_SIZE, SNAKE_SIZE])

    def update(self):
        self.last_locations.append([self.x, self.y])
        if len(self.last_locations) > self.length - 1:
            del(self.last_locations[0])

        self.x += self.xspeed
        self.y += self.yspeed

    def is_on_screen(self):
        on_screen = True
        if self.x < 0 or self.x > self.screen.get_width():
            on_screen = False
        if self.y < 0 or self.y > self.screen.get_height():
            on_screen = False
        return on_screen

    def hit_tail(self):
        if [loc for loc in self.last_locations if loc[0] == self.x and loc[1] == self.y]:
            return True
        return False

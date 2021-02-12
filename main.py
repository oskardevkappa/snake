import pygame
from objects.snake import Snake
from objects.food import Food
from objects.highscore import Highscore
from pathlib import Path

FPS = 10

BACKGROUND_COLOR = (179, 179, 255)
WHITE = (255, 255, 255)
GAME_HEIGHT = 600
GAME_WIDTH = 400
SNAKE_START_LOCATION = (int(GAME_WIDTH / 2), int(GAME_HEIGHT / 2))
GO_TAG_LOCATION_X = (GAME_WIDTH / 4) - 25
GO_TAG_LOCATION_Y = (GAME_HEIGHT / 2) - 25
GO_TAG_LOCATION = (GO_TAG_LOCATION_X, GO_TAG_LOCATION_Y)
ICON_PATH = f'{Path(__file__).parents[0]}\\resources\\icon.png'


def main():
    # initializing the pygame module
    pygame.init()

    # general information
    logo = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Snake')

    # creating screen
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

    # creating snake2 object
    snake = Snake(screen, SNAKE_START_LOCATION)

    # creating food object
    food = Food(screen)
    food.update(snake.last_locations)

    # creating highscore object
    highscore = Highscore()

    # creating highscore object

    # set game to running
    running = True
    clock = pygame.time.Clock()

    # initializing game_over variable
    game_over = False

    # mainloop
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # other controls
                # restart
                if event.key == pygame.K_r:
                    running = False
                    main()

                # quit
                if event.key == pygame.K_ESCAPE:
                    running = False

                # movement keys
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.change_direction('r')

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.change_direction('l')

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.change_direction('u')

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.change_direction('d')

        if not game_over:

            # 'clears' the background
            screen.fill(BACKGROUND_COLOR)

            # moves snake2
            snake.update()

            # checks if snake2 is on the screen. if not = Game Over
            if not snake.is_on_screen():
                game_over = True

            # checks if the snake2 hit its tail
            if snake.hit_tail():
                game_over = True

            # draws snake2
            snake.draw()

            # check if snake2 hits food
            if snake.x == food.x and snake.y == food.y:
                snake.length += 1
                food.update(snake.last_locations)

                # check if score is over the highscore
                if snake.length - 1 > highscore.get():
                    highscore.score = snake.length - 1

            # draw food rectangle
            food.draw()

            # update score
            font = pygame.font.SysFont('bahnschrift', 20)
            tag = font.render(f'Score: {snake.length - 1}', True, WHITE)
            screen.blit(tag, (25, 25))

            # update highscore
            font = pygame.font.SysFont('bahnschrift', 20)
            tag = font.render(f'Highscore: {highscore.get()}', True, WHITE)
            screen.blit(tag, (250, 25))

        if game_over:
            screen.fill((194, 61, 128))

            highscore.update()

            go_font = pygame.font.SysFont('times new roman', 40)
            go_tag = go_font.render('GAME OVER', True, WHITE)

            score_font = pygame.font.SysFont('bahnschrift', 30)
            score_tag = score_font.render(f'your score: {snake.length -1}', True, WHITE)

            ctrl_font = pygame.font.SysFont('bahnschrift', 30)
            ctrl_tag = ctrl_font.render('r: restart       esc: quit', True, WHITE)

            screen.blits(((go_tag, GO_TAG_LOCATION),
                          (score_tag, (GAME_WIDTH / 4, GAME_HEIGHT * 0.75)),
                          (ctrl_tag, (GAME_WIDTH / 8, GAME_HEIGHT - 50))))

        # update display
        pygame.display.flip()


if __name__ == "__main__":
    main()

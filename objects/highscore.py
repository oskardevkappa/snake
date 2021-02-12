from pathlib import Path
import os

FILE_PATH = f'{Path(__file__).parents[1]}\\resources\\highscore.txt'


class Highscore:

    def __init__(self):

        self.score = 0

        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w') as file:
                file.write(str(self.score))
        else:
            with open(FILE_PATH, mode='r') as file:
                self.score = int(file.read())

    def get(self):
        return self.score

    def update(self):
        with open(FILE_PATH, mode='w') as file:
            file.write(str(self.score))

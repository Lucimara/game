import pygame as pg

from code import Const
from code.Menu import Menu
from code.Score import Score


class Game:

    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(Const.WIN_WIDTH, Const.WIN_HEIGHT))
        pg.mixer.init()

    def run(self):
        score = Score(self.window)
        menu = Menu(self.window)
        menu.run()


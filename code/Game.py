import pygame as pg

from code import Const
from code.Menu import Menu


class Game:

    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(Const.WIN_WIDTH, Const.WIN_HEIGHT))

    def run(self):
        menu = Menu(self.window)
        self.tocar_musica()
        menu.run()

    # Responsável por tocar a música inicial do jogo
    @staticmethod
    def tocar_musica():
        pg.mixer_music.load('./asset/sound-tribal-ambient-meditative-texture.wav')
        pg.mixer_music.play(-1)


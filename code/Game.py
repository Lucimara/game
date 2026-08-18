import pygame as pg

from code.Menu import Menu


class Game:

    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(600, 600))

    def run(self):

        while True:
            # Checando todos os eventos

            menu = Menu(self.window)
            menu.run()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # Fecha janela
                    quit()  # Finaliza o pygame

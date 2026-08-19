import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COR_BEGE, MENU_OPCOES, COR_BRANCO


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/Battleground2.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        self.tocar_musica()
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.escrever_titulo()

            for i in range(len(MENU_OPCOES)):
                self.menu_texto(self, 20, MENU_OPCOES[i], COR_BRANCO, (WIN_WIDTH / 2, 790 + 30 *i))

            pg.display.flip()

            # Checando todos os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.fim_game()

    # Responsável por exibir o título do jogo
    def escrever_titulo(self):
        # Catstle é a junção de cat e castle. Como Castelo Felino
        self.menu_texto(self, 50, "Catstle", COR_BEGE, (WIN_WIDTH / 2, 700))
        self.menu_texto(self, 50, "Blood", COR_BEGE, (WIN_WIDTH / 2, 745))

    # Responsável por tocar a música inicial do jogo
    @staticmethod
    def tocar_musica():
        pg.mixer_music.load('./asset/sound-tribal-ambient-meditative-texture.wav')
        pg.mixer_music.play(-1)

    # Responsável por finalizar o jogo
    @staticmethod
    def fim_game():
        pg.quit()  # Fecha janela
        quit()  # Finaliza o pygame

    @staticmethod
    def menu_texto(self, tamanho: int, texto: str, cor_texto: tuple, posicao_texto: tuple):
        text_font: Font = pg.font.SysFont(name='Lucida Sans Typewriter', size=tamanho)
        text_surf: Surface = text_font.render(texto, True, cor_texto).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=posicao_texto)
        self.window.blit(source=text_surf, dest=text_rect)

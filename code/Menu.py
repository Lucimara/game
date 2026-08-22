import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code import Const
from code.Const import WIN_WIDTH, COR_BEGE, MENU_OPCOES, COR_BRANCO, COR_INDIGO
from code.Level import Level


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/Battleground2.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.escrever_titulo()
            self.escrever_opcoes(menu_option)
            pg.display.flip()

            # Checando todos os eventos
            for event in pg.event.get():
                if event.type == pg.KEYDOWN: # EVENTOS DO TECLADO
                    if event.key == pg.K_DOWN:
                        if menu_option < len(MENU_OPCOES) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pg.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPCOES) - 1
                    if event.key == pg.K_RETURN: # Tecla ENTER
                        print('Menu_option: ', menu_option)
                        print("Constante: ", Const.MENU_OPCOES[menu_option])
                        if menu_option in [0, 1, 2]:
                            print('Entrou na opção: ', Const.MENU_OPCOES[menu_option])
                            level = Level(self.window, 'Level1', Const.MENU_OPCOES[menu_option])
                            level.run()
                            # level_return = level.run()
                        elif menu_option == 4:
                            self.fim_game()
                        else:
                            pass

                if event.type == pg.QUIT:
                    self.fim_game()


    def escrever_opcoes(self, menu_option):
        for i in range(len(MENU_OPCOES)):
            if i == menu_option:
                self.menu_texto(self, 20, MENU_OPCOES[i], COR_INDIGO, (WIN_WIDTH / 2, 790 + 30 * i))
            else:
                self.menu_texto(self, 20, MENU_OPCOES[i], COR_BRANCO, (WIN_WIDTH / 2, 790 + 30 * i))

    # Responsável por exibir o título do jogo
    def escrever_titulo(self):
        # Catstle é a junção de cat e castle. Como Castelo Felino
        self.menu_texto(self, 50, "Catstle", COR_BEGE, (WIN_WIDTH / 2, 700))
        self.menu_texto(self, 50, "Blood", COR_BEGE, (WIN_WIDTH / 2, 745))

    # Responsável por finalizar o jogo
    @staticmethod
    def fim_game():
        pg.quit()  # Fecha janela
        quit()  # Finaliza o pygame

    @staticmethod
    def menu_texto(self, tamanho: int, texto: str, cor_texto: tuple, posicao_texto: tuple):
        text_font: Font = pg.font.SysFont(name='Kristen ITC', size=tamanho)
        text_surf: Surface = text_font.render(texto, True, cor_texto).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=posicao_texto)
        self.window.blit(source=text_surf, dest=text_rect)

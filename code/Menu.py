import pygame as pg

from code import Const
from code.Const import WIN_WIDTH, COR_LARANJA, MENU_OPCOES, COR_ROSA, COR_INDIGO
from code.Level import Level
from code.TextUtils import draw_text


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/InicioJogo.png').convert_alpha()
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
            cor = COR_INDIGO if i == menu_option else COR_ROSA
            draw_text(self.window, MENU_OPCOES[i], 20, cor, ((WIN_WIDTH / 2)+30, 100 + 30 * i), center=False)

    # Responsável por exibir o título do jogo
    def escrever_titulo(self):
        # Catstle é a junção de cat e castle. Como Castelo Felino
        draw_text(self.window, "Catstle Blood", 80, COR_LARANJA, (WIN_WIDTH / 2, 50), center=True)

    # Responsável por finalizar o jogo
    @staticmethod
    def fim_game():
        pg.quit()  # Fecha janela
        quit()  # Finaliza o pygame

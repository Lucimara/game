import pygame as pg

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.TextUtils import draw_text

class Help:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/help.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        ajuda_ativa = True
        while ajuda_ativa:
            # desenha a imagem diretamente na janela
            self.window.blit(self.surf, self.rect)
            # adiciona instrução em inglês no rodapé
            draw_text(self.window,
                      "Press ESC or ENTER to exit",
                      24,
                      (255, 255, 255),
                      (WIN_WIDTH / 2 - 530, WIN_HEIGHT / 2 + 80),
                      center=False)
            pg.display.flip()

            # eventos para sair da ajuda
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                        ajuda_ativa = False
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
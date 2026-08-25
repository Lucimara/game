import pygame as pg

from code.Const import WIN_WIDTH, WIN_HEIGHT, COR_LARANJA
from code.TextUtils import draw_text
# Ainda não implementei score
class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/score.jpg').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        score_ativo = True
        while score_ativo:
            # desenha a imagem diretamente na janela
            self.window.blit(self.surf, self.rect)
            # adiciona instrução em inglês no rodapé
            draw_text(self.window,
                      "Press ESC or ENTER to exit",
                      24,
                      COR_LARANJA,
                      (WIN_WIDTH / 2 - 400, WIN_HEIGHT / 2 + 100),
                      center=False)
            pg.display.flip()

            # eventos para sair do score
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                        score_ativo = False
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

    def save(self, menu_opcao: str, player_score: list[int]):
        pass
    def show_score(self):
        pass
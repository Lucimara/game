# from abc import ABC
import pygame as pg

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.TextUtils import draw_text

class ScreenBase:
    def __init__(self, background_path: str, window, color, position: tuple):
        self.window = window
        self.color = color
        self.surf = pg.image.load(f'./asset/{background_path}.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.position = position

    def run(self):
        ativo = True
        while ativo:
            # desenha a imagem diretamente na janela
            self.window.blit(self.surf, self.rect)
            # adiciona instrução em inglês no rodapé
            draw_text(self.window,
                      "Press ESC or ENTER to exit",
                      24,
                      self.color,
                      self.position,
                      center=True)
            pg.display.flip()

        # eventos para sair da ajuda
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key in (pg.K_ESCAPE, pg.K_RETURN):
                        ativo = False
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
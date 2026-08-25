
import pygame as pg
from code.TextUtils import draw_text
from code.Const import COR_LARANJA

class BtnBack:
    def __init__(self, rect, texto, cor=COR_LARANJA):
        self.rect = rect
        self.texto = texto
        self.cor = cor

    def desenhar(self, window):
        # sombra
        shadow_rect = self.rect.move(3, 3)
        pg.draw.rect(window, (180, 90, 90), shadow_rect, border_radius=20)

        # botão principal
        pg.draw.rect(window, self.cor, self.rect, border_radius=20)

        # texto centralizado (usa Broadway do TextUtils)
        draw_text(window, self.texto, 30, (255, 255, 255), self.rect.center, center=True)

    def clicado(self, pos):
        return self.rect.collidepoint(pos)

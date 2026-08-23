import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

def draw_text(window, texto: str, tamanho: int, cor: tuple, posicao: tuple, center: bool = False):
    """
    Função utilitária para desenhar texto na tela.
    :param window: Surface da janela principal
    :param texto: Texto a ser exibido
    :param tamanho: Tamanho da fonte
    :param cor: Cor do texto (tuple RGB)
    :param posicao: Posição (x, y)
    :param center: Se True, centraliza no ponto; caso contrário, usa como top-left
    """
    text_font: Font = pg.font.SysFont('Broadway', tamanho)
    text_surf: Surface = text_font.render(texto, True, cor).convert_alpha()
    if center:
        text_rect: Rect = text_surf.get_rect(center=posicao)
    else:
        text_rect: Rect = text_surf.get_rect(left=posicao[0], top=posicao[1])
    window.blit(text_surf, text_rect)

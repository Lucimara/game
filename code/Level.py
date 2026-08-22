import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_HEIGHT, COR_INDIGO, COR_BRANCO
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        self.entity_list.extend(EntityFactory.get_entity('Player1'))
        self.timeout = 20000

    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(120)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # Fecha janela
                    quit()

            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000 }s', COR_BRANCO, (10, 5))
            self.level_text(20, f'fps: {clock.get_fps() :.0f}', COR_INDIGO, (10, WIN_HEIGHT - 35))
            self.level_text(20, f'entidades: {len(self.entity_list)}', COR_INDIGO, (10, WIN_HEIGHT - 20))
            pg.display.flip()


    def level_text(self, tamanho_texto: int, texto: str, cor: tuple, posicao: tuple):
        text_font: Font = pg.font.SysFont('Broadway', tamanho_texto)
        text_surf: Surface = text_font.render(texto, True, cor).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=posicao[0], top=posicao[1])
        self.window.blit(text_surf, text_rect)
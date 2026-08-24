import random

import pygame as pg

from code.Backgound import Background
from code.Const import WIN_HEIGHT, COR_INDIGO, COR_ROSA, ENTITY_SPEED, MENU_OPCOES, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH, \
    COR_LARANJA
from code.Enemy import Enemy

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.TextUtils import draw_text


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.timeout = 20000
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        self.entity_list.extend(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPCOES[1], MENU_OPCOES[2]]:
            self.entity_list.extend(EntityFactory.get_entity('Player2'))
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)


    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(120)
            # desenha o parallax
            for ent in sorted(
                    [e for e in self.entity_list if isinstance(e, Background)],
                    key=lambda bg: ENTITY_SPEED[bg.name]):
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            # desenha player antigo
            for ent in [e for e in self.entity_list if not isinstance(e, Background)]:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if ent.name == 'Player1':
                        draw_text(self.window, f'Player1 - Health: {ent.health}', 15, COR_LARANJA, (WIN_WIDTH-180, 10))
                    if ent.name == 'Player2':
                        draw_text(self.window, f'Player2 - Health: {ent.health}', 15, COR_LARANJA, (WIN_WIDTH-180, 30))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # Fecha janela
                    quit()
                if event.type == EVENT_ENEMY:
                    choice =  random.choice(('Enemy2', 'Enemy1'))
                    self.entity_list.extend(EntityFactory.get_entity(choice))

            draw_text(self.window, f'{self.name} - Timeout: {self.timeout / 1000}s', 20, COR_ROSA, (10, 5))
            draw_text(self.window, f'fps: {clock.get_fps() :.0f}', 20, COR_INDIGO, (10, WIN_HEIGHT - 35))
            draw_text(self.window, f'entidades: {len(self.entity_list)}', 20, COR_INDIGO, (10, WIN_HEIGHT - 20))
            pg.display.flip()
            # Verificando colisões e vida
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


import random

import pygame as pg
from pygame.surface import Surface

from code.Backgound import Background
from code.BtnBack import BtnBack
from code.Const import WIN_HEIGHT, COR_INDIGO, COR_ROSA, ENTITY_SPEED, MENU_OPCOES, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH, \
    COR_LARANJA, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.TextUtils import draw_text


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.timeout = TIMEOUT_LEVEL
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1BG'))
        player1 = EntityFactory.get_entity('Player1')[0]
        player1.score = player_score[0]
        self.entity_list.append(player1)
        if game_mode in [MENU_OPCOES[1], MENU_OPCOES[2]]:
            player2 = EntityFactory.get_entity('Player2')[0]
            player2.score = player_score[1]
            self.entity_list.append(player2)
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
        self.btn_back = BtnBack(pg.Rect(WIN_WIDTH - 150, WIN_HEIGHT - 60, 140, 40), "Back")

    def run(self, player_score: list[int]):
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

            # desenha player
            for ent in [e for e in self.entity_list if not isinstance(e, Background)]:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if ent.name == 'Player1':
                        draw_text(self.window, f'Player1 - Health: {ent.health} | Score: {ent.score}', 15, COR_LARANJA, (WIN_WIDTH-270, 10))
                    if ent.name == 'Player2':
                        draw_text(self.window, f'Player2 - Health: {ent.health} | Score: {ent.score}', 15, COR_LARANJA, (WIN_WIDTH-270, 30))

            # Botão de voltar
            self.btn_back.desenhar(self.window)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # Fecha janela
                    quit()
                if event.type == EVENT_ENEMY:
                    choice =  random.choice(('Enemy2', 'Enemy1'))
                    self.entity_list.extend(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.btn_back.clicado(event.pos):
                        pg.mixer_music.stop()
                        return False # Sai do loop e volta para quem chamou

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            draw_text(self.window, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', 20, COR_ROSA, (10, 5))
            draw_text(self.window, f'fps: {clock.get_fps() :.0f}', 20, COR_INDIGO, (10, WIN_HEIGHT - 35))
            draw_text(self.window, f'entidades: {len(self.entity_list)}', 20, COR_INDIGO, (10, WIN_HEIGHT - 20))
            pg.display.flip()
            # Verificando colisões e vida
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


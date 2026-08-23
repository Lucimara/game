import pygame

# C
COR_LARANJA = (255, 150, 90)
COR_ROSA = (255, 120, 150)
COR_INDIGO = (126, 132, 247)

# E
ENTITY_SPEED = {
    'Level1BG0': 6,  # fumaça
    'Level1BG1': 4,  # nuvem grossa
    'Level1BG2': 5,  # nuvem mais elevada
    'Level1BG3': 1,  # fundo gradiente
    'Level1BG4': 10,  # nuvem base
    'Level1BG5': 3,  # estrelas mais fracas
    'Level1BG6': 2,  # estrelas fracas
    'Level1BG7': 3,  # estrelas fortes
    'Level1BG8': 2,  # castelinho
    'Level1BG9': 2,  # imagem completa
    'Player1': 7,  # velocidade player1
    'Player2': 7,  # velocidade player1
    'Enemy1': 6,  # velocidade player1
    'Enemy2': 4  # velocidade player1
}
EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPCOES = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 1920
WIN_HEIGHT = 1080

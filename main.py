import pygame

print('Início do Jogo!')
pygame.init()

window = pygame.display.set_mode(size=(600, 600))

while True:
    # Checando todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Fecha janela
            print('Fim do Jogo!')
            print('Saindo...')
            quit()  # Finaliza o pygame

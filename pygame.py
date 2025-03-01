import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
done=False
while not done:
    for event in pygame.event.get():
        pygame.quit()
    pygame.display.flip()  
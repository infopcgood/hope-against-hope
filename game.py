import pygame
import src.constants.base_constants as Constants
from src.characters.player import Player
import src.constants.spritesheet_constants as SpriteSheet_Constants

pygame.init()
screen = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
running = True
screen.fill("white")
main_player = Player()

while running:
    delta_time = clock.tick(Constants.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        main_player.move(SpriteSheet_Constants.FACING_UP, delta_time)
    elif keys_pressed[pygame.K_a]:
        main_player.move(SpriteSheet_Constants.FACING_LEFT, delta_time)
    elif keys_pressed[pygame.K_s]:
        main_player.move(SpriteSheet_Constants.FACING_DOWN, delta_time)
    elif keys_pressed[pygame.K_d]:
        main_player.move(SpriteSheet_Constants.FACING_RIGHT, delta_time)
    screen.fill("white")
    main_player.blit(screen)
    pygame.display.update()

pygame.quit()
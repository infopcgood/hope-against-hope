import pygame

from src.base.assets import assets


# basic Projectile class
class Projectile:
    def __init__(self, x, y, vx, vy, has_gravity=False):
        # set x and y
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        # set rect
        self.rect = pygame.Rect(x, y, 12, 12)
        # set attack power
        self.power = 4
        # choose asset depending on gravity
        if has_gravity:
            self.image = assets.get_asset('textures/extra/gravity_projectile.png')
            self.has_gravity = True
        else:
            self.image = assets.get_asset('textures/extra/projectile.png')
            self.has_gravity = False

    # move the projectile every frame
    def move(self, screen, scene, main_player, dt):
        if self.has_gravity:
            self.vy += scene.g_accel * 1.25 * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rect.move_ip(self.vx * dt, self.vy * dt)

    # draw projectile to screen
    def update(self, screen, scene, main_player, dt):
        screen.blit(self.image, self.rect)

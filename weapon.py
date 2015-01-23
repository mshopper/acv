import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, location, direction, *groups):
        super(Weapon, self).__init__(*groups)
        self.image = pygame.image.load('resources/features/bullet.png')
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.direction = direction
        self.lifespan = 1

    def update(self, dt, game):
        self.lifespan -= dt
        if self.lifespan < 0:
            self.kill()
            return
        self.rect.x += self.direction * 400 * dt

        if pygame.sprite.spritecollide(self, game.enemies, True):
            self.kill()
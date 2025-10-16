import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

    def move(self, sounds):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Wall bounce
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            sounds["wall"].play()



    def check_collision(self, player, ai, sounds):
        # Player paddle collision
        if self.rect().colliderect(player.rect()):
            self.velocity_x = abs(self.velocity_x)
            self.x = player.rect().right
            sounds["paddle"].play()  # Play paddle hit sound

        # AI paddle collision
        elif self.rect().colliderect(ai.rect()):
            self.velocity_x = -abs(self.velocity_x)
            self.x = ai.rect().left - self.width
            sounds["paddle"].play()  # Play paddle hit sound

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

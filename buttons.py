import pygame

class Button:
    def __init__(self, x, y, width, height, action=None):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action
        self.color = (200, 200, 200)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def handle_event(screen, event):
        if event.type == event.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()
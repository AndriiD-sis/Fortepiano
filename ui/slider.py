import pygame

class Slider:
    def __init__(self, x, y, width, height, min_value, max_value, initial, label=""):
        self.track_rect = pygame.Rect(x, y, width, 6)
        self.handle_radius = 8
        self.min = min_value
        self.max = max_value
        self.value = initial
        self.lable = lable
        self.draging = False
        self.on_change = None

    def set_on_change(self, callback):
        self.on_change = callback

    def value_to_pos(self):
        ratio = (self.value - self.min) / (self.max - self.min)
        return int(self.track_rect.left + ratio * self.track_rect.width)

    def pos_to_value(self):
        ratio = (x - self.track_rect.left) / self.track_rect.width
        ratio = max(0, min(1, ratio))
        return self.min + ratio * (self.max - self.min)

    def draw(self, screen, font=None):
        pygame.draw.rect(screen, (180, 180, 180), self.track_rect)
        hx = self.value_to_pos()
        hy = self.track_rect.centery
        pygame.draw.circle(screen, (50, 50, 50), (hx, hy), self.handle_radius)

        if font and self.lable:
            percent = int((self.value - self.min) / (self.max - self.min) * 100)
            text = font.render(f"{self.lable}: {percent}%", True, (0, 0, 0))
            screen.blit(text, (self.track_rect.left, self.track_rect.top - 25))
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.track_rect.collidepoint(event.pos):
                self.draging = True
                self.value = self.pos_to_value(event.pos[0])
        elif event.type == pygame.MOUSEMOTION and self.draging:
            self.value = self.pos_to_value(event.pos[0])
        elif event.type == pygame.MOUSEBUTTONUP:
            self.draging = False

        if self.on_change:
            self.on_change(self.value)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.track_rect.collidepoint(event.pos):
                self.draging = True
                self.value = self.pos_to_value(event.pos[0])
            elif event.type == pygame.MOUSEMOTION and self.draging:
                self.value = self.pos_to_value(event.pos[0])
            elif event.type == pygame.MOUSEBUTTONUP and self.draging:
                self.draging = False
                self.value = self.pos_to_value(event.pos[0])

            if hasattr(self, "on_change") and self.on_change:
                self.on_change(self.value)
import pygame
from buttons import Button
from ui.slider import Slider

class SettingsMenu:
    def __init__(self, screen_rect, initial_volume, on_change, on_back):
        self.screen_rect = screen_rect
        self.on_change = on_change
        self.on_back = on_back

        cx = screen_rect.centerx
        top = 140

        self.back_btn = Button(
            60, 20, 50, 50, self._back
        )

        self.volume_slider = Slider(
            cx - 200, top, 400,
            0.0, 1.0, initial=initial_volume,
            label="Гучність"
        )

        self.volume_slider.set_on_change(self._on_volume)

    def _on_volume(self, v):
        if self.on_change:
            self.on_change(float(v))

    def _back(self):
        if self.on_back:
            self.on_back()

    def draw(self, screen, font):
        title = font.render("Налаштування", True, (0, 0, 0))
        screen.blit(title, title.get_rect(center=(self.screen_rect.centerx, 80)))

        self.back_btn.draw(screen)
        self.volume_slider.draw(screen, font)

    def handle_event(self, event):
        self.back_btn.handle_event(event)
        self.volume_slider.handle_event(event)
from pygame import *
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, KEYS
from keys import create_key_rects, draw_keys
from sounds import load_sounds
from buttons import Button
from ui.settings_menu import SettingsMenu
sounds = load_sounds(KEYS)
keys_list = list(KEYS.keys())

pressed = set()
key_rects = create_key_rects(7)

screen_mode = "main"
settings_menu = None
current_volume = 0.5

def set_volume(val):
    for sound in sounds.values():
        try:
            sound.set_volume(val)
        except Exception:
            pass
set_volume(current_volume)

def apply_settings(volume: float, *_):
    global current_volume
    current_volume = float(max(0.0, min(1.0, volume)))
    set_volume(current_volume)

def open_settings():
   global screen_mode, settings_menu
   screen_mode = "settings"
   settings_menu = SettingsMenu(
      screen.get_rect(),
      initial_volume=current_volume,
      on_change=apply_settings,
      on_back=_back_to_main,
      
   )


def _back_to_main():
   global screen_mode, settings_menu
   screen_mode = "main"
   settings_menu = None

init()
my_font = font.Font(None, 36)
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
settings_img = image.load("assets/images/buttons/settings_hover.png").convert_alpha()
settings_img = transform.scale(settings_img, (50, 50))
display.set_caption("Fortepiano")
running = True

buttons = [
   Button(
      700, 20, settings_img, action=open_settings
   )
]

while running:
   screen.fill(WHITE)
   if screen_mode == "settings" and settings_menu:
      settings_menu.draw(screen, my_font)
   else:
      for button in buttons:
         button.draw(screen)
      draw_keys(screen, key_rects, pressed)

   display.flip()

   for e in event.get():
      if e.type == QUIT:
         running = False
      if screen_mode == "settings" and settings_menu:
         settings_menu.handle_event(e)
         continue
      for button in buttons:
         button.handle_event(e)
      if e.type == KEYDOWN:
         k = key.name(e.key)
         if k in sounds:
            sounds[k].play()
            pressed.add(keys_list.index(k))

      if e.type == KEYUP:
         k = key.name(e.key)
         if k in sounds:
            pressed.discard(keys_list.index(k))

      if e.type == MOUSEBUTTONDOWN:
         for i, rect in enumerate(key_rects):
            if rect.collidepoint(e.pos):
               sounds[keys_list[i]].play()
               pressed.add(i)

      if e.type == MOUSEBUTTONUP:
         for i, rect in enumerate(key_rects):
            if i in pressed and rect.collidepoint(e.pos):
               pressed.remove(i)
from pygame import Rect, transform, image
from effects import spawn_flying_notes, update_and_draw_flying_notes

KEY_UNPRESSED = transform.scale(image.load("assets/images/key_unpressed.png"), (100, 250))

NOTE_BY_INDEX = {
    0: "C",
    1: "D",
    2: "E"
}

PREV_PRESSED = set()

def draw_keys(screen, key_rects, pressed_keys):
    global PREV_PRESSED
    pressed_set = set(pressed_keys)
    for i, rect in enumerate(key_rects):
        is_pressed = i in pressed_keys
        screen.blit(KEY_UNPRESSED, (rect.x, rect.y))
        if is_pressed and i not in PREV_PRESSED:
            spawn_flying_notes(rect, NOTE_BY_INDEX.get(i))
    PREV_PRESSED = pressed_set
    update_and_draw_flying_notes(screen)


def create_key_rects(num_keys, start_x=50, start_y=100, key_width=100, key_height=250):
    rects = []
    for i in range(num_keys):
        x = start_x + i * key_width
        rects.append(Rect(x, start_y, key_width, key_height))
    return rects
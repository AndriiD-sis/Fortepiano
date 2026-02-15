from pygame import draw, transform, image
from settings import BLACK

c_image = transform.scale(image.load("assets/images/notes/c.png"), (50, 50))
d_image = transform.scale(image.load("assets/images/notes/d.png"), (50, 50))
e_image = transform.scale(image.load("assets/images/notes/e.png"), (50, 50))

NOTE_IMAGES = {
    "c": c_image,
    "d": d_image,
    "e": e_image
}

FLYING_NOTES = []

def spawn_flying_note(rect, note_name: str | None):
    if not note_name:
        return
    img = NOTE_IMAGES.get(note_name)
    if not img:
        return
    x = rect.centerx = img.get_width() // 2
    y = rect.y - img.get_height() - 10
    FLYING_NOTES.append({"img": img, "x": x, "y": y, "vy": -1})

def update_and_draw_flying_notes(screen):
    to_remove = []
    for n in FLYING_NOTES:
        n["y"] += n["vy"]
        screen.blit(n["img"], (n["x"], n["y"]))
        if n["y"] + n["img"].get_height() < 0:
            to_remove.append(n)
    for n in to_remove:
        FLYING_NOTES.remove(n)

def draw_key_effect(screen, rect, is_pressed=False):
    if not is_pressed:
        base_color = (220, 220, 220)
    else:
        base_color = (170, 220, 255)
    border_color = BLACK

    draw.rect(screen, base_color, rect, border_radius=8)
    draw.rect(screen, border_color, rect, 2, border_radius=8)
from pygame import draw, transform, image
from settings import BLACK

C_IMG = transform.scale(image.load("assets/images/notes/c.png"), (50, 50))
D_IMG = transform.scale(image.load("assets/images/notes/d.png"), (50, 50))
E_IMG = transform.scale(image.load("assets/images/notes/e.png"), (50, 50))
F_IMG = transform.scale(image.load("assets/images/notes/f.png"), (50, 50))
G_IMG = transform.scale(image.load("assets/images/notes/g.png"), (50, 50))
A_IMG = transform.scale(image.load("assets/images/notes/a.png"), (50, 50))
B_IMG = transform.scale(image.load("assets/images/notes/b.png"), (50, 50))

NOTE_IMAGES = {
    "C": C_IMG,
    "D": D_IMG,
    "E": E_IMG,
    "F": F_IMG,
    "G": G_IMG,
    "A": A_IMG,
    "B": B_IMG
}

FLYING_NOTES = []

def spawn_flying_notes(rect, note_name:str | None):
    if not note_name:
        return
    img = NOTE_IMAGES.get(note_name)
    if not img:
        return
    x = rect.centerx - img.get_width() // 2
    y = rect.top - img.get_height() - 10
    FLYING_NOTES.append({"image": img, "x": x, "y": y, "vy": -1})

def update_and_draw_flying_notes(screen):
    to_remove = []
    for n in FLYING_NOTES:
        n["y"] += n["vy"]
        screen.blit(n["image"], (n["x"], n["y"]))
        if n["y"] + n["image"].get_height() < 0:
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
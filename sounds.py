from pathlib import Path
from pygame import mixer

SOUNDS_DIR = Path(__file__).resolve().parent / "assets" / "sounds"

def load_sounds(keys):
    if not mixer.get_init():
        mixer.init()

    sounds = {}
    for key, filename in keys.items():
        sound_path = SOUNDS_DIR / filename
        sounds[key] = mixer.Sound(str(sound_path))
    return sounds
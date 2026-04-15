# main.py

print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
keyboard = KMKKeyboard()
from kmk.extensions.media_keys import MediaKeys


macros = Macros()
keyboard.modules.append(macros)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())



PINS = [board.GP3, board.GP4, board.GP2, board.GP1, board.GP0, board.GP7, board.GP28]


keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)



rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=2,
    rgb_order=(1, 0, 2),
    hue_default=100,
    sat_default=100,
    val_default=100,
    
)
keyboard.extensions.append(rgb)

encoder_handler.pins = ((board.GP27, board.GP26),) 


keyboard.keymap = [
    [KC.DELETE, KC.L, KC.SLASH, KC.C, KC.SPACE, KC.ENTER, KC.AUDIO_MUTE]
]

encoder_handler.map = [
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN),),
]

if __name__ == '__main__':
    keyboard.go()
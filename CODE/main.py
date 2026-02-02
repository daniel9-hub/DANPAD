# main.py

print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DirectPins
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)



PINS = [board.GP3, board.GP4, board.GP2, board.GP1, board.GP7, board.GP0, board.GP28]


    
keyboard.matrix = DirectPins(
    pins=PINS,
    value_when_pressed=False,
     diode_orientation=DiodeOrientation.COL2ROW,
)

keyboard.coord_mapping = [0,1,2,3,4,5,6]

encoder_handler.pins = ((board.GP27, board.GP26, None, False, 2),)

rgb = RGB(pixel_pin=board.GP29, 
          num_pixels=2,
          brightness=0.3,                   # reasonable default
          animation_mode=AnimationModes.STATIC
)

keyboard.extensions.append(rgb)

keyboard.keymap = [
    [KC.ESCAPE, KC.L, KC.SLASH, KC.C, KC.EXCLAIM, KC.ENTER, KC.AUDIO_MUTE]
]

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
]

if __name__ == '__main__':
    keyboard.go()
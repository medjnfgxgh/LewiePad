import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers

# setup
keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(Layers())

macros = Macros()
keyboard.modules.append(macros)

keyboard.extensions.append(MediaKeys())

rgb = RGB(pixel_pin=board.D7, num_pixels=2)
keyboard.extensions.append(rgb)
#rgb.set_rgb_fill(255, 255, 255)

holdtap = HoldTap()
keyboard.modules.append(holdtap)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

xxxx = KC.NO

# macros
KC_copy = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)

KC_paste = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.V),
    Release(KC.LCTL)
)

# pins
encoder_handler.pins = ((board.D5, board.D6, board.D4),)
keyboard.col_pins = (board.D10, board.D9, board.D8)
keyboard.row_pins = (board.D0, board.D1,board.D2 , board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# map
keyboard.keymap = [
    #number layer
    [KC.KP_7, KC.KP_8, KC.KP_9, 
     KC.KP_4, KC.KP_5, KC.KP_6, 
     KC.KP_1, KC.KP_2, KC.KP_3, 
     KC_copy, KC.KP_0, KC_paste], 
    #gaming layer
    [KC.Q, KC.W, KC.E, 
     KC.A, KC.S, KC.D, 
     KC.TAB, KC.Z, KC.X,
     KC.LSHIFT, KC.LCTRL, KC.SPACE]
]
encoder_handler.map = [
    [(KC.DELETE, KC.BSPACE, KC.DF(1))],
    [(KC.VOLU, KC.VOLD, KC.DF(0))]
]

# Start
if __name__ == '__main__':
    keyboard.go()
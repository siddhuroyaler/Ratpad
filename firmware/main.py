import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.oled import Oled, OledDisplayMode

keyboard = KMKKeyboard()

# --------- KEYS ----------
keyboard.matrix = KeysScanner(
    pins=[board.D0, board.D1, board.D2, board.D3, board.D4],
    value_when_pressed=False,
)

keyboard.keymap = [[
    KC.A,
    KC.B,
    KC.C,
    KC.D,
    KC.E,
]]

# --------- ENCODER ----------
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.D6, board.D7, board.D8),
)

encoder.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),)
]

# --------- RGB ----------
rgb = RGB(
    pixel_pin=board.D10,
    num_pixels=6,
    val_limit=100,
)
keyboard.extensions.append(rgb)

# --------- OLED ----------
oled = Oled(
    width=128,
    height=32,
    rotation=0,
    sda=board.SDA,
    scl=board.SCL,
    addr=0x3C,
)

oled.display_mode = OledDisplayMode.TXT
oled.corner_one = "Custom Pad"
oled.corner_two = "KMK"
oled.corner_three = "Layer 0"
oled.corner_four = "Ready"

keyboard.extensions.append(oled)

# --------- START ----------
if __name__ == "__main__":
    keyboard.go()

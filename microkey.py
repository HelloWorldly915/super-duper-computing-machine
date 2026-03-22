# This was designed for Microslop Bimbows machines
# Use on the Lock Screen
def on_button_pressed_a():
    led.stop_animation()
    keyboard.send_string("A") # Even though you think its useless, it actually is on the lock screen
    basic.pause(500)
    keyboard.send_string("00000") # Your password here
input.on_button_pressed(Button.A, on_button_pressed_a)
# Use for passkeys
def on_button_pressed_b():
    led.stop_animation()
    keyboard.send_string("00000") # Your password here
    control.wait_micros(6000)
input.on_button_pressed(Button.B, on_button_pressed_b)

keyboard.start_keyboard_service()
basic.show_icon(IconNames.HAPPY)

def on_gesture_tilt_left():
    radio.send_string("left")
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_received_string(receivedString):
    if receivedString == "left":
        basic.show_arrow(ArrowNames.WEST)
    elif receivedString == "right":
        basic.show_arrow(ArrowNames.EAST)
radio.on_received_string(on_received_string)

def on_gesture_tilt_right():
    radio.send_string("right")
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

basic.show_icon(IconNames.ANGRY)
radio.set_group(48)
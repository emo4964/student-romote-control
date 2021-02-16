input.onGesture(Gesture.TiltLeft, function () {
    radio.sendString("left")
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "left") {
        basic.showArrow(ArrowNames.West)
    } else if (receivedString == "right") {
        basic.showArrow(ArrowNames.East)
    }
})
input.onGesture(Gesture.TiltRight, function () {
    radio.sendString("right")
})
basic.showIcon(IconNames.Angry)
radio.setGroup(48)

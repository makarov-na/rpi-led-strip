from ledstrip_module import LedStrip, RGBColour
import time


def colourWipe(strip: LedStrip, colour: RGBColour, wait_ms=50):
    """Wipe colour across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColour(i, colour)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def wheel(pos):
    """Generate rainbow colours across 0-255 positions."""
    if pos < 85:
        return RGBColour(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return RGBColour(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return RGBColour(0, pos * 3, 255 - pos * 3)


def rainbow(strip: LedStrip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColour(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip: LedStrip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColour(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip: LedStrip, colour: RGBColour, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColour(i + q, colour)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColour(i + q, RGBColour(0, 0, 0))


def theaterChaseRainbow(strip: LedStrip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColour(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColour(i + q, RGBColour(0, 0, 0))


# Main program logic follows:
if __name__ == '__main__':

    strip = LedStrip()

    while True:
        colour = RGBColour(0, 0, 255)
        colourWipe(strip, colour, wait_ms=50)
        print('Color wipe animations.')
        colourWipe(strip, RGBColour(255, 0, 0))  # Red wipe
        colourWipe(strip, RGBColour(0, 255, 0))  # Blue wipe
        colourWipe(strip, RGBColour(0, 0, 255))  # Green wipe
        print('Theater chase animations.')
        theaterChase(strip, RGBColour(127, 127, 127))  # White theater chase
        theaterChase(strip, RGBColour(127, 0, 0))  # Red theater chase
        theaterChase(strip, RGBColour(0, 0, 127))  # Blue theater chase
        print('Rainbow animations.')
        rainbow(strip)
        rainbowCycle(strip)
        theaterChaseRainbow(strip)

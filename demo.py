from ledstrip_module import LedStrip, RGBColour
import time

def colourWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)



# Main program logic follows:
if __name__ == '__main__':

    strip = LedStrip()

    while True:
        colour = RGBColour(0, 0, 255)
        colourWipe(strip, colour, wait_ms=50)



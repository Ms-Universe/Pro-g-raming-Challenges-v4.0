import os
import time

from gol import GOL


def main():
    width, height = os.get_terminal_size()
    gol = GOL(width, height)
    gol.simulate()
    gol.set_up_screen()
    input()
    while True:
        gol.simulate()
        gol.draw()
        time.sleep(.5)


if __name__ == "__main__":
    main()

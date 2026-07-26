import string
import time

import keyboard

CANCEL_KEY = "esc"
DELAY_BETWEEN_LETTERS = 0


def main():
    delay_before_start = 5

    print(f"Start in {delay_before_start} seconds - switch to the desired window...")
    print(f"To stop typing at any time, press '{CANCEL_KEY}'.")
    for i in range(delay_before_start, 0, -1):
        print(i)
        time.sleep(1)

    print("Start typing (repeat the alphabet until cancel is pressed)...")

    while not keyboard.is_pressed(CANCEL_KEY):
        keyboard.write(string.ascii_lowercase, delay=DELAY_BETWEEN_LETTERS)
        if keyboard.is_pressed(CANCEL_KEY):
            break

    print(f"Stopped (pressed '{CANCEL_KEY}').")


if __name__ == "__main__":
    main()
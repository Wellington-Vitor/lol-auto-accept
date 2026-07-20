from threading import Thread
from time import sleep

import pyautogui

from ui import theme
from core.image_search import check_screen_accept


class Bot:

    def __init__(self, window, status_label):

        self.running = False

        self.window = window
        self.status_label = status_label

    def start(self):

        if self.running:
            return

        self.running = True

        self.update_status(
            theme.STATUS_SEARCHING_TEXT,
            theme.STATUS_SEARCHING
        )

        Thread(
            target=self.loop,
            daemon=True
        ).start()

    def stop(self):

        self.running = False

        self.update_status(
            theme.STATUS_STOPPED_TEXT,
            theme.STATUS_STOPPED
        )

    def update_status(self, text, color):

        self.window.after(
            0,
            lambda: self.status_label.config(
                text=text,
                fg=color
            )
        )

    def loop(self):

        while self.running:

            button = check_screen_accept()

            if button:

                pyautogui.click(
                    pyautogui.center(button)
                )

                self.update_status(
                    theme.STATUS_ACCEPTED_TEXT,
                    theme.STATUS_ACCEPTED
                )

                while self.running:

                    if not check_screen_accept():
                        break

                    sleep(0.2)

            else:

                self.update_status(
                    theme.STATUS_SEARCHING_TEXT,
                    theme.STATUS_SEARCHING
                )

            sleep(0.5)
import threading
from time import sleep

import pyautogui

from core.bot import Bot
from core.image_search import check_screen_accept

from ui import theme
from ui.window import create_window, create_buttons


# ==========================
# Interface
# ==========================

window, status_label = create_window()

bot = Bot(window, status_label)


def bot_loop():

    while bot.running:

        button = check_screen_accept()

        if button:

            pyautogui.click(pyautogui.center(button))

            bot.update_status(
                theme.STATUS_ACCEPTED_TEXT,
                theme.STATUS_ACCEPTED
            )

            while bot.running:

                if not check_screen_accept():
                    break

                sleep(0.2)

        else:

            bot.update_status(
                theme.STATUS_SEARCHING_TEXT,
                theme.STATUS_SEARCHING
            )

        sleep(0.5)


def start_bot():

    if bot.running:
        return

    bot.start()

    start_button.config(state="disabled")
    stop_button.config(state="normal")

    bot.update_status(
        theme.STATUS_SEARCHING_TEXT,
        theme.STATUS_SEARCHING
    )

    threading.Thread(
        target=bot_loop,
        daemon=True
    ).start()


def stop_bot():

    bot.stop()

    start_button.config(state="normal")
    stop_button.config(state="disabled")

    bot.update_status(
        theme.STATUS_STOPPED_TEXT,
        theme.STATUS_STOPPED
    )


start_button, stop_button = create_buttons(
    window,
    start_bot,
    stop_bot
)

window.mainloop()
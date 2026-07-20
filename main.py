import threading

from core.bot import Bot

from ui.window import create_window, create_buttons


# ==========================
# Interface
# ==========================

window, status_label = create_window()

bot = Bot(window, status_label)


def start_bot():

    start_button.config(state="disabled")
    stop_button.config(state="normal")

    bot.start()


def stop_bot():

    start_button.config(state="normal")
    stop_button.config(state="disabled")

    bot.stop()


start_button, stop_button = create_buttons(
    window,
    start_bot,
    stop_bot
)

window.mainloop()
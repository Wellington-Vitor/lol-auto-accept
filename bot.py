import os
import sys
import threading
from time import sleep
from tkinter import Tk, Label, Button, Frame

import pyautogui

from ui import theme

ACCEPT_IMAGES = [
    "assets/aceitar1.png",
    "assets/aceitar2.png",
    "assets/aceitar3.png",
    "assets/aceitar4.png",
]

running = False


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


def update_status(text, color):
    window.after(
        0,
        lambda: status_label.config(
            text=text,
            fg=color
        )
    )


def check_screen_accept():
    for image in ACCEPT_IMAGES:
        try:
            button = pyautogui.locateOnScreen(
                resource_path(image),
                confidence=0.7
            )

            if button:
                return button

        except pyautogui.ImageNotFoundException:
            pass

    return None


def bot_loop():
    global running

    while running:

        button = check_screen_accept()

        if button:

            pyautogui.click(pyautogui.center(button))

            update_status(
                theme.STATUS_ACCEPTED_TEXT,
                theme.STATUS_ACCEPTED
            )

            while running:
                if not check_screen_accept():
                    break
                sleep(0.2)

        else:

            update_status(
                theme.STATUS_SEARCHING_TEXT,
                theme.STATUS_SEARCHING
            )

        sleep(0.5)


def start_bot():
    global running

    if running:
        return

    running = True
    start_button.config(state="disabled")
    stop_button.config(state="normal")

    update_status(
        theme.STATUS_SEARCHING_TEXT,
        theme.STATUS_SEARCHING
    )

    threading.Thread(
        target=bot_loop,
        daemon=True
    ).start()


def stop_bot():
    global running

    running = False
    start_button.config(state="normal")
    stop_button.config(state="disabled")

    update_status(
        theme.STATUS_STOPPED_TEXT,
        theme.STATUS_STOPPED
    )

# ==========================
# Interface
# ==========================

window = Tk()
window.iconbitmap(resource_path("icon.ico"))
window.title(theme.WINDOW_TITLE)
window.geometry(theme.WINDOW_SIZE)
window.configure(bg=theme.BACKGROUND)
window.resizable(False, False)

welcome_label = Label(
    window,
    text=theme.TITLE_TEXT,
    font=theme.TITLE_FONT,
    fg=theme.TITLE_COLOR,
    bg=theme.BACKGROUND
)
welcome_label.pack(pady=(20, 10))

status_label = Label(
    window,
    text=theme.STATUS_READY_TEXT,
    font=theme.STATUS_FONT,
    fg=theme.STATUS_READY,
    bg=theme.BACKGROUND
)
status_label.pack(pady=(5, 20))

button_frame = Frame(
    window,
    bg=theme.BACKGROUND
)
button_frame.pack()

start_button = Button(
    button_frame,
    text=theme.START_BUTTON_TEXT,
    command=start_bot,
    bg=theme.BUTTON_START,
    fg=theme.BUTTON_TEXT,
    activebackground=theme.BUTTON_START_ACTIVE,
    activeforeground=theme.BUTTON_TEXT,
    relief="flat",
    width=theme.BUTTON_WIDTH,
    cursor="hand2"
)
start_button.pack(side="left", padx=10)

stop_button = Button(
    button_frame,
    text=theme.STOP_BUTTON_TEXT,
    command=stop_bot,
    bg=theme.BUTTON_STOP,
    fg=theme.BUTTON_TEXT,
    activebackground=theme.BUTTON_STOP_ACTIVE,
    activeforeground=theme.BUTTON_TEXT,
    relief="flat",
    width=theme.BUTTON_WIDTH,
    cursor="hand2"
)
stop_button.pack(side="left", padx=10)

window.mainloop()
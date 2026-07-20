from tkinter import Tk, Label, Button, Frame

from ui import theme
from core.utils.resource import resource_path


def create_window():

    window = Tk()

    window.title(theme.WINDOW_TITLE)
    window.geometry(theme.WINDOW_SIZE)
    window.configure(bg=theme.BACKGROUND)
    window.resizable(False, False)

    try:
        window.iconbitmap(resource_path("icon.ico"))
    except Exception:
        pass

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

    return window, status_label


def create_buttons(window, start_command, stop_command):

    button_frame = Frame(
        window,
        bg=theme.BACKGROUND
    )
    button_frame.pack()

    start_button = Button(
        button_frame,
        text=theme.START_BUTTON_TEXT,
        command=start_command,
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
        command=stop_command,
        bg=theme.BUTTON_STOP,
        fg=theme.BUTTON_TEXT,
        activebackground=theme.BUTTON_STOP_ACTIVE,
        activeforeground=theme.BUTTON_TEXT,
        relief="flat",
        width=theme.BUTTON_WIDTH,
        cursor="hand2",
        state="disabled"
    )
    stop_button.pack(side="left", padx=10)

    return start_button, stop_button
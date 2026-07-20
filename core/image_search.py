import os
import sys
from core.utils.resource import resource_path
import pyautogui

ACCEPT_IMAGES = [
    "assets/aceitar1.png",
    "assets/aceitar2.png",
    "assets/aceitar3.png",
    "assets/aceitar4.png",
]

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
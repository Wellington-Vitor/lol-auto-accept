import pyautogui


def find_champion(name):
    image = f"assets/champions/{name.upper()}.png"

    return pyautogui.locateOnScreen(
        image,
        confidence=0.8
    )


def click_champion(name):
    champion = find_champion(name)

    if champion:
        pyautogui.click(
            pyautogui.center(champion)
        )
        return True

    return False

def find_search():
    return pyautogui.locateOnScreen(
        "assets/search.png",
        confidence=0.8
    )
    
def click_search():

    search = find_search()

    if search:
        pyautogui.click(pyautogui.center(search))
        return True

    return False

def search_champion(name):

    if not click_search():
        return False

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(name, interval=0.03)

    return True

def auto_pick(name):

    if not search_champion(name):
        return False

    pyautogui.sleep(0.3)

    return click_champion(name)
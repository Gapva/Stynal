import pygetwindow as gw
import pyautogui
import pyperclip
from plyer import notification as notif
from time import sleep
import typer
from typing_extensions import Annotated
from os import listdir

app = typer.Typer()

err = False

def wdur():
    sleep(1) # one whole second just to be safe

def cnotif(title: str, text: str):
    try:
        notif.notify(
            title=title,
            message=text,
            app_name="Stynal",
            app_icon="./assets/stynal.ico"
        )
    except:
        print("Failed to throw notification")

@app.command()
def apply(theme: Annotated[str, typer.Argument(help="The path of the Signal theme (e.g. 'themes\\theme.css')")], flavor: Annotated[str, typer.Argument(help="The flavored branch of Signal (e.g. 'beta')")] = "stable"):
    """
    Apply a theme to your Signal Desktop application
    """
    target = "Signal"
    match flavor.lower().strip():
        case "beta":
            target += " Beta"
    # find target
    global err
    err = False
    try:
        test = gw.getWindowsWithTitle(target)[0]
        del test
    except:
        err = True
    if not err:
        # cnotif("Applying theme", "Please be patient while your theme is being applied.")
        # focus
        gw.getWindowsWithTitle(target)[0].activate()
        wdur()
        pyautogui.hotkey('ctrl', 'shift', 'i') # open devtools
        wdur(); wdur() # might need to wait double here
        pyautogui.hotkey('ctrl', 'shift', 'c') # focus devtools
        pyautogui.press('tab', presses=14) # navi to most recent manifest locator
        pyautogui.press('enter') # confirm selection
        wdur()
        pyautogui.press('tab', presses=4) # navi to most recent manifest locator
        pyautogui.hotkey('ctrl', 'a') # focus devtools
        pyperclip.copy(open(f"{theme}", 'r').read())
        wdur()
        pyautogui.hotkey('ctrl', 'v') # paste theme data
        wdur(); wdur() # might need to wait double here
        pyautogui.hotkey('ctrl', 'shift', 'i') # close devtools
        pyautogui.hotkey('alt', 'tab') # switch back to cli
        print("Theme applied")
        # cnotif("Theme applied", "The theme was successfully applied.")
    else:
        print(f"Failed to apply theme (could not locate a {target} instance)")
        print("\nTroubleshooting:")
        print(f"- Ensure that {target} is open and visible on your taskbar, not just minimized to the system tray.")
        print(f"- {target}'s window must be accessible on your screen, even if it's not the active window.")

@app.command()
def list(dir: Annotated[str, typer.Argument(help="The directory you want to scan for themes (e.g. 'themes')")]):
    """
    List all available themes in a directory
    """
    themes = [f"- {theme}" for theme in listdir(dir) if theme.endswith('.css')]
    print(', '.join(themes))

if __name__ == "__main__":
    app()

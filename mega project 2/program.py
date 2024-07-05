import pyautogui
import pyperclip
import time

try:
    # Move the mouse to the chrome icon location and click
    pyautogui.moveTo(1424, 1044, duration=1)  # move to icon location in 1 second
    pyautogui.click()
    time.sleep(0.5)  # wait for 0.5 seconds

    # Drag the mouse to select the text
    pyautogui.moveTo(1336, 237, duration=1)  # move to start of selection in 1 second
    pyautogui.mouseDown()
    pyautogui.moveTo(1806, 924, duration=2)  # drag to end of selection in 2 seconds
    pyautogui.mouseUp()
    time.sleep(0.5)  # wait for 0.5 seconds

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # wait for 0.5 seconds

    # Get the text from the clipboard
    selected_text = pyperclip.paste()

    print("Selected text: ", selected_text)

except KeyboardInterrupt:
    print('\nDone')
import tkinter as tk
from gui_functions import program_calibrate, calibrate_continue, add_swash
from pynput import mouse


# make the main window for stuff to run in
def make_base():
    window = tk.Tk()
    window.resizable = False
    window.attributes("-topmost", True)

    # listen for mouse events during calibration (and forever after that because i'm lazy and this is unimportant)
    calibration_recorder = mouse.Listener(on_click=add_swash)
    calibration_recorder.start()

    # all layouts
    tk.Label(window, name="title", text="Calibrate the program and\nselect an image, and then click Go!")

    # home
    tk.Button(window, text="Calibrate", name="calibrate", command=lambda: program_calibrate(window))
    tk.Button(window, text="Select image", name="browse")
    tk.Button(window, text="Go!", name="go")

    # calibration
    #   select swashes
    tk.Button(window, name="calibrate_continue", text="Continue", command=lambda: calibrate_continue())
    tk.Button(window, name="calibrate_restart", text="Restart")

    return window

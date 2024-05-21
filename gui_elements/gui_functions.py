swashes = []


# hide a widget
def hide(widget_name):
    global root
    root.nametowidget(widget_name).pack_forget()


# show a widget
def show(widget_name):
    global root
    root.nametowidget(widget_name).pack()


# change the title/ instructions
def retitle(text):
    global root
    root.nametowidget("title").configure(text=text)


# add a swash to the swashes list
def add_swash(a, b, c, d):
    global root
    global swashes
    if str(c) == "Button.left" and d:
        swashes.append((a, b))


# continue with the calibration process from swashes to canvas
def calibrate_continue():
    global swashes
    del swashes[-1]
    print(swashes)


# hide every widget
def clean():
    global root

    for child in root.children:
        hide(child)


# show the listed widgets
def populate(widget_list):
    global root

    clean()
    for widget in widget_list:
        show(widget)

    root.update()


# run the calibration function
def program_calibrate(window):
    global root
    global swashes
    root = window
    swashes = []
    stage = "add_swashes"

    # calibration screen
    show("title")
    show("calibrate")
    retitle("click on each of the\nswashes and then click continue")
    populate(["title", "calibrate_continue", "calibrate_restart"])


# load the home screen
def home_layout(window):
    global root
    root = window

    retitle("Calibrate the program and\nselect an image, and then click Go!")
    populate(["title", "calibrate", "browse", "go"])



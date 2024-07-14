from guiFunctions import *
from gui_fonts import *
from calibrators import Calibrator

# calibrator
calibrator = Calibrator()

# Window
root = CTk()
root.geometry("450x250")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(False, False)
root.wm_attributes("-topmost", True)

# Frames
welcomePage = make_frame(root)
color_calibrate = make_frame(root)
frame_calibrate = make_frame(root)
upload_img = make_frame(root)
exit_page = make_frame(root)

# Welcome page
CTkLabel(welcomePage, text="Welcome to AutoPixelPaint!", font=title).pack()
CTkButton(welcomePage, text="Begin", font=body, command=color_calibrate.tkraise).pack(side="bottom", pady=20)

# Calibrate colors
CTkLabel(color_calibrate, text="Click on each color swash in the \napplication that would like to use.", font=title).pack()

c_cal_buttons_frame = CTkFrame(color_calibrate, fg_color="transparent")
c_cal_buttons_frame.pack(pady=20)

for button_text, cmd in (("Reset", calibrator.color_cal_reset), ("Finish", calibrator.color_cal_finish)):
    CTkButton(c_cal_buttons_frame, text=button_text, command=cmd).pack(side="left", padx=10)

# raise the welcome page to start
welcomePage.tkraise()

root.mainloop()

from customtkinter import *


def make_frame(root, create_margin=True):
    """
    Generates a frame that you can tkraise() for switchable frames

    :param root: master that you want the frame to go into
    :param create_margin: if you want to add margins to the frame (default True)
    :return: the frame object created
    """
    frame = CTkFrame(root, fg_color="transparent")
    frame.grid(row=0, column=0, sticky="news")

    # make a margin
    if create_margin:
        for side in ("bottom", "top"):
            CTkLabel(frame, text="").pack(fill="x", expand=True, side=side)
    return frame

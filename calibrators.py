from pynput import mouse
import overlay_lib as overlay


class Calibrator:
    def __init__(self):
        self.picking_colors = False
        self.swash_locations = []

        # start watching the mouse
        self.listener = mouse.Listener(on_click=self.mouse_click)

    def draw_overlay_circles(self):
        circles = []
        for x, y in self.swash_locations:
            circles.append(overlay.SkDrawCircle(overlay.Vector2D(x, y), 5, overlay.RgbaColor(255, 0, 0, 255), 5))

        def callback():
            return circles

        tmp = overlay.Overlay(
            drawlistCallback=callback,
            refreshTimeout=500
        )
        tmp.spawn()

    def mouse_click(self, x, y, button, pressed):
        """function to run when the user clicks. used for both swashes and frames."""

        if button == mouse.Button.left and pressed and self.picking_colors:  # if left click
            if self.picking_colors:
                self.swash_locations.append((x, y))  # add the position to the swashes
                self.draw_overlay_circles()

    def color_cal_begin(self):
        """begin color calibration"""
        self.picking_colors = True

        # start the mouse listener
        if not self.listener.is_alive():
            self.listener.start()

    def color_cal_finish(self):
        """end color calibration if the user has picked at least one swash
        :returns: True if the user has picked at least one swash, None otherwise"""

        # if there are swashes picked
        if len(self.swash_locations) > 0:
            self.picking_colors = False


            # stop listening to the mouse
            if self.listener.is_alive():
                self.listener.stop()

            return True

    def color_cal_reset(self):
        """clear out the swash locations and restart picking"""
        print("reset color calibration!")

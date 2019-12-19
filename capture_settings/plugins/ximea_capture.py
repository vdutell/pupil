"""
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2019 Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
"""

from plugin import Plugin
from pyglui.cygl.utils import draw_points_norm, RGBA
from pyglui import ui


class Ximea_Capture(Plugin):
    """
    Ximea Capture captures frames from a Ximea camera
    during collection in parallel with world camera
    """
    icon_chr = chr(0xEC22)
    icon_font = "pupil_icons"

    def __init__(self, g_pool, record_ximea=True, serial_num='XECAS1930001'):
        super().__init__(g_pool)
        self.order = 0.8
        #self.pupil_display_list = []

        self.record_ximea = record_ximea
        self.serial_num = serial_num

    # def recent_events(self, events):
    #     #for pt in events.get("gaze", []):
    #     #    self.pupil_display_list.append((pt["norm_pos"], pt["confidence"] * 0.8))
    #     #self.pupil_display_list[:-3] = []
    #     pass


    def init_ui(self):
        self.add_menu()
        self.menu.label = "Ximea Cpature"
        self.update_menu()

    def deinit_ui(self):
        self.remove_menu()


    def gl_display(self):
        #for pt, a in self.pupil_display_list:
            # This could be faster if there would be a method to also add multiple colors per point
            #draw_points_norm([pt], size=35, color=RGBA(1.0, 0.2, 0.4, a))
        pass

    def get_init_dict(self):
        return {}


    def update_menu(self):

        del self.menu.elements[:]

        def set_iface(record_ximea):
            self.record_ximea = record_ximea
            self.update_menu()

        if self.record_ximea:

            def set_serial_num(new_serial_num):
                self.serial_num = new_serial_num
                self.update_menu()

        else:
            self.update_menu()

        help_str = "Ximea Capture Captures frames from Ximea Cameras in Parallel with Record."
        self.menu.append(ui.Info_Text(help_str))
        self.menu.append(
            ui.Switch(
                "record_ximea",
                self,
                setter=set_iface,
                label="Record From Ximea Cameras",
            )
        )
        if self.record_ximea:
            self.menu.append(ui.Text_Input("serial_num", self, setter=set_serial_num, label="Serial Number"))

        else:
            self.menu.append(ui.Text_Input("No Camera Selected"))

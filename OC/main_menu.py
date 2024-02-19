''' En esta parte del codigo importo la clase pricipal y le asocio el evento de cierre'''

import wx
from comic_managerBK import frameMain
import sys

class main_menu(frameMain):
    def __init__(self, *args, **kw):
        super(main_menu, self).__init__(*args, **kw)

        self.Bind(wx.EVT_MENU, self.on_exit_select, id = frameMain.menu_main_file_exit.GetId())

    def on_exit_select():
        sys.exit()


    
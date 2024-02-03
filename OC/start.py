'''
<a href="https://www.flaticon.es/iconos-gratis/sav" title="sav iconos">Sav iconos creados por IconMarketPK - Flaticon</a>
'''
import wx
from comic_manager import *



class MainApp(wx.App):
	def OnInit(self):
		mainFrame = frameMain(None)
		mainFrame.Show(True)
		return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()
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
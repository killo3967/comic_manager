# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.grid

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"COMIC MANAGER", pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.DragAcceptFiles( True )

		self.menubar_Main = wx.MenuBar( 0 )
		self.menu_Main_File = wx.Menu()
		self.menu_main_file_newfile = wx.MenuItem( self.menu_Main_File, wx.ID_ANY, u"New File", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_main_file_newfile.SetBitmap( wx.Bitmap( u"icons/open_folder.png", wx.BITMAP_TYPE_ANY ) )
		self.menu_Main_File.Append( self.menu_main_file_newfile )

		self.menu_main_file_openfile = wx.MenuItem( self.menu_Main_File, wx.ID_ANY, u"Open File...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_Main_File.Append( self.menu_main_file_openfile )

		self.menu_main_file_save = wx.MenuItem( self.menu_Main_File, wx.ID_ANY, u"Save"+ u"\t" + u"CTRL+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_Main_File.Append( self.menu_main_file_save )

		self.menu_main_file_saveas = wx.MenuItem( self.menu_Main_File, wx.ID_ANY, u"Save as...", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_Main_File.Append( self.menu_main_file_saveas )

		self.menu_Main_File.AppendSeparator()

		self.menu_main_file_exit = wx.MenuItem( self.menu_Main_File, wx.ID_ANY, u"Exit"+ u"\t" + u"CTRL+X", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_main_file_exit.SetBitmap( wx.Bitmap( u"exit-white.png", wx.BITMAP_TYPE_ANY ) )
		self.menu_Main_File.Append( self.menu_main_file_exit )

		self.menubar_Main.Append( self.menu_Main_File, u"File" )

		self.menu_Main_Edit = wx.Menu()
		self.m_edit_new_panel = wx.Menu()
		self.menu_main_edit_new_panel_directories = wx.MenuItem( self.m_edit_new_panel, wx.ID_ANY, u"Directory", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit_new_panel.Append( self.menu_main_edit_new_panel_directories )

		self.menu_main_edit_new_panel_viewers = wx.MenuItem( self.m_edit_new_panel, wx.ID_ANY, u"Viewers", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit_new_panel.Append( self.menu_main_edit_new_panel_viewers )

		self.menu_main_edit_new_panel_library = wx.MenuItem( self.m_edit_new_panel, wx.ID_ANY, u"Library", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit_new_panel.Append( self.menu_main_edit_new_panel_library )

		self.menu_main_edit_new_panel_shelf = wx.MenuItem( self.m_edit_new_panel, wx.ID_ANY, u"Shelf", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit_new_panel.Append( self.menu_main_edit_new_panel_shelf )

		self.menu_main_edit_new_panel_pages = wx.MenuItem( self.m_edit_new_panel, wx.ID_ANY, u"Pages", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit_new_panel.Append( self.menu_main_edit_new_panel_pages )

		self.menu_main_edit_new_panel_comicviewer = wx.MenuItem( self.m_edit_new_panel, wx.ID_ANY, u"Comic Viewer", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit_new_panel.Append( self.menu_main_edit_new_panel_comicviewer )

		self.menu_main_edit_new_panel_metadata = wx.MenuItem( self.m_edit_new_panel, wx.ID_ANY, u"Metadata", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_edit_new_panel.Append( self.menu_main_edit_new_panel_metadata )

		self.menu_Main_Edit.AppendSubMenu( self.m_edit_new_panel, u"New Panel" )

		self.menubar_Main.Append( self.menu_Main_Edit, u"Edit" )

		self.menu_Main_Utilities = wx.Menu()
		self.menu_main_Utilities_Check_Comic_Integrity = wx.MenuItem( self.menu_Main_Utilities, wx.ID_ANY, u"Check Comic Integrity", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_Main_Utilities.Append( self.menu_main_Utilities_Check_Comic_Integrity )

		self.menuUtilities_Repair_Comic = wx.MenuItem( self.menu_Main_Utilities, wx.ID_ANY, u"Repair Comic", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_Main_Utilities.Append( self.menuUtilities_Repair_Comic )

		self.menuUtilities_Remove_ADS = wx.MenuItem( self.menu_Main_Utilities, wx.ID_ANY, u"Remove ADS", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_Main_Utilities.Append( self.menuUtilities_Remove_ADS )

		self.menubar_Main.Append( self.menu_Main_Utilities, u"Utilities" )

		self.menuMain_Configuration = wx.Menu()
		self.menu_main_configuration_configuration = wx.MenuItem( self.menuMain_Configuration, wx.ID_ANY, u"Generic Configuration", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuMain_Configuration.Append( self.menu_main_configuration_configuration )

		self.menu_main_configuration_displayoptions = wx.MenuItem( self.menuMain_Configuration, wx.ID_ANY, u"Display Options", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuMain_Configuration.Append( self.menu_main_configuration_displayoptions )

		self.m_menu1 = wx.Menu()
		self.menu_main_configuration_addprofile = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Add Profile", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menu_main_configuration_addprofile )

		self.menu_main_configuration_delprofile = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Delete Profife", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menu_main_configuration_delprofile )

		self.menu_main_configuration_cloneprofile = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Clone Profile", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menu_main_configuration_cloneprofile )

		self.menuMain_Configuration.AppendSubMenu( self.m_menu1, u"Mange Profiles" )

		self.menubar_Main.Append( self.menuMain_Configuration, u"Configuration" )

		self.menuPlugins = wx.Menu()
		self.menuPlugin_Repository = wx.MenuItem( self.menuPlugins, wx.ID_ANY, u"Plugin Repository", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuPlugins.Append( self.menuPlugin_Repository )

		self.menuPlugin_manage = wx.MenuItem( self.menuPlugins, wx.ID_ANY, u"Manage Plugin", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuPlugins.Append( self.menuPlugin_manage )

		self.menubar_Main.Append( self.menuPlugins, u"Plugins" )

		self.menuFileHelp = wx.Menu()
		self.menuHelp_onlinehelp = wx.MenuItem( self.menuFileHelp, wx.ID_ANY, u"OnLine Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFileHelp.Append( self.menuHelp_onlinehelp )

		self.menuHelp_about = wx.MenuItem( self.menuFileHelp, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFileHelp.Append( self.menuHelp_about )

		self.menubar_Main.Append( self.menuFileHelp, u"Help" )

		self.SetMenuBar( self.menubar_Main )

		bSizer_FrameMain = wx.BoxSizer( wx.HORIZONTAL )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.auiToolBar_Main = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.aui.AUI_TB_HORZ_LAYOUT )
		self.auiToolBar_Main.SetMargins( wx.Size( 0,0 ) )
		self.auiToolBar_Main.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.auiToolBar_Main.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.tool_open_folder = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/open_folder.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool2 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool3 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool4 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool5 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.auiToolBar_Main.AddSeparator()

		self.m_tool6 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool7 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool8 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool9 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool10 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool11 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.auiToolBar_Main.AddSeparator()

		self.m_tool12 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool13 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool14 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool15 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool16 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool17 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_tool18 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.auiToolBar_Main.AddSeparator()

		self.m_tool19 = self.auiToolBar_Main.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/exit.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.auiToolBar_Main.Realize()

		bSizer14.Add( self.auiToolBar_Main, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer14, 0, wx.EXPAND, 0 )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.auinotebook_main = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.auinotebook_main_panel_directories = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_genericDirCtrl1 = wx.GenericDirCtrl( self.auinotebook_main_panel_directories, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl1.ShowHidden( False )
		bSizer5.Add( self.m_genericDirCtrl1, 1, wx.EXPAND |wx.ALL, 5 )


		self.auinotebook_main_panel_directories.SetSizer( bSizer5 )
		self.auinotebook_main_panel_directories.Layout()
		bSizer5.Fit( self.auinotebook_main_panel_directories )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_directories, u"Directories", True, wx.NullBitmap )
		self.auinotebook_main_panel_viewers = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_viewers, u"Viewers", False, wx.NullBitmap )
		self.auinotebook_main_panel_library = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_library, u"Library", False, wx.NullBitmap )
		self.auinotebook_main_panel_shelf = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_shelf, u"Shelf", False, wx.NullBitmap )
		self.auinotebook_main_panel_pages = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid_pages = wx.grid.Grid( self.auinotebook_main_panel_pages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid_pages.CreateGrid( 5, 5 )
		self.m_grid_pages.EnableEditing( True )
		self.m_grid_pages.EnableGridLines( True )
		self.m_grid_pages.EnableDragGridSize( False )
		self.m_grid_pages.SetMargins( 0, 0 )

		# Columns
		self.m_grid_pages.EnableDragColMove( False )
		self.m_grid_pages.EnableDragColSize( True )
		self.m_grid_pages.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid_pages.EnableDragRowSize( True )
		self.m_grid_pages.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid_pages.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer8.Add( self.m_grid_pages, 0, wx.ALL|wx.EXPAND, 5 )


		self.auinotebook_main_panel_pages.SetSizer( bSizer8 )
		self.auinotebook_main_panel_pages.Layout()
		bSizer8.Fit( self.auinotebook_main_panel_pages )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_pages, u"Pages", False, wx.NullBitmap )
		self.auinotebook_main_panel_viewer = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )


		self.auinotebook_main_panel_viewer.SetSizer( bSizer6 )
		self.auinotebook_main_panel_viewer.Layout()
		bSizer6.Fit( self.auinotebook_main_panel_viewer )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_viewer, u"Comic Viewer", False, wx.NullBitmap )
		self.auinotebook_main_panel_metadata = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_metadata, u"Metadata", False, wx.NullBitmap )
		self.auinotebook_main_panel_configuration = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_configuration, u"Configuration", False, wx.NullBitmap )
		self.auinotebook_main_panel_Log = wx.Panel( self.auinotebook_main, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer81 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox1 = wx.CheckBox( self.auinotebook_main_panel_Log, wx.ID_ANY, u"Error", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox111 = wx.CheckBox( self.auinotebook_main_panel_Log, wx.ID_ANY, u"Warning", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_checkBox111, 0, wx.ALL, 5 )

		self.m_checkBox1111 = wx.CheckBox( self.auinotebook_main_panel_Log, wx.ID_ANY, u"Notice", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_checkBox1111, 0, wx.ALL, 5 )

		self.m_checkBox11111 = wx.CheckBox( self.auinotebook_main_panel_Log, wx.ID_ANY, u"Info", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_checkBox11111, 0, wx.ALL, 5 )

		self.m_checkBox111111 = wx.CheckBox( self.auinotebook_main_panel_Log, wx.ID_ANY, u"Debug", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_checkBox111111, 0, wx.ALL, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self.auinotebook_main_panel_Log, wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer9.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.auinotebook_main_panel_Log, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


		bSizer81.Add( bSizer9, 0, wx.ALL|wx.EXPAND, 5 )

		self.auinotebook_main_panel_Log_scrolledWindow = wx.ScrolledWindow( self.auinotebook_main_panel_Log, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.auinotebook_main_panel_Log_scrolledWindow.SetScrollRate( 5, 5 )
		bSizer81.Add( self.auinotebook_main_panel_Log_scrolledWindow, 1, wx.EXPAND |wx.ALL, 5 )


		self.auinotebook_main_panel_Log.SetSizer( bSizer81 )
		self.auinotebook_main_panel_Log.Layout()
		bSizer81.Fit( self.auinotebook_main_panel_Log )
		self.auinotebook_main.AddPage( self.auinotebook_main_panel_Log, u"Log", False, wx.NullBitmap )

		bSizer161.Add( self.auinotebook_main, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer15.Add( bSizer161, 1, wx.EXPAND, 0 )


		bSizer_FrameMain.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_FrameMain )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.menuItemFile_NewOnMenuSelection, id = self.menu_main_file_newfile.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemFile_File_OpenOnMenuSelection, id = self.menu_main_file_openfile.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemFile_SaveOnMenuSelection, id = self.menu_main_file_save.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemFile_Save_asOnMenuSelection, id = self.menu_main_file_saveas.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def menuItemFile_NewOnMenuSelection( self, event ):
		pass

	def menuItemFile_File_OpenOnMenuSelection( self, event ):
		pass

	def menuItemFile_SaveOnMenuSelection( self, event ):
		pass

	def menuItemFile_Save_asOnMenuSelection( self, event ):
		pass



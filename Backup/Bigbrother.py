# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BBMain
###########################################################################

class BBMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BigBrother - v0.1 alpha", pos = wx.DefaultPosition, size = wx.Size( 750,400 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Loaded picture", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 11, 77, 90, 91, False, "Ubuntu" ) )
		
		bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.FIXED_MINSIZE|wx.TOP|wx.BOTTOM, 15 )
		
		self.M_Pic_Frame = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"./res/1.jpg", wx.BITMAP_TYPE_ANY ), wx.Point( 20,20 ), wx.Size( 500,200 ), 0 )
		bSizer4.Add( self.M_Pic_Frame, 0, wx.RIGHT|wx.LEFT, 20 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Picture file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer5.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.M_Pic_Picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		bSizer5.Add( self.M_Pic_Picker, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 50 )
		
		
		bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Tesseract", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		bSizer6.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.M_Tesseract = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.M_Tesseract.SetMaxLength( 20 ) 
		bSizer6.Add( self.M_Tesseract, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Correction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer6.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.M_Correction = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.M_Correction, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.M_Validate = wx.Button( self, wx.ID_ANY, u"Validate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.M_Validate, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 40 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Tesseract Statistics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer6.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.M_Tessics = wx.StaticText( self, wx.ID_ANY, u"100%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.M_Tessics.Wrap( -1 )
		bSizer6.Add( self.M_Tessics, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer2.Add( bSizer6, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.M_Pic_Picker.Bind( wx.EVT_FILEPICKER_CHANGED, self.EventFileChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def EventFileChanged( self, event ):
		event.Skip()
	


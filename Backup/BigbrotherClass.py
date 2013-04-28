"""Subclass of BBMain, which is generated by wxFormBuilder."""

import wx
import Bigbrother
import tesseract
import locale

# Implementing BBMain
class BigbrotherClass( Bigbrother.BBMain ):
	def __init__( self, parent ):
		Bigbrother.BBMain.__init__( self, parent )
		locale.setlocale(locale.LC_ALL, 'C')
		# Init the Tesseract API
		api = tesseract.TessBaseAPI()
		api.Init(".","fra",tesseract.OEM_DEFAULT)
		api.SetVariable("tessedit_char_whitelist", "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		api.SetPageSegMode(tesseract.PSM_AUTO)

	
	# Handlers for BBMain events.
	def EventFileChanged( self, event ):
		# TODO: Implement EventFileChanged
		pass
	
	

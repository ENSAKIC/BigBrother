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
		self.api = tesseract.TessBaseAPI()
		self.api.Init(".","eng",tesseract.OEM_DEFAULT)
		self.api.SetVariable("tessedit_char_whitelist", "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		self.api.SetPageSegMode(tesseract.PSM_AUTO)
		#Tesseract API started !
		# TODO : Implement SQLite3 access to store data
	
	# Handlers for BBMain events.
	def EventFileChanged( self, event ):
		# When a new file is charged, do the following :
		# 1 - Get the file's location
		self.current_pic = self.M_Pic_Picker.GetPath()
		# 2 - Call Tesseract's API function to handle the new picture
		self.TesseractNewPic(self.current_pic)
		# 3 - Update GUI elements to handle the new data
		self.UpdateGUI()


	def TesseractNewPic(self,pathtopic):
		""" Function that handle the new picture loaded """
		self.mBuffer = open(pathtopic,"rb").read()
		self.readresult = tesseract.ProcessPagesBuffer(self.mBuffer,len(self.mBuffer),self.api)

	def UpdateGUI(self):
		""" Function that will update the GUI so it displays the new elements """
		# 1 - Update the picture's frame
		self.M_Pic_Frame.SetBitmap(wx.Bitmap( self.current_pic, wx.BITMAP_TYPE_ANY ))
		# 2 - Update Tessseract's output text
		self.M_Tesseract.SetValue(self.readresult)
			
		
		
	
	

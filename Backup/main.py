#!/bin/python2.8
# -*- coding: utf-8 -*-

#BigBrother, v0.1, alpha
#Based on Tesseract

import wx
from BigbrotherClass import BigbrotherClass

app = wx.App()

frame = BigbrotherClass(None)
frame.Show()


app.MainLoop()

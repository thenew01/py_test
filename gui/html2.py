#! /usr/bin/env python
#coding=utf-8
#-*- encoding:UTF-8 -*-
import wx
import wx.html

class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(600,400))
        self.CreateStatusBar()
        html = wx.html.HtmlWindow(self)
        
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()
        html.SetRelatedFrame(self, self.GetTitle() + " -- %s") #关联HTML到框架
        html.SetRelatedStatusBar(0) #关联HTML到状态栏
        wx.CallAfter(
        html.LoadPage, "http://www.wxpython.org")

app = wx.PySimpleApp()
frm = MyHtmlFrame(None, "Simple HTML Browser")
frm.Show()
app.MainLoop()

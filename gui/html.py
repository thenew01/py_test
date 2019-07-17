#! /usr/bin/env python
#coding=utf-8
import wx
import wx.html


class MyHtmlWindow(wx.html.HtmlWindow):
    '''def __init__(self, parent):
        pass'''
    
    def OnCellClicked(self, cell, x, y, event):
        msg = repr(cell)+str(x)+str(y)+repr(event)
        wx.MessageBox(msg,'',0)
        
    def OnCellMouseHover(self, cell, x, y):
        pass
    
class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(600,400))
        #html = wx.html.HtmlWindow(self)
        html = MyHtmlWindow(self)
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()
            
        wx.CallAfter(
        html.LoadPage, "http://www.baidu.com")
        
app = wx.PySimpleApp()
frm = MyHtmlFrame(None, "Simple HTML Browser")
frm.Show()
app.MainLoop()

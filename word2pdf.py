#! /usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*- 
#---------------------------------------------------------------------------
# wxDoc2PDF.pyw::将word 2007/2003文件转换为pdf文件的wxPython GUI界面
# Author:Wu Xuping
# 2012-04-18
#---------------------------------------------------------------------------
import sys, os
import wx

from win32com.client import Dispatch, constants, gencache

#---------------------------------------------------------------------------

def doc2pdf(input, output):
    w = Dispatch("Word.Application") 
    try:
        doc = w.Documents.Open(input, ReadOnly = 1)
        doc.ExportAsFixedFormat(output, constants.wdExportFormatPDF, 
        Item = constants.wdExportDocumentWithMarkup, CreateBookmarks = constants.wdExportCreateHeadingBookmarks)
        return 0
    except:
        return 1
    finally:
        w.Quit(constants.wdDoNotSaveChanges)
        

# Generate all the support we can.
def GenerateSupport():
    gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)

#---------------------------------------------------------------------------
wildcard = "Word 2007/2003 File (*.docx *.doc)|*.doc*|"     \
           "All files (*.*)|*.*"
#---------------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        
        self.frame=parent

        b = wx.Button(self, -1, "Select Word 2007/2003 Files and Convert to PDF", (50,50),(480,80))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):

        dlg = wx.FileDialog(
            self, message="Choose Word 2007/2003 file:",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )

        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            GenerateSupport()
            for path in paths:
                input = path
                output = os.path.splitext(input)[0]+'.pdf'
                self.frame.SetTitle(u'正在转换文档--->'+path)
                if (not os.path.isabs(input)):
                    input = os.path.abspath(input)
                if (not os.path.isabs(output)):
                    output = os.path.abspath(output)
                        
                doc2pdf(input, output)               
                
            self.frame.SetTitle('OK:-->'+output) 
            mdlg = wx.MessageDialog(None, u"转换已完成,是否继续转换?", u"标题信息", wx.YES_NO | wx.ICON_QUESTION)
            if mdlg.ShowModal() == wx.ID_YES:
                self.frame.SetTitle('please choose a file') 
            else:
                self.Close(True)
                wx.Exit()
            mdlg.Destroy()            
                

        dlg.Destroy()


#---------------------------------------------------------------------------

if __name__ == '__main__':
    app = wx.PySimpleApp(False)
    frame = wx.Frame(None,size = (600,250))
    frame.SetTitle('wxDoc2PDF::Wu Xuping')
    frame.Center(wx.BOTH)
    tp=TestPanel(frame)
    frame.Show()
    app.MainLoop()

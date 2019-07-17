#! /usr/bin/env python
#coding=utf-8
import wx  
'''
def main():  
    app=wx.PySimpleApp()  
    frame=wx.Frame(None,-1,'Icon',wx.DefaultPosition,wx.Size(350,300))  
    frame.SetIcon(wx.Icon('Tipi.ico',wx.BITMAP_TYPE_ICO))  
    frame.Center()  
    frame.Show()  
    app.MainLoop()  
if __name__ == '__main__':  
    main()  
'''


#!/usr/bin/env python  
# FileName: menu1.py  



class MyMenu( wx.Frame ):  
    def __init__(self,parent,ID,title):  
        wx.Frame.__init__(self,parent,-1,title,wx.DefaultPosition,wx.Size(200, 150))  
        menubar=wx.MenuBar()  
        file=wx.Menu()  
        edit=wx.Menu()  
        help=wx.Menu()  
        file.Append(101,'&Open','Open a new document')  
        file.Append(102,'&Save','Save the document')  
        file.AppendSeparator()  
        quit=wx.MenuItem(file,105,'&Quit\tCtrl+Q','Quit the Application')  
        quit.SetBitmap(wx.Image('stock_exit-16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())  
        file.AppendItem(quit)  
        
        edit.Append(201, 'check item1', '', wx.ITEM_CHECK)  
        edit.Append(202, 'check item2', kind= wx.ITEM_CHECK)  

        submenu = wx.Menu()  
        submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)  
        submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)  
        submenu.Append(303, 'radio item3', kind= wx.ITEM_RADIO)  
        edit.AppendMenu(203, 'submenu', submenu)  

        
        menubar.Append(file,'&File')  
        menubar.Append(edit,'&Edit')  
        menubar.Append(help,'&Help')  
        
        self.SetMenuBar( menubar )  
  
        self.Centre()
        
       
        self.statusbar = self.CreateStatusBar() 

        
        wx.EVT_MENU(self, 105, self.OnQuit)  # samae as the following
        #self.Bind(wx.EVT_MENU, self.OnQuit, 105)  
    def OnQuit(self, event):  
        self.Close()  


     
    '''def OnMOve(self, event):
        pos = event.GetPosition()        
        self.statusbar.SetStatusText( '%s,%s' % (pos.x,pos.y )  )
    '''
        
        
class MyToolBar( wx.Frame ):  
  
    def __init__( self, parent, ID, title ):  
        wx.Frame.__init__( self, parent, ID, title, wx.DefaultPosition, wx.Size( 350, 250 ) )  
          
        vbox = wx.BoxSizer( wx.VERTICAL )  
        toolbar = wx.ToolBar( self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER )  
        toolbar.AddSimpleTool( 1, wx.Image( 'stock_new.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'New', '' )  
        toolbar.AddSimpleTool( 2, wx.Image( 'stock_open.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Opne', '' )  
        toolbar.AddSimpleTool( 3, wx.Image( 'stock_save.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Save', '' )  
        toolbar.AddSeparator()  
        toolbar.AddSimpleTool( 4, wx.Image( 'stock_exit.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Exit', '' )  
        toolbar.Realize()  
          
        vbox.Add( toolbar, 0, border=5 )  
        self.SetSizer( vbox )  
        self.statusbar = self.CreateStatusBar()  
          
        self.Centre()  
          
        wx.EVT_TOOL( self, 1, self.OnNew )  
        wx.EVT_TOOL( self, 2, self.OnOpen )  
        wx.EVT_TOOL( self, 3, self.OnSave )  
        wx.EVT_TOOL( self, 4, self.OnExit )  
          
      
        
    def OnNew( self, event ):  
        self.statusbar.SetStatusText( 'New Command' )  
      
    def OnOpen( self, event ):  
        self.statusbar.SetStatusText( 'Open Command' )  
      
    def OnSave( self, event ):  
        self.statusbar.SetStatusText( 'Save Command' )  
      
    def OnExit( self, event ):  
        self.Close()  


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'My Frame', size=(300, 300))
        panel = wx.Panel(self, -1)
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, "Pos:", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))
    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))


class MyApp(wx.App):  
    def OnInit(self):  
        frame=MyMenu(None,-1,'menu1.py')  
        #frame = MyToolBar( None, -1, ' toolbar.py' )  
        #frame = MyFrame( )
        frame.Show(True)  
        return True  
      
app=MyApp(0)  
app.MainLoop()  

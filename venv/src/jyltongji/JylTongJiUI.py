# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class BaseFrame
###########################################################################

class BaseFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"JYL基本数据统计", pos=wx.DefaultPosition,
                          size=wx.Size(542, 544), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        content = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText19 = wx.StaticText(self, wx.ID_ANY, u"这个处理框可以自行拉大缩小", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)

        content.Add(self.m_staticText19, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 9)

        self.m_staticline4 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        content.Add(self.m_staticline4, 0, wx.EXPAND | wx.ALL, 9)

        fgSizer1 = wx.FlexGridSizer(5, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"选择数据源", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        fgSizer1.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_filePicker = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"选择Excel文件", u"*.*", wx.DefaultPosition,
                                              wx.DefaultSize, wx.FLP_DEFAULT_STYLE | wx.FLP_FILE_MUST_EXIST)
        fgSizer1.Add(self.m_filePicker, 0, wx.ALL, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"选择文件保存位置", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        fgSizer1.Add(self.m_staticText10, 0, wx.ALL, 5)

        self.m_dirPicker = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"选择文件夹", wx.DefaultPosition,
                                            wx.DefaultSize, wx.DIRP_DEFAULT_STYLE | wx.DIRP_DIR_MUST_EXIST)
        fgSizer1.Add(self.m_dirPicker, 0, wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"输入间隔步长", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        fgSizer1.Add(self.m_staticText11, 0, wx.ALL, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl_dt = wx.TextCtrl(self, wx.ID_ANY, u"1000000", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl_dt, 0, wx.ALL, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"默认为1000000, 即1M", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTER_HORIZONTAL)
        self.m_staticText12.Wrap(-1)

        bSizer2.Add(self.m_staticText12, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"输入数据源表头名称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        fgSizer1.Add(self.m_staticText16, 0, wx.ALL, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_textCtrl_name = wx.TextCtrl(self, wx.ID_ANY, u"position", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_textCtrl_name, 0, wx.ALL, 5)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"默认为 position ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)

        bSizer3.Add(self.m_staticText17, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        self.m_button_check = wx.Button(self, wx.ID_ANY, u"点击检查数据", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_button_check, 0, wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText18 = wx.StaticText(self, wx.ID_ANY, u"以下展示前5列数据,请自行检查值是否正确", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)

        bSizer4.Add(self.m_staticText18, 0, wx.ALL, 5)

        m_listBoxChoices = []
        self.m_listBox = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxChoices, 0)
        bSizer4.Add(self.m_listBox, 0, wx.ALL, 5)

        fgSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        content.Add(fgSizer1, 0, wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        content.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        self.m_button_proccess = wx.Button(self, wx.ID_ANY, u"开始处理数据", wx.DefaultPosition, wx.DefaultSize, 0)
        content.Add(self.m_button_proccess, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 9)

        self.SetSizer(content)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button_check.Bind(wx.EVT_BUTTON, self.checkData)
        self.m_button_proccess.Bind(wx.EVT_BUTTON, self.proccessData)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def checkData(self, event):
        event.Skip()

    def proccessData(self, event):
        event.Skip()

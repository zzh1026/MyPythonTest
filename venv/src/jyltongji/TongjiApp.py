#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by zhaozehui at 2020/9/15

__author__ = 'zzh'

import JylTongJiData
import JylTongJiUI
import wx


class CalcFrame(JylTongJiUI.BaseFrame):
    def __init__(self, parent):
        JylTongJiUI.BaseFrame.__init__(self, parent)

    def showMsg(self, msg, suggest):
        dlg = wx.MessageDialog(None, suggest, msg, wx.OK | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.OK:
            dlg.Destroy()
            # self.Close(True)
        dlg.Destroy()
        pass

    def checkData(self, event):
        inputPath = self.m_filePicker.GetPath()
        textName = self.m_textCtrl_name.GetValue()
        if str(inputPath).strip() == '':
            self.showMsg("输入地址为空", "选择输入的地址")
            return
        if str(textName).strip() == '':
            self.showMsg("文件列表表头为空", "输入列表表头字段")
            return
        dataHead = tongjiData.checkData(inputPath, textName)
        listData = list(dataHead)
        self.m_listBox.Clear()
        self.m_listBox.Append([str(x) for x in listData])
        pass

    def proccessData(self, event):
        inputPath = self.m_filePicker.GetPath()
        textName = self.m_textCtrl_name.GetValue()
        dT = self.m_textCtrl_dt.GetValue()
        outputPath = self.m_dirPicker.GetPath()
        if str(inputPath).strip() == '':
            self.showMsg("输入地址为空", "选择输入的地址")
            return
        if str(textName).strip() == '':
            self.showMsg("文件列表表头为空", "输入列表表头字段")
            return
        if str(dT).strip() == '':
            self.showMsg("取值间隔为空", "选择步长内容")
            return
        if str(outputPath).strip() == '':
            self.showMsg("输出文件夹位置为空", "选择输出文件夹")
            return
        resultPath = tongjiData.proccessData(inputPath, textName, dT, outputPath)
        self.showMsg("写出完毕", "请检查位于 " + resultPath + " 的文件是否正常")
        pass


app = wx.App(False)
tongjiData = JylTongJiData.TongJiData()
frame = CalcFrame(None)
frame.Show(True)
# start the applications
app.MainLoop()

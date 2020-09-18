# -*- coding: utf-8 -*-

import pandas as pd  # 数据处理


class TongJiData:

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def checkData(self, inputPath, titleName):
        datas = pd.read_excel(inputPath)
        datas = datas[titleName]
        return datas.head()

    def proccessData(self, inputPath, titleName, dTWork, outputPath):
        datas = pd.read_excel(inputPath)
        datas = datas[titleName]

        dT = int(dTWork)
        resultPath = outputPath

        # 分割起始位置
        start = 0
        # 区间的列表
        qujian = [start]
        # 区间的列表对应的标签
        qujian_lable = []

        while True:
            end = start + dT
            # 标签添加数据内容为 [0M-1M, 1M-2M ...]等等用来进行自己查看,这个可以不使用
            qujian_lable.append('%sM- %sM' % (start / dT, end / dT))
            # 完善区间,用来最后对数据进行分割统计,内容为 [0,dT, 2*dT,3*dT...]
            qujian.append(end)
            start = end
            if start > datas.max():
                break

        # 切割数据
        result_cut = pd.cut(datas, bins=qujian, right=False, labels=qujian_lable, include_lowest=True, retbins=False)
        # print(qujian)
        # print(qujian_lable)
        # print(result_cut.head())
        # lists = list(result_cut)
        # result_data = pd.Series(lists)
        # print(result_data)
        # print('数据数量为: %s' % (lists.__len__()))
        # print('数据数量为: %s' % (datas.count()))

        results = result_cut.value_counts(sort=False, ascending=True)
        print(results)

        finalsResultPath = resultPath + "\\resultsss.xlsx"

        # 写出到xlsx文件
        results.to_excel(finalsResultPath)
        return finalsResultPath
        pass

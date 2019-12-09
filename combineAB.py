#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-12-09 09:37
__author__ = 'Ted'


import pandas as pd

# 先获取要合并的表格名称，由于涉及编码，尽量用字母+数字组合的名称，避免中文名称导致的编码格式问题
name_a = "表A.xlsx"
name_b = "表B.xlsx"

# 使用导入的 pandas 简写为 pd 来读取 excel 表格
table_a = pd.read_excel(name_a)
table_b = pd.read_excel(name_b)

# 将两表纵向合并
result = pd.concat([table_a,table_b])

# 合并后数据的 index 索引需要重置
# 参数中 drop=True 指放弃旧的 index,否则旧 index 会出现在表中；inplace=True 重置行为直接修改在本数据结构中
result.reset_index(drop=True,inplace=True)
# 新合并后 "序号" 列内的数字需更新
result["序号"]=range(1,len(result)+1)
# 将合并后的数据保存为 result1.xlsx 表格，名字可以修改，index=False 表示不将数据结构中的 index 加入表中
result.to_excel("result1.xlsx",index=False)
print(f"{name_a} 和 {name_b} 合并完毕！")


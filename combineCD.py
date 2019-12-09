#!/usr/bin/env python
# encoding: utf-8
# @Time : 2019-12-09 10:39

__author__ = 'Ted'

import pandas as pd


# 先获取要合并的表格名称，由于涉及编码，尽量用字母+数字组合的名称，避免中文名称导致的编码格式问题
name_a = "表C.xlsx"
name_b = "表D.xlsx"

# 使用导入的 pandas 简写为 pd 来读取 excel 表格
table_a = pd.read_excel(name_a)
table_b = pd.read_excel(name_b)

# 通过数据格式.iloc[行，列]的形式来提取某行某列，取第x列=iloc[所有行，x]=iloc[:,x]
# 此处取表 C 的第 C 列（数据结构中序列从0开始，A列-0，B列-1，C列-2）
part_a = table_a.iloc[:,2]
# 取特定 m,n 列时通过 .iloc[:,[m,n]];若连续取第x到y列还可以 .iloc[:,x:y]
# 此处取表 D 的 A、B 列
part_b = table_b.iloc[:,[0,1]]

# 将取出的两部分通过 pd.concat([x,y],axis=1) 合并，此处 axis=1 表示沿列方向合并
result = pd.concat([part_b,part_a],axis=1)
# 将表格导出保存，index=False 表示不将数据结构中的 index 加入表中
result.to_excel("result2.xlsx",index=False)
print(f"{name_a} 和 {name_b} 合并完毕！")
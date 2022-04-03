'''
1.正态分布曲线的特点：1. 左右对称的曲线；2. 两边都是弧线；3. 线的两端无限延长。
2.正态分布的因素条件：1. 影响结果的因素有很多；2. 各个因素的影响力相似；3. 所有因素之间相互独立。
3.具有两个及以上多个波峰的分布曲线称为“双峰分布”或“M峰分布”、“多峰分布”。在大多数情况下，如果出现了多峰曲线，往往意味着将两个不同的数据集拼凑在了一起绘制为一条曲线。
4.在符合正态分布的数据集中，在平均值左右一个标准差范围内的人数是 68.27%，在平均值左右两个标准差范围内的人数是 95.45% 。标准差与分布区间：
    σ   68%
   2σ   95%
   3σ   99.7%
   4σ   99.9937%'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid',{'font.sans-serif':['SimHei','Ariel']})
plt.rcParams['font.sans-serif'] = ['SimHei','Ariel']
plt.rcParams['axes.unicode_minus'] = 'False'

df = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
print(df.info())
dfc = df[df['商品子类'] =='Chairs']
print(dfc.head())
dfc = dfc[['总额','运费','折扣','数量','市场']]
print(dfc.describe())
P1 = plt.figure(dpi = 300, figsize = (8,6))
g = sns.jointplot(data = dfc, x = '数量', y = '折扣', kind = 'kde', shade = 'True', color = 'pink')
plt.suptitle("销售数量折扣相关性热力图")
plt.savefig(r'D:\项目代码\国际卖场数据\数量折扣相关性热力图.jpg')

P2 = plt.figure(dpi = 300, figsize = (8,6))
dfr = dfc.corr()
g = sns.heatmap(data = dfr, cmap = 'autumn_r', annot = True, fmt = '0.2f') #cmap 指定配色方案；autumn:由红到黄，autumn_r：r代表颜色反向设置，由黄到红
plt.suptitle("各因素相关系数热力图")
plt.savefig(r'D:\项目代码\国际卖场数据\相关系数热力图.jpg')





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid',{'font.sans-serif':['SimHei','Ariel']})
plt.rcParams['font.sans-serif'] = ['SimHei','Ariel']
plt.rcParams['axes.unicode_minus'] = 'False'

df = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
df = df[['顾客编号','顾客类型','总额']]

df_buyer = df.groupby('顾客编号').aggregate({'顾客类型':min, '总额':sum})

df_buyer['级别'] = pd.cut(df_buyer['总额'], bins = [0, 1000, 10000, 20000, 35000], labels = ['1','2','3','4'])
df_level = df_buyer.groupby('级别').count()

plt.figure(dpi = 300, figsize = (10,6))
fig, axes = plt.subplots(1,2)

g = sns.barplot(data = df_level, x = df_level.index, y = '总额', palette = 'coolwarm',ax = axes[0])
g2 = sns.histplot(data = df_buyer, x = '总额', stat = 'count', binwidth = 3000, kde = True, axes = axes[1])  #stat代表y轴统计方式，也可以为‘probability’; binwidth为每个柱子的区间跨度
axes[0].set_title("顾客级别分类")
axes[1].set_title("顾客消费金额")
axes[1].set_ylabel('人数')
plt.suptitle("客户级别&消费金额分类")
plt.subplots_adjust(wspace = 0.5)
plt.savefig(r'D:\项目代码\国际卖场数据\客户级别&消费金额分类.jpg')

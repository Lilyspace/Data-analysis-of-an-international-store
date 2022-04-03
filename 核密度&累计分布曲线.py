'''“核密度估计法”根据有限的样本数据估计出总体全部数据的分布情况。
在KDE曲线图中，根据横轴两个点x1与x2之间的曲线阴影面积与整体曲线阴影面积的比值可以得出x1~x2范围内的个数出现的概率。
计算概率密度曲线面积使用“累计分布曲线”。kdeplot方法的参数 cumulative=True 时展示累计分布曲线。'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid',{'font.sans-serif':['SimHei','Ariel']})
plt.rcParams['font.sans-serif'] = ['SimHei','Ariel']
plt.rcParams['axes.unicode_minus'] = 'False'

df = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
df = df[['顾客编号','顾客类型','总额']]

df_buyer = df.groupby('顾客编号').aggregate({'顾客类型':min, '总额':sum})
plt.figure(dpi = 300, figsize = (15,6))
fig, axes = plt.subplots(1,2)

g = sns.kdeplot(data = df_buyer, x = '总额', ax = axes[0])
g = sns.kdeplot(data = df_buyer, x = '总额', ax = axes[1], cumulative = True)

axes[0].set_title("核密度曲线")
axes[1].set_title("累计分布曲线")

plt.suptitle("客户金额分布")
plt.subplots_adjust(wspace = 0.5)
plt.savefig(r'D:\项目代码\国际卖场数据\客户金额分布.jpg')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid',{'font.sans-serif':['SimHei','Ariel']})
plt.rcParams['font.sans-serif'] = ['SimHei','Ariel']
plt.rcParams['axes.unicode_minus'] = 'False'

dfs = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
dfs.index = pd.to_datetime(dfs['订单日期'])

'''重采样无论对于时间数据还是其他数据，凡是涉及到区间概念时都要特别注意起点与终点的问题，避免造成歧义。
resample()方法的 closed 参数用于设置采样区间是包含左边界还是右边界，closed='left' 表示包含左边，closed='right'表示包含右边。
对于包含右侧边界的情况，左侧剩下的日期数据自动包含更早时间点的数据。
如果按三天间隔重采样，系统会取出四天的数据，具体使用哪三天，根据closed，标签显示的日期根据label。'''

df2 = dfs.resample('1d', closed='left', label='left').sum()[['总额','营利','运费']]

fig, axes = plt.subplots(1,2,figsize = (12,6))

g1 = sns.lineplot(data = df2, x = '订单日期', y = '总额', ax = axes[0])
g1.tick_params(labelrotation=60) #子图设置坐标轴旋转


df3 = df2.rolling(15, center = True, min_periods = 1).mean() #df3中每一天的数字都是以这一天为中心前后15天金额的平均值
g2 = sns.lineplot(data = df3, x = '订单日期', y = '总额',ax = axes[1])
for tick in g2.get_xticklabels():
    tick.set_rotation(60) #子图设置坐标轴旋转


plt.tight_layout()

plt.suptitle("销售金额随时间变化情况")
plt.subplots_adjust(wspace = 0.3)
plt.savefig(r'D:\项目代码\国际卖场数据\时间销售额关系图.jpg')
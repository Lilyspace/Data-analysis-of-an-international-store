import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid',{'font.sans-serif':['SimHei','Ariel']})
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = 'False'

df = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
df.info()
df['国家地区'].unique()
len(df['国家地区'].unique())

df = df[['订单号','国家地区','商品门类','总额']]
df_top5 = df.groupby('国家地区')[['总额']].sum().sort_values('总额',ascending = False)[:5]
df = df[df['国家地区'].isin(df_top5.index)]



'''plt.ticklabel_format(style='plain',axis='both') #横纵坐标都以普通数字（非科学计数法）'''
#seaborn的catplot方法创建分类绘图，自动对数据分组，每组绘制一个图表，全部放入一个多图表个（FacetGrid）对象

g = sns.catplot(data=df, x='国家地区', y='总额', col='商品门类',hue = '商品门类',kind='bar',estimator = sum, palette = 'cool',alpha = 0.7, ci=None)
#通过FacetGrid对象的axes.flat属性可以获取到对象中的某一个图表对象，根据索引获取图表，例如修改多图表格中所有图表的x轴标签：
for f in g.axes.flat:
    f.set_xticklabels(f.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.savefig(r'D:\项目代码\国际卖场数据\Top5分组柱状图1.jpg',dpi = 200, bbox_inches = 'tight') # 最后一个参数解决avefig保存时图片保存不完整的问题，dpi=200可以使图片不会失真

g = sns.catplot(data=df, x='国家地区', y='总额',hue = '商品门类',kind='bar',estimator = sum, palette = 'cool',alpha = 0.7, ci=None)
for f in g.axes.flat:
    f.set_xticklabels(f.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.suptitle("销量Top5国家各类商品销售额")
plt.savefig(r'D:\项目代码\国际卖场数据\Top5分组柱状图2.jpg',dpi = 200, bbox_inches = 'tight')

#堆叠柱状图
#堆叠透视图可以通过DataFrame中的DataFrame.plot方法进行绘制，在使用绘图方法之前需要先将数据集转换为透视表形式，拿到想要展示的总和数据
'''DataFrame.pivot_table(数据, 行标题, 列标题)方法根据数据集创建数据透视表。
其中数据参数设置需要展示的数值所属的列名，index参数设置作为行标题的行名，columns参数设置作为列标题的列名，默认统计平均值。
pivot_table方法的aggfunc参数设置统计方法的名称,fill_value参数设置NaN的填充值'''

df_cat = pd.pivot_table(df, index = ['国家地区'], columns = ['商品门类'], values = '总额', aggfunc = 'sum')
g = df_cat.plot(kind = 'bar', stacked = 'True',style='plain',alpha = 0.7, colormap = "tab20b")#通过colormap自定义颜色
g.set_xticklabels(labels=g.get_xticklabels(), rotation=30,horizontalalignment='right', size='medium')
g.get_yaxis().get_major_formatter().set_scientific(False) # y轴设置为普通数字（非科学计数法）
plt.suptitle("销量Top5国家各类商品销售额")
plt.savefig(r'D:\项目代码\国际卖场数据\Top5堆叠组柱状图.jpg',dpi = 300, bbox_inches = 'tight')
plt.show()

#雷达图
import pygal
import cairosvg
from pygal.style import Style
style = Style(font_family = "Yahei Consolas Hybrid")#正常显示中文
P1 = plt.figure(dpi = 300, figsize = (8,6))
radar_chart = pygal.Radar(style = style)
radar_chart.title = '销量Top5国家各类商品销量对比'
radar_chart.x_labels = df_cat.columns
radar_chart.style = Style(foreground_subtle = 'lightgrey') #设定雷达图中等高线为浅灰色
for area in df_cat.index:
    radar_chart.add(area, df_cat.loc[area,:]) #第一个参数area为雷达图中一条曲线的名字；loc按索引（行）取数据
radar_chart.render_to_file(r'D:\项目代码\国际卖场数据\Top5雷达图1.svg')
radar_chart.render_to_png(r'D:\项目代码\国际卖场数据\Top5雷达图1.png')

df_cat = df_cat.T
style = Style(font_family="Yahei Consolas Hybrid")
P2 = plt.figure(dpi = 300, figsize = (8,6))
radar_chart2 = pygal.Radar(style = style)
radar_chart2.title = '销量Top5国家各类商品销量对比'
radar_chart2.x_labels = df_cat.columns
radar_chart2.style = Style(foreground_subtle = 'lightgrey') #设定雷达图中等高线为浅灰色
for area in df_cat.index:
    radar_chart2.add(area, df_cat.loc[area,:]) #第一个参数area为雷达图中一条曲线的名字；loc按列索引取数据
radar_chart2.render_to_file(r'D:\项目代码\国际卖场数据\Top5雷达图2.svg')
radar_chart2.render_to_png(r'D:\项目代码\国际卖场数据\Top5雷达图2.png')






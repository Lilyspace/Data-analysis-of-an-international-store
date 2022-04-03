import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid',{'font.sans-serif':['SimHei','Ariel']})

# 文件路径
import os
for root, dirs, files in os.walk('D:\项目代码\国际卖场数据'):
    for name in files:
        print(os.path.join(root, name))

'''了解数据集的基本情况：
    1. 理解字段：理解字段的含义，各字段之间的关系。
    2. 分析缺失情况：通过info方法观察字段类型，注意数字类型、对象类型（字符串形式）、日期类型等，内容是否完整，主要字段的缺失值情况。'''

df = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
df.info()
print(df.head())
print(df.info())
print(df.describe())

df['国家地区'].unique()
len(df['国家地区'].unique())

df = df[['订单号','国家地区','商品门类','总额']]
df_top5 = df.groupby('国家地区')[['总额']].sum().sort_values('总额',ascending = False)[:5]
df = df[df['国家地区'].isin(df_top5.index)]

#柱状图
plt.ticklabel_format(style='plain',axis='both') #横纵坐标都以普通数字（非科学计数法）显示
g = sns.barplot(data = df, x = '国家地区',y = '总额',palette = 'spring', alpha = 0.7,ci = None,estimator = sum) #ci参数指定误差线，None表示不显示误差线
g.set_xticklabels(labels=g.get_xticklabels(), rotation=30,horizontalalignment='right', size='medium')；#加了；之后就不显示返回值
g.figure.set_size_inches(8,6)
plt.suptitle("销量最高的五个国家销售总额")
plt.savefig(r'D:\项目代码\国际卖场数据\Top5柱状图.jpg')
plt.show()

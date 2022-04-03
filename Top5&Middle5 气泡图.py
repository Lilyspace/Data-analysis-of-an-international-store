import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid',{'font.sans-serif':['SimHei','Ariel']})
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = 'False'

# 文件路径
import os
for root, dirs, files in os.walk('D:\项目代码\国际卖场数据'):
    for name in files:
        print(os.path.join(root, name))

df = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
df = df[['订单号','国家地区','商品门类','总额']]
df_top5 = df.groupby('国家地区')[['总额']].sum().sort_values('总额',ascending = False)[:5]
df_mid5 = df.groupby('国家地区')[['总额']].sum().sort_values('总额',ascending = False)[71:76]

df_sample = df_top5.append(df_mid5)
df = df[df['国家地区'].isin(df_sample.index)]
df = df.groupby('国家地区')[['总额']].sum()

plt.ticklabel_format(style='plain',axis='both')
g = sns.scatterplot(x='国家地区', y=[0]*len(df), size='总额',data=df,hue = '国家地区',legend = False,sizes=( 50, 50 * df['总额'].max()/df['总额'].min() ))
g.figure.canvas.draw()
g.set_xticklabels(labels=g.get_xticklabels(), rotation=30,horizontalalignment='right', size='medium')
g.figure.set_size_inches(16,5)
plt.suptitle("Top5&Middle5销售情况对比")
plt.savefig(r'D:\项目代码\国际卖场数据\Top5&Middle5气泡图.jpg')
plt.show()


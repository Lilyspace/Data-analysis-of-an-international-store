


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid',{'font.sans-serif':['SimHei','Ariel']})
plt.rcParams['font.sans-serif'] = ['SimHei','Ariel']
plt.rcParams['axes.unicode_minus'] = 'False'

df = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
df = df[['订单号','国家地区','商品门类','总额']]
df_mid5 = df.groupby('国家地区')[['总额']].sum().sort_values('总额',ascending = False)[71:76]
df_mid5 = df[df['国家地区'].isin(df_mid5.index)]



g3 = sns.boxenplot(data = df_mid5,x = '总额',y = '国家地区',orient='h',palette = 'coolwarm', k_depth = 'proportion', outlier_prop = 0.2)
g3.set_yticklabels(labels=g3.get_yticklabels(), rotation=30,horizontalalignment='right', size='medium')
plt.savefig(r'D:\项目代码\国际卖场数据\Middle5增强箱型图2.jpg',bbox_inches = 'tight')
plt.show()

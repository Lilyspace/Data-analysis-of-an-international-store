''' 箱型图中的最大值与最小值线是通过估算得出的值，而不是数据集中真实的最大值与最小值。
boxplot方法的whis参数设置估算最大值和最小值的倍数，默认值为1.5;
箱型图判读常识：
    1. 胡须长、异常点远，说明存在少数极度“富裕”或“贫困”的数据；
    2. 箱型扁，说明中间部分（25%-75%）的数据跨度小，更集中。
'''
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
g = sns.boxplot(data = df_mid5,x = '国家地区',y = '总额',palette = 'coolwarm', showfliers = False, showmeans = True, meanline = True)
g.set_xticklabels(labels=g.get_xticklabels(), rotation=30,horizontalalignment='right', size='medium')
plt.suptitle("销量Middle5国家销售数据分布情况")
plt.savefig(r'D:\项目代码\国际卖场数据\Middle5箱型图.jpg')

#增强箱型图
'''箱型图只能将数据集划分为四个空间，每个空间只有25%这一个笼统指标，无法对两端的数据进行更详细的区间估计。
增强箱型图弥补了箱型图的缺点。增强箱型图使用更多的分位数来展示更细致的数据分布情况。
在增强箱型图中，每个箱子中数据点的个数都是前一个箱子的一半，也是后面所有数据点的总数
boxenplot方法的outlier_prop参数设置异常点的比例，参数类型为浮点数，取值范围在 0~1 之间，值越小异常点越少。
k_depth参数设置箱子划分深度的依据，参数类型为字符串，设置为'proportion'表示根据异常点比例划分箱子深度。'''
df_mid5.describe()
g2 = sns.boxenplot(data = df_mid5,x = '国家地区',y = '总额',palette = 'coolwarm', k_depth = 'proportion', outlier_prop = 0.2)
g2.set_xticklabels(labels=g2.get_xticklabels(), rotation=30,horizontalalignment='right', size='medium')
plt.suptitle("销量Middle5国家销售数据分布情况")
plt.savefig(r'D:\项目代码\国际卖场数据\Middle5增强箱型图1.jpg')


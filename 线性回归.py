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

from sklearn.linear_model import LinearRegression
rm = LinearRegression()
#设置拟合数据。注意x、y必须是二维数组或DataFrame，而不能是一维数组或Series。使用花式索引得到二维结构：
rm.fit( dfc[['总额']], dfc[['运费']] )
#通过属性获取方程参数值，rm.coef_ 得到斜率a，rm.intercept 得到截距b
c = rm.coef_
i = rm.intercept
#通过score方法获取准确性，最高是1，最低-∞。
s = rm.score( dfc[['总额']], dfc[['运费']] ) #score和r^2含义一致
#通过predict方法预测。注意参数必须是二维结构：
df['估计运费'] = rm.predict( df[['总额']] )
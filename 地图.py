import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts

df = pd.read_csv(r'D:\项目代码\国际卖场数据\国际卖场数据2011-2015.csv.csv')
df['国家地区'] = df['国家地区'].str.replace('China Mainland', 'China') #将数据集中中国的名字改为China以便与地图库中的名字对应
dfp = df.groupby('国家地区').sum()
dfp2 = dfp.sort_values(by = '总额', ascending = False)

print(dfp2.head())
print(dfp2.info())
print(dfp2.describe())


iopt = opts.InitOpts(width = '1200px', height = '800px')
lopt = opts.LabelOpts(is_show = False, formatter = '{b}\n{c}')# {b}代表地区名称，{c}代表对应的数字
vopt = opts.VisualMapOpts(min_ = dfp['总额'].min(), max_ = dfp['总额'].max()/2) #比较排名第一和第二的数据倍数差异，这样设定最大值可以让总额小的地区也显示颜色

pop_map = Map(iopt)
pop_map.set_global_opts(visualmap_opts = vopt) #全局设定
pop_map.add('全球各国家地区销售情况', list(zip(dfp.index, dfp['总额'])), maptype = 'world',label_opts = lopt)
pop_map.render(r'D:\项目代码\国际卖场数据\销售地图.html')
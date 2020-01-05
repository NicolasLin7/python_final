from flask import Flask,render_template
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line,Scatter
from pyecharts.globals import SymbolType
from pyecharts.charts import EffectScatter
from pyecharts.components import Table
from pyecharts.charts import Tab
from pyecharts.charts import Pie,Page
from pyecharts.charts import Timeline
from pyecharts.charts import Map



app = Flask(__name__, template_folder='../templates', static_folder="", static_url_path="")



df = pd.read_csv('美元指数.csv', index_col = 'US')
df

x=[str(x)for x in df.columns.values]
x

美元 =list(df.loc["Number"].values)

df1 = pd.read_csv('美GDP.csv', encoding='gbk',index_col = 'Country')
df1

GDP =list(df1.loc["美国"].values)




def grid_mutil_yaxis() -> Grid:
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis(
            "美元指数",美元,
            yaxis_index=0,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="指数",
                type_="value",
                min_=0,
                max_=150,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="blue")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="增长率",
                min_=-3,
                max_=8,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="red")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )

    )

    line = (
        Line()
        .add_xaxis(x)
        .add_yaxis(
            "GDP增长率",GDP,
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),

        )
    )
    bar.overlap(line)
    return Grid().add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
grid_mutil_yaxis().render_notebook()


df2 = pd.read_csv('拉美.csv', encoding='gbk',index_col = 'Country')
df2

拉美GDP =list(df2.loc["拉美"].values)
美国GDP =list(df2.loc["美国"].values)
世界GDP =list(df2.loc["世界"].values)

x1=[str(x)for x in df2.columns.values]
x1

def line_areastyle_boundary_gap() -> Line:
    a = (
        Line()
        .add_xaxis(x1)
        .add_yaxis("拉美", 拉美GDP, is_smooth=True)
        .add_yaxis("美国", 美国GDP, is_smooth=True)
        .add_yaxis("世界", 世界GDP, color="#5793f3", is_smooth=True)
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="1971-1990GDP增长率"),
            toolbox_opts=opts.ToolboxOpts(),
            datazoom_opts=opts.DataZoomOpts(),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
        )
    )
    return a
line_areastyle_boundary_gap().render_notebook()


df3 = pd.read_csv('东亚.csv', encoding='gbk',index_col = 'Country')
df3

东亚外资 =list(df3.loc["东亚与太平洋地区"].values)
美国外资 =list(df3.loc["美国"].values)

x2=[str(x)for x in df3.columns.values]
x2

def bar_stack1() -> Bar:
    b = (
        Bar()
        .add_xaxis(x2)
        .add_yaxis("东亚和太平洋地区", 东亚外资, stack="stack1")
        .add_yaxis("美国", 美国外资, stack="stack1")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="1986-2005外资净投入"),datazoom_opts=opts.DataZoomOpts(),toolbox_opts=opts.ToolboxOpts(),)
    )
    return b
bar_stack1().render_notebook()


df4 = pd.read_csv('泰国.csv', encoding='gbk',index_col = 'Country')
df4

泰国 =list(df4.loc["泰国"].values)
x3=[str(x)for x in df4.columns.values]



def effectscatter_splitline() -> EffectScatter:
    c = (
        EffectScatter()
        .add_xaxis(x3)
        .add_yaxis("泰国汇率", 泰国)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="1987-2001泰国汇率变化"),
            toolbox_opts=opts.ToolboxOpts(),
            datazoom_opts=opts.DataZoomOpts(),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        )
    )
    return c
effectscatter_splitline().render_notebook()


df5 = pd.read_csv('中国.csv', encoding='gbk',index_col = 'Country')
df5

中国外资 =list(df5.loc["中国"].values)
美国的外资 =list(df5.loc["美国"].values)
x4=[str(x)for x in df5.columns.values]

df6 = pd.read_csv('中美.csv', encoding='gbk',index_col = 'Country')
df6

中国GDP =list(df6.loc["中国"].values)
美国的GDP =list(df6.loc["美国"].values)

def bar_base() -> Bar:
    d = (
        Bar()
        .add_xaxis(x4)
        .add_yaxis("中国", 中国外资)
        .add_yaxis("美国", 美国的外资)
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval=5
            )
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中美外资净投入对比"),
            toolbox_opts=opts.ToolboxOpts(),
            datazoom_opts=opts.DataZoomOpts(),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} ")
            ),
        )
    )
    return d
bar_base().render_notebook()


df7 = pd.read_csv('油价.csv', encoding='gbk',index_col = 'Year')
df7

石油价格 =list(df7.loc["Dollars per Barrel"].values)

x5=[str(x)for x in df7.columns.values]

df8 = pd.read_csv('油量.csv', encoding='gbk',index_col = '国家')
df8

石油产量 =list(df8.loc["百分比"].values)

volumn = []

for s in 石油产量:
    volumn.append(float(s[:-1]))
volumn

x6=[x for x in df8.columns.values]

[list(z) for z in zip(x6, volumn)]



def pie_rosetype() -> Pie:
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(x6,volumn)],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="2018石油产量%"))
    )
    return c

def line_base() -> Line:
    c = (
        Line()
        .add_xaxis(x5)
        .add_yaxis("石油价格", 石油价格,)
        .set_global_opts(title_opts=opts.TitleOpts(title="21世纪历年国际油价/美元"))
    )
    return c

page = Page()
page.add(pie_rosetype(), line_base())
page.render_notebook()

df12 = pd.read_csv('委内瑞拉.csv', encoding='gbk', index_col='Year')
df12

委内瑞拉 = list(df12.loc["Rate"].values)

def line_base2() -> Line:
    c = (
        Line()
            .add_xaxis(x4)
            .add_yaxis("委内瑞拉", 委内瑞拉, )
            .set_global_opts(title_opts=opts.TitleOpts(title="近年委内瑞拉通货膨胀率%"))
    )
    return c

line_base().render_notebook()


df9 = pd.read_csv('产业.csv', encoding='gbk', index_col='Country')
df9

中国产业加值 = list(df9.loc["中国"].values)
美国产业加值 = list(df9.loc["美国"].values)
x7 = [x for x in df9.columns.values]
[list(z) for z in zip(x7, 中国产业加值)]

[list(z) for z in zip(x7, 美国产业加值)]

def Pie_base() -> Pie:
    c = (
        Pie()
            .add("", [list(z) for z in zip(x7, 中国产业加值)])
            .set_global_opts(title_opts=opts.TitleOpts(title="2018中国产业加值占GDP比重%"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

def Pie_base1() -> Pie:
    c = (
        Pie()
            .add("", [list(z) for z in zip(x7, 美国产业加值)])
            .set_global_opts(title_opts=opts.TitleOpts(title="2018美国产业加值占GDP比重%"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

page1 = Page()
page1.add(Pie_base(), Pie_base1())
page1.render_notebook()

df10 = pd.read_csv('中国贸易.csv', encoding='gbk', index_col='Year')
df10

x8 = [str(x) for x in df10.columns.values]

中国贸易总额 = list(df10.loc["贸易总额"].values)
中国贸易增长率 = list(df10.loc["贸易增长率"].values)

df11 = pd.read_csv('商贸.csv', encoding='gbk', index_col='Country')
df11

贸易占比 = list(df11.loc["百分比"].values)
贸易总额 = list(df11.loc["总额"].values)
x9 = [x for x in df11.columns.values]
[list(z) for z in zip(x9, 贸易占比)]

[list(z1) for z1 in zip(x9, 贸易总额)]

def bar_datazoom_slider() -> Bar:
    c = (
        Bar()
            .add_xaxis(x8)
            .add_yaxis("中国贸易总额", 中国贸易总额)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国贸易总额/亿美元）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c

def line_markpoint() -> Line:
    c = (
        Line()
            .add_xaxis(x8)
            .add_yaxis(
            "中国贸易增长率",
            中国贸易增长率,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]
                                              ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="中国贸易增长率%"))
    )
    return c

def pie_base() -> Pie:
    c = (
        Pie()
            .add("", [list(z) for z in zip(x9, 贸易占比)])
            .set_global_opts(title_opts=opts.TitleOpts(title="2018主要国家贸易占比%"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

def table_base() -> Table:
    table = Table()

    headers = ["国家", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]
    rows = [
        ["中国", 3.867, 4.158, 4.301, 3.953, 3.685, 4.107, 4.622],
    ]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="近年中国贸易总额/万亿美元")
    )
    return table

df13 = pd.read_csv('GDP增.csv', encoding='gbk')
df13

list1 = list(zip(list(df13['2012'])))

list2 = list(zip(list(df13['2013'])))

list3 = list(zip(list(df13['2014'])))

list4 = list(zip(list(df13['2015'])))

list5 = list(zip(list(df13['2016'])))

list6 = list(zip(list(df13['2017'])))

list7 = list(zip(list(df13['2018'])))

data = [list1, list2, list3, list4, list5, list6, list7]

list8 = list(zip(list(df13['Country'])))

def timeline_map(data) -> Timeline:
    tl = Timeline()
    for i in range(2012, 2019):
        map0 = (
            Map()
                .add(
                "Country", [list(z) for z in zip(df13['Country'], data[i - 2012])], "world")
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年GDP增长率".format(i)),
                visualmap_opts=opts.VisualMapOpts(max_=8),
            )
        )
        tl.add(map0, "{}年".format(i))

    return tl

@app.route("/")
def index():
    tab = Tab()
    tab.add(grid_mutil_yaxis(), "美元指数及GDP增长率")
    tab.add(line_areastyle_boundary_gap(), "1971-1990GDP增长率")
    tab.add(bar_stack1(), "1986-2005外资净投入")
    tab.add(effectscatter_splitline(), "1987-2001泰国汇率变化")
    tab.add(bar_base(), "中美外资净投入对比")
    tab.add(pie_rosetype(), "2018石油产量")
    tab.add(line_base(), "21世纪历年国际油价/美元")
    tab.add(line_base2(), "近年委内瑞拉通货膨胀率")
    tab.add(Pie_base(), "2018中国产业加值占GDP比重%")
    tab.add(Pie_base1(), "2018美国产业加值占GDP比重%")
    tab.add(bar_datazoom_slider(), "中国贸易总额")
    tab.add(line_markpoint(), "中国贸易总额增长率")
    tab.add(pie_base(), "主要国家贸易占比")
    tab.add(table_base(), "历年中国贸易总额")
    tab.add(timeline_map(data), "2012-2018GDP增长率")

    return Markup(tab.render_embed())



if __name__ == "__main__":
    app.run(debug=True)
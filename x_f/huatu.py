import matplotlib.pyplot as plt
import numpy as np
import datetime


def show_it(positive_sports, negative_sports, draw_sports, x_date):
    # 设置Matplotlib的字体为支持中文字符的字体，例如'SimHei'或'Microsoft YaHei'
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # # 正路赛事数据
    # positive_sports = ['日乙', '意甲', '西甲', '俄超', '意甲', '西甲', '挪超', '意甲', '葡超', '美职足']
    # # 反路赛事数据
    # negative_sports = ['英超', '瑞超', '挪超']
    # # 平局赛事数据
    # draw_sports = ['法甲', '德乙', '德甲', '英超', '瑞超', '西甲']

    # 定义固定的联赛顺序
    # fixed_order = ['俄超', '英超', '瑞超', '挪超', '法甲', '德乙', '德甲', '意甲', '日乙', '西甲', '葡超', '美职足']
    all_sports = positive_sports + negative_sports + draw_sports
    fixed_order = list(set(all_sports))

    # 初始化正路赛事、反路赛事和平局赛事的数量列表
    positive_counts = []
    negative_counts = []
    draw_counts = []
    # 计算每个联赛的正路赛事、反路赛事和平局赛事数量
    for sport in fixed_order:
        positive_count = positive_sports.count(sport)
        negative_count = negative_sports.count(sport)
        draw_count = draw_sports.count(sport)

        if positive_count != 0 or negative_count != 0 or draw_count != 0:
            positive_counts.append(positive_count)
            negative_counts.append(negative_count)
            draw_counts.append(draw_count)

    # 设置柱状图的宽度
    bar_width = 0.25

    # 设置x轴位置
    x = np.arange(len(fixed_order))

    # 创建一个新的画布，并指定画布的大小
    plt.figure(figsize=(12, 6))

    # 创建柱状图
    plt.bar(x, positive_counts, width=bar_width, label='正路赛事')
    plt.bar(x + bar_width, negative_counts, width=bar_width, label='反路赛事')
    plt.bar(x + 2 * bar_width, draw_counts, width=bar_width, label='平局赛事')

    # 设置x轴标签
    plt.xticks(x + bar_width, fixed_order, rotation=-90)
    # plt.gcf().autofmt_xdate()

    # 设置图例
    plt.legend()

    # 设置图表标题和坐标轴标签
    plt.title('正路赛事、反路赛事和平局赛事统计')
    plt.xlabel('联赛名称')
    plt.ylabel('出现次数')

    # 设置纵坐标刻度间隔为1
    plt.yticks(range(0, max(positive_counts + negative_counts + draw_counts) + 1, 1))

    # 在柱子顶部显示数量
    for i, count in enumerate(positive_counts):
        if count != 0:
            plt.text(x[i], count, str(count), ha='center', va='bottom')
    for i, count in enumerate(negative_counts):
        if count != 0:
            plt.text(x[i] + bar_width, count, str(count), ha='center', va='bottom')
    for i, count in enumerate(draw_counts):
        if count != 0:
            plt.text(x[i] + 2 * bar_width, count, str(count), ha='center', va='bottom')

    # 保存柱状图为图片
    d1 = datetime.date.today()
    # new_xlsx_file = str(d1) + '_demand_2' + '.xlsx'
    png_name = str(d1) + '_demand_2' + '.png'

    plt.savefig(png_name, dpi=300, bbox_inches='tight')

    # 显示柱状图
    plt.tight_layout()
    plt.show()




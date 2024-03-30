"""
查询过去30天内所有的胜负情况
    有用
"""
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw


def lucky_dog():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                      "86.0.4240.198 Safari/537.36"
    }

    # columns = ['让球','胜','平','负']
    title = {'编号': '', '赛事': '', '开赛时间': '', '主队排名': '', '主队': '', '比分': '', '客队': '', '客队排名': '',
             '让球': ''}
    data = {'胜': '', '平': '', '负': ''}
    serial_numbers, game_names, game_times = [], [], []
    i0, i1, a0, a1, a2 = [], [], [], [], []
    concede, victory, flat, defeat = [], [], [], []
    victory_index, flat_index, defeat_index = [], [], []
    today = time.strftime('%Y-%m-%d')
    tm_rng = pd.date_range(end=today, periods=30, freq='D')

    date_list = [x.strftime('%F') for x in tm_rng]
    xlsx_name = '最近30天内所有比赛数据_' + str(date_list[0]) + '_' + str(date_list[-1]) + '_'
    print('xlsx_name: {}'.format(xlsx_name))

    for tms in tm_rng:
        tm = tms.strftime('%Y-%m-%d')
        url = 'https://trade.500.com/jczq/?date={}'.format(tm)
        print(url)
        respone = requests.get(url, headers=header)
        print(respone.status_code)

        content = respone.content.decode('ISO-8859-1')
        soup = BeautifulSoup(respone.text, 'lxml')
        trs = soup.find_all('tr', class_="bet-tb-tr bet-tb-end")
        for tr in trs:
            # 编号
            td_no = tr.find_all('td', class_="td td-no")
            serial_number = td_no[0].text
            # 重复赋值是为了合并之后能够进行筛选
            serial_numbers.extend((serial_number, serial_number))
            # 赛事
            td_evt = tr.find_all('td', class_="td td-evt")
            game_name = td_evt[0].text.strip('\n')
            game_names.extend((game_name, game_name))
            # 开赛时间
            td_end_time = tr.find_all('td', class_="td td-endtime")
            game_time = td_end_time[0].text
            game_times.extend((game_time, game_time))
            # 依次为主队排名':'','主队':'','比分':'','客队':'','客队排名': ''
            td_team = tr.find_all('td', class_="td td-team")
            i = td_team[0].find_all('i')
            i0.extend((i[0].text, ''))
            i1.extend((i[2].text, ''))
            a = td_team[0].find_all('a')
            if len(a) == 3:
                a0.extend((a[0].text, ''))
                a1.extend((a[1].text, ''))
                a2.extend((a[2].text, ''))
            # 比赛未进行标签数量有变
            if len(a) < 3:
                a0.extend((a[0].text, ''))
                a1.extend((i[1].text, ''))
                a2.extend((a[1].text, ''))
            # 让球
            td_rang = tr.find_all('td', class_="td td-rang")
            p = td_rang[0].find_all('p')
            p0 = p[0].text
            p1 = p[1].text
            concede.extend((p0, p1))
            # 赔率
            td_bet_btn = tr.find_all('td', class_="td td-betbtn")
            p = td_bet_btn[0].find_all('p')
            if len(p) == 6:
                # 同时加载多个元素到列表
                victory.extend((p[0].text, p[3].text))
                # 加载字体标识判断值到列表
                victory_index.extend((p[0].attrs['class'][-1], p[3].attrs['class'][-1]))
                flat.extend((p[1].text, p[4].text))
                flat_index.extend((p[1].attrs['class'][-1], p[4].attrs['class'][-1]))
                defeat.extend((p[2].text, p[5].text))
                defeat_index.extend((p[2].attrs['class'][-1], p[5].attrs['class'][-1]))
            else:
                # 同时加载多个元素到列表
                victory.extend(('未开售', p[0].text))
                victory_index.extend(('未开售', p[0].attrs['class'][-1]))
                flat.extend(('未开售', p[1].text))
                flat_index.extend(('未开售', p[1].attrs['class'][-1]))
                defeat.extend(('未开售', p[2].text))
                defeat_index.extend(('未开售', p[2].attrs['class'][-1]))
    data['胜'], data['平'], data['负'] = victory, flat, defeat
    title['编号'], title['赛事'], title['开赛时间'], title['让球'] = serial_numbers, game_names, game_times, concede
    title['主队排名'], title['主队'], title['比分'], title['客队'], title['客队排名'] = i0, a0, a1, a2, i1
    p_victory = pd.Series(data=victory, index=victory_index)
    p_flat = pd.Series(data=flat, index=flat_index)
    p_defeat = pd.Series(data=defeat, index=defeat_index)
    df1 = pd.DataFrame(title)
    df2 = pd.DataFrame(data)

    now = time.time()
    ls = time.localtime(now)
    filetime = time.strftime('%Y_%m_%d_%H_%M')
    # df = pd.merge(df2,df1,how="inner",left_index=True,right_index=True)
    df1.to_excel('{}_table_{}.xlsx'.format(xlsx_name, filetime))
    # 通过p[n].attrs['class'] = ['betbtn'] or ['betbtn', 'betbtn-ok']确定中奖赔率(如何带格式写入)
    # 打开Excel程序，默认设置：程序可见，只打开不新建工作薄，屏幕更新关闭
    app = xw.App(visible=True, add_book=False)
    app.screen_updating = False  # 关闭显示更新
    app.display_alerts = False  # 关闭提示信息
    wk = app.books.open('{}_table_{}.xlsx'.format(xlsx_name, filetime))
    sht1 = wk.sheets['sheet1']
    sht1.range('K1').value = '胜'
    sht1.range('L1').value = '平'
    sht1.range('M1').value = '负'
    sht1.range('K1:M1').api.Font.Bold = True
    for nrows in range(1, len(p_flat) + 1):
        sht1.range(nrows + 1, 11).value = p_victory[nrows - 1]
        sht1.range(nrows + 1, 12).value = p_flat[nrows - 1]
        sht1.range(nrows + 1, 13).value = p_defeat[nrows - 1]
        if p_victory.index[nrows - 1] == 'betbtn-ok':
            sht1.range(nrows + 1, 11).api.Font.ColorIndex = 3
            sht1.range(nrows + 1, 11).api.Font.Bold = True
        if p_flat.index[nrows - 1] == 'betbtn-ok':
            sht1.range(nrows + 1, 12).api.Font.ColorIndex = 3
            sht1.range(nrows + 1, 12).api.Font.Bold = True
        if p_defeat.index[nrows - 1] == 'betbtn-ok':
            sht1.range(nrows + 1, 13).api.Font.ColorIndex = 3
            sht1.range(nrows + 1, 13).api.Font.Bold = True
    # 居中
    sht1.range('A1:M{}'.format(len(p_flat) + 1)).api.HorizontalAlignment = -4108
    sht1.range('A1:M{}'.format(len(p_flat) + 1)).api.VerticalAlignment = -4108
    # 增加边框
    sht1.range('A1:M{}'.format(len(p_flat) + 1)).api.Borders(9).LineStyle = 1
    sht1.range('A1:M{}'.format(len(p_flat) + 1)).api.Borders(10).LineStyle = 1
    sht1.range('A1:M{}'.format(len(p_flat) + 1)).api.Borders(11).LineStyle = 1
    sht1.range('A1:M{}'.format(len(p_flat) + 1)).api.Borders(12).LineStyle = 1
    sht1.autofit()
    # 合并单元格
    n_clos = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    nrows = sht1.used_range.last_cell.row
    for nclo in n_clos:
        for nrow in range(2, nrows, 2):
            cell = nclo + str(nrow) + ':' + nclo + str((nrow + 1))
            sht1.range(cell).merge()
    wk.save()
    wk.close()
    app.quit()


def main():
    lucky_dog()


if __name__ == '__main__':
    main()

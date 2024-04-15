# -*- coding: utf-8 -*-
"""
    @Time : 2024-04-14
    Description : 有用
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

columns_list = ['编号', '赛事', '开赛时间', '主队', '客队', '胜', '胜变化', '平', '平变化', '负', '负变化',
                'wdl变化时间', '让胜', '让胜变化', '让平', '让平变化', '让负', '让负变化', 'h_wdl变化时间']
df = pd.DataFrame(columns=columns_list)

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "86.0.4240.198 Safari/537.36"
}

url = 'https://trade.500.com/jczq/?playid=269&g=2&date=2024-04-11'
print(f'url: {url}')

response = requests.get(url, headers=header)
content = response.content.decode('ISO-8859-1')
soup = BeautifulSoup(response.text, 'lxml')

trs = soup.find_all('tr', class_="bet-tb-tr bet-tb-end")
for tr in trs:
    home_team = tr['data-homesxname']
    away_team = tr['data-awaysxname']
    match_events = tr['data-simpleleague']
    match_date = tr['data-matchdate']
    match_time = tr['data-matchtime']
    match_datetime = match_date + match_time
    interface_date = tr['data-processdate']
    match_no = tr['data-matchnum']
    data_id = tr['data-id']

    # 请求数据的 sp 变化接口
    win_draw_lose_url = 'https://trade.500.com/interface/request.php?q=public.readfile&step=readpl&playid=354&zxid={}&date={}'.format(
        data_id, interface_date)
    handicap_wdl_url = 'https://trade.500.com/interface/request.php?q=public.readfile&step=readpl&playid=269&zxid={}&date={}'.format(
        data_id, interface_date)
    # print("胜平负 sp 变化接口: {}".format(win_draw_lose_url))
    # print("受让球 sp 变化接口: {}".format(handicap_wdl_url))
    wdl_response = requests.get(win_draw_lose_url)
    handicap_wdl_response = requests.get(handicap_wdl_url)
    wdl_data = wdl_response.json()
    handicap_wdl_data = handicap_wdl_response.json()

    print(len(wdl_data['list']))
    print(len(handicap_wdl_data['list']))

    if len(wdl_data['list']) >= len(handicap_wdl_data['list']):
        for i in range(len(wdl_data['list'])):
            # print(i)
            data = {
                '编号': match_no,
                '赛事': match_events,
                '开赛时间': match_datetime,
                '主队': home_team,
                '客队': away_team
            }
            df = df.append(data, ignore_index=True)
    else:
        for i in range(len(handicap_wdl_data['list'])):
            data = {
                '编号': match_no,
                '赛事': match_events,
                '开赛时间': match_datetime,
                '主队': home_team,
                '客队': away_team
            }
            df = df.append(data, ignore_index=True)
    print(df)

    for i in wdl_data['list']:
        data = {
            '胜': i['win'],
            '胜变化': i['w'],
            '平': i['draw'],
            '平变化': i['d'],
            '负': i['lost'],
            '负变化': i['l'],
            'wdl变化时间': i['time']
        }
        # df = df.append(data, ignore_index=True)
        # 使用 loc 方法将数据插入到指定列的下一行
        # df.loc[len(df), ['胜', '胜变化', '平', '平变化', '负', '负变化', 'wdl变化时间']] = [data['胜'], data['胜变化'],
        #                                                                                     data['平'], data['平变化'],
        #                                                                                     data['负'], data['负变化'],
        #                                                                                     data['wdl变化时间']]
        # 找到 '胜' 列的第一行，并在该位置插入数据
        df.iloc[0, df.columns.get_loc('胜')] = data['胜']
        df.iloc[0, df.columns.get_loc('胜变化')] = data['胜变化']
        df.iloc[0, df.columns.get_loc('平')] = data['平']
        df.iloc[0, df.columns.get_loc('平变化')] = data['平变化']
        df.iloc[0, df.columns.get_loc('负')] = data['负']
        df.iloc[0, df.columns.get_loc('负变化')] = data['负变化']
        df.iloc[0, df.columns.get_loc('wdl变化时间')] = data['wdl变化时间']

    # print('================')

    for i in handicap_wdl_data['list']:
        data = {
            '让胜': i['win'],
            '让胜变化': i['w'],
            '让平': i['draw'],
            '让平变化': i['d'],
            '让负': i['lost'],
            '让负变化': i['l'],
            'h_wdl变化时间': i['time']
        }
        df.iloc[0, df.columns.get_loc('让胜')] = data['让胜']
        df.iloc[0, df.columns.get_loc('让胜变化')] = data['让胜变化']
        df.iloc[0, df.columns.get_loc('让平')] = data['让平']
        df.iloc[0, df.columns.get_loc('让平变化')] = data['让平变化']
        df.iloc[0, df.columns.get_loc('让负')] = data['让负']
        df.iloc[0, df.columns.get_loc('让负变化')] = data['让负变化']
        df.iloc[0, df.columns.get_loc('h_wdl变化时间')] = data['h_wdl变化时间']
        # df = df.append(data, ignore_index=True)
        # 使用 loc 方法将数据插入到指定列的下一行
        # df.loc[len(df), ['让胜', '让胜变化', '让平', '让平变化', '让负', '让负变化', 'h_wdl变化时间']] = [data['让胜'],
        #                                                                                                   data[
        #                                                                                                       '让胜变化'],
        #                                                                                                   data['让平'],
        #                                                                                                   data[
        #                                                                                                       '让平变化'],
        #                                                                                                   data['让负'],
        #                                                                                                   data[
        #                                                                                                       '让负变化'],
        #                                                                                                   data[
        #                                                                                                       'h_wdl变化时间']]

    print('')
    # print(df)

    # 保存新文件
    output_xlsx_file = 'test.xlsx'
    df.to_excel(output_xlsx_file, index=False)

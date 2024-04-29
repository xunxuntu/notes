def get_double_draw(excel_file=r'all_games.xlsx'):
    """
    获取比赛中双平的场次
    :return:
    """
    # excel_file = r'all_games.xlsx'
    current_date = datetime.now().date()
    current_date_path = Path(str(current_date))
    current_date_path.mkdir(exist_ok=True)
    output_xlsx_file = current_date_path / f"{excel_file.split(':')[0]}-双平场次-{current_date}.xlsx"

    # 读取原始 Excel 文件
    df = pd.read_excel(excel_file)

    # 新建一个 DataFrame 用于存储符合条件的数据
    new_df = pd.DataFrame(columns=df.columns)

    num_range = range(0, len(df), 2)  # 适用于每行两个球队比赛的情况
    for num in tqdm(num_range, desc='Processing'):  # 使用 tqdm 显示处理进度
        # print(f'num: {num}')
        score = df.at[num, '比分']
        # print(f'score: {score}')
        if pd.isna(score):
            continue  # 跳过NaN值的处理
        if score == 'VS':
            continue
        home_score, away_score = map(int, str(score).split(':'))
        # print(f'home_score: {home_score}, away_score: {away_score}')

        # 让球
        handicap_score = df.at[num + 1, '让球']
        if isinstance(handicap_score, str) and len(handicap_score) > 4:  # 过滤出 " 单关-3" 这样的字符
            if handicap_score[:3] == " 单关":
                handicap_score = int(handicap_score[3:])
        else:
            handicap_score = int(handicap_score)

        if home_score + handicap_score == away_score or home_score == away_score:
            # 双平局
            new_df = new_df.append(df.iloc[num:num + 2])

    match_count = new_df['比分'].count()
    all_match_count = df['比分'].count()
    percentage = match_count / all_match_count * 100
    print(f"双平场次: {match_count}, 占比: {percentage:.1f}%", )

    # 保存新文件
    new_df.to_excel(output_xlsx_file, index=False)

    # 美化 excel
    format_excel(output_xlsx_file)

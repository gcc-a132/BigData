def answer_three():
    # create sub dataframe of only elements with greater than 0 Gold and Gold.1
    sub_df = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)].copy()
    # calculate difference between Gold medals relative to total metal count
    sub_df['rel'] = sub_df['diff'] / sub_df['Gold.2']
    return sub_df[sub_df['rel'] == max(sub_df['rel'])].index[0]

answer_three()
def answer_two():
    # create new row containing abs value of Gold and Gold.1 differences
    df['diff'] = abs(df['Gold'] - df['Gold.1'])
    # index / name from the element with the largest difference
    return df[df['diff'] == df['diff'].max()].index[0]

answer_two()
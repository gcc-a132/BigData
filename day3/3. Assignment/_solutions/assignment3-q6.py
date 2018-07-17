def answer_six():
    df1 = pd.DataFrame(census_df.where(census_df['SUMLEV'] == 50).groupby(['STNAME'])['POPESTIMATE2015'].nlargest(3))
    df1 = df1.reset_index()

    return list(df1.groupby(['STNAME']).sum()['POPESTIMATE2015'].nlargest(3).index)

answer_six()
def answer_five():
    return census_df.groupby('STNAME')['COUNTY'].count().idxmax()

answer_five()
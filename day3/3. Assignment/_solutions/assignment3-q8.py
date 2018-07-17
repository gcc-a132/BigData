def answer_eight():

    return census_df[((census_df['REGION'] == 1) | (census_df['REGION'] == 2)) & (census_df['CTYNAME'].str.startswith("Washington") & (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014']))].loc[:,['STNAME','CTYNAME']]

answer_eight()
def answer_seven():
    d = census_df[census_df.SUMLEV==50].copy()
    d['max'] = d[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].max(axis=1)
    d['min'] = d[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].min(axis=1)
    d['diff'] = d['max'] - d['min']

    return d[d['diff'] == d['diff'].max()].iloc[0]['CTYNAME']

answer_seven()
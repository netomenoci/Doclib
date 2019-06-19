def score(corr_miss_info, df_user, name_miss_info, df_user_number):        #df_user: ligne correspondant à l'utilisateur
    #corr_miss_info: colonne de corrélation de l'information à estimer
    score = 0
    for column in corr_miss_info.columns.tolist()[1:65]:
        if column != "zipcode":
            if df_user.at[df_user_number,column] != np.nan:
                if column == "delay_in_days":
                    score += log(df_user.at[df_user_number,column]+1)*corr_miss_info.at[name_miss_info,column]/5
                elif column == "appt_duration":
                    score += df_user.at[df_user_number,column]*corr_miss_info.at[name_miss_info,column]/30
                else:
                    score += df_user.at[df_user_number,column]*corr_miss_info.at[name_miss_info,column]
    return score

def estimation_zipcode(corr_df, df_user_number, dataframe):     #corr_df matrice (type: dataframe) de corrélation du dataframe 
    df_user = dataframe.iloc[[df_user_number]].copy()               #dataframe: dataframe des données
    scores = []
    for i in range(24): 
        corr_area = corr_df.iloc[[65 + i]]                      #corr_area: renvoie le dataframe de corrélation correspondant à la région 65+i
        area_name = corr_df.index.tolist()[65 + i]
        score1 = score(corr_area, df_user, area_name, df_user_number)
        scores += [score1]
    m = max(scores)
    k = 0
    while scores[k] != m:
        k += 1
    return corr_df.index.tolist()[65 + k]

def count_total_area(name_area, dataframe):
    area_data = dataframe[[name_area]]
    n = 0
    l = area_data.size
    for i in range(l):
        if dataframe.at[i,name_area] == 1:
            n += 1
    return (n, n/l, name_area)

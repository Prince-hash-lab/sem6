def ujjwal_topsis(df, weight, impact):
    initial_df = df
    # Converting to floats - handling non-numeric values
    col = df.columns

    for i in range(1,len(col)):
        df[col[i]] = pd.to_numeric(df[col[i]], downcast="float")

    for i in range(len(weight)):
        weight[i] = float(weight[i])


    # Normalisation
    squares = []
    for i in df.columns[1:]:
        temp = 0
        for j in range(len(df.index)):
            temp += np.square(float(df.iloc[j][i]))
        squares.append(temp)

    # print(squares)
    k=0
    df_li = []
    for i in df.columns[1:]:
        # print(i)
        li = []
        for j in range(len(df.index)):
            a = float(df.iloc[j][i] / np.sqrt(squares[k]))
            li.append(a)

        df_li.append(li)
        k+=1

    new_df = pd.DataFrame()
    new_df[df.columns[0]] = df[df.columns[0]]


    for i in range(len(df_li)):
        new_df[df.columns[i+1]] = df_li[i]

    df = new_df


    # Multiplying with weights
    df_li = []
    k=0
    for i in df.columns[1:]:
        li = []
        for j in range(len(df.index)):
            a = df.iloc[j][i] * (weight[k])
            # df.iloc[j][i] = a
            li.append(a)
        df_li.append(li)
        k+=1

    new_df = pd.DataFrame()
    new_df[df.columns[0]] = df[df.columns[0]]

    for i in range(len(df_li)):
        new_df[df.columns[i+1]] = df_li[i]

    df = new_df

    # STEP 4 - Find ideal best and ideal worst 
    maximum = ['Ideal Best']
    minimum = ['Ideal Worst']

    for i in df.columns[1:]:
        column = df[i]
        max_value = column.max()
        maximum.append(max_value)
        min_value = column.min()
        minimum.append(min_value)

    k=1
    for i in impact:
        if i=='-':
            temp = maximum[k]
            maximum[k] = minimum[k]
            minimum[k] = temp
        k+=1
          
    df.loc[len(df.index)] = maximum
    df.loc[len(df.index)] = minimum

    # print(maximum)
    # print(minimum)

    # STEP 5 - Row wise Eucledian
    s_max = []
    s_min = []

    for j in range(len(df.index) - 2):
        temp_max = 0
        temp_min = 0
        for i in df.columns[1:]:
            temp_max += np.square(df.iloc[j][i] - df.iloc[-2][i])
            temp_min += np.square(df.iloc[j][i] - df.iloc[-1][i])

        s_max.append(round(np.sqrt(temp_max),4))
        s_min.append(round(np.sqrt(temp_min),4))

    df = df.iloc[:-2 , :] # Removing the last two rows
    
    avg_s = []
    for i in range(len(s_max)):
        avg_s.append((s_max[i] + s_min[i]))

    # print('S_max: ', s_max)
    # print('S_min: ', s_min)
    # print('Avg s: ', avg_s)

    # STEP 6 - Finding performance
    per = []
    for i in range(len(s_min)):
        per.append((s_min[i]/avg_s[i]))


    df = df.assign(Topsis_Score = per)
    df['Rank'] = df['Topsis_Score'].rank(ascending = 0)

    ranking = []
    for m in range(len(df.index)):
        ranking.append(int(df.loc[m]['Rank']))
            
    df.drop(['Rank'], axis = 1)

    df['Rank'] = ranking

    initial_df['Topsis Score'] = df['Topsis_Score']
    initial_df['Rank'] = df['Rank']

    # print(df)
    return initial_df
#This generates the correlation matrix 
import pandas as pd
import numpy as np
corr_matrix = []
def correlation_matrix(df):
    corr_mat = df.corr()
    i = 0
    for p in corr_mat:
        for j in corr_mat:
            corr_val = corr_mat.iloc[i][j]
            corr_matrix.append(
                {
                    'x': p,
                    'y': j,
                    'corr_val': corr_val
                }
                )
        i =+ i
    return pd.DataFrame(corr_matrix)

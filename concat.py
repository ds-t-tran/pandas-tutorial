import pandas as pd

df_addition_row = pd.DataFrame([["day1","tieptest",100,180]])
df_addition_row.columns =["day_no","class","point1","point2"]
df_addition_row.index   =[17]

pd.concat([df_sample,df_addition_row],axis=0)

# Add column point3
df_addition_col = pd.DataFrame([[120,160,100,180,110,80]]).T
df_addition_col.columns =["point3"]
df_addition_col.index   = [11,12,13,14,15,16]

pd.concat([df_sample,df_addition_col],axis=1)
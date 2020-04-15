import pandas as pd

df_sample.pivot_table("point1",     # column total
                       aggfunc="sum",  # sum total
                       fill_value=0,   # Trong TH không có giá trị thì fill 0
                       index="class",  # Giống như groupby, Cột nào sẽ làm hàng
                       columns="day_no")   #Cột nào sẽ làm cột
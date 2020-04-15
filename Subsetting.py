import pandas as pd

# Column filter with row values is day_no = tieptest1
df_sample[df_sample.day_no == "tieptest1"]  
#    day_no class point1 point2
# 11   day1     A    100    120
# 13   day1     A    200    100
# 15   day1     C    100    110

# Using arr boolean filter row dataframe:
series_bool = [True,False,True,False,True,False] 
#row = len(series_bool)
df_sample[series_bool]


#Using method query of Pandas
df_sample.query("day_no == 'tieptest1'")

# condition or is "|" and "&"
df_sample.query("day_no == 'tieptest1'|day_no == 'tieptest2'")

# Using variable
select_condition = "test1"
df_sample.query("day_no == @select_condition")

#Subsetting using index
df_sample.query("index == 11 ")  # get row with index 11
df_sample.query("index in [11,12] ") #　or là「in」
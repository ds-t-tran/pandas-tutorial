import pandas as pd 

# Sắp xếp df tăng dần theo cột nào đó
df = pd.DataFrame({'name': ['Nam', 'Hiếu', 'Mai', 'Hoa'], 'age': [18,18,17,19]})
print('Before sort\n', df)
df = df.sort_values('age', ascending=True)
print('After sort\n', df)
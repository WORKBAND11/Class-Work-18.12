import pandas as pd
# Чтение Excel-файла
df = pd.read_excel('tbl.xlsx')

# Посмотреть рандомные 5 строк
print(df.tail(5))


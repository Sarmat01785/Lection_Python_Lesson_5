
import pandas as pd


df = pd.read_csv('california_housing_train.csv') # DataFrame.head(n=5)
# df = pd.read_csv('california_housing_train.csv', sep=",") # DataFrame.head(n=5)

# df.head()
print(df) #  по умолчанию будут выведены первые 5 строк таблицы и последние 5 строк таблицы.
print(df.head())  #  по умолчанию будут выведены первые 5 строк таблицы
print(df.head(10)) #  по умолчанию будут выведены первые 10 строк таблицы

# df.tail()
print(df.tail()) # последние 5 строк таблицы.
print(df.tail(10)) # последние 10 строк таблицы.

df.shape  # Функция shape возвращает размеры таблицы: кортеж из 2 значений, 1 - количество строк, 2 - количество столбцов.
print(df.shape)
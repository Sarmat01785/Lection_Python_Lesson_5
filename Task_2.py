
import pandas as pd

df = pd.read_csv('california_housing_train.csv')

# Чтобы обнаружить пустые значения в таблице данных необходимо воспользоваться
# функцией .isnull().
# df.isnull()
print(df.isnull())
# Функция привела нашу таблицу к следующему виду True-False, где True - это пустая
# ячейка, False - это заполненная ячейка.

#  функцией .sum(). Данная функция выведет количество null-значений в каждой ячейке по столбцам.
# df.isnull().sum()
print(df.isnull().sum())


# Что бы нужно посмотреть тип даных столбца нужно применить функцию .dtypes.
# df.dtypes
print(df.dtypes)


# Чтобы узнать название всех столбцов в таблице, воспользуйтесь функцией .columns.
# df.columns
print(df.columns)


# Выборка данных

import pandas as pd

df = pd.read_csv('california_housing_train.csv')

# Если Вы хотите вывести 1 столбец на экран, то можно указать следующее выражение, которое позволит это сделать.
# df['latitude']
print(df['latitude'])

# вывести на экран сразу несколько столбцов
# df[['latitude', 'population']]
print(df[['latitude', 'population']])


# Задание: Необходимо вывести столбец total_rooms, у которого медианный возраст здания(housing_median_age) меньше 20.
# df[df['housing_median_age'] < 20]
print(df[df['housing_median_age'] < 20])


# Если Вам нужно поставить другое условие, то аналогично.
# & - выполнение одновременно всех условий.
# | - выполнение хотя бы одного из условия.

# df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]
print(df[df['housing_median_age'] > 20] & (df['total_rooms']))
print(df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)])


# или (если необходимо вывести 2 и более столбцов
# df[df['housing_median_age'] < 20, ['total_bedrooms', 'total_rooms']]

print(df[df['housing_median_age'] < 20, ['total_bedrooms', 'total_rooms']])


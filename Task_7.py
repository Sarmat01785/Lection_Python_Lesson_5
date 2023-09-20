# Гистограмма
# Способ представления табличных данных в графическом виде — в виде столбчатой
# диаграммы. По оси x обычно указывают значение, а по оси y - встречаемость(кол-во
# таких значений в выборке)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Можно видеть что у большинства семей доход находится между значениями 2 и 6. И
# только очень небольшое количество людей обладают доходом > 10.
df = pd.read_csv('california_housing_train.csv')
sns.histplot(data=df, x="median_income")
plt.show()


# Изобразим гистограмму по housing_median_age
# Распределение по возрасту более равномерное. Большую часть жителей
# составляют люди в возрасте от 20 до 40 лет. Но и молодежи не мало. Также очень
# много пожилых людей > 50 лет медианный возраст
sns.histplot(data = df, x = 'housing_median_age')
plt.show()



# посмотрим медианный доход у пожилых жителей
sns.histplot(data=df[df['housing_median_age']>50], x="median_income")
plt.show()


print(df.columns)


# разобьем возрастные группы на 3 категории те кто моложе 20 лет, от 20 до
# 50 и от 50, чтобы посмотреть влияет ли это на доход.
# Что в этом случае происходит внутри таблицы? Добавился новый столбец
# age_group, в котором будет указана соответствующая категория.
df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50),
'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'
print(df.columns)
print(df.head)


# Применим group_by, чтобы получить среднее значение
df.groupby('age_group')['median_income'].mean().plot(kind='bar')
plt.show()



# Seaborn так же позволяет нам смотреть распределение по многим параметрам.
# Давайте поделим группы по доходам на 2. Те у кого медианный доход выше 6 и те у
# кого меньше. Изобразим дополнительное измерение с помощью оттенка в виде
# возрастных групп и групп по доходам
df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'
print(df.columns)
print(df.head)
sns.displot(df, x="median_house_value", hue="income_group")
plt.show()
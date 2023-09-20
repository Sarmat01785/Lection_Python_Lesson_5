# Линейные графики
# Хорошо подойдут, если есть временная или какая-либо иная последовательность и
# значения, которые могут меняться в зависимости от нее. Для генерации линейных
# графиков в seaborn используется relplot функцию. Она также принимает
# DataFrame, x, y - столбцы.
# Для визуализации выбирается тип line:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_train.csv')
sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)
plt.show()

# Можно видеть, что в определенных местах долготы цена за дома резко
# подскакивает.
# Попробуем визуализировать longitude по отношения к median_house_value и поймем
# в чем же дело, почему цена так резко подскакивает.
sns.relplot(x = 'longitude', y = 'median_house_value', kind = 'line', data = df)
plt.show()


# Можно видеть, что в определенных местах широты цена за дома также очень
# высока.
# Используя точечный график можно визуализировать эти отношения с большей
# четкостью. Скорее всего резкий рост цен связан с близостью к ценному объекту,
# повышающему качество жизни, скорее всего побережью океана или реки.
sns.scatterplot(data=df, x="latitude", y="longitude", hue="median_house_value")
plt.show()

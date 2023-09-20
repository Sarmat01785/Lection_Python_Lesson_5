# Изображаем статистические отношения
# Scatterplot (Точечный график)
# Математическая диаграмма, изображающая значения двух переменных в виде
# точек на декартовой плоскости. Библиотека seaborn без труда принимает pandas
# DataFrame(таблицу). Чтобы изобразить отношения между двумя столбцами
# достаточно указать, какой столбец отобразить по оси x, а какой по оси y.


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv('california_housing_train.csv')

# Изображение точек долготы по отношению к широте
sns.scatterplot(data=df, x="longitude", y="latitude")
plt.show()

# Изображение точек количества домохозяйств по отношению к населению, с раскраской по количеству комнат
sns.scatterplot(data=df, x="households", y="population", hue="total_rooms")
plt.show()

# Помимо обозначения дополнительного измерения цветом мы можем использовать size.(Меняеться размер точек)
sns.scatterplot(data=df, x="households", y="population", hue="total_rooms", size=10)
plt.show()


# Мы можем визуализировать сразу несколько отношений, используя класс PairGrid
# внутри seaborn. PairGrid принимает как аргумент pandas DataFrame и
# визуализирует все возможные отношения между ними, в соответствии с
# выбранным типом графика.
cols = ['population', 'median_income', 'housing_median_age','median_house_value']
g = sns.PairGrid(df[cols])
g.map(sns.scatterplot)
plt.show()





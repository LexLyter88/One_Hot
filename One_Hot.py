# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = data['whoAmI'].unique() # Получаем уникальные категории из столбца 'whoAmI'

for category in categories:
    data[category] = (data['whoAmI'] == category).astype(int) # Создаем столбцы для каждой категории и заполняем их нулями

data = data.drop('whoAmI', axis=1)  # Можно удалить столбец 'whoAmI', так как у нас уже есть one-hot столбцы

data.head()

# С помощью метода pd.get_dummies

# import pandas as pd
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})

#categories = {'robot': 0, 'human': 1} # Создаем словарь для кодирования категорий в числовые значения

#data['whoAmI_numeric'] = data['whoAmI'].map(categories) # Преобразуем столбец 'whoAmI' в числовой формат

#one_hot = pd.get_dummies(data['whoAmI_numeric'], prefix='whoAmI') # Создаем one-hot вектора, используя метод pandas get_dummies

#data = pd.concat([data, one_hot], axis=1) # Добавляем one-hot вектора к исходному DataFrame

#data.head()
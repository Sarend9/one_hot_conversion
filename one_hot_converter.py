""""
Задача 44:
    В ячейке ниже представлен код генерирующий DataFrame,
    которая состоит всего из 1 столбца.

    Ваша задача перевести его в one hot вид.
    Надо это сделать без get_dummieНs.
"""

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("\nИсходные данные:")
print(data.head())
# print(data.to_string())

unique_values = list(set(data['whoAmI']))

for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype('int')

data = data.drop('whoAmI', axis=1)

print("\nДанные в one-hot виде:")
print(data.head())
# print(data.to_string())

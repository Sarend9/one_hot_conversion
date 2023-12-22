""""
Задача 44:
    В ячейке ниже представлен код генерирующий DataFrame,
    которая состоит всего из 1 столбца.

    Ваша задача перевести его в one hot вид.
    Надо это сделать без get_dummieНs.
"""

import pandas as pd
import random


def generate_data(num_robots=10, num_humans=10):
    lst = ['robot'] * num_robots
    lst += ['human'] * num_humans
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})
    return data


def one_hot_encode(df, column_name):
    unique_values = list(set(df[column_name]))

    for value in unique_values:
        df[value] = (df[column_name] == value).astype('int')

    df = df.drop(column_name, axis=1)
    return df


if __name__ == "__main__":
    data = generate_data()

    print("\nИсходные данные:")
    print(data.head())

    data = one_hot_encode(data, 'whoAmI')

    print("\nДанные в one-hot виде:")
    print(data.head())

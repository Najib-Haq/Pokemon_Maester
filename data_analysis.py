import loading_saving_dictionaries as lsd
import get_image as gm
import pandas as pd
import numpy as np

df = pd.read_csv("Dataset/combats.csv")
index = np.random.randint(0,len(df))

name2index = lsd.load_dict('name2index')
index2name = lsd.load_dict('index2name')

pokemon1 = df.iloc[index]['First_pokemon']
print(pokemon1)
pokemon2 = df.iloc[index]['Second_pokemon']
print(pokemon2)
winner = df.iloc[index]['Winner']

pokemon1 = index2name[pokemon1].split(" ")[0]
print(pokemon1)
pokemon2 = index2name[pokemon2].split(" ")[0]
print(pokemon2)
winner = index2name[winner]
gm.show(pokemon1, pokemon2, winner)


# count of names more than 1 string is 97
# TODO : can't show images from the site. any way to solve?
# df_pok = pd.read_csv("Dataset/pokemon.csv")
# count = 0
# for i in range(len(df_pok)):
#     if len(df_pok.iloc[i]['Name'].split(" "))!=1:
#         count += 1
#
# print(count)

# TODO : data analysis


import pandas as pd
import Random_forest_classifier as rfc
#import DNN as nn
import numpy as np
from sklearn.preprocessing import MinMaxScaler


types = ['Grass', 'Dark', 'Rock', 'Fighting', 'Psychic', 'Dragon', 'Water', 'Bug', 'Electric', 'Ice', 'Ghost', 'Ground', 'Steel', 'Fire', 'Flying', 'Normal', 'Poison', 'Fairy']

df_pokemon = pd.read_csv("Dataset/pokemon_ohe.csv")
df_combats = pd.read_csv("Dataset/combats.csv")

df_combats['Winner_index'] = df_combats['Winner']==df_combats['First_pokemon'] #attached y_true
###################### DATASET PREPROCESSING ################################
# df_pokemon = df_pokemon.drop('Name',1)
# df_pokemon = df_pokemon.drop('Generation',1)
#
# for type in types:
#     df_pokemon[type] = 0
#
#
# for i in range(len(df_pokemon)):
#     # print(df_pokemon['Type 1'].iloc[i])
#     df_pokemon[df_pokemon['Type 1'].iloc[i]].iloc[i] = 1
#     if not pd.isnull(df_pokemon['Type 2'].iloc[i]):
#         df_pokemon[df_pokemon['Type 2'].iloc[i]].iloc[i] = 1
#
# df_pokemon = df_pokemon.drop('Type 1',1)
# df_pokemon = df_pokemon.drop('Type 2',1)
# df_pokemon = df_pokemon.drop('#',1)
# df_pokemon.to_csv("Dataset/pokemon_ohe.csv")


# df_pokemon = pd.read_csv("Dataset/pokemon_ohe.csv")
# print(df_pokemon.head())

########################### TRIED DNN #########################################
#  dnn = nn.Neural_Net(num_features=df_pokemon.shape[1]-1,
#                     num_classes=2)
# scaler = MinMaxScaler()
# print(df_pokemon.head())
# df_pokemon[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']] = scaler.fit_transform(
#     df_pokemon[['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed']])
# print(df_pokemon.head())
# dnn.train(df_pokemon, df_combats, 10, 500)
###################################################################################################






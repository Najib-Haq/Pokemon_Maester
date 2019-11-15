import loading_saving_dictionaries as lsd
import get_image as gm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

types = ['Grass', 'Dark', 'Rock', 'Fighting', 'Psychic', 'Dragon', 'Water', 'Bug', 'Electric', 'Ice', 'Ghost', 'Ground', 'Steel', 'Fire', 'Flying', 'Normal', 'Poison', 'Fairy']
colors = ['lime', 'darkslateblue', 'silver', 'olive', 'gold', 'purple', 'cornflowerblue', 'lawngreen','yellow','skyblue','black','peru','dimgrey','orangered','azure','tan','magenta','pink']

color_dict = {}
for i in range(len(types)):
    color_dict[types[i]] = colors[i]

def add_to_dict(dict, key):
    if not pd.isnull(key):
        if key in dict.keys():
            dict[key] = dict[key] + 1
        else:
            dict[key] = 1


def add_dict_to_dict(dict, key1, key2):
    if pd.isnull(key1) or pd.isnull(key2):
        return
    else:
        if key1 in dict.keys():
            if key2 in dict[key1].keys():
                dict[key1][key2] += 1
            else:
                dict[key1][key2] = 1
        else:
            dict[key1] = {key2:1}





def get_max3(dict):
    vals = sorted(dict.values(), reverse=True)
    max_3 = []
    for i in vals[:5]:
        for key in dict.keys():
            if dict[key] == i:
                max_3.append(key)
                break
    return max_3


df = pd.read_csv("Dataset/combats.csv")
index = np.random.randint(0,len(df))

name2index = lsd.load_dict('name2index')
index2name = lsd.load_dict('index2name')

#################### TESTING THE DATASET #############################

# pokemon1 = df.iloc[index]['First_pokemon']
# print(pokemon1)
# pokemon2 = df.iloc[index]['Second_pokemon']
# print(pokemon2)
# winner = df.iloc[index]['Winner']
#
# pokemon1 = index2name[pokemon1].split(" ")[0]
# print(pokemon1)
# pokemon2 = index2name[pokemon2].split(" ")[0]
# print(pokemon2)
# winner = index2name[winner]
# gm.show(pokemon1, pokemon2, winner)

# count of names more than 1 string is 97
# TODO : can't show images from the site. any way to solve?
df_pok = pd.read_csv("Dataset/pokemon.csv")
# count = 0
# for i in range(len(df_pok)):
#     if len(df_pok.iloc[i]['Name'].split(" "))!=1:
#         count += 1
#
# print(count)

# TODO : data analysis

#################### DATASET ANALYSIS #############################

# find which type has the most appearences
# get all the types
type_set = {}
#save data
# for i in range(len(df_pok)):
#     type1 = df_pok.iloc[i]['Type 1']
#     type2 = df_pok.iloc[i]['Type 2']
#     if type1 in type_set.keys():
#         type_set[type1] = type_set[type1] + 1
#     else:
#         type_set[type1] = 1
#     if not pd.isnull(type2):
#         if type2 in type_set.keys():
#             type_set[type2] = type_set[type2] + 1
#         else:
#             type_set[type2] = 1
#
# lsd.save_dict(type_set, 'type')

# load data
type_set = lsd.load_dict('type')
# 
# print(type_set.keys())
# plt.figure()
# plt.bar(type_set.keys(), type_set.values())
# plt.title("Number of pokemon by type")
# plt.xticks(rotation=50)
# plt.xlabel("Maximum five types are = " + str(get_max3(type_set)))
# plt.savefig("Analysis/types_hist.png", bbox_inches = 'tight')
# 
# plt.figure()
# plt.pie([float(v) for v in type_set.values()], labels=[k for k in type_set.keys()],
#            autopct='%1.2f')
# plt.title("Percentage of pokemon by type")
# plt.savefig("Analysis/types_pie.png", bbox_inches = 'tight')

# get percentage of types based on combats
types_combats = {}
winner_combats = {}
loser_combats = {}
#load data
# for i in range(len(df)):
#     pok1 = df.iloc[i]['First_pokemon']
#     pok2 = df.iloc[i]['Second_pokemon']
#     winner = df.iloc[i]['Winner']
#     pok1_t1 = df_pok.iloc[pok1-1]['Type 1']
#     pok1_t2 = df_pok.iloc[pok1 - 1]['Type 2']
#     pok2_t1 = df_pok.iloc[pok2 - 1]['Type 1']
#     pok2_t2 = df_pok.iloc[pok2 - 1]['Type 2']
#     #print("First pokemon is : "+str(pok1) + " and in dict " + str(df_pok.iloc[pok1-1]["#"]))
#     if i%1000 == 0:
#         print(str(i)+"/"+str(len(df)) + " done.")
#     add_to_dict(types_combats, pok1_t1)
#     add_to_dict(types_combats, pok1_t2)
#     add_to_dict(types_combats, pok2_t1)
#     add_to_dict(types_combats, pok2_t2)
#     if pok1 == winner:
#         (winner_t1, winner_t2) = (pok1_t1, pok1_t2)
#         (loser_t1, loser_t2) = (pok2_t1, pok2_t2)
#     else:
#         (winner_t1, winner_t2) = (pok2_t1, pok2_t2)
#         (loser_t1, loser_t2) = (pok1_t1, pok1_t2)
#
#     add_to_dict(winner_combats, winner_t1)
#     add_to_dict(winner_combats, winner_t2)
#     add_to_dict(loser_combats, loser_t1)
#     add_to_dict(loser_combats, loser_t2)
#
# lsd.save_dict(types_combats,"type_combat")
# lsd.save_dict(winner_combats, "winners")
# lsd.save_dict(loser_combats, "losers")

#load_data
types_combats = lsd.load_dict("type_combat")
winner_combats = lsd.load_dict("winners")
loser_combats = lsd.load_dict("losers")
#load data
# plt.figure()
# plt.bar(types_combats.keys(), types_combats.values(), color = 'cyan')
# plt.title("Pokemon in combat by type")
# plt.xlabel("Maximum five types are = " + str(get_max3(types_combats)))
# plt.xticks(rotation=50)
# plt.savefig("Analysis/combat_types_hist.png", bbox_inches = 'tight')
# 
# plt.figure()
# plt.pie([float(v) for v in types_combats.values()], labels=[k for k in types_combats.keys()],
#            autopct='%1.2f')
# plt.title("Percentage of pokemon in combat list by type")
# plt.savefig("Analysis/combat_types_pie.png", bbox_inches = 'tight')
sorted_winner_percentage = {}
for key in types_combats.keys():
    sorted_winner_percentage[key] = (winner_combats[key] / types_combats[key])*100
# plt.figure()
# plt.bar(sorted_winner_percentage.keys(), sorted_winner_percentage.values(), color = 'seagreen')
# plt.title("Most winning ratio by type")
# plt.xlabel("Maximum five types are = " + str(get_max3(sorted_winner_percentage)))
# plt.xticks(rotation=50)
# plt.savefig("Analysis/winning_ratio_hist.png", bbox_inches = 'tight')
#
# plt.figure()
# plt.pie([float(v) for v in sorted_winner_percentage.values()], labels=[k for k in sorted_winner_percentage.keys()],
#            autopct='%1.2f')
# plt.title("Percentage of winner ratio list by type")
# plt.savefig("Analysis/winning_ratio_pie.png", bbox_inches = 'tight')
# plt.show()


# type_advantage = {}
# type_disadvantage = {}
# for i in range(len(df)):
#     if i % 1000 == 0:
#         print(str(i)+"/"+str(len(df)) + " done.")
#     winner_t1 = df_pok.iloc[df.iloc[i]['Winner'] - 1]['Type 1']
#     winner_t2 = df_pok.iloc[df.iloc[i]['Winner'] - 1]['Type 2']
#     if df.iloc[i]['Winner'] == df.iloc[i]['First_pokemon']:
#         loser_t1 = df_pok.iloc[df.iloc[i]['Second_pokemon']-1]['Type 1']
#         loser_t2 = df_pok.iloc[df.iloc[i]['Second_pokemon'] - 1]['Type 2']
#     else:
#         loser_t1 = df_pok.iloc[df.iloc[i]['First_pokemon'] - 1]['Type 1']
#         loser_t2 = df_pok.iloc[df.iloc[i]['First_pokemon'] - 1]['Type 2']
#
#     add_dict_to_dict(type_advantage, winner_t1, loser_t1)
#     #add_dict_to_dict(type_advantage, winner_t1, loser_t2)
#     #add_dict_to_dict(type_advantage, winner_t2, loser_t1)
#     #add_dict_to_dict(type_advantage, winner_t2, loser_t2)
#
#     add_dict_to_dict(type_disadvantage, loser_t1, winner_t1)
#     #add_dict_to_dict(type_disadvantage, loser_t2, winner_t1)
#     #add_dict_to_dict(type_disadvantage, loser_t1, winner_t2)
#     #add_dict_to_dict(type_disadvantage, loser_t2, winner_t2)
#
# lsd.save_dict(type_advantage, 'type_advantage')
# lsd.save_dict(type_disadvantage, 'type_disadvantage')



type_advantage = lsd.load_dict('type_advantage')
type_disadvantage = lsd.load_dict('type_disadvantage')
for i in type_disadvantage.keys():
    for j in types:
        if j not in type_disadvantage[i].keys():
            type_disadvantage[i][j] = 0

type_superiority = {}
for i in type_advantage.keys():
    type_superiority[i] = {}
    for j in type_advantage[i].keys():
        winning = type_advantage[i][j]
        total = type_advantage[i][j] + type_disadvantage[i][j]
        type_superiority[i][j] = (winning/total)*100

# for i in type_superiority.keys():
#     plt.figure()
#     type = []
#     vals = []
#     colors = []
#     for j in sorted(type_superiority[i], key=lambda k: type_superiority[i][k]):
#         type.append(j)
#         vals.append(type_superiority[i][j])
#         colors.append(color_dict[j])
#     plt.bar(type, vals, color=colors)
#     plt.title(str(i) + " type winnings")
#     plt.xticks(rotation=50)
#     plt.savefig("Analysis/Type_advantage/" + str(i)+" type.png", bbox_inches = 'tight')
#     plt.show()









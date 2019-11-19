import loading_saving_dictionaries as lsd
import get_image as gm
import Random_forest_classifier as rfc
import pandas as pd

name2index = lsd.load_dict("name2index")
index2name = lsd.load_dict("index2name")

df_pokemon = pd.read_csv('Dataset/pokemon_ohe.csv')
df_combats = pd.read_csv('Dataset/combats.csv')
df_combats['Winner_index'] = df_combats['Winner']==df_combats['First_pokemon']
############################TRAINING MODEL###################################
# print("Training Part commencing : ")
# rf_classifier = rfc.RFC(df_pokemon, df_combats, len(df_combats))
# rf_classifier.train()
#
# lsd.save_dict(rf_classifier, "classifier")

rf_classifier = lsd.load_dict("classifier")


print("Testing Part commencing : ")
while True:
    pok1 = input("Please enter pokemon 1 name : ")
    pok2 = input("Please enter pokemon 2 name : ")
    pok1i = name2index[pok1]
    pok2i = name2index[pok2]
    if rf_classifier.test(pok1i, pok2i, df_pokemon)[0] == 0:
        winner = pok1
    else:
        winner = pok2
    gm.show(pok1, pok2, winner)



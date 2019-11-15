import pickle
import pandas as pd

location_name = 'Dictionaries/'

def save_dict(dict, filename):
    location = location_name + filename + '.p'
    with open(location, 'wb') as fp:
        pickle.dump(dict, fp, protocol=pickle.HIGHEST_PROTOCOL)


def load_dict(filename):
    location = location_name + filename + '.p'
    with open(location, 'rb') as fp:
        HMap = pickle.load(fp)
    return HMap


if __name__ == "__main__":
    df = pd.read_csv('Dataset/pokemon.csv')
    name_to_index = {}
    index_to_name = {}
    for i in range(len(df)):
        name_to_index[df.iloc[i]['Name']] = df.iloc[i]['#']
        index_to_name[df.iloc[i]['#']] = df.iloc[i]['Name']
    save_dict(name_to_index, 'name2index')
    save_dict(index_to_name, 'index2name')
















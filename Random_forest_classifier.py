import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer

class RFC:
    def __init__(self, df_pok, df_combat, x_size, test_size=0.25):
        self.X, self.y = self.get_batches(df_pok, df_combat, 0, x_size)
        self.test_size = test_size
        self.X_train, self.X_test, self.y_train, self.y_test = 0,0,0,0
        self.pipeline = make_pipeline(Imputer(), RandomForestClassifier())
        self.sc = StandardScaler()

    def get_batches(self,df_pok, df_combat, index_start, index_end):
        x1 = []
        x2 = []
        x = []
        y = []
        for i in range(index_start, index_end):
            if i%1000 == 0:
                print(str(i) + " done")

            x1.append(list(df_pok.iloc[df_combat['First_pokemon'].iloc[i] - 1][1:]))
            x2.append(list(df_pok.iloc[df_combat['Second_pokemon'].iloc[i] - 1][1:]))
            x.append(x1[i]+x2[i])
            y.append(df_combat['Winner_index'].iloc[i])


        return np.array(x, dtype=np.float32), np.array(y, dtype=np.int32)


    def preprocessing(self):
        self.X_train, self.X_test, self.y_train, self.y_test=train_test_split(
            self.X,self.y,test_size=self.test_size,random_state=0)

        self.X_train=self.sc.fit_transform(self.X_train)
        self.X_test=self.sc.transform(self.X_test)


    def train(self):
        self.preprocessing()
        self.pipeline.fit(self.X_train, self.y_train)
        y_pred = self.pipeline.predict(self.X_test)

        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(self.y_test, y_pred)
        print("Confusion matrix : ")
        print(cm)  # accuracy 93%
        return cm


    def test(self, pok1, pok2, df_pok):
        x1 = list(df_pok.iloc[pok1 - 1][1:])
        x2 = list(df_pok.iloc[pok2 - 1][1:])
        test_data = [x1+x2]

        y_pred = self.pipeline.predict(test_data)
        return y_pred



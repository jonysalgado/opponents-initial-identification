import os 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

CSV_DIR = os.getcwd() + "/../csv/"
dataset = pd.read_csv(CSV_DIR + "dataset.csv")
columns = dataset.shape[1]
# print(columns)
previsores = dataset.iloc[:, 1:columns-1].values
classe = dataset.iloc[:, columns-1].values
labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)
labelencoder.inverse_transform([0,1,2,3,4])
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(
                                                    previsores,
                                                    classe,
                                                    test_size = 0.3,
                                                    random_state = 0
                                                    )

neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(x_treinamento, y_treinamento)
# print(y_treinamento.shape[0])
y_pred = neigh.predict(x_teste)
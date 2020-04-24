import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from  sklearn import svm, model_selection, neighbors
import random
import joblib
import pickle

def getName(userData):
    # print("사용자 데이터:",userData)
    # df = pd.read_csv("iris.csv")
    # train_data, test_data, train_label, test_label = tuple(
    #     model_selection.train_test_split(df.iloc[:, 0:4], df.iloc[:, 4]))
    #
    # knn = neighbors.KNeighborsClassifier(n_neighbors=1)
    # knn.fit(train_data, train_label)
    # # 4.8,3.1,1.6,.2,"Setosa"
    # # userData = [[4.8, 3.1, 1.6, .2]]
    # result = knn.predict(userData)
    model =joblib.load("iris.pkl")
    result = model.predict(userData)
    return result
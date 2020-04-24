import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from  sklearn import svm, model_selection, neighbors
import random
import pickle
import joblib

#4.8,3.1,1.6,.2,"Setosa"
model = joblib.load('iris_model.pkl')
userData = [[4.8,3.1,1.6,.2]]
result = model.predict(userData)
print(result)


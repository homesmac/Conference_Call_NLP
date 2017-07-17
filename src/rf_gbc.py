from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import textwrap
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_predict
from sklearn import preprocessing

def load_and_split_data():

    gbdata = pd.read_csv('./data/alldata.csv', delimiter='\t')
    nlp_model = TfidfVectorizer(stop_words="english")
    le = preprocessing.LabelEncoder()
    X = gbdata.apply(LabelEncoder().fit_transform)
    X = X.drop(['Classifier_x'], axis=1)
    X = X.drop(['Link_x'], axis=1)
    X = X.drop(['Link_y'], axis=1)
    X = X.drop(['Labels_x'], axis=1)
    X = X.drop(['Labels_y'], axis=1)
    X = X.drop(['Train_x'], axis=1)
    X = X.drop(['Next_y'], axis=1)
    X = X.drop(['Compound'], axis=1)
    X = X.drop(['Train_y'], axis=1)
    y = gbdata['Classifier_x'].values.reshape(len(gbdata['Classifier_x'], ))

    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                       test_size = 0.2, 
                                       random_state = 5)
    return (X_train, X_test, y_train, y_test)

def cross_val(estimator, X_test, y_test, nfolds):

    mse = cross_val_score(estimator, X_test, y_test, 
                          scoring='neg_mean_squared_error',
                          cv=nfolds, n_jobs=-1) * -1
    # mse multiplied by -1 to make positive
    r2 = cross_val_score(estimator, X_test, y_test, 
                         scoring='r2', cv=nfolds, n_jobs=-1)
    
    mean_mse = mse.mean()
    mean_r2 = r2.mean()
    name = estimator.__class__.__name__
    print "{0:<25s} Test CV | MSE: {1:0.3f} | R2: {2:0.3f}".format(name,
                                                        mean_mse, mean_r2)
    return mean_mse, mean_r2

#load and train-test-split data 
(X_train, X_test, y_train, y_test) = load_and_split_data()

#define models and compare the mse and r2 
rf = RandomForestClassifier(n_estimators=100, random_state=5)

gdbc = GradientBoostingClassifier(learning_rate=0.1,
                                 n_estimators=100, random_state=5)

# number of folds in the cross-validation 
k = 10 
cross_val(rf, X_train, y_train, k) 
cross_val(gdbc, X_train, y_train, k)
cross_val_predict(gdbc, X_train, y_train, method='predict_proba')
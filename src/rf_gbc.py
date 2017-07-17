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

from sklearn import preprocessing

def load_and_split_data():

    data = pd.read_csv('./data/alldata.csv', delimiter='\t')
    nlp_model = TfidfVectorizer(stop_words="english")

    le = preprocessing.LabelEncoder()
    X = data.apply(LabelEncoder().fit_transform)


    y = data['Classifier_x'].values.reshape(len(data['Classifier_x'], ))

    #column_names = ['Ticker', 'Link_x', 'Labels_x', 'Train_x', 'Classifier_x', 'Current_x', 'Next_x', 'Link_y', 'Labels_y', 'Train_y', 'Classifier_y', 'Current_y', 'Next_y', 'Compound', 'Neg', 'Neu', 'Pos', 'Wordcount']
    #print column_names
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                       test_size = 0.2, 
                                       random_state = 1)
    return (X_train, X_test, y_train, y_test)

def cross_val(estimator, X_train, y_train, nfolds):
    ''' Takes an instantiated model (estimator) and returns the average
        mean square error (mse) and coefficient of determination (r2) from
        kfold cross-validation.
        Parameters: estimator: model object
                    X_train: 2d numpy array
                    y_train: 1d numpy array
                    nfolds: the number of folds in the kfold cross-validation
        Returns:  mse: average mean_square_error of model over number of folds
                  r2: average coefficient of determination over number of folds
    
        There are many possible values for scoring parameter in cross_val_score.
        http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
        kfold is easily parallelizable, so set n_jobs = -1 in cross_val_score
    '''
    mse = cross_val_score(estimator, X_train, y_train, 
                          scoring='neg_mean_squared_error',
                          cv=nfolds, n_jobs=-1) * -1
    # mse multiplied by -1 to make positive
    r2 = cross_val_score(estimator, X_train, y_train, 
                         scoring='r2', cv=nfolds, n_jobs=-1)
    mean_mse = mse.mean()
    mean_r2 = r2.mean()
    name = estimator.__class__.__name__
    print "{0:<25s} Train CV | MSE: {1:0.3f} | R2: {2:0.3f}".format(name,
                                                        mean_mse, mean_r2) 
    return mean_mse, mean_r2



if __name__ == '__main__':

    # 2) load and train-test-split data 
    (X_train, X_test, y_train, y_test) = load_and_split_data()
    
    # 3) define models then compare the mse and r2 
    # instantiate models, note random forest can be parallelized (n_jobs = -1)
    rf = RandomForestClassifier(n_estimators=100, random_state=1)

    gdbc = GradientBoostingClassifier(learning_rate=0.1,
                                     n_estimators=100, random_state=1)


   
    # 4) perform the cross-validation and print results
    k = 10 # number of folds in the cross-validation 
    #print "\nScript output."
    #print "Using {0} folds in cross validation.".format(k)
    #print "\n4) Train MSE and R2 for the 3 models"
    cross_val(rf, X_train, y_train, k) 
    cross_val(gdbc, X_train, y_train, k) 

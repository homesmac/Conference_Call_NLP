import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split


def MNB():
    # read in data
    data = pd.read_csv('../data/train2.txt', header=None, delimiter='\n')
    labels = pd.read_csv('../data/labels2.txt', header=None, delimiter='\n')

    # vectorize words
    nlp_model = TfidfVectorizer(stop_words="english")

    # get the nlp vectorized
    X = nlp_model.fit_transform(data[0])

    print "Words in corpus:", len(X.toarray())

    # modify the shape of the labels array
    # do this before train_test_split
    y_labels = np.array(labels)
    y_labels.reshape(len(y_labels), )


    # train test split would be nice but later
    X_train, X_test, y_train, y_test = train_test_split(X, y_labels, test_size=0.25)


    # create the classifier model
    mnb_classifier = MultinomialNB(threshold)

    # do some unoptimized hyperparamter tuning
    gbc_classifier = GradientBoostingClassifier(learning_rate=0.1, n_estimators=100)

    # fit the classier, currently on all data (bad)
    mnb_class_result = mnb_classifier.fit(X_train, y_train)
    gbc_class_result = gbc_classifier.fit(X_train, y_train)

    print "Multinomial Naive Bayes Score: ", mnb_class_result.score(X_test, y_test)
    print "GBC Score: ", gbc_class_result.score(X_test.toarray(), y_test)

0

if __name__ == '__main__':
    MNB()


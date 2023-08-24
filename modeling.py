from pydataset import data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

import warnings
warnings.filterwarnings('ignore')

import acquire
import prepare
import explore


def rforest(X_train, X_validate, y_train, y_validate):
    '''This function runs multiple random forest models up to 10 max depth and 10 min samples
    and provides them in a dataframe
    
    arguments: X_train, X_validate, y_train, y_validate 
    
    returns a pandas dataframe'''

    scores_all = []

    for x in range(1,11):
        
        # looping through min_samples_leaf front to back 
        # looping through max_depth back to front
        rf = RandomForestClassifier(random_state=7, min_samples_leaf=x, max_depth=11-x) # different if x = 10 vs x = 1
        #fit it
        rf.fit(X_train, y_train)
        #transform it
        train_acc = rf.score(X_train, y_train)
        
        #evaluate on my validate data
        val_acc = rf.score(X_validate, y_validate)
        diff_acc = train_acc - val_acc
        scores_all.append([x, 11-x, train_acc, val_acc, diff_acc])

    scores_df = pd.DataFrame(scores_all, columns =['min_samples_leaf','max_depth','train_acc','val_acc', 'diff_acc'])
    scores_df = scores_df.sort_values('diff_acc', ascending=True)
    return scores_df

def plotForest(scores_df):  
    '''graphs the random forest models from rforest function
    
    arguments: scores_df
    
    returns a matplotlib visual'''

    plt.figure(figsize=(12,6))
    plt.plot(scores_df.max_depth, scores_df.train_acc, label='train', marker='o')
    plt.plot(scores_df.max_depth, scores_df.val_acc, label='validate', marker='o')
    plt.xlabel('max depth and min leaf sample')
    plt.ylabel('accuracy')

    plt.xticks([1,2,3,4,5,6,7,8,9,10],
            [('1 and 10'),('2 and 9'),('3 and 8'),('4 and 7'),('5 and 6'),
            ('6 and 5'),('7 and 4'), ('8 and 3'), ('9 and 2'), ('10 and 1') ]
            )

    plt.title('Random Forest\nThe accuracy change with hyper parameter tuning on train and validate')
    plt.legend()
    plt.show()

def get_knn(X_train, X_validate, y_train, y_validate):
    ''''''
    k_range = range(1, 20)
    train_scores = []
    validate_scores = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors = k, weights='uniform')
        knn.fit(X_train, y_train)
        train_scores.append(knn.score(X_train, y_train))
        validate_scores.append(knn.score(X_validate, y_validate))
    plt.figure(figsize=(12,6))
    plt.xlabel('k')
    plt.ylabel('accuracy')
    plt.title('KNN\nThe accuracy change with hyper parameter tuning on train and validate')
    plt.plot(k_range, train_scores, label='Train')
    plt.plot(k_range, validate_scores, label='Validate')
    plt.legend()
    plt.xticks([0,5,10,15,20])
    plt.show()



def get_knn10(X_train, X_validate, y_train, y_validate):
    knn10 =  KNeighborsClassifier(n_neighbors=10, weights='uniform')
    knn10.fit(X_train, y_train)
    print(f' Accuracy of KNN on train data is {knn10.score(X_train, y_train)}')
    print(f' Accuracy of KNN on validate data is {knn10.score(X_validate, y_validate)}')


def get_logreg(X_train, X_validate, y_train, y_validate):
    logit = LogisticRegression()
    logit.fit(X_train, y_train)
    print(f' Accuracy of Logistic Regression on train is {logit.score(X_train, y_train)}')
    print(f' Accuracy of Logistic Regression on train is {logit.score(X_validate, y_validate)}')

def get_logreg_test(X_train, X_test, y_train, y_test):
    '''get logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
    logit = LogisticRegression()
    logit.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Logistic Regression on test is {logit.score(X_test, y_test)}")

def get_rf(X_train, X_validate, y_train, y_validate):

    rf = RandomForestClassifier(random_state=7, min_samples_leaf=8, max_depth=3)
    rf.fit(X_train, y_train)
    print(f' Accuracy of Random Forest on train data is {rf.score(X_train, y_train)}')
    print(f' Accuracy of Random Forest on train data is {rf.score(X_validate, y_validate)}')

def log_to_csv(X_train, X_test, y_train, y_test):
    # Train the Logistic Regression model
    logit = LogisticRegression()
    logit.fit(X_train, y_train)
    # Obtain predictions and probabilities on the test set
    logit_y_test_pred = logit.predict(X_test)
    logit_y_test_proba = logit.predict_proba(X_test)
    
    
    # Create a DataFrame to store results for the test set
    results_test_df = pd.DataFrame({
        'customer_id': X_test.index,
        'probability_of_churn': logit_y_test_proba[:, 1],  # Probability of churn
        'prediction_of_churn': logit_y_test_pred  # Binary prediction (1 for churn, 0 for not churn)
    })
    results_test_df.to_csv('churn_predictions.csv', index=False)
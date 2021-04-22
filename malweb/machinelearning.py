# scipy
import scipy
# numpy
import numpy
# matplotlib
import matplotlib
# pandas
import pandas
# scikit-learn
import sklearn

from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression #Using this one
from sklearn.tree import DecisionTreeClassifier #Using this one
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB #Using this one
from sklearn.svm import SVC

def run_models(Xnew):
    lrClassification = ''
    nbClassification = ''
    dtClassification = ''
    le = preprocessing.LabelEncoder()
    dataset = pandas.read_csv("https://raw.githubusercontent.com/kdavis34/Malweb/dataset/AlteredB2Datasetv2.csv")
    dataset = dataset.apply(lambda col: le.fit_transform(col.astype(str)), axis=0, result_type='expand')
    #processed_dataset = dataset.apply(lambda col: le.fit_transform(col.astype(str)), axis=0, result_type='expand')

    X = dataset.drop(['TYPE','URL','SERVER'], axis=1)
    y = dataset['TYPE']



    modelLR = LogisticRegression(max_iter=2500)
    modelLR.fit(X, y) #Supplying the model with data and its target

    modelBayes = GaussianNB()
    modelBayes.fit(X, y) #Supplying the model with data and its target

    modelTree = DecisionTreeClassifier()
    modelTree.fit(X, y) #Supplying the model with data and its target

    yNewLR = modelLR.predict(Xnew)
    yNewBayes = modelBayes.predict(Xnew)
    yNewTree = modelTree.predict(Xnew)

    class_results = [yNewLR[0], yNewBayes[0], yNewTree[0]] #1 = malicious, 0 = not malicious

    if (yNewLR[0] == 1):
        lrClassification = 'Malicious'
    else:
        lrClassification = 'Benign'
    if (yNewBayes[0] == 1):
        nbClassification = 'Malicious'
    else:
        nbClassification = 'Benign'
    if (yNewTree[0] == 1):
        dtClassification = 'Malicious'
    else:
        dtClassification = 'Benign'

    return class_results, lrClassification, nbClassification, dtClassification

#Now all that's necessary is to get the new data instance from the user submitted URL, call the predict function and return the value
#I know that everything is just in a Python file for right now, but all of this stuff should be able to be moved to a function, which could be called when the user presses "submit" on the website



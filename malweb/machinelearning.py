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

url = "https://raw.githubusercontent.com/kdavis34/Malweb/dataset/AlteredB2Dataset.csv"
names = ['url', 'url_length', 'tld', 'server', 'state', 'reg_date', 'zipcode', 'city', 'content_encoding', 'content_type', 'class']
dataset = read_csv(url, names=names)

array = dataset.values
X = array[:, 0:10] #This is all of the features of the data set
y = array[:,10] #This is the type classification (1 (malicious) or 0 (good))

modelLR = LogisticRegression()
modelLR.fit(X, y) #Supplying the model with data and its target

modelBayes = GaussianNB()
modelBayes.fit(X, y) #Supplying the model with data and its target

modelTree = DecisionTreeClassifier()
modelTree.fit(X, y) #Supplying the model with data and its target

#Now all that's necessary is to get the new data instance from the user submitted URL, call the predict function and return the value
#I know that everything is just in a Python file for right now, but all of this stuff should be able to be moved to a function, which could be called when the user presses "submit" on the website



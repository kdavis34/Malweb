from flask import Flask, render_template, request, redirect, url_for
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

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
@app.route('/results', methods=['GET','POST'])
def search():
	if request.method =='POST':
		
		url_raw = request.form['webURL']
		
		#This dummy format function should be format function (slightly modified though to return a URL) from the format Python script
		#The format script can probably be added to the directory and then the function could be imported
		url = dummy_format_func(url_raw)

		#This dummy extraction function should be the extraction function that returns a list of the data instance's values
		#The extraction script can probably be added to the directory and then the function could be imported
		XnewRaw = dummy_extract_func(url) 
		
		#Then, preprocess XnewRaw so that it matches the coding in the data set.
		#Should probably do this within this Python file
		Xnew = preprocess_instance(XnewRaw)

		#run_models should return a list of classification results
		class_results = run_models(Xnew)

		#This final classification should be a 0 or 1 and determines if the website is malicious or not
		#This value and other values (like the list of classification results) should be fed to the results page
		final_classification = weight_results(class_results)
		
		return render_template('results.html')

#@app.route("/page2")
#def page2():
#	return render_template('page2.html')

def dummy_format_func(raw_url):
	print("placeholder function")
	return True

def dummy_extract_func(formatted_url):
	print("placeholder function")
	return True

def preprocess_instance(data_instance):
	print("preprocessing")
	preprocessed_instance = 0
	return preprocessed_instance #The new preprocessed list should be returned

def weight_results(results):
	#Take list of results (which should be 0's or 1's or both) and weights them according to some alg. determined by team
	weighted_results = 0
	return weighted_results

def run_models(Xnew):
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

    #Now, we should take Xnew (the new data instance) and call the predict function for each model.
    #Then, take the results from each model and put them into a list

    return True #This should be a list of the classification results from the 3 algorithms (in order of LR, Bayes, Tree)

if __name__ == "__main__":
	app.run()

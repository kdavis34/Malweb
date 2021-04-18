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
from FormatURLs import format_url, convert_extracted_features
from FeatureExtractor import extract_features
from machinelearning import run_models

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
@app.route('/results', methods=['GET','POST'])
def search():
	if request.method =='POST':
		global url_raw
		url_raw = request.form['webURL']
		
		#The format_url is imported from the FormatURLs script
		url = format_url(url_raw)
		print(url)
		#The extract_features function is imported from the FeatureExtractor script
		XnewRaw = extract_features(url) 
		print(XnewRaw)
		#This preprocessing function formats the new data instance so that it correctly matches the data items in the data set
		Xnew = preprocess_instance(XnewRaw)
		print(Xnew)
		#This function encodes the features of the url to integers to be used by the models
		XnewProcessed = convert_extracted_features(Xnew)
		print(XnewProcessed)
		#run_models should return a list of classification results (Ordered LR, Bayes, Tree)
		try:
			class_results, lrClassification, nbClassification, dtClassification = run_models(XnewProcessed)
			print(class_results)
		except:
			return Error()
		#This value and other values (like the list of classification results) should be fed to the results page
		try:
			final_classification = weight_results(class_results)
			print(final_classification)
			return render_template('results.html', url=url_raw, classification=final_classification,
				lrClass=lrClassification, nbClass=nbClassification, dtClass=dtClassification)
		except:
			return Error()

@app.route("/error")
def Error():
	return render_template('error.html', url=url_raw)

#Preprocesses the data so that the new data instances match the data instances within the data set
def preprocess_instance(data_instance):
    for index, item in enumerate(data_instance):
        if item == None and index > 4 and index < 9:
            data_instance[index] = '0'
        if item != None and index > 4 and index < 9:
            data_instance[index] = '1'
    return data_instance

#Weights the classification results of the 3 ML algorithms used
def weight_results(class_results):
	#LR - .833 = 31.8%
	#Bayes - .838 = 32.0%
	#Tree - .948 = 36.2%
	#Total = 2.619   

	weighted_class = ""

	summation = (.318*class_results[0]) + (.32*class_results[1]) + (.362*class_results[2])
	
	if summation > .5:
		weighted_class = "Malicious"
	else:
		weighted_class = "Benign"

	return weighted_class


if __name__ == "__main__":
	app.run()

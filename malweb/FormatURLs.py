import pandas
import numpy
from sklearn import preprocessing

# Formats a list of urls given in a txt file by concatenating "http://" to the beginning and stripping the new line character
def format_txt_urls():
	reading_file = open("websites.txt", "r")
	new_file_content = ""

	for line in reading_file:
	    stripped_line = line.split(',')[0]
	    new_line = "http://" + stripped_line
	    new_file_content += new_line +"\n"
	    
	reading_file.close()
	writing_file = open("websites.txt", "w")
	writing_file.write(new_file_content)
	writing_file.close()

# Formats the url given as input by concatenating "http://" to the beginning if not already present and returns the formatted string
def format_url(raw_url):
	url = ''
	if ((raw_url.startswith('http://',0) == False) and (raw_url.startswith('https://',0) == False)):
		url = 'http://' + raw_url
	elif ((raw_url.startswith('http://',0) == True) or (raw_url.startswith('https://',0) == True)):
		url = raw_url
	# ***Place exception handling***
	return url
		

def convert_extracted_features(Xnew):
	le = preprocessing.LabelEncoder()
	XnewProcessed = pandas.DataFrame(Xnew)
	XnewProcessed = XnewProcessed.apply(lambda col: le.fit_transform(col.astype(str)), axis=0, result_type='expand')
	XnewProcessed =XnewProcessed.T
	return (XnewProcessed)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
@app.route('/results', methods=['GET','POST'])
def search():
	if request.method =='POST':
		url = request.form['webURL']
		#Execute all functions first to determine if malicious or not
		#Then display results v
		return render_template('results.html')

#@app.route("/page2")
#def page2():
#	return render_template('page2.html')


if __name__ == "__main__":
	pass

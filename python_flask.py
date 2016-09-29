from flask import Flask, render_template
from flask import jsonify
from flask import request
import nltk
import csv
from textblob.classifiers import NaiveBayesClassifier
from nltk.tokenize import sent_tokenize

application = Flask(__name__)

@application.route('/')
def homepage():
    return render_template("main.html")

# Route that will process the AJAX request, run the magically Depth of Knowledge classifier.)
@application.route('/background_process')
def background_process():
	try:
		lang = request.args.get('proglang', 0, type=str)

		train = []

		answer = []

		with open('static/data/dot_examples.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				train.append((row['Text'], row['Classification']))

		cl = NaiveBayesClassifier(train)

		if (cl.classify(lang) == "1"):
			answer.append("Level One: Recall")
		elif (cl.classify(lang) == "2"):
			answer.append("Level Two: Skill/Concept")
		elif (cl.classify(lang) == "3"):
			answer.append("Level Three: Strategic Thinking")
		else:
			answer.append("Level Four: Extended Thinking")

		prob_dist = cl.prob_classify(lang)
	
		# ans = "Probability of Level 1: " + str(round(prob_dist.prob("1"), 2) * 100) + "%"
		answer.append("Probability of Level 1: " + str(round(prob_dist.prob("1"), 2) * 100) + "%")
		answer.append("Probability of Level 2: " + str(round(prob_dist.prob("2"), 2) * 100) + "%")
		answer.append("Probability of Level 3: " + str(round(prob_dist.prob("3"), 2) * 100) + "%")
		answer.append("Probability of Level 4: " + str(round(prob_dist.prob("4"), 2) * 100) + "%")

		return jsonify(result=answer)
	except Exception as e:
		return str(e)


if __name__ == "__main__":
    application.run(
    	host='0.0.0.0',
    	debug=True
    )

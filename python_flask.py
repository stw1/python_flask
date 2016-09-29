from flask import Flask, render_template
from flask import jsonify
from flask import request

application = Flask(__name__)

@application.route('/')
def homepage():
    return render_template("main.html")

# Route that will process the AJAX request, run the magically Depth of Knowledge classifier.)
@application.route('/background_process')
def background_process():
	try:
		lang = request.args.get('proglang', 0, type=str)
		if lang.lower() == 'python':
			return jsonify(result='You are wise')
		else:
			return jsonify(result='Try again.')
	except Exception as e:
		return str(e)


if __name__ == "__main__":
    application.run(
    	host='0.0.0.0',
    	debug=True
    )

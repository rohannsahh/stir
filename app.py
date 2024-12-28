from flask import Flask, jsonify
from trends import fetch_trending_topics  # Import your script

app = Flask(__name__)

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        result = fetch_trending_topics()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

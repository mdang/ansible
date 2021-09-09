from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
  return "Flask REST API"

@app.route('/courses')
@cross_origin()
def courses():
  return jsonify(
    [dict(name="Software Engineering Immersive"), dict(name="Java Developer Immersive"), dict(name="Front-End Web Development")]
  )

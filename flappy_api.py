from flask import Flask, jsonify, make_response, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app, resources=r'/flappy_api/*')
app.config['MONGO1_DBNAME'] = 'flappy'
mongo = PyMongo(app, config_prefix='MONGO1')

"""
returns the <num_score> highest scores 
"""
@app.route('/flappy_api/scores/<int:num_score>', methods=['GET'])
def get_n_score(num_score):
    l_score = []
    try:
        cursor = mongo.db.flappy_score.find({}, {'_id': False}).sort([("score",-1), ("date",1)]).limit(num_score)
        for score in cursor:
            l_score.append(score)
        response = make_response(dumps(l_score), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    except:
        return make_response (jsonify({'error':'the database doesn \'t appear to be available'}), 504)

"""
returns all scores 
"""
@app.route('/flappy_api/scores/', methods=['GET'])
def get_score():
    l_score = []
    try:
        cursor = mongo.db.flappy_score.find({}, {'_id': False}).sort([("score",-1)])
        for score in cursor:
                l_score.append(score)
        response = make_response(dumps(l_score), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    except:
        return make_response(jsonify({'error':'the database doesn \'t appear to be available'}), 504)

"""
implements player's score & name in the database
"""
@app.route('/flappy_api/scores/', methods=['POST'])
def set_score():
    if not request.get_json:
        make_response(jsonify({'error':'No Json find'}), 404)
    try:
        #TODO: Implement secret key to prevent cheating
        now = datetime.datetime.now()
        data = request.get_json()
        mongo.db.flappy_score.insert({"score":data['score'], "name":data['playerName'], "date":now})
        response = make_response(jsonify({'response':'Insertion done'}), 201)
        response.headers['Content-Type'] = 'application/json'
        return response
    except:
        response = make_response(jsonify({'error':'the database doesn \'t appear to be available post'}), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

if __name__ == '__main__':
    # TODO: not suitable for prod environment
    app.run(host='0.0.0.0', debug=True)
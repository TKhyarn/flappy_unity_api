from flask import Flask, jsonify, make_response
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO1_DBNAME'] = 'flappy'
mongo = PyMongo(app, config_prefix='MONGO1')

"""
returns the <num_score> highest scores 
"""
@app.route('/flappy_api/getscore/<int:num_score>', methods=['GET'])
def get_n_score(num_score):
    l_score = []
    cursor = mongo.db.flappy_score.find({}).sort([("score",-1)]).limit(num_score)
    for score in cursor:
            l_score.append(score)
    return dumps(l_score)

"""
returns all scores 
"""
@app.route('/flappy_api/getscore', methods=['GET'])
def get_score():
    l_score = []
    cursor = mongo.db.flappy_score.find({})
    for score in cursor:
            tmp = score
            l_score.append(tmp)
    return dumps(l_score)

"""
implements player's score & name in the database
"""
@app.route('/flappy_api/setscore/<string:player_name>/<int:score_val>', methods=['GET'])
def set_score(player_name, score_val):
    try:
        mongo.db.flappy_score.insert({"score":score_val, "name":player_name})
        return jsonify("response:OK")
    except:
        return make_response(jsonify({'error':'the database doesn \'t appear to be available'}), 504)

if __name__ == '__main__':
    # TODO: not suitable for prod environment
    app.run(host='0.0.0.0', debug=True)
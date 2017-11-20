from flask_cors import CORS
from app import app

CORS(app, resources=r'/flappy_api/*')
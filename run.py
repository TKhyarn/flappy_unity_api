#!flask/bin/python
from app import app
# not suitable for prod environment
app.run(host='0.0.0.0', debug=True)
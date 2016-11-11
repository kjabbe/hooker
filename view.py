"""
Routes and views for the flask application.
"""

from flask import Flask, request, Response
#render_template, session, jsonify

from os import environ
import hmac, hashlib

#config file
from config import key

app = Flask(__name__)
app.debug = True

@app.route('/Spillet', methods=['POST'])
def index():
    calculatedHash = str('sha1=' + calcHash(request.get_data())) 
    if (calculatedHash == str(request.headers['X-Hub-Signature'])):
        print ('git pull')
    #print(h)
    return Response("foo bar")


def calcHash(data):
    byteKey = bytes(key, 'UTF-8')
    return hmac.new(byteKey, data, hashlib.sha1).hexdigest()
    

def deploy():
    os.system('')
    os.system('git pull')

"""
The flask application package.
"""

if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '8888'))
    except ValueError:
        PORT = 8888
    app.run(HOST, PORT)

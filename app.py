import os
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def print_environment(**kwargs):
    output = ""
    for k, v in os.environ.items():
        output += "%s: %s\n" % (k,v)
    return Response(output, mimetype='text/plain')

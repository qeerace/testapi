import flask
from flask_cors import CORS
from flask import request, jsonify

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
services = [
    {'province': 'Bangkok',
     'distinct': 'Ladkrabang',
     'power': '2hr',
     'time': '1hr',
     },
    {'province': 'Bangkok',
     'distinct': 'Ladkrabang',
     'percen': '100',
     'status': 'Full',
     },
    {'province': 'Bangkok',
     'distinct': 'Ladkrabang',
     'status': 'Good',
     'air': '10',
     'pm': '27'},
    {'province': 'Bangkok',
     'distinct': 'Ladkrabang',
     'name': 'Faculty of Engineering',
     'no': '1',
     'destination': 'ECC Building',
     'arrived': '5min'},
    {'province': 'Bangkok',
     'distinct': 'Ladkrabang',
     'water': '50',
     'status': 'safe'},
    {'province': 'Bangkok',
     'distinct': 'Ladkrabang',
     'status': 'heavy traffic'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/services/all', methods=['GET'])
def api_all():
    return jsonify(services)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,threaded=True, debug=True)
   

import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)


@app.route('/',methods=['GET'])
def default():
    return ''' <h1> Hi.. Data Folks!!!
        </h1>'''


@app.route('/search',methods=['GET'])
def search():
    return ''' <h1> Searching
        </h1>'''

@app.route('/predict',methods=['GET'])
def predict():
    from sklearn.externals import joblib
    model = joblib.load('hppredict25AUG.ml')
    return str(model.predict([[1600,3,2,1,1]]))


@app.route('/hpaug',methods=['GET'])
def hpaug():
    from sklearn.externals import joblib
    model = joblib.load('hppredict25AUG.ml')
    return str(model.predict([[int(request.args['sqft']),
                               int(request.args['place']),
                               int(request.args['yo']),
                               int(request.args['tf']),
                               int(request.args['bhk'])]]))

@app.route('/newpredict',methods=['GET'])
def newpredict():
    from sklearn.externals import joblib
    model = joblib.load('hp22jul.ml')
    return str(model.predict([[int(request.args['sqft']),
                               int(request.args['place']),
                               int(request.args['yo']),
                               int(request.args['tf']),
                               int(request.args['bhk'])]]))






@app.route('/ola',methods=['GET'])
def ola():
    from sklearn.externals import joblib
    model = joblib.load('hp_trained8jul.ml')
    return  str(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['bhk'])]]))


@app.route('/happy',methods=['GET'])
def happy():
	return ''' <h1> Hi.. Happy Day!
        </h1>'''

@app.route('/predictjune',methods=['GET'])
def predictjune():
    from sklearn.externals import joblib
    model = joblib.load('hp_jun30.ml')
    pr = str(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['bhk'])]]))
    return pr

@app.route('/predhp',methods=['GET'])
def predhp():
    from sklearn.externals import joblib
    model = joblib.load('../hp-2jun.ml')
    return  str(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]]))



@app.route('/hello',methods=['GET'])
def hello():
    return ''' <h1> Helloo.. just checking..</h1>'''


@app.route('/mayhp',methods=['GET'])
def mayhp():
    from sklearn.externals import joblib
    model = joblib.load('../hp-3May.ml')
    return str(int(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]])))


@app.route('/testing',methods=['GET'])
def testing():
    return ''' <h1> Hi.. My testing successful.</h1>'''

@app.route('/predicthp',methods=['GET'])
def predicthp():
    from sklearn.externals import joblib
    model = joblib.load('hp-21apr.ml')
    
    return str(int(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]])))




@app.route('/test',methods=['GET'])
def test():
	return ''' <h1> Testing.. </h1>'''


@app.route('/hp-predict',methods=['GET'])
def hp():
    from sklearn.externals import joblib
    model = joblib.load('hp-18feb.ml')
    return str(int(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]])))




@app.route('/sales_returns', methods=['GET'])
def returns():
    from sklearn.externals import joblib
    model = joblib.load('sales_returns_trained_model.ml')
    return str(model.predict([[int(request.args['age']),int(request.args['gender']),int(request.args['city']),int(request.args['cat'])]]))

@app.route('/hp', methods=['GET'])
def home1():
    from sklearn.externals import joblib
    model = joblib.load('hp_team_train.ml')
    return str(int(model.predict([[int(request.args['sqft']),int(request.args['yo']),int(request.args['tf']),int(request.args['p']),int(request.args['b'])]])))


app.run()

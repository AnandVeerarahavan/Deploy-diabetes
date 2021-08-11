# Importing the libraries

from flask import Flask, render_template, request
from flask.globals import request
import joblib

# Create instance of app
app = Flask(__name__)
model =joblib.load('dib_79.pkl')

# Decorater(@) and routing

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/contact')
def contact_page():
    return 'Contact Us anytime'

@app.route('/blogs', methods =['POST'])
def blogs_page():
    Preg = request.form.get('preg')
    Plas = request.form.get('plas')
    Pres = request.form.get('pres')
    Skin = request.form.get('skin')
    Test = request.form.get('test')
    Mass = request.form.get('mass')
    Pedi = request.form.get('pedi')
    Age = request.form.get('age')

  

    print(Preg,Plas,Pres,Skin,Test,Mass,Pedi,Age)

    pred = model.predict([[int(Preg), int(Plas),int(Pres),int(Skin),int(Test),int(Mass),int(Pedi),int(Age)]])
    print(pred)

    if pred[0]==1:
        result = 'diabetic'
    else:
        result = 'non-diabetic'
   
    
    return render_template('blogs.html', predicted_text = f'You are {result}')

# run the app

if __name__ == '__main__':
    app.run(debug=True)

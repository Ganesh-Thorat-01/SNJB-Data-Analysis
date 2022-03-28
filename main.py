from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pickle
import pandas as pd

app=Flask(__name__)

placement_model=pickle.load(open('src/Placement.pkl','rb'))
students_model=pickle.load(open('src/Students.pkl','rb'))
events_model=pickle.load(open('src/Events.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction/placement',methods=['GET','POST'])
def placement():
    if request.method == 'POST':
        year=int(request.form['year'])
        strength=int(request.form['classstrength'])

        df=pd.DataFrame([[year,strength]],columns=['Academic Year','Class Strength'])

        forecast = placement_model.predict(df)
        
        y_pred = forecast
        y_pred=round(y_pred[0])
  
        Output=f"Predicted Placement Count is {y_pred}"
        return render_template('placement.html', output=Output)

    return render_template('placement.html')

@app.route('/prediction/students',methods=['GET','POST'])
def students():
    if request.method == 'POST':
        year=int(request.form['year'])
        df=pd.DataFrame([[year]],columns=['Academic Year'])


        forecast = students_model.predict(df)
        y_pred = forecast
        y_pred=round(y_pred[0])
  
        Output=f"Predicted Student Count is {y_pred}"
        return render_template('students.html', output=Output)

    return render_template('students.html')

@app.route('/prediction/events',methods=['GET','POST'])
def events():
    if request.method == 'POST':
        year=int(request.form['year'])
        df=pd.DataFrame([[year]],columns=['Academic Year'])
    

        forecast = events_model.predict(df)
        y_pred = forecast
        y_pred=round(y_pred[0])
  
        Output=f"Predicted Event Count is {y_pred}"
        return render_template('events.html', output=Output)
    return render_template('events.html')

if __name__=="__main__":
    app.run()


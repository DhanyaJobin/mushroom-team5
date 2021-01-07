from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/mushroom')
def mushroom():
	return render_template('mushroom.html')
@app.route('/nutrient')
def nutrient():
	return render_template('nutrient.html')	
@app.route('/listt')
def listt():
    return render_template('listt.html')
    
@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()] 
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)
    out=round(prediction[0], 2)
    if out == 1: 
            output ='Poisonous'
    else: 
            output ='Edible' 
    return render_template('index.html', prediction_text='Your Mushroom Should Be  {}'.format(output))
if __name__=="__main__":
    app.run()
    
from flask import Flask, request, render_template
import numpy as np
import pandas as pd



from sklearn.preprocessing import LabelEncoder
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('results.html')

    else:
        data=CustomData(
            Administrative=int(request.form.get('Administrative')),
            Administrative_Duration=float(request.form.get('Administrative_Duration')),
            Informational=int(request.form.get('Informational')),
            Informational_Duration=float(request.form.get('Informational_Duration')),
            ProductRelated=int(request.form.get('ProductRelated')),
            ProductRelated_Duration=float(request.form.get('ProductRelated_Duration')),
            BounceRates=float(request.form.get('BounceRates')),
            ExitRates=float(request.form.get('ExitRates')),
            PageValues=float(request.form.get('PageValues')),
            SpecialDay=float(request.form.get('SpecialDay')),
            Month=str(request.form.get('Month')),
            OperatingSystems=int(request.form.get('OperatingSystems')),
            Browser=int(request.form.get('Browser')),
            TrafficType=int(request.form.get('TrafficType')),
            Region=int(request.form.get('Region')),
            VisitorType=str(request.form.get('VisitorType')),
            Weekend=bool(request.form.get('Weekend'))
        )
        pred_df=data.get_data_as_dataframe()
        print(pred_df)

        predict_pipeline=PredictPipeline()
        result=predict_pipeline.predict(pred_df)
        
        categories={0:'False',1:'True'}
        
        results = categories[result[0]]
        

        return render_template("results.html",results=results)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)
    
    
     

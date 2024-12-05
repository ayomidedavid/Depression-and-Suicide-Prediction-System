# predictor/views.py
from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd


def home(request):
    return render(request, 'home.html')

def depression(request):
    with open('newdepression_model.pkl', 'rb') as f:
            DepressionPredictor = pickle.load(f)
    if request.method == 'POST':
        # Get user input data from the form
        data = {
            'age': request.POST['age'],
            'income': request.POST['income'],
            'gender': request.POST['gender'],
            'sexuallity': request.POST['sexuallity'],
            'race': request.POST['race'],
            'bodyweight': request.POST['bodyweight'],
            'virgin': request.POST['virgin'],
            'prostitution_legal': request.POST['prostitution_legal'],
            'pay_for_sex': request.POST['pay_for_sex'],
            'social_fear': request.POST['social_fear'],
            'attempt_suicide': request.POST['attempt_suicide'],
            'employment': request.POST['employment'],
            'job_title': request.POST['job_title'],
            'edu_level': request.POST['edu_level'],
        }
        
        values_list = list(data.values())
        input_data = np.array([values_list])
        feature_names = ['age','income','gender', 'sexuallity', 'race', 'bodyweight', 'virgin','prostitution_legal', 'pay_for_sex', 'social_fear', 'attempt_suicide','employment', 'job_title', 'edu_level']
        final_df = pd.DataFrame(input_data, columns = feature_names)

        # Use the model for predictions
        prediction_result = DepressionPredictor.predict(final_df)
        result = prediction_result[0]
        return render(request, 'depression.html', {'result': result})
    
    return render(request, 'home.html')



# SUICIDE
def home2(request):
    return render(request, 'home2.html')

def suicide(request):
    with open('newsuicide_model.pkl', 'rb') as f:
            SuicidePredictor = pickle.load(f)
    if request.method == 'POST':
        # Get user input data from the form
        data = {
            'age': request.POST['age'],
            'income': request.POST['income'],
            'gender': request.POST['gender'],
            'sexuallity': request.POST['sexuallity'],
            'race': request.POST['race'],
            'bodyweight': request.POST['bodyweight'],
            'virgin': request.POST['virgin'],
            'prostitution_legal': request.POST['prostitution_legal'],
            'pay_for_sex': request.POST['pay_for_sex'],
            'social_fear': request.POST['social_fear'],
            'depressed': request.POST['depressed'],
            'employment': request.POST['employment'],
            'job_title': request.POST['job_title'],
            'edu_level': request.POST['edu_level'],
        }
        values_list = list(data.values())
        input_data = np.array([values_list])
        feature_names = ['age', 'income','gender', 'sexuallity', 'race', 'bodyweight', 'virgin','prostitution_legal', 'pay_for_sex', 'social_fear', 'depressed','employment', 'job_title', 'edu_level']
        final_df = pd.DataFrame(input_data, columns = feature_names)
        
        # Use the model for predictions
        prediction_result = SuicidePredictor.predict(final_df)
        result = prediction_result[0]
        return render(request, 'suicide.html', {'result': result})
    return render(request, 'home2.html')

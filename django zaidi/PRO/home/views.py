from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Prediction
import joblib
import sklearn
import pandas as pd
import numpy as np
import pickle
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.linear_model import Logistic
import sklearn.linear_model._logistic
#from django_pandas.io import read_frame



from django.contrib import messages

# Create your views here.
def index1(Request):
   # return HttpResponse("its my HOME page")
   return render(Request, 'index1.html')

def aboutus(Request):
    return render(Request, 'aboutus.html')
    #return HttpResponse("its my about page")

def contact(Request):
    if Request.method == "POST":
        name = Request.POST.get('name')
        email = Request.POST.get('email')
        phone = Request.POST.get('phone')
        desc = Request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
      #  messages.success(Request, 'Form submission successful')
   
       


    return render(Request, 'contact.html')
 #   return HttpResponse("its my contact page")

def servies(Request):
     return render(Request, 'servies.html')
    #return HttpResponse("its my servies page")

def Graph(Request):
    return render(Request, 'Graph.html')
   
def vis(Request):

    return render(Request, 'vis.html')   
def prediction(Request):
    
    return render(Request, 'prediction.html')   

#######################################################

#@login_required(login_url='/login')

        
# def cause(Request):
    
#     if Request.method == "POST":
#      p = Request.POST.get('Pollutants')
#      if p == 0:
#       {print("This is always 0.")}
#      if p == 1:
#       {print("This is always 1.")}
#      if p == 2:
#       {print("This is always 2.")}
#      if p == 3:
#       {print("This is always 3.")}
#      if p == 5:
#       {print("This is always 4.")}
     
#      return  render(Request,'prediction.html',{p}) 
        
 


def prediction(Request):
    if Request.method == "POST":
        State = Request.POST.get('State')
        Avg = Request.POST.get('Avg')
        Max = Request.POST.get('Max')
        Min = Request.POST.get('Min')
        Pollutants = Request.POST.get('Pollutants')
        print(Pollutants)
        prediction = Prediction.objects.create(State=State, Avg=Avg, Max=Max, Min=Min, Pollutants=Pollutants)
        prediction.save()
        print('1 data var m data sav hogaya')
       # file ='static/finalized_model.sav'
       
       # model1 = pickle.load("")
        model=joblib.load('finalized_model.sav')
       #State	Avg	Max	Min	Pollutants
        X_pred =pd.DataFrame(np.array([[int(State),int(Avg),int(Max),int(Min),int(Pollutants)]]),
                   columns=['State','Avg','Max','Min','Pollutants'])
        predict = model.predict(X_pred)
        suggestion="none"    
        if(predict)==1:
            suggestion="There is air pollution in this place due to high air quality index"
        sug1="mehrab"
        sug2="May cause minor breathing discomfort to sensitive people"
        sug3="May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults."
        sug4="May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases"
        sug5="May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease"

        dt={"sus":suggestion,'result':predict,"1":sug1,
        "2":sug2,"3":sug3,"4":sug4,"5":sug5,
                
        }        
        print('2 predict var k ander model agaya')
        prediction.result=predict
        print('3 ab data.analsishistory ka result print hoga')
        print(prediction.result)
       # dic_cause(Request);
        my_dict = {"1": "May_cause_breathing_discomfort_to_people_with_lung_disease_such_as_asthma",
         '2': '_Effect_may_be_more_pronounced'}

        # suggest="May_cause_minor_breathing_discomfort_to_sensitive_people"
        # if(predict)==1:
        #     suggest="May_cause_minor_breathing_discomfort_to_sensitive_people"
        # dt1={"sus1":suggest,'result':predict}    
       
        #cause(Request)
        return  render(Request,'prediction.html',{'dt':dt})
       
    else:
        return  render(Request,'prediction.html')
    
    return render(Request, 'prediction.html',{'dt':dt})   



    
   



# def dic_cause(Request):
#    if Request.method == "POST":
#        Pollutants = Request.POST.get('Pollutants')
#        sug2="2May cause minor breathing discomfort to sensitive people"
#        sug3="2May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults."
#        sug4="2May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases"
#        sug5="2May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease"

#        dt={"sus":suggestion,'result':predict,"1":sug1,
#       "2":sug2,"3":sug3,"4":sug4,"5":sug5,    
               
#        return  render(Request,'prediction.html',{'dt':dt})
       
#     else:
#         return  render(Request,'prediction.html')
    
#     return render(Request, 'prediction.html',{'dt':dt})   
    
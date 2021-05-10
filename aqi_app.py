import base64
import numpy as np
import pandas as pd
import pickle
import streamlit as st


def welcome():
    return " welcome all"



def predict_AQI(T,TM,Tm,SLP,H,VV,V,Vm,city):
    
    if city=='Banglore':
      pickle_in = open("random_forest_regression_model_bngl.pkl","rb")
      random_forest_regressor=pickle.load(pickle_in)
      
      prediction=random_forest_regressor.predict([[ T,TM,Tm,SLP,H,VV,V,Vm]])
      print(prediction)
      return prediction



    
    if city=='Chennai':
      pickle_in = open("random_forest_regression_model_chennai.pkl","rb")
      random_forest_regressor=pickle.load(pickle_in)
      
      prediction=random_forest_regressor.predict([[ T,TM,Tm,SLP,H,VV,V,Vm]])
      print(prediction)
      return prediction


    
    if city=='Goa':
      pickle_in = open("random_forest_regression_model_Goa.pkl","rb")
      random_forest_regressor=pickle.load(pickle_in)
      
      prediction=random_forest_regressor.predict([[ T,TM,Tm,SLP,H,VV,V,Vm]])
      print(prediction)
      return prediction


     
    if city=='Hyderabad':
      pickle_in = open("random_forest_regression_model_hyd.pkl","rb")
      random_forest_regressor=pickle.load(pickle_in)

      prediction=random_forest_regressor.predict([[ T,TM,Tm,SLP,H,VV,V,Vm]])
      print(prediction)
      return prediction



    if city=='Mumbai':
      pickle_in = open("random_forest_regression_model_mumbai.pkl","rb")
      random_forest_regressor=pickle.load(pickle_in)  

      prediction=random_forest_regressor.predict([[ T,TM,Tm,SLP,H,VV,V,Vm]])
      print(prediction)
      return prediction




    if city=='New Delhi':
      pickle_in = open("random_forest_regression_model_del.pkl","rb")
      random_forest_regressor=pickle.load(pickle_in)

      prediction=random_forest_regressor.predict([[ T,TM,Tm,SLP,H,VV,V,Vm]])
      print(prediction)
      return prediction



    if city=='Vishakapatnam':
      pickle_in = open("random_forest_regression_model_Vizag.pkl","rb")
      random_forest_regressor=pickle.load(pickle_in)

      prediction=random_forest_regressor.predict([[ T,TM,Tm,SLP,H,VV,V,Vm]])
      print(prediction)
      return prediction




def main():
    st.title("AQI prediction of Indian Cities")
    html_temp = '''
    <style>
    body {
    background-image: url("https://media.nationalgeographic.org/assets/photos/000/282/28259.jpg");
    background-size: cover;
    }
    </style>
    '''
    
    st.markdown(html_temp,unsafe_allow_html=True)
    T = st.text_input("Average_Temperature ","Type Here")
    TM = st.text_input("Maximum_Temperature ","Type Here")
    Tm = st.text_input("Minimum_Temperature ","Type Here")
    SLP = st.text_input("Atm_pressure_at_sea_level ","Type Here")
    H = st.text_input("Average_relative_Humidity ","Type Here")
    VV = st.text_input("Average_visibility ","Type Here")
    V = st.text_input("Average_wind_speed ","Type Here")
    Vm = st.text_input("Maximum sustained wind speed ","Type Here")
    city=st.selectbox('select a City',('Banglore','Chennai','Goa','Hyderabad','Mumbai','New Delhi','Vishakapatnam'))
    result=""
    if st.button("Predict"):
        result=predict_AQI(T,TM,Tm,SLP,H,VV,V,Vm,city)
    st.success('The output is {}'.format(result))
    
    if st.button("About"):
        st.text("project by VEENA SAI NIGAMA")
        st.text(" 2021 ")

if __name__=='__main__':
    main()
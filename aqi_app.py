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


    
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return






def main():
    st.title("AQI prediction of Indian Cities")
#    html_temp = '''
#    <style>
#    body {
#    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
#    background-size: cover;
#    }
#    </style>
#    '''
    set_png_as_page_bg('air pollution.PNG')
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
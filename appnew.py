import numpy as np
import pandas as pd
import pickle
import streamlit as st



pickle_in = open("Random_forest_regressornew.pkl","rb")
random_forest_regressor=pickle.load(pickle_in)


def welcome():
    return " welcome all"



def predict_AQI(T,TM,Tm,SLP,H,VV,V,Vm):
    
    
    prediction=tuned_model.predict([[ T,TM,Tm,SLP,H,VV,V,Vm]])
    print(prediction)
    return prediction


def main():
    st.title("Hyderabad AQI prediction")
    html_temp = """
    <div style="background-color:green;padding:20px">
    <h2 style="color:white;text-align:center;">AQI prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    T = st.text_input("Average_Temperature ","Type Here")
    TM = st.text_input("Maximum_Temperature ","Type Here")
    Tm = st.text_input("Minimum_Temperature ","Type Here")
    SLP = st.text_input("Atm_pressure_at_sea_level ","Type Here")
    H = st.text_input("Average_relative_Humidity ","Type Here")
    VV = st.text_input("Average_visibility ","Type Here")
    V = st.text_input("Average_wind_speed ","Type Here")
    Vm = st.text_input("Maximum sustained wind speed ","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_AQI(T,TM,Tm,SLP,H,VV,V,Vm)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("project by VEENA SAI NIGAMA")
        st.text(" 2021 ")

if __name__=='__main__':
    main()
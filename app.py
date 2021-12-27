import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
st.title('MONTHLY CAR SALES PREDICTION')
st.subheader('Here is the prediction of car sales in the future months using fbprophet')
st.caption('Use the menu at left to select options')
st.caption('Your plots will appear below')
model = joblib.load('monthly_carsales')
st.sidebar.header('select menu')
st.sidebar.subheader('select number of months for prediction')
periods = st.sidebar.slider("pick number of months",min_value = 12,max_value= 60)
future_pred = model.make_future_dataframe(periods,freq='M')
forecast = model.predict(future_pred)
st.sidebar.subheader('click here for the output')
if st.sidebar.button('Predict'):
  st.caption('Loading ....please wait!!')
  fig = model.plot(forecast)
  st.pyplot(fig)
st.sidebar.subheader('click here to see the trends')
if st.sidebar.button('Trends'):
  st.caption('Loading ....please wait!!')
  figure = model.plot_components(forecast)
  st.pyplot(figure)



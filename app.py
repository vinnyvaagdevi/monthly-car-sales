import streamlit as st
import joblib
st.title('MONTHLY CAR SALES PREDICTION')
op = joblib.load('monthly_carsales')
ip = st.slider("pick number of months",0,100)
fig = op.predict([ip])
if st.button('Predict'):
   st.pyplot(fig[0])
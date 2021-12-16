import streamlit as st
import joblib
st.title('MONTHLY CAR SALES PREDICTION')
op = joblib.load('monthly_carsales')
months = st.slider("pick number of months",0,100)
fig = op.predict([months])
st.pyplot(fig)

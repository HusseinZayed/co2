import streamlit as st

import streamlit as st
import pickle

# load pkl file
with open('./model.pkl','rb') as f:
  model = pickle.load(f)

#title the page
st.title("predict the CO2 EMISSIONS of car")

#set image
st.image('/content/drive/MyDrive/Colab Notebooks/Capture1.PNG')

#inputs
engine_size = st.number_input('Engine Size' , min_value=0.0 , max_value=10.0,value=1.0)
cylinder = st.number_input('Cylinder' , min_value=0.0 , max_value=10.0,value=1.0)
fuel_consumption =  st.number_input('Fuel Consumption' , min_value=0.0 , max_value=100.0,value=1.0)

output = model.predict([[engine_size,cylinder,fuel_consumption]])

#display the result
st.write("the predict CO2 of car is : ",round(output[0][0],2))

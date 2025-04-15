import streamlit as st
import pickle

# load pkl file
with open('model.pkl','rb') as f:
  model = pickle.load(f)

#title the page
st.title("predict the CO2 EMISSIONS of car")


#inputs
engine_size = st.number_input('Engine Size' , min_value=0.0 , max_value=10.0,value=1.0)
cylinder = st.number_input('Cylinder' , min_value=0.0 , max_value=10.0,value=1.0)
FUELCONSUMPTION_CITY =  st.number_input('FUEL CONSUMPTION CITY' , min_value=0.0 , max_value=100.0,value=1.0)
FUELCONSUMPTION_HWY = st.number_input('FUEL CONSUMPTION HWY' , min_value=0.0 , max_value=10.0,value=1.0)
FUELCONSUMPTION_COMB = st.number_input('FUEL CONSUMPTION COMB' , min_value=0.0 , max_value=10.0,value=1.0)
FUELCONSUMPTION_COMB_MPG =  st.number_input('FUEL CONSUMPTION COMB_MPG' , min_value=0.0 , max_value=100.0,value=1.0)



output = model.predict([[engine_size, cylinder, FUELCONSUMPTION_CITY,FUELCONSUMPTION_HWY, FUELCONSUMPTION_COMB,FUELCONSUMPTION_COMB_MPG]])

#display the result
st.write("the predict CO2 of car is : ",output[0])

import streamlit as st
from datetime import time, datetime
st.header("st.silder")


#example 1
st.subheader("slider")
age=st.slider("how old are you",0,100,30)
st.write(f"I am {age} years old")
#example 2
st.subheader("range slider")
#selecting 2 values instead of one, passing a tuple instead of a numerical value
values=st.slider("choose your values",0,100,(25,75))
st.write(f"the values are {values}")
#example 3
#setting a slider of time, passing time objects to "value" instead of values, these are the default values and you don't need to set a range
st.subheader("Time slider")
values=st.slider("choose a time Range",value=(time(2,25),time(5,25)))
st.write(f"from {values[0]} to {values[1]}")
#example 4
values=st.slider("choose a time Range",value=time(2,25))
st.write(f"time {values}")
#example 5
values=st.slider("Choose a datetime range",value=datetime(2020,1,1,9,25))
st.write("current date is ",values)
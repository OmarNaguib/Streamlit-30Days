import streamlit as st

st.header("st.button")

if st.button("say Hello"):
    st.write("Hello there")
else: st.write("Goodbye then")

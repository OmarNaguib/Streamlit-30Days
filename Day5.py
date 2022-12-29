import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import numpy as np
st.write("this is just a text")


st.write("hello, *Hello* :sunglasses")


st.write(1234)

df=pd.DataFrame({"first column":[1,2,3],
                 "second column":[4,5,6]
                 
                 })

st.write(df)


st.write("below is a df",df,"above is a df")


# =============================================================================
# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)
# =============================================================================

figure=px.scatter(data_frame=df,x="first column",y="second column")

st.write(figure)


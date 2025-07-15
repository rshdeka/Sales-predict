import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import pickle
import warnings
warnings.filterwarnings('ignore')

# Load the pickle models
model = pickle.load(open('model(1).pkl', 'rb'))
df = pickle.load(open('sales(1).pkl', 'rb'))

html_temp = """ 
<div style = "background-color: #70d4bc; padding: 10px">
<h2 style = "color: white; text-align: center;">Food items Prices Prediction
</div>
<div style = "background-color: white; padding: 5px">
<p style= "color: #7c4deb; text-align: center; font-family: Courier; font-size: 15px;">
<i>Get an idea of the prices of basic food items across each state of India.</i></p>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

image_path = 'img.jpg'
image = Image.open(image_path)
st.image(image, use_container_width=True)


# Define the features
# state
state = st.selectbox('State', df['State'].unique())
# centre
centre = st.selectbox('Centre', df[df['State']==state]['Centre'].unique())
# category
category = st.selectbox('Category', df['Category'].unique())
# commodity
commodity = st.selectbox('Commodity', df[df['Category']==category]['Commodity'].unique())
# variety
variety = st.selectbox('Variety', df[df['Commodity']==commodity]['Variety'].unique())
# unit
unit = st.selectbox('Unit', df[df['Commodity']==commodity]['Unit'].unique())
# month
month = st.selectbox('Month', df['Month'].unique())

# Get the inputs
inputs = [[state, centre, commodity, variety, category, unit, month]]
features = pd.DataFrame(inputs, index=[0])
features.columns = ['State', 'Centre', 'Commodity', 'Variety', 'Category', 'Unit', 'Month']
st.markdown('##### Selected parameters')
st.write(features)

# Predict the price
def prediction():
    if (st.button('Predict Price')):
        #query = np.array([state, centre, commodity, variety, category, unit, month], dtype=object)
        #query = query.reshape(1,7)
        query_df = pd.DataFrame([[state, centre, commodity, variety, category, unit, month]],
                                columns=['State', 'Centre', 'Commodity', 'Variety', 'Category', 'Unit', 'Month'])
        st.title(model.predict(query_df)[0])
prediction()

html_temp1 = """ 
<div style = "background-color: white; padding: 5px">
<p style= "color: #7c4deb; text-align: center; font-family: Courier; font-size: 15px;"><i>*Note: Price is in INR</i></p>
</div>
<div style = "background-color: #70d4bc">
<p style = "color: white; text-align: center;">Designed & Developed By: <b>Rajashri Deka</b></p>
</div>
"""
st.markdown(html_temp1, unsafe_allow_html=True)

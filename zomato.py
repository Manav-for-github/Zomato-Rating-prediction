
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import re 
import pickle
import streamlit as st

df = pd.read_csv('Zomato_df.csv')

model=pickle.load(open('model.pkl','rb'))

#Streamlit code
st.title('ZOMATO_Restaurant_Rating_Prediction_app')
with st.sidebar:
    st.title(':orange[Top 3 famous restaurants chain in banglore are:]')
    st.header(':orange[>Onesta]') 
    st.header(':orange[>Empire Restaurant]') 
    st.header(':orange[>KFC]')
    st.title (':orange[Two main type of services are]') 
    st.header(':orange[>Delivery]')
    st.header(':orange[>Dine-out]')
R,M,L = st.columns(3)
with R:
    st.image('zomato_background.jpg',width=900)
    st.title('ZOMATO_Restaurant_Rating_Prediction_app')

with M:
    
    online_order = st.selectbox('Online Order',df['online_order'].unique())
    book_table= st.selectbox('Table Booking',df['book_table'].unique())
    votes =st.selectbox('Votes',df['votes'].unique())
    location =st.selectbox('location',df['location'].unique())
    rest_type= st.selectbox('Restaurant Type',df['rest_type'].unique())
    cuisines =st.selectbox('Cuisines',df['cuisines'].unique())
    cost =st.selectbox('Cost',df['cost'].unique())
    menu =st.selectbox('Menu Items',df['menu'].unique())
    
    if st.button ('Predict Rating'):  
         prediction = model.predict([[online_order, book_table, votes, location, rest_type,
                    cuisines, cost, menu]])    
         PREDICT = '%.1f'%prediction
         st.text('RATING : '+ PREDICT)
         st.success('prediction for restaurant rating have been successfully made')

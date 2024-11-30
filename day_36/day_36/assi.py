import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px
from ydata_profiling import ProfileReport
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error ,r2_score,precision_score, recall_score

import streamlit as st

from ydata_profiling import ProfileReport


st.write('''
# Amazon Data Sales
## Made by AKM(#@$%)
         
This app is made on the data of Amazon Sales Data.
''')

st.sidebar.header("User Input Params")

# creating a radio button
options = ['Dicision Tree Regressor', 'Dicision Tree Classifier']
selected_option = st.sidebar.radio('Choose model ', options)

if selected_option == 'Dicision Tree Regressor':
        def user_input_features():
            Units_Sold = st.sidebar.number_input("Units_sold", value=0, step=1)
            Unit_Price = st.sidebar.number_input("Unit_price", value=0.0, step=0.1)
            Unit_Cost = st.sidebar.number_input("Unit_cost", value=0.0, step=0.1)
            Total_Revenue = st.sidebar.number_input("Total_revenue", value=0.0, step=0.1)
            Total_Cost = st.sidebar.number_input("Total_cost", value=0.0, step=0.1)

            data = {
                'Units Sold' : Units_Sold,
                'Unit Price' : Unit_Price,
                'Unit Cost' : Unit_Cost,
                'Total Revenue' : Total_Revenue,
                'Total Cost' : Total_Cost, 
            }
            features = pd.DataFrame(data, index=[0])
            return features

        df = user_input_features()

else :
    def user_input_features():
        Units_Sold = st.sidebar.number_input("Units_sold", value=0, step=1)
        Unit_Price = st.sidebar.number_input("Unit_price", value=0.0, step=0.1)
        Unit_Cost = st.sidebar.number_input("Unit_cost", value=0.0, step=0.1)
        Total_Revenue = st.sidebar.number_input("Total_revenue", value=0.0, step=0.1)
        Total_Cost = st.sidebar.number_input("Total_cost", value=0.0, step=0.1)
        Total_Profit = st.sidebar.number_input("Total Profit", value=0.0, step=0.1)

        data = {
            'Units Sold' : Units_Sold,
            'Unit Price' : Unit_Price,
            'Unit Cost' : Unit_Cost,
            'Total Revenue' : Total_Revenue,
            'Total Cost' : Total_Cost,
            'Total Profit': Total_Profit 
        }
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

sales = pd.read_csv('AmazonSalesData.csv')

st.subheader("Amazon Sales Data")
st.write(sales)

if selected_option == 'Dicision Tree Regressor':
    # define features and labels
    X = sales[['Units Sold','Unit Price','Unit Cost',	'Total Revenue'	,'Total Cost']]
    y = sales['Total Profit']

    # X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42 )

    # fitting and creating a model for it
    model = DecisionTreeRegressor(max_depth=10)

    model.fit(X,y)

    predicts = model.predict(df)
    # printing predictions
    st.subheader("Prediction")
    st.write(f"Predicted value: **{predicts}**")


else :
     # define features and labels
    X1 = sales[['Units Sold','Unit Price'	,'Unit Cost',	'Total Revenue'	,'Total Cost','Total Profit']]
    y1 = sales['Region']

    # X_train, X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=42 )

    # fitting and creating a model for it
    model = DecisionTreeClassifier(max_depth=10)

    model.fit(X1,y1)

    predictss = model.predict(df)
    # printing predictions
    st.subheader("Prediction")
    st.write(f"Predicted Region: **{predictss}**") 

with st.container(height=150, border=True):
     st.write("""
**About Developer :**\
              This app is made by Ahmad kattak

**Mail :** 93245ahmad@gmail.com
""")
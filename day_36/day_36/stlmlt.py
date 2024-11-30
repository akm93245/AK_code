import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Random forest Classifier
 This app predict the type of iris based on sepal length,sepal width, petal length and petal width.
""" )

st.sidebar.header("User input Parameters")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length',4.3,7.9,5.4)                                           
    sepal_width = st.sidebar.slider("Sepal Width",2.0 , 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0 ,6.9, 1.3)
    petal_width = st.slider.slider("Petal Length",0.1, 2.5, 0.2 )

    data = {
        'Sepal_Length': sepal_length,
        'Sepal_width' : sepal_width,
        'petal_length' : petal_length,
        'petal_width' : petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("Input User Parameters")
st.write(df)

iris = sns.load_dataset('iris')

st.subheader("iris dataset")
st.write(iris)

X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y= iris['species']

clf = RandomForestClassifier()
clf.fit(X,y)


predictions = clf.predict(df)
preditction_proba = clf.predict_proba(df)
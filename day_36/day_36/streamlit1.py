import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from ydata_profiling import ProfileReport

st.write("""
# Random Forest Classifier
## made by Ahmad
This app predicts the type of iris based on sepal length, sepal width, petal length, and petal width.
""")

st.sidebar.header("Iris Params")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)
    Units_Sold = st.number_input("Label", value=0, step=1)

    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width,
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

# Load Iris dataset
iris = sns.load_dataset('iris')

st.subheader("Iris Dataset")
st.write(iris)

# Define features and labels
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = iris['species']

# # Encode labels
le = LabelEncoder()
ye = le.fit_transform(y)

# Train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X, ye)

# Make predictions
prediction = model.predict(df)
prediction_proba = model.predict_proba(df)

# prediction labes
st.subheader("Predicted Labels")
st.write(iris['species'].unique())

# Map numeric prediction back to species labels
predicted_species = le.inverse_transform(prediction)
 
st.subheader("Prediction")
st.write(f"Predicted Species: **{predicted_species[0]}**")

st.subheader("Prediction Probability")
st.write(prediction_proba)


# graph2
st.subheader("Graphing the iris dataset")
fig = px.scatter_3d(iris , x="species" , y='petal_length' , z='sepal_width')
st.plotly_chart(fig)

#another one
st.subheader("box plot in plotly")
fig2 = px.box(iris , x='species' , y='petal_length' , color='species')
st.plotly_chart(fig2)
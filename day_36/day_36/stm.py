import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.write("""
# Random Forest Classifier
This app predicts the type of iris based on sepal length, sepal width, petal length, and petal width.
""")

st.sidebar.header("User Input Parameters")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)

    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
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

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train Random Forest Classifier
clf = RandomForestClassifier()
clf.fit(X, y_encoded)

# Make predictions
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

# Map numeric prediction back to species labels
predicted_species = le.inverse_transform(prediction)

st.subheader("Prediction")
st.write(f"Predicted Species: **{predicted_species[0]}**")

st.subheader("Prediction Probability")
st.write(prediction_proba)

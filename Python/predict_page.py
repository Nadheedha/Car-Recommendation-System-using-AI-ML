import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('C:/Users/ASUS/Desktop/proo/survey_sparrow.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_Brand = data["le_Brand"]
le_Model= data["le_Model"]

def show_predict_page():
    st.title("Customers Car Efficiency Prediction")

    st.write("""### We need some information to predict the salary""")

    Brand = (
        'BMW ', 'CUPRA ', 'Fiat ', 'Honda ', 'Mini ', 'Nissan ', 'Opel ', 'Peugeot ', 'Renault ', 'SEAT ', 'Skoda ', 'Smart ', 'Sono ', 'Volkswagen '
    )

    Model = (
        '500e Hatchback', 'Ariya 63kWh', 'Ariya 87kWh', 'Ariya e-4ORCE 63kWh', 'Ariya e-4ORCE 87kWh', 'Ariya e-4ORCE 87kWh Performance', 'CITIGOe iV ', 'Cooper SE ', 'Corsa-e ', 'EQ forfour ', 'EQ fortwo coupe', 'ID.3 1st', 'ID.3 Pro', 'ID.3 Pro Performance', 'ID.3 Pro S', 'ID.3 Pure', 'Leaf ', 'Leaf e+', 'Mii Electric ', 'Sion ', 'Twingo ZE', 'Zoe ZE40 R110', 'Zoe ZE50 R110', 'Zoe ZE50 R135', 'e ', 'e Advance', 'e-208 ', 'e-Golf ', 'e-Up! ', 'el-Born ', 'i3 120 Ah', 'i3s 120 Ah'
    )

    brand = st.selectbox("Brand", Brand)
    model = st.selectbox("Model", Model)

    Price = st.slider("Price", 20000, 50000, 20000)

    ok = st.button("Calculate Efficiency")
    if ok:
        X = np.array([[brand, model, Price]])
        X[:, 0] = le_Brand.transform(X[:,0])
        X[:, 1] = le_Model.transform(X[:,1])
        X = X.astype(float)

        eff = regressor.predict(X)
        st.subheader(f"The estimated efficiency is {eff[0]:.2f}")
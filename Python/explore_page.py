import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_Price(x):
    if x ==  'More than 50000':
        return 50
    if x == 'Less than 20000':
        return 0.5
    return float(x)




@st.cache
def load_data():
    df = pd.read_csv("C:/Users/ASUS/Desktop/proo/ElectricCarData_Clean.csv")
    df = df[["Brand", "Model", "Efficiency_WhKm", "BodyStyle", "PriceEuro"]]
    df = df.rename({"Efficiency_WhKm": "Efficiency"}, axis=1)
    df = df[df["Efficiency"].notnull()]
    df = df.dropna()
    df = df[df["BodyStyle"] == "Hatchback"]
    df = df.drop("BodyStyle", axis=1)


    Brand_map = shorten_categories(df.Brand.value_counts(), 1)
    df['Brand'] = df['Brand'].map(Brand_map)
    df = df[df["Efficiency"] <= 500]
    df = df[df["Efficiency"] >= 50]
    df = df[df['Brand'] != 'Other']

    df["PriceEuro"] = df["PriceEuro"].apply(clean_Price)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Efficiency statistics")

    st.write(
        """
    ### CAR MANUFACTURER SURVEY
    """
    )

    data = df["Brand"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Data collected from different Car Brands""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Performance frequency based On Car Brands
    """
    )

  #  data = df.groupby(["Brand"])["Model"].mean().sort_values(ascending=True)
   # st.bar_chart(data)

  #  st.write(
  #      """

    ####  Performance frequency based On Car Brands
  #  """
   # )

   # data = df.groupby(["Brand"])["Model"].mean().sort_values(ascending=True)
    st.line_chart(data) 

import streamlit as st 
import pandas as pd
import pickle as pkl

ds = pd.read_csv("cleaned_data.csv")
model = pkl.load(open("CarProject.pkl" , "rb"))

st.title('Car Price Prediction Project!')

st.write("We take following inputs to predict the price of car:")
st.write("1. Company")
st.write("2. Name")
st.write("3. Year")
st.write("4. Kms Driven")
st.write("5. Fuel Type")

companies = ds["company"].unique()
selectedCompany = st.sidebar.selectbox("Select Company" , companies)

names = ds["name"][ds["company"] == selectedCompany].unique()
selectedName = st.sidebar.selectbox("Select Car" , names)

years = sorted(ds["year"].unique())
selectedYear = st.sidebar.selectbox("Select Year" , years)

kms = st.sidebar.number_input("Enter kms Driven")

fuels = ds["fuel_type"].unique()
selectedFuel = st.sidebar.selectbox("Select fueltype" , fuels)

if st.button("Predict Price"):
    data = [selectedCompany , selectedName , selectedYear , kms , selectedFuel]
    columns = ['company' , 'name' , 'year' , 'kms_driven' , 'fuel_type']
    myinp = pd.DataFrame(data = [data ], columns = columns)
    myinp
    st.write("Predicted price: " , round(model.predict(myinp)[0,0]))


    
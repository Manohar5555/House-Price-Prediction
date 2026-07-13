import streamlit as st
from src.predict import predict_price

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)

st.title("🏠 House Price Prediction")

st.write("Enter the details below to predict the house price.")

overall_qual = st.slider("Overall Quality", 1, 10, 5)

gr_liv_area = st.number_input("Ground Living Area (sq ft)", value=1500)

garage_cars = st.number_input("Garage Capacity", value=2)

garage_area = st.number_input("Garage Area (sq ft)", value=500)

total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", value=800)

full_bath = st.number_input("Full Bathrooms", value=2)

year_built = st.number_input("Year Built", value=2000)

lot_area = st.number_input("Lot Area (sq ft)", value=9000)

if st.button("Predict Price"):
    price = predict_price(
        overall_qual,
        gr_liv_area,
        garage_cars,
        garage_area,
        total_bsmt_sf,
        full_bath,
        year_built,
        lot_area,
    )

    st.success(f"Estimated House Price: ${price:,.2f}")
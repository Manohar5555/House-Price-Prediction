import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/house_price_model.pkl")

def predict_price(
    overall_qual,
    gr_liv_area,
    garage_cars,
    garage_area,
    total_bsmt_sf,
    full_bath,
    year_built,
    lot_area,
):
    data = pd.DataFrame({
        "OverallQual": [overall_qual],
        "GrLivArea": [gr_liv_area],
        "GarageCars": [garage_cars],
        "GarageArea": [garage_area],
        "TotalBsmtSF": [total_bsmt_sf],
        "FullBath": [full_bath],
        "YearBuilt": [year_built],
        "LotArea": [lot_area]
    })

    prediction = model.predict(data)

    return prediction[0]
import pandas as pd

def remove_cols_with_nans(df):
    del df["Maisonneuve_1"]
    del df["Parc U-Zelt Test"]
    del df["Pont_Jacques_Cartier"]
    del df["Saint-Laurent U-Zelt Test"]
    del df["Unnamed: 1"]
    return df

def prepare_data():
    bike_df = pd.read_csv("bikecount.csv")
    weather_df = pd.read_csv("weather.csv")

    bike_df.rename(columns={'Date': 'date'}, inplace=True)
    weather_df.rename(columns={'Date/Time': 'date'}, inplace=True)

    weather_df = weather_df[
        ["date", "Mean Temp (°C)", "Total Precip (mm)", "Snow on Grnd (cm)", "Min Temp (°C)", "Max Temp (°C)"]]

    df = pd.concat([bike_df, weather_df], axis=1)

    df = df[df['Berri1'].notna()]

    df = remove_cols_with_nans(df)

    df["Total Precip (mm)"] = df["Total Precip (mm)"].fillna(0)
    df["Snow on Grnd (cm)"] = df["Snow on Grnd (cm)"].fillna(0)

    df = df.loc[:, ~df.columns.duplicated()]
    df["date"] = pd.to_datetime(df['date'], format='%d/%m/%Y')

    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["day_of_week"] = df["date"].dt.dayofweek

    df.reset_index(inplace=True)

    return df
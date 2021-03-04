import pandas as pd
from matplotlib import pyplot as plt

bike_df = pd.read_csv("bikecount.csv")
weather_df = pd.read_csv("weather.csv")

bike_df.rename(columns={'Date': 'date'}, inplace=True)
weather_df.rename(columns={'Date/Time': 'date'}, inplace=True)

to_plot = bike_df.columns[2:]


def columns_with_nans():
    for elem in to_plot:
        print(bike_df[elem].isnull().sum(), " Nans in", elem)


def boxplots():

    fig, axs = plt.subplots(7, 3)

    column_pointer = 0
    for i in range(7):
        for j in range(3):
            axs[i, j].boxplot(bike_df[to_plot[column_pointer]], 0, 'rs', 0)
            axs[i, j].set_title(to_plot[column_pointer])
            column_pointer+=1

    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                        hspace=0.9, wspace=0.3)

    plt.show()


def weather_bike_correlation():
    to_plot = bike_df.columns[2:]
    to_plot = list(to_plot[i] for i in [1, 13, 18])
    weather_to_plot = ["Mean Temp (°C)",
                        "Total Precip (mm)",
                        "Snow on Grnd (cm)",
                        "Min Temp (°C)",
                        "Max Temp (°C)"]

    _weather_df = weather_df[["date"] + weather_to_plot]

    df = pd.concat([bike_df, _weather_df], axis=1)
    fig, axs = plt.subplots(3, 5)
    df = df[df['Berri1'].notna()]
    bike_column_pointer = 0

    for i in range(3):
        weather_column_pointer = 0
        for j in range(5):
            axs[i, j].scatter(df[to_plot[bike_column_pointer]],
                               df[weather_to_plot[weather_column_pointer]],
                               color='blue', s=1)
            axs[i, j].set_title(weather_to_plot[weather_column_pointer]+"/"+to_plot[bike_column_pointer])
            weather_column_pointer+=1
        bike_column_pointer += 1

    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9, hspace=0.9, wspace=0.3)

    plt.show()


def correlations_between_some_lanes():
    to_plot = bike_df.columns[2:]
    to_plot = list(to_plot[i] for i in [1, 13, 18, 2, 8, 20])

    fig, axs = plt.subplots(3, 3)
    df = bike_df[bike_df['Berri1'].notna()]
    bike_column_pointer = 0

    for i in range(3):
        to_compare_pointer = 3
        for j in range(3):
            axs[i, j].scatter(df[to_plot[bike_column_pointer]],
                              df[to_plot[to_compare_pointer]],
                              color='blue', s=1)
            axs[i, j].set_title(to_plot[to_compare_pointer] + "/" + to_plot[bike_column_pointer])
            to_compare_pointer+=1
        bike_column_pointer += 1

    fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9, hspace=0.9, wspace=0.3)

    plt.show()


def correlations_between_lanes():
    columns_to_check = bike_df.columns[2:]

    results = []

    for i in range(len(columns_to_check)):
        for j in range(i,len(columns_to_check)):
            if bike_df[columns_to_check[i]].isnull().values.any() or bike_df[columns_to_check[j]].isnull().values.any():
                continue
            corr = bike_df[columns_to_check[i]].corr(bike_df[columns_to_check[j]], method='spearman')
            results.append((columns_to_check[i],columns_to_check[j],corr))

    results = sorted(results, key=lambda x: x[2], reverse=True)
    for res in results:
        print(res)


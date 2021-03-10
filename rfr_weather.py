import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from helper import prepare_data

df = prepare_data()

y = df["Berri1"]

X = df[["day", "month", "day_of_week", "Mean Temp (°C)", "Total Precip (mm)", "Snow on Grnd (cm)", "Min Temp (°C)", "Max Temp (°C)"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

regr = RandomForestRegressor(max_depth=10, n_estimators=200)
regr.fit(X_train, y_train)
print(regr.score(X_test,y_test))

result = regr.predict(X)

plt.plot(list(y.index), y, label="true")
plt.plot(list(y.index), result, label="predicted")
plt.legend()
plt.show()

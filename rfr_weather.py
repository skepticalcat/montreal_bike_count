import matplotlib.pyplot as plt
import statistics as stat

from sklearn import model_selection, metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from helper import prepare_data

df = prepare_data()

y = df["Berri1"]

X = df[["day", "month", "day_of_week", "Mean Temp (°C)", "Total Precip (mm)", "Snow on Grnd (cm)", "Min Temp (°C)", "Max Temp (°C)"]]

regr = RandomForestRegressor(n_estimators=100)

rkf = model_selection.RepeatedKFold()

score, mse, r2 = [], [], []

for train_index, test_index in rkf.split(X):

    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    regr.fit(X_train, y_train)

    score.append(regr.score(X_test, y_test))

    y_pred = regr.predict(X_test)

    mse.append(metrics.mean_squared_error(y_test, y_pred))
    r2.append(metrics.r2_score(y_test, y_pred))

print("Score: Mean {}, Stdv: {}".format(stat.mean(score), stat.stdev(score)))
print("MSE: Mean {}, Stdv: {}".format(stat.mean(mse), stat.stdev(mse)))
print("R2: Mean {}, Stdv: {}".format(stat.mean(r2), stat.stdev(r2)))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regr.fit(X_train, y_train)
print(regr.score(X_test,y_test))

result = regr.predict(X)

plt.plot(list(y.index), y, label="true")
plt.plot(list(y.index), result, label="predicted")
plt.legend()
plt.show()

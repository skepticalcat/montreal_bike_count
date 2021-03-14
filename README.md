### Montreal Bicycle Count Regression

Uses the Montreal bike lane count dataset [1] and a Montreal weather dataset [2].

Implemented AdaBoost, RFR and Poisson Regression.
RFR with k-fold CV.
Achieves a mean accuracy of 0.86 with a std deviation of 0.04, similar values for r2. 

Written out of personal interest

###### Weather / Bike count correlations

![Alt text](cnt_weather_corr.png "Weather/Bike Count Corr")

###### Bike Lane / Bike Lane correlations

![Alt text](some_lanes_corr.png "Weather/Bike Count Corr")

###### RFR result

![Alt text](rfr_result.png "RFR Result")

#### How to run

Just run poisson_weather, rfr_weather or adaboost_weather.

#### Dependencies
* pandas
* sklearn

[1]https://www.kaggle.com/pablomonleon/montreal-bike-lanes
[2]https://www.kaggle.com/rosemondeld/weather-montreal-2015-en
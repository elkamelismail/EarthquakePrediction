import pandas as pd
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

#loading data
dt = pd.read_csv('data/dt_pre_.csv')

#splitting data
X = dt.drop('meandamage',axis = 1)
y = dt['meandamage']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

#scaling data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#training model
xgb_regressor = xgb.XGBRegressor(objective="reg:squarederror", random_state=42, n_estimators=150, learning_rate=0.1, max_depth=5)
xgb_regressor.fit(X_train, y_train)

y_pred = xgb_regressor.predict(X_test)

#saving model
pickle.dump(xgb_regressor, open('models/model_.pkl','wb'))
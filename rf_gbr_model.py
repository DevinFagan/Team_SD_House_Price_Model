from ordinal_ranker import *
from fillna import *
import pandas as pd
import numpy as np
from sklearn import model_selection as ms
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.ensemble import RandomForestRegressor,  GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV


house_price = pd.read_csv('train.csv')
house_test = pd.read_csv('test.csv')
house_train = house_price.drop('SalePrice',axis =1)
data = pd.concat([house_train, house_test])



data = data_process(data)


# split data back into training and submission data set
train = data.iloc[:house_price.shape[0],:]
sub = data.iloc[house_price.shape[0]:,:]

# split data into train and test data
X_train, X_test, Y_train, Y_test = train_test_split(x_train, y_train, test_size=0.2)

#Set models
randomForest= RandomForestRegressor()
gbr = GradientBoostingRegressor()

# GridSearchCV - randomForest
grid_para_tree_rf = [{
    "n_estimators": np.linspace(start=500, stop=1600, num=10, dtype=int),
    "max_depth": range(5, 20, 2),
    "max_leaf_nodes": range(5, 20, 2),
    "min_samples_leaf": range(1, 10),
    "min_samples_split": np.linspace(start=2, stop=30, num=15, dtype=int)
}]
randomForest.set_params(random_state=42)
grid_search_tree = GridSearchCV(randomForest, grid_para_tree_rf, cv=8, n_jobs=-1).fit(X_train,Y_train)
print (rnint, grid_search_randomForest.best_params_, '%.2f' % randomForest.score(X_train,Y_train), '%.2f' % randomForest.score(X_test,Y_test))


# GridSearchCV - Gradient Boosting Regressor
grid_para_tree_gbr = [{
    "n_estimators": np.linspace(start=500, stop=8000, num=10, dtype=int),
    "learning_rate": [0.05,0.1,0.2,0.25,0.5],
    "max_depth": range(5, 20, 2),
    "max_leaf_nodes": range(5, 20, 2),
    "min_samples_leaf": range(1, 20, 2),
    "min_samples_split": np.linspace(start=2, stop=30, num=15, dtype=int)
}]
gbr.set_params(random_state=42)
grid_search_tree = GridSearchCV(gbr, grid_para_tree_gbr, cv=8, n_jobs=-1).fit(X_train,Y_train)
print (rnint, grid_search_gbr.best_params_, '%.2f' % gbr.score(X_train,Y_train), '%.2f' % gbr.score(X_test,Y_test))

# set model
# Random Forest Regressor
randomForest= RandomForestRegressor(n_estimators=1200, max_depth=15,
                          min_samples_split=5,
                          min_samples_leaf=5,
                          max_features=None,
                          oob_score=True,
                          random_state=42)

# gbr

#find Feature importance
feature_importance = list(zip(train.columns, randomForest.feature_importances_))
dtype = [('feature', 'S20'), ('importance', 'float')]
feature_importance = np.array(feature_importance, dtype=dtype)
feature_sort = np.sort(feature_importance, order='importance')[::-1]
featureNames, featureScores = zip(*list(feature_sort))
plt.barh(range(20), featureScores[:20], tick_label=featureNames[:20])
plt.title("Random Forest: Feature Importance(Top 20)")
plt.show()


feature_importance = list(zip(train.columns, gbr.feature_importances_))
dtype = [('feature', 'S20'), ('importance', 'float')]
feature_importance = np.array(feature_importance, dtype=dtype)
feature_sort = np.sort(feature_importance, order='importance')[::-1]
featureNames, featureScores = zip(*list(feature_sort))
plt.barh(range(20), featureScores[:20], tick_label=featureNames[:20])
plt.title("GradientBoostingRegressor: Feature Importance(Top 20)")
plt.show()
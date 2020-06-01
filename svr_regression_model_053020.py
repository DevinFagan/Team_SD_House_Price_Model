# script to generate sv regression model for ames, iowa housing file

# import necessary librarys, modules
from ordinal_ranker import *
from fillna import *
import pandas as pd
import numpy as np
import csv
import statistics
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn import model_selection as ms
from sklearn import datasets
import matplotlib
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.rc('figure', figsize=(6, 6))

# read in training and submission files so they can be processed together to have 
# same # columns. sample_submission is a dummy sale price column same # rows as test.csv.
house_price = pd.read_csv('train.csv')
house_sub = pd.read_csv('test.csv')
sub_ys=pd.read_csv('sample_submission.csv')
house_sub = pd.merge(house_sub,sub_ys,how = 'inner', on = 'Id')
data = pd.concat([house_price, house_sub])

# call overall preprocessing fxn from fillna
data = data_process(data)

# save data after preprocessing
data.to_csv('cleaned_all_data.csv')

# break data file back apart into training and submission data set
train = data.iloc[:house_price.shape[0],:]
sub = data.iloc[house_price.shape[0]:,:]

# separate the predictors and response in the training data set
x_train = np.array(train.drop('SalePrice',axis=1))
y_train = np.ravel(train['SalePrice'])
# separate the predictors and response in the test data set
x_sub = np.array(sub.drop('SalePrice',axis=1))

# log transform target ('saleprice') since it has a rightward skew
y_train_log = np.log(y_train)

# scale the features for both training and submission set (same scale since model is on that scale)
x_scaled = (x_train-x_train.min(axis=0))/(x_train.max(axis=0)-x_train.min(axis=0))
x_sub_scaled = (x_sub-x_train.min(axis=0))/(x_train.max(axis=0)-x_train.min(axis=0))

# create support vector regression model
svr = SVR()

# parameters were generated in notebook 'svr_notebook_052920'
x_traincv, x_testcv, y_traincv, y_testcv = ms.train_test_split(x_scaled, y_train_log, \
		test_size=0.20, random_state=396462)
svr.set_params(C= 0.045, epsilon = 0.06, kernel = 'linear')
svr.fit(x_traincv,y_traincv)

# generate dictionary from svr model coefficients and scaling factors for each parameter
scale_fctr=[]
for i in range(x_train.shape[1]):
    scale_fctr.append(1/(x_train.max(axis=0)[i]-x_train.min(axis=0)[i]))
coefs_scl = list(zip(train.columns[train.columns!='SalePrice'],list(svr.coef_[0]),scale_fctr))
coefs_dict = pd.DataFrame(coefs_scl).set_index(0).T.to_dict('list')

# generate sale price predictions for submission set
test_y_predict = np.exp(svr.predict(x_sub_scaled))

# write the sales predictions and coefficients to csv
with open('coefs_dict.csv', 'w') as f:
    for key in coefs_dict.keys():
        f.write("%s,%f8,%f10\n"%(key,coefs_dict[key][0],coefs_dict[key][1]))

team_SD_submission1=pd.DataFrame(range(1461,2920))
team_SD_submission1.columns = ['Id']
team_SD_submission1['SalePrice']=test_y_predict
team_SD_submission1.to_csv('teamSD_submission_svr.csv')
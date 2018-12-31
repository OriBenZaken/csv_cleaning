from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import linear_model
from sklearn.neighbors import KNeighborsRegressor

def main(train_file, train_target_file, test_file, test_target_file):
    train_df = np.loadtxt(train_file, delimiter=',')
    train_target_df =  np.loadtxt(train_target_file, delimiter=',')
    test_df =  np.loadtxt(test_file, delimiter=',')
    test_target_df =  np.loadtxt(test_target_file, delimiter=',')

    #regr = tree.DecisionTreeRegressor()
    #regr = RandomForestRegressor(random_state=0, n_estimators=500, min_samples_leaf= 2)
    #regr = svm.SVR(gamma='scale', C=1.0, epsilon=0.2)
    #regr = linear_model.Lasso(alpha=0.1) # alpha is regularization const
    #regr = GradientBoostingRegressor(n_estimators=50000, learning_rate=0.1, loss='ls')
    regr = KNeighborsRegressor(n_neighbors=1)
    regr = regr.fit(train_df, train_target_df)
    y_list, y_hat_list = run_test(test_df, test_target_df, regr)
    print("Mean absolute error: {}".format(get_mean_absolute_error(y_list, y_hat_list)))
    print("Average relative error: {}".format(get_average_relative_error(y_list, y_hat_list)))

    # y_list = []
    # y_hat_list = []
    # regr = regr.fit(train_df, train_target_df)
    # for example, target in zip(test_df, test_target_df):
    #     pred = regr.predict([example])
    #     y_list.append(target)
    #     y_hat_list.append(pred)
    #     print("Real value: {}, Predicted value: {}".format(target, pred))
    # print str(mean_absolute_error(y_list,y_hat_list))

    pass

def run_test(test_df, test_target_df, model):
    y_list = []
    y_hat_list = []
    for example, target in zip(test_df, test_target_df):
        pred = model.predict([example])
        y_list.append(target)
        y_hat_list.append(pred)
        print("Real value: {}, Predicted value: {}".format(target, pred))
    return y_list,y_hat_list

def get_mean_absolute_error(y_list, y_hat_list):
    return mean_absolute_error(y_list, y_hat_list)

def get_average_relative_error(y_list, y_hat_list):
    sum = 0
    for y, y_hat in zip(y_list,y_hat_list):
        if (y > y_hat):
            relative_error = (1 - float(y_hat)/float(y)) * 100
        else:
            relative_error = (1 - float(y)/float(y_hat)) * 100
        sum += relative_error
    average_relative_error = float(sum)/len(y_list)
    return average_relative_error



if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Missing arguments!")
        sys.exit(1)
    main(*sys.argv[1:])
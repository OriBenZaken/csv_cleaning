import sys
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
import utils as ut
from sklearn.utils import resample

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", help="Filtered data file")
    parser.add_argument("-resample", help="Number of examples to resample", default=0)
    args = parser.parse_args()
    data_frame = pd.read_csv(args.data_file, low_memory=False)
    # split the data
    cols = [col for col in data_frame.columns if col != 'demand']
    # dropping the 'demand' column
    data = data_frame[cols]
    # assigning the fare_amount column as target
    target = data_frame['demand']
    # operate resample to get important rows
    if args.resample != 0:
        data, target = resample(data, target, n_samples=args.resample, random_state=0)
    # split data set into train and test sets
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.30, random_state=10)
    ut.save_filtered_file('train', data_train, header=False)
    ut.save_filtered_file('test', data_test, header=False)
    ut.save_filtered_file('target_train', target_train, header=False)
    ut.save_filtered_file('target_test', target_test, header=False)


if __name__ == '__main__':
    main()
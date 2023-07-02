import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from numpy import loadtxt
from sklearn.tree import DecisionTreeClassifier


def classify(age, job, martial, education, default, balance, housing, loan, day, month, duration, campaign):
    #bank_additional_full_df = pd.read_csv(r"C:\Users\Admin\Desktop\BE Project\Datasets\Acquisition\bank-additional-full.csv", sep=';')
    bank_additional_full_df = pd.read_csv(r"C:\Users\hp\Desktop\BE Project\bank-full.csv")

    test_age = age
    test_job = job
    test_martial = martial
    test_education = education
    test_balance=balance
    test_default = default
    test_housing = housing
    test_loan = loan
    test_contact = "unknown"
    test_month = month
    test_day = day
    test_duration = duration
    test_campaign = campaign
    test_pdays = -1
    test_previous = 0
    test_poutcome = "unknown"

    test = pd.DataFrame({"age": [test_age], "job": [test_job], "martial": [test_martial], "education": [test_education],
                         "default": [test_default], "balance":[test_balance],
                         "housing": [test_housing], "loan": [test_loan], "contact": [test_contact],
                         "month": [test_month], "day": [test_day], "duration": [test_duration],
                         "campaign": [test_campaign],
                         "pdays": [test_pdays], "previous": [test_previous], "poutcome": [test_poutcome]})

    # Create a flag for Train and Test Data set
    bank_additional_full_df['Type'] = 'Train'
    test['Type'] = 'Test'
    fullData = pd.concat([bank_additional_full_df, test], axis=0, sort=True)
    fullData = fullData.reset_index(drop=True)

    # Taking only those column which will affect more to output
    features_columns = ['age', 'job', 'education', 'default', 'balance', 'housing', 'loan',
                        'month', 'day', 'duration', 'campaign']

    # Encode the categorical data
    for col in fullData.columns:
        if fullData[col].dtype == object:
            fullData[col] = fullData[col].astype('category')
            fullData[col] = fullData[col].cat.codes
    print(fullData)
    train_modified = fullData[fullData['Type'] == 1]
    test_modified = fullData[fullData['Type'] == 0]

    # train_modified["Exited"] = number.fit_transform(train_modified["Loan_Status"].astype('str'))

    x_train = train_modified[list(features_columns)].values

    y_train = train_modified["y"].values
    x_test = test_modified[list(features_columns)].values

    # Normalization
    scaler = MinMaxScaler(feature_range=(0, 1))
    x_train = scaler.fit_transform(x_train)

    np.set_printoptions(precision=3)

    # Defining
    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)

    # Predict Output
    predicted = model.predict(x_test)
    print("PREDICTED", predicted)


#classify(58, "management", "married", "tertiary", "no", 2143, "yes", "no", 5, "may", 261, 1)
    if predicted==0:
        return "no"
    else:
        return "yes"
   # return predicted
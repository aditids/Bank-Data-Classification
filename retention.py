import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns


def classify(credit_score, gender, age, tenure, balance, num_of_products, has_card, active_member, estimated_salary):
    df = pd.read_csv(r'C:\Users\hp\Desktop\BE Project\Churn_Modelling.csv')
    print(df.head(n=5))

    df = df.drop(['RowNumber', 'CustomerId', 'Surname', 'Geography'], axis=1)


    test_CreditScore = credit_score
    test_gender = gender
    test_age = age
    test_tenure = tenure
    test_balance = float(balance)
    test_NumOfProducts = num_of_products
    test_HasCrCard = has_card
    test_IsActiveMembert = active_member
    test_EstimatedSalary = float(estimated_salary)

    test=pd.DataFrame({"CreditScore":[test_CreditScore], "Gender":[test_gender], "Age":[test_age], "Tenure":[test_tenure], "Balance":[test_balance],
                   "NumOfProducts":[test_NumOfProducts], "HasCrCard":[test_HasCrCard], "IsActiveMember":[test_IsActiveMembert],
                   "EstimatedSalary": [test_EstimatedSalary]})

#Create a flag for Train and Test Data set
    df['Type'] = 'Train'
    test['Type'] = 'Test'
    fullData = pd.concat([df, test], axis=0)

    fullData = fullData.replace(to_replace={'Gender': {'Female': 1, 'Male':0}})
    print(fullData.head())

    train_modified=fullData[fullData['Type']=='Train']
    test_modified=fullData[fullData['Type']=='Test']
#train_modified["Exited"] = number.fit_transform(train_modified["Loan_Status"].astype('str'))

    predictors_Logistic=['CreditScore', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
    x_train = train_modified[list(predictors_Logistic)].values

    y_train = train_modified["Exited"].values
    x_test=test_modified[list(predictors_Logistic)].values

# Defining
    rf = RandomForestClassifier(n_estimators=100, criterion='entropy', max_depth=8, random_state=4)

# Train the model using the training sets
    rf.fit(x_train, y_train)

#Predict Output
    predicted = rf.predict(x_test)
    print("PREDICTED", predicted)
    return predicted



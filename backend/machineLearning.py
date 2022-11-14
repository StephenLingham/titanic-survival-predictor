import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

def trainModel():
    global df 
    df = pd.read_csv('./titanic-data.csv')

    df['Male'] = df['Sex'] == 'male'

    X = df[['Pclass', 'Male', 'Age']].values
    y = df['Survived'].values

    model.fit(X,y)

def predictSurvived(passengerClass, male, age):
    predictorValues = [[passengerClass, male, age]]

    prediction = model.predict(predictorValues)
    predictionAsInt = int(prediction)

    return predictionAsInt

def predictSurvivedProbability(passengerClass, male, age):
    predictorValues = [[passengerClass, male, age]]

    global prediction
    prediction = model.predict_proba(predictorValues)
    percentage_of_survival = prediction[0][1]
    prediction_percentage = round(percentage_of_survival, 2) * 100

    return prediction_percentage

def sex_prediction():
    fig, ax = plt.subplots(figsize=(12,8))

    gender_count = df['Sex'].value_counts(sort=False)

    s_count = df.loc[df['Survived'] == 1, ['Sex']].value_counts(sort=False)

    ax.bar('Female', s_count['female']/gender_count['female'], color='green')

    ax.bar('Male', s_count['male']/gender_count['male'], color='green')

    ax.set_ylabel('% Survived')

    plt.show()

def class_prediction():
    fig, ax = plt.subplots(figsize=(6,4))

    pclass_count = df['Pclass'].value_counts(sort=False)

    s_count = df.loc[df['Survived'] == 1, ['Pclass']].value_counts(sort=False)

    ax.bar('First class', s_count.iloc[2]/pclass_count.iloc[2], color='green')

    ax.bar('Second class', s_count.iloc[1]/pclass_count.iloc[1], color='green')

    ax.bar('Third class', s_count.iloc[0]/pclass_count.iloc[0], color='green')

    ax.set_ylabel('% Survived')

    plt.show()

def age_histogram():
    survival_by_age = df.groupby(['Age', 'Survived']).size().unstack('Survived')
    survival_by_age.columns = ['No', 'Yes']
    survival_by_age.plot.bar(title='Survival by Age')

    plt.xticks(np.arange(-1, 80, 10))
    plt.show()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, confusion_matrix
import mlflow
import mlflow.sklearn
from mlflow import log_metric, log_param, log_artifacts

# Get url from DVC
import dvc.api

path = 'data/titanic.csv'
repo = '/Users/pwaghray/SEDS - IIITH/Part B - Data Science/Week - 2/project/'
version = 'v1' 
data_url = dvc.api.get_url(
    path=path,
    repo=repo,
    rev=version)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting the experiment')
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment(experiment_name='mlflow - project')

    mlflow.autolog()  ##record automatically

    df = pd.read_csv(data_url, sep=',')

    # log data params
    mlflow.log_param('data_url',data_url)
    mlflow.log_param('data_version',version)
    mlflow.log_param('input_rows',df.shape[0])
    mlflow.log_param('input_cols',df.shape[1])

    # Converting categorical columns to discrete numeric
    df['Sex'].replace(to_replace='male', value=1, inplace=True)
    df['Sex'].replace(to_replace='female', value=2, inplace=True)
    df['Sex'].fillna(df.Sex.median(), inplace=True)
    df['Sex'] = df['Sex'].astype(int)
    df['Embarked'].replace(to_replace='C', value=1, inplace=True)
    df['Embarked'].replace(to_replace='Q', value=1, inplace=True)
    df['Embarked'].replace(to_replace='S', value=3, inplace=True)
    df['Embarked'].fillna(df.Embarked.median(), inplace=True)
    df['Embarked'] = df['Embarked'].astype(int)

    # Filling empty data with median values
    df['Age'].fillna(df.Age.median(), inplace=True)

    # Dropping unnecessary columns
    df = df.drop('Name', axis=1)
    df = df.drop('Ticket', axis=1)
    df = df.drop('Cabin', axis=1)
    df = df.drop('PassengerId', axis=1)

    print(df['Survived'].value_counts())

    log_param("Value counts", df['Survived'].value_counts())

    # splitting data into training and test set for independent attributes
    X_train, X_test, y_train, y_test = train_test_split(df.drop('Survived', axis=1), 
                                                        df['Survived'],
                                                        test_size=.20,
                                                        random_state=123)
    print(X_train.shape, X_test.shape)
    log_param("Train shape", X_train.shape)


    model_entropy = DecisionTreeClassifier(criterion="entropy",
                                           max_depth=10, min_samples_leaf=4)
    model_entropy_rf = RandomForestClassifier(criterion='entropy', max_depth=6,
                                              min_samples_leaf=3, n_estimators=149)

    model_entropy.fit(X_train, y_train)
    print("Decision Tree Model trained")

    model_entropy_rf.fit(X_train, y_train)
    print("Random Forest Model trained")

    train_accuracy = model_entropy.score(X_train, y_train)  # performance on train data
    test_accuracy = model_entropy.score(X_test, y_test)  # performance on test data
    train_accuracy1 = model_entropy_rf.score(X_train, y_train)  # performance on train data
    test_accuracy1 = model_entropy_rf.score(X_test, y_test)  # performance on test data

    log_metric("DT - Accuracy for this run", test_accuracy)
    log_metric("RF - Accuracy for this run", test_accuracy1)
    mlflow.sklearn.log_model(model_entropy, "Decision Tree Model")
    mlflow.sklearn.log_model(model_entropy_rf, "Random Forest Model")
    print(mlflow.active_run().info.run_uuid)
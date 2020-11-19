# importing libraries
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


"""To implement Gaussian naves bayes for flowers clssification"""


def main():

    iris = load_iris()
    print(iris.keys())
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target
    print(iris_df.head())
    X, y = iris_df.drop('target', 1), iris_df.target
    print(X.shape, y.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(y_pred[:10])
    accuracy = accuracy_score(y_test, y_pred)
    print("The accuracy of Gaussian naves is {}".format(accuracy))
    # classification report
    print(classification_report(y_test, y_pred))


main()

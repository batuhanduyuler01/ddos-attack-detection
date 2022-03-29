from MethodBuilder import MethodBuilder
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import time


class MLMethodBuilder(MethodBuilder):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        MethodBuilder.__init__(self, dataframe)
        print("ML Builder is invoke")

    def SVM(self, kernelType: str) -> None:

        startingTime = time.time()

        if (False == MethodBuilder.is_data_splitted(self)):
            MethodBuilder.split_data(self)

        if (kernelType.lower() == "linear"):
            classifier = SVC(kernel=kernelType.lower(), random_state=42)
        elif (kernelType.lower() == "rbf"):
            classifier = SVC(kernel=kernelType.lower(), random_state=42)
        else:
            assert False, "Error! Wrong Classifier"

        classifier.fit(self.xTrain.values, self.yTrain.values)
        predictions = classifier.predict(self.xTest.values)

        endTime = time.time()
        print(f'SVM Results calculated in: {endTime - startingTime} s')

        print(
            f'Confusion Matrix of {kernelType}: \n {confusion_matrix(self.yTest, predictions)}')

        MethodBuilder.metrics_calculator(
            predictions, self.yTest.reset_index().values[:, 1])

    def NaiveBayes(self) -> None:
        # Naive Bayes algoritması
        startingTime = time.time()

        if (False == MethodBuilder.is_data_splitted(self)):
            MethodBuilder.split_data(self)

        gnb = GaussianNB()
        gnb.fit(self.xTrain.values, self.yTrain.values)
        predictions = gnb.predict(self.xTest.values)

        endTime = time.time()
        print(f'NaiveBayes Results calculated in: {endTime - startingTime} s')

        print(
            f'Confusion Matrix of Naive Bayes Classifier: \n {confusion_matrix(self.yTest, predictions)}')

        MethodBuilder.metrics_calculator(
            predictions, self.yTest.reset_index().values[:, 1])

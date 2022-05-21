from MethodBuilder import MethodBuilder
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB as GNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from diffprivlib.models import GaussianNB as DifferentialGNB
from diffprivlib.models.forest import DecisionTreeClassifier as DifferentialDecisionTreeClassifier
import time


class MLMethodBuilder(MethodBuilder):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        MethodBuilder.__init__(self, dataframe)
        print("ML Builder is invoke")

    def DecisionTreeClassifier(self, maxDepth = 2) -> None :
        startingTime = time.time()

        if (False == MethodBuilder.is_data_splitted(self)):
            MethodBuilder.split_data(self)

        self.decisionTreeClassifier = DecisionTreeClassifier(max_depth = maxDepth, random_state = 25)
        self.decisionTreeClassifier.fit(self.xTrain.values, self.yTrain.values)

        predictions = self.decisionTreeClassifier.predict(self.xTest.values)

        endTime = time.time()
        print(f'Decision Tree Classifier Results calculated in: {endTime - startingTime} s')

        self.print_results(self.yTest.values, predictions, "Decision Tree Classifier")
        pass

    def DifferentialDecisionTreeClassifier(self, maxDepth = 5) -> None :
        startingTime = time.time()

        if (False == MethodBuilder.is_data_splitted(self)):
            MethodBuilder.split_data(self)

        self.differentialDecisionTreeClassifier = DifferentialDecisionTreeClassifier(epsilon = 5, max_depth = maxDepth, random_state = 25)
        self.differentialDecisionTreeClassifier.fit(self.xTrain.values, self.yTrain.values)

        predictions = self.differentialDecisionTreeClassifier.predict(self.xTest.values)

        endTime = time.time()
        print(f'Differential Decision Tree Classifier Results calculated in: {endTime - startingTime} s')

        self.print_results(self.yTest.values, predictions, "Differential Decision Tree Classifier")

    def NaiveBayes(self) -> None:
        # Naive Bayes algoritması
        startingTime = time.time()

        if (False == MethodBuilder.is_data_splitted(self)):
            MethodBuilder.split_data(self)

        self.gaussianNaiveBayes = GNB()
        self.gaussianNaiveBayes.fit(self.xTrain.values, self.yTrain.values)
        predictions = self.gaussianNaiveBayes.predict(self.xTest.values)

        endTime = time.time()
        print(f'NaiveBayes Results calculated in: {endTime - startingTime} s')

        print(
            f'Confusion Matrix of Naive Bayes Classifier: \n {confusion_matrix(self.yTest, predictions)}')

        MethodBuilder.metrics_calculator(
            predictions, self.yTest.reset_index().values[:, 1])

    def DifferentialNaiveBayes(self) -> None: 
        #Differential Privacy Naive Bayes with IBM diffpriv framework
        startingTime = time.time()
        if (False == MethodBuilder.is_data_splitted(self)):
            MethodBuilder.split_data(self)
        self.diffGaussianNaiveBayes = DifferentialGNB()
        self.diffGaussianNaiveBayes.fit(self.xTrain.values, self.yTrain.values)
        predictions = self.diffGaussianNaiveBayes.predict(self.xTest.values)

        endTime = time.time()
        print(f'Differential NaiveBayes Results calculated in: {endTime - startingTime} s')

        print(
            f'Confusion Matrix of Naive Bayes Classifier: \n {confusion_matrix(self.yTest, predictions)}')

        MethodBuilder.metrics_calculator(
            predictions, self.yTest.reset_index().values[:, 1])

    def print_results(self, yTest, predictions, algorithmName) :
        print(
            f'Confusion Matrix of {algorithmName}: \n {confusion_matrix(yTest, predictions)}')

        MethodBuilder.metrics_calculator(
            predictions, list(yTest))

    def predict(self, TestFrame, Algorithm = "naive_bayes") :
        algo = Algorithm.lower()
        if (algo == "naive_bayes"):
            return self.gaussianNaiveBayes.predict(TestFrame)
        elif (algo == "differential_naive_bayes"):
            return self.diffGaussianNaiveBayes.predict(TestFrame)
        elif (algo == "decision_tree"):
            return self.decisionTreeClassifier.predict(TestFrame)
        elif (algo == "differential_decision_tree"):
            return self.differentialDecisionTreeClassifier.predict(TestFrame)
        else:
            print("ERROR")


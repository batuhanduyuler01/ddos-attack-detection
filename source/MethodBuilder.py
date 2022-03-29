import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


class MethodBuilder:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        if (dataframe.empty):
            print("Dataframe is empty!")
            assert False
        print("Generic Method Builder is invoke.")

        self.__df = dataframe.copy()
        self.xTrain = pd.DataFrame()
        self.xTest = pd.DataFrame()
        self.yTrain = pd.DataFrame()
        self.yTest = pd.DataFrame()

    def is_data_splitted(self) -> bool:
        # Herhangi biri boş olsa bile split edilmemiş sayılacaktır.
        if (self.xTest.empty or self.xTrain.empty or self.yTest.empty or self.yTrain.empty):
            return False

        # tüm datalar doluysa true dönecektir.
        return True

    def split_data(self, testSize=0.2,) -> None:
        # eğer data split edilmişse işlem yapılmasına gerek yok.
        if (self.is_data_splitted() == True):
            print("Data is already splitted.")
            return

        print("Data will split.")
        self.xTrain, self.xTest, self.yTrain, self.yTest = train_test_split(self.__df.drop(
            [" Label"], axis=1), self.__df[" Label"], test_size=testSize, random_state=0)

    def metrics_calculator(predictionOutputs, testOutputs) -> None:
        print("\n\nCalculated Metrics: \n")
        tp = []
        fp = []
        fn = []
        tn = []

        for i in range(0, len(predictionOutputs)):
            if (predictionOutputs[i] == 1 and testOutputs[i] == 1):
                tp.append(1)
            elif (predictionOutputs[i] == 0 and testOutputs[i] == 1):
                fp.append(1)
            elif (predictionOutputs[i] == 1 and testOutputs[i] == 0):
                fn.append(1)
            elif (predictionOutputs[i] == 0 and testOutputs[i] == 0):
                tn.append(1)

        precision = 0
        recall = 0

        if (len(predictionOutputs) != 0):
            acc = (len(tp) + len(tn)) / len(predictionOutputs)
            print('accuracy:', acc)

        if (len(tp) + len(fp) != 0):
            precision = len(tp) / (len(tp) + len(fp))
            print('\nprecision:', precision)

        if (len(fn) + len(tp) != 0):
            recall = len(tp) / (len(fn) + len(tp))
            print('\nrecall:', recall)

        if (precision + recall != 0):
            f1_score = (2*precision * recall) / (precision + recall)
            print('\nf1 score:', f1_score)

    def get_dataframe(self) -> pd.DataFrame:
        return self.__df

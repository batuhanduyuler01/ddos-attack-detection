from MethodBuilder import MethodBuilder
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix


class MLMethodBuilder(MethodBuilder):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        MethodBuilder.__init__(self, dataframe)
        print("ML Builder is invoke")

    def SVM(self, kernelType: str) -> None:
        if (False == MethodBuilder.is_data_splitted(self)):
            MethodBuilder.split_data(self)

            

        if (kernelType.lower() == "linear"):
            classifier = SVC(kernel=kernelType.lower(), random_state=42)
            classifier.fit(self.xTrain, self.yTrain.ravel())
            predictions = classifier.predict(self.xTest)
            print(
                f'Confusion Matrix of Linear Kernel: \n {confusion_matrix(self.yTest, predictions)}')
        elif (kernelType.lower() == "rbf"):
            classifier = SVC(kernel=kernelType.lower(), random_state=42)
            classifier.fit(self.xTrain.values, self.yTrain.values)
            predictions = classifier.predict(self.xTest.values)
            print(
                f'Confusion Matrix of Radial Basis Kernel: \n {confusion_matrix(self.yTest, predictions)}')

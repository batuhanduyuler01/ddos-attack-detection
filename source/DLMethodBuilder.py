from MethodBuilder import MethodBuilder
import pandas as pd
import numpy as np
import time
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, ZeroPadding1D, Dense


class DLMethodBuilder(MethodBuilder):
    def __init__(self, dataframe: pd.DataFrame) -> None:
        MethodBuilder.__init__(self, dataframe)
        print("DL Builder is invoke")

    def ConvolutionalNeuralNetwork(self, filterNumber: int = 64, kernelSize: int = 3, activationFunc: str = 'relu', poolSize: int = 2) -> None:
        self.inputShape: tuple = (
            MethodBuilder.get_dataframe(self).shape[1], 1)
        self.__model = Sequential()
        self.__model.add(Conv1D(filters=filterNumber, kernel_size=kernelSize,
                         activation=activationFunc, input_shape=self.inputShape))
        self.__model.add(MaxPooling1D(pool_size=poolSize))
        self.__model.add(Flatten())
        self.__model.add(Dense(1, activation="sigmoid"))
        self.__model.summary()

    def start_to_compile(optimizer: str):
        pass

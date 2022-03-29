from MethodBuilder import MethodBuilder
import pandas as pd
import numpy as np
import time
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, ZeroPadding1D, Dense


import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

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

    def start_to_compile(self, optimizer: str = 'SGD', loss: str = 'mean_absolute_error', metrics: str = 'accuracy', epochNum: int =20, batchSize : int = 10) -> None:
        
        startingTime = time.time()

        if (False == MethodBuilder.is_data_splitted(self)):
            MethodBuilder.split_data(self)
        
        self.__model.compile(loss= loss, optimizer= optimizer, metrics = [metrics])
        self.__model.fit(self.xTrain.values, self.yTrain.values, epochs=epochNum, batch_size=batchSize, validation_data=(self.xTest.values, self.yTest.values))

        endTime = time.time()
        print(f'1D CNN Results calculated in: {endTime - startingTime} s')

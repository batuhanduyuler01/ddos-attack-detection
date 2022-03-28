import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder


class DataProcessor:

    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.__df = dataframe.copy()

    def __clean_data_row_based(self, dataframe: pd.DataFrame) -> pd.DataFrame:

        dataframe.dropna(inplace=True)
        indicesToKeep = ~dataframe.isin([np.nan, np.inf, -np.inf]).any(1)

        df = dataframe.drop([" Label"], axis=1)
        dfLabel = pd.DataFrame(dataframe[" Label"], columns=[" Label"])

        return pd.concat([df[indicesToKeep].astype(np.float64), dfLabel[indicesToKeep]], axis=1)

    def __clean_data_col_based(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        df = dataframe.copy()
        for column in df.columns:
            if column != " Label":
                colState = np.any(np.isnan(df[f'{column}']))
                if (colState):
                    df = df.drop([f'{column}'], axis=1)

        return df

    def print_data_statistics(self, dataframe: pd.DataFrame) -> None:
        if (dataframe.empty == True):
            print("This DataFrame is Empty")
        else:
            labels = dataframe[" Label"].unique()
            print(
                f'No Of Labels: {len(labels)} as : {dataframe[" Label"].unique()}')

            ddosPaketSayisi = len(dataframe[dataframe[" Label"] != "BENIGN"])
            normalPaketSayisi = len(dataframe[dataframe[" Label"] == "BENIGN"])
            packetNumber = len(dataframe)

            print("\n---DataSet---\n")
            print(f'Atak Sayisi: {ddosPaketSayisi}')
            print(f'Normal Paket Sayisi: {normalPaketSayisi}')
            print(f'Total Sayisi: {packetNumber}')
            print(f'Atak Orani: {100 * ddosPaketSayisi / packetNumber}')

    def min_max_scaler(self, dataframe: pd.DataFrame) -> pd.DataFrame:

        df = self.__clean_data_row_based(dataframe)
        df = dataframe.copy()
        forbiddenColumns: list = [" Label"]

        for column in df.columns:
            if column in forbiddenColumns:
                pass
            else:
                tempMax = max(df[f'{column}'])
                tempMin = min(df[f'{column}'])
                tempDenominator = (tempMax - tempMin)

                df[f'{column}'] = (df[f'{column}'] - tempMin) / tempDenominator

        return self.__clean_data_col_based(df)

    def chi_square_feature_selector(self, dataframe: pd.DataFrame, nLargest: int = 10) -> None:
        bestFeatures = SelectKBest(score_func=chi2, k=20)
        featureSpace = dataframe.drop([" Label"], axis=1)

        labelEncoder = LabelEncoder()
        dependentVariable = labelEncoder.fit_transform(dataframe[" Label"])

        fit = bestFeatures.fit(featureSpace, dependentVariable)
        featureScores = pd.concat([pd.DataFrame(
            featureSpace.columns), pd.DataFrame(fit.scores_)], axis=1)
        featureScores.columns = ['Specs', 'Score']
        print(featureScores.nlargest(nLargest, 'Score'))

        return featureScores

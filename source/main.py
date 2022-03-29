import pandas as pd
import numpy as np

import DataProcessor as dp


fridayDataSet: pd.DataFrame = pd.read_csv(
    "../verisetleri/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv", low_memory=False)

dataProcessor: dp.DataProcessor = dp.DataProcessor(fridayDataSet)
# dataProcessor.print_data_statistics(fridayDataSet)
scaledData = dataProcessor.min_max_scaler(fridayDataSet)
print("Include NaN: ", np.any(np.isnan(scaledData.drop([" Label"], axis=1))))
bestFeatureFrame = dataProcessor.chi_square_feature_selector(scaledData)
bestFeatures = bestFeatureFrame.Specs

print(bestFeatures)

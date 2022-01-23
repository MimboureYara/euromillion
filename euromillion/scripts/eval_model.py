from keras.models import Sequential
from keras.models import load_model
from keras.layers import LSTM, Dense,Dropout
import pandas as pd
import numpy as np
from config import Config
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(Config.DATASET_PATH.data.df.values)
transformed_dataset = scaler.transform(Config.DATASET_PATH.data.df.values)
transformed_df = pd.DataFrame(data=transformed_dataset, index=Config.DATASET_PATH.data.df.index)


to_predict=Config.DATASET_PATH.data.df.iloc[-5:]
scaled_to_predict = scaler.transform(to_predict)

scaled_predicted_output_1 = Config.MODELS_PATH.model.predict(np.array([scaled_to_predict]))
data = Config.scripts.scaler.inverse_transform(scaled_predicted_output_1).astype(int)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'Bonus', 'Extra'])
df.to_csv('euro-millions-ireland.csv', index=False)  
df
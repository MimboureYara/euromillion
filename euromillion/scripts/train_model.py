import pickle # Serialiser des objets (y comporis des modeles)
from keras.models import Sequential
from keras.models import load_model
from keras.layers import LSTM, Dense,Dropout
import os
import numpy as np
import pandas as pd
from config import Config
batch_size = 25 

Config.MODELS_PATH.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(str(Config.ROW_DATASET_FILE_PATH))

df2 = df['Winning Numbers'].str.split(" ",expand=True,)
df = df.drop(['Winning Numbers','Draw Date', 'Outcome', 'Jackpot'], axis = 1)
df = df2.join(df)
df.columns = ['A', 'B', 'C', 'D', 'E', 'Bonus', 'Extra']

number_of_rows= df.values.shape[0] 
window_length = 5 
number_of_features = df.values.shape[1] 

X_train = pd.read_csv(str(Config.FEATURES_PATH / "train_features.csv"))
y_train = pd.read_csv(str(Config.FEATURES_PATH / "train_labels.csv"))

train = np.empty([number_of_rows-window_length, window_length, number_of_features], dtype=float)
label = np.empty([number_of_rows-window_length, number_of_features], dtype=float)

filename = 'euro-millions-ireland' 

if os.path.exists('../input/euromillion/'+filename+'.h5'):
    model = load_model('../input/euromillion/'+filename+'.h5')

else:
    model = Sequential()
    model.add(LSTM(32,      
               input_shape=(window_length, number_of_features),
               return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(32,           
               return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(number_of_features))
    model.compile(loss='mse', optimizer='rmsprop')
    model.fit(train, label,
          batch_size=64, epochs=100)
    model.save(Config.MODELS_PATH /"euromillion.h5")

# Enregisrement du model
pickle.dump(model, open(str(Config.MODELS_PATH / "model.pk"), mode='wb'))

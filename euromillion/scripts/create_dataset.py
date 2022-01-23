# Telecharger le dataset depuis un GDrive
# Pretraiter des données en de trainement et de test
# Enregistrer dans "assets/data"

from numpy.core.defchararray import index
from scipy.sparse.construct import rand
import gdown
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config import Config

# Set seed
np.random.seed(Config.RANDON_SEED)

# Creer les dossier dont on a besoin dans ce script
# ./assets/original_datasets & ./assets/data
Config.ROW_DATASET_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
Config.DATASET_PATH.mkdir(parents=True, exist_ok=True)

# Telecharge notre fichier
gdown.download(
    "https://drive.google.com/uc?id=1SnzyQOiGMOpOrL4QbVpKe3K1j6fzW4Yg",
    str(Config.ROW_DATASET_FILE_PATH)
)

# dataframe
df = pd.read_csv(str(Config.ROW_DATASET_FILE_PATH))

df2 = df['Winning Numbers'].str.split(" ",expand=True,)
df = df.drop(['Winning Numbers','Draw Date', 'Outcome', 'Jackpot'], axis = 1)
df = df2.join(df)
df.columns = ['A', 'B', 'C', 'D', 'E', 'Bonus', 'Extra']
df.to_csv(str(Config.DATASET_PATH / "df.csv"), index=None)

df_train, df_test = train_test_split(
    df, test_size=Config.TEST_SIZE, 
    random_state=Config.RANDON_SEED
)

df_train.to_csv(str(Config.DATASET_PATH / "train.csv"), index=None)
df_test.to_csv(str(Config.DATASET_PATH / "test.csv"), index=None)

scaler = StandardScaler().fit(df.values)
transformed_dataset = scaler.transform(df.values)
transformed_df = pd.DataFrame(data=transformed_dataset, index=df.index)


number_of_rows= df.values.shape[0] 
window_length = 5 
number_of_features = df.values.shape[1] 

train = np.empty([number_of_rows-window_length, window_length, number_of_features], dtype=float)
label = np.empty([number_of_rows-window_length, number_of_features], dtype=float)

for i in range(0, number_of_rows-window_length):
    train[i]=transformed_df.iloc[i:i+window_length, 0: number_of_features]
    label[i]=transformed_df.iloc[i+window_length: i+window_length+1, 0: number_of_features]

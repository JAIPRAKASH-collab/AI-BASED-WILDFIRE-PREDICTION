import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle

warnings.filterwarnings("ignore")

data = pd.read_csv("wildfire_edited.csv")
data=data.drop(['X','Y','month','day','area'],axis=1)

data = np.array(data)
X = data[:]
y = data[1:, -1]
y = y.astype('int')
X = X.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()

log_reg.fit(X_train, y_train)

pickle.dump(log_reg,open('ml.pkl','wb'))


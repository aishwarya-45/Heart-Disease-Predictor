import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import pickle
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import metrics

df = pd.read_csv(r'heart.csv')
x = df.iloc[:, :-1].values
y = df.iloc[:, 13].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=42)
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
classifier = KNeighborsClassifier(n_neighbors = 20)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
file=open('predictor.pkl', 'wb')
pickle.dump(classifier, file)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
prob=classifier.predict([[63,	1,	3	,145,	233,	1	,0,	150	,0,	2.3	,0,	0,	1	]])
file.close();

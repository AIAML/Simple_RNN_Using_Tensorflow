import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential

from keras.layers import Dense,SimpleRNN

import pandas as pd
import matplotlib.pyplot as plt

#Input sequence
input = np.array([[0.1],[0.2],[0.3],[0.4],[0.5],[0.6],[0.7],[0.8],[0.9],[1],[1.1],[1.2],[1.3],[1.4],[1.5]])

#Target sequence

target = np.array([[1.42],[1.68],[1.98],[2.32],[2.7],[3.12],[3.58],[4.08],[4.62],[5.2],[5.82],[6.48],[7.18],[7.92],[8.7]])

#RNN model

model = Sequential()

model.add(SimpleRNN(units=1,input_shape=(1,1)))
model.add(Dense(units=1,activation='linear'))

#Compile

model.compile(loss='mean_squared_error',optimizer='sgd')

#Train

history = model.fit(input,target, epochs=1000)

#Pridict

output = model.predict(input)

pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)  # set the vertical range to [0-1]
plt.show()

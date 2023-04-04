<h2> Simple RNN (Recurrent Neural Networks) Using Tensorflow </h2>

First,the following packages need to be inserted in your code
<p>
  <code>
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    from keras.models import Sequential
    from keras.layers import Dense,SimpleRNN
    import pandas as pd
    import matplotlib.pyplot as plt
  </code>
</p>
Next, the input data is generated.
<code>
  input = np.array([[0.1],[0.2],[0.3],[0.4],[0.5],[0.6],[0.7],[0.8],[0.9],[1],[1.1],[1.2],[1.3],[1.4],[1.5]])  
</code>
Then, we need our test dataset to be created. So go on and add the following code.
<code>
  target = np.array([[1.42],[1.68],[1.98],[2.32],[2.7],[3.12],[3.58],[4.08],[4.62],[5.2],[5.82],[6.48],[7.18],[7.92],[8.7]])
</code>  
<p>
After All, Our model is implemented using the code below. Then this model is compiled and ready to be predict.
</p>
<code>
  model = Sequential()
  model.add(SimpleRNN(units=1,input_shape=(1,1)))
  model.add(Dense(units=1,activation='linear'))
  model.compile(loss='mean_squared_error',optimizer='sgd')
</code>
<p>
After these steps, we need to deal with training and testing our model.
</p>
<code>
  history = model.fit(input,target, epochs=1000)
  output = model.predict(input)
  pd.DataFrame(history.history).plot(figsize=(8, 5))
  plt.grid(True)
  plt.gca().set_ylim(0, 1)  # set the vertical range to [0-1]
  plt.show()
</code>
<img src="https://github.com/AIAML/Simple_RNN_Using_Tensorflow/blob/main/test.jpg" width='80%'>

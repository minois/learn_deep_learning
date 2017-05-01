# coding:utf-8
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

# >>> x = np.array([-1.0, 1.0, 2.0])
# >>> sigmoid(x)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'sigmoid' is not defined
#
# >>> from sigmoid import sigmoid
# >>> sigmoid(x)
# array([ 0.26894142,  0.73105858,  0.88079708])

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

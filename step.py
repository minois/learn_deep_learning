# coding:utf-8
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
  y = x > 0
  return y.astype(np.int)

# >>> import numpy as np
# >>> x = np.array([-1.0, 1.0, 2.0])
# >>> x
# array([-1.,  1.,  2.])
# >>> y = x > 0
# >>> y
# array([False,  True,  True], dtype=bool)

# >>> y = y.astype(np.int)
# >>> y
# array([0, 1, 1])


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y軸の範囲指定
plt.show()


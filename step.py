# coding:utf-8
import numpy as np

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

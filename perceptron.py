# coding:utf-8
import numpy as np

# y = 0 (w1 * x1 + w2 * x2 <= θ
# y = 1 (w1 * x1 + w2 * x2 >   θ)

# def AND(x1, x2):
#   w1, w2, theta = 0.5, 0.5, 0.7
#   tmp = x1 * w1 + x2 * w2
#   if tmp <= theta:
#     return 0
#   elif tmp > theta:
#     return 1
# print AND(0, 0)


# y = 0 (b + w1 * x1 + w2 * x2 <= 0)
# y = 1 (b + w1 * x1 + w2 * x2 >   0)

def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b  = -0.7
  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  else:
    return 1
# memo:
#  ・-θ をバイアスbと命名
#  ・バイアスは重みのw1とw2とは別の働き
#  ・w1やw2は入力信号への重要度をコントロールするパラメータとして機能
#  ・バイアスは発火のしやすさ(出力信号が1を出力する度合い)を調整するパラメータとして機能
#  ・文脈によってはb, w1, w2のすべてのパラメータを指して「重み」と呼ぶことも

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 重みだけがANDと異なる
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
      return 0
    else:
      return 1

# y = 0 (-0.5 +  x1 + x2 <= 0)
# y = 1 (-0.5 +  x1 + x2 >   0)
# ・線形
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 重みとバイアスがANDと異なる
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
      return 0
    else:
      return 1

# y = 0 (-0.5 +  x1 + x2 <= 0)
# y = 1 (-0.5 +  x1 + x2 >   0)
# ・非線形
# ・「層を重ねる」ことで表現
# ・2層のパーセプトロン(多層パーセプトロン)
def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)
  return y

print XOR(0, 0)  # -> 0
print XOR(1, 0)  # -> 1
print XOR(0, 1)  # -> 1
print XOR(1, 1)  # -> 0

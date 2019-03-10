# 引入matplotlib的分模块pyplot
import matplotlib.pyplot as plt

import numpy as np

# 创建数据
x = np.linspace(-5, 5, 50)
y1 = 3 * x + 4
y2 = x ** 2
# 创建第一张图
plt.figure(num=1, figsize=(7, 6))
plt.plot(x, y1)
plt.plot(x, y2, color="red", linewidth=3.0, linestyle="--")

# 创建第二张图
plt.figure(num=2)
plt.plot(x, y2, color="green", linewidth=1)

# 显示图像
plt.show()

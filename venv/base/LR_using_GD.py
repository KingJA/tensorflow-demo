# 用梯度下降的优化方法来快速解决线性回归问题
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# 利用numpy的正态分布函数随机生成100个点，对应线性方程y=0.1*x+0.2
# 权重0.1，偏差0.2
pointNum = 100
vectors = []

for i in range(pointNum):
    x1 = np.random.normal(0.0, 0.66)
    y1 = 0.1 * x1 + 0.2 + np.random.normal(0.0, 0.04)
    vectors.append([x1, y1])

x_data = [v[0] for v in vectors]  # 坐标X值
y_data = [v[1] for v in vectors]  # 坐标y值

# 构建线性回归模型
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 初始化权重
b = tf.Variable(tf.zeros([1]))  # 初始化偏差 所有参数都为０的tensor对象
y = W * x_data + b



# 定义损失函数loss function 或代价函数 cost function
# 对Tensor的所有维度计算((y-y_data)^2)之和/N
loss = tf.reduce_mean(tf.square(y - y_data))  # reduce_mean某一维度的平均值
# 用梯度下降的优化器来优化我们的loss function
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 学习率0.5
train = optimizer.minimize(loss)
# 创建会话
sess = tf.Session()

# 初始化数据流图中的所有变量
init = tf.global_variables_initializer()
sess.run(init)
# print(sess.run(W))
# print(sess.run(b))
# print(sess.run(y))
# 训练20步

for step in range(20):
    # 优化每一步
    sess.run(train)
    # 打印每一步的损失，权重和偏差
    print("Step=%d, Loss=%f,[Weight=%f Bias=%f]" % (step, sess.run(loss), sess.run(W), sess.run(b)))
# 绘制所有的店并绘制出最佳拟合直线

# 打印图像 红色*
plt.plot(x_data, y_data, 'r*', label="Original data")
plt.title("Linear Regression using Gradient Descent")
plt.legend("legend")
plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
plt.xlabel("x")
plt.ylabel("y")
plt.show()
# 关闭对话
sess.close()

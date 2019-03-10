import tensorflow as tf

# 定义线性方程 y=W*x+b

# help(tf.Tensor) 查看文档

W = tf.Variable(2.0, dtype=tf.float32, name="KWeight")  # 权重
b = tf.Variable(1.0, dtype=tf.float32, name="KBias")  # 偏差
x = tf.placeholder(dtype=tf.float32, name="KInput")  # 输入

# 定义输出命名空间
with tf.name_scope("KOutput"):
    y = W * x + b

# 定义日志存放地址
logPath = ("E:/python/PycharmProjects/t1/venv/base/log")

# 初始化所有变量
init = tf.global_variables_initializer()

# 创建会话

with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter(logPath, sess.graph)
    result = sess.run(y, {x: 3.0})
    print("y=%s" % result)

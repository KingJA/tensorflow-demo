# 无视CPU警告
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 导入tensorflow
import tensorflow as tf

# 创建一个常量 operation (操作)
hw = tf.constant("Hello world")

# 创建会话
session = tf.Session()

# 运行会话

print(session.run(hw))

# 结束会话

session.close()

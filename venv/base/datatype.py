import tensorflow as tf

cons = tf.constant(3, name='c')
print(cons)

graph = cons.graph
print(graph)
print(tf.get_default_graph)
if graph is tf.get_default_graph:
    print(true)

var = tf.Variable(3)
print(var)

placeholder = tf.placeholder

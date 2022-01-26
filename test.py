import tensorflow as tf
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

tensor1 = tf.Variable([1,1], tf.int8)
tensor2 = tf.ones([2,3,3])

print(tf.rank(tensor1))
print(tensor2)
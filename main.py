import tensorflow as tf
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



train_set = pd.read_csv("datasets/titanic/train.csv")
eval_set = pd.read_csv("datasets/titanic/eval.csv")

y_train = train_set.pop("survived")
y_eval = eval_set.pop("survived")


CATEGORICAL_COLUMNS = ["sex", "n_siblings_spouses", "parch", "class", "deck",
                       "embark_town", "alone"]
NUMERIC_COLUMNS = ["age", "fare"]
feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = train_set[feature_name].unique()
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds
    return input_function


train_input_fn = make_input_fn(train_set, y_train)
eval_input_fn = make_input_fn(eval_set, y_eval, num_epochs=1, shuffle=False)

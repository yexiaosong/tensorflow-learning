#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tensorflow as tf

const = tf.constant(11)
# 此时const是<tf.Tensor 'Const:0' shape=() dtype=int32>, 可以使用Session run解析

var1 = tf.Variable(1, dtype=tf.int64)
# out:  <tf.Variable 'Variable_4:0' shape=() dtype=int64_ref>

var2 = tf.Variable([[1,2],[3,4]])
# out:  <tf.Variable 'Variable_5:0' shape=(2, 2) dtype=int32_ref>
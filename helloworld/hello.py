#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import tensorflow as tf

hw = tf.constant("hello")

sess = tf.Session()

res = sess.run(hw).decode('utf-8')
print(res)

sess.close()

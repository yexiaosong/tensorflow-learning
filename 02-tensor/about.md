## tensorflow 的基础模型
+ 数据模型 --- Tensor
+ 计算模型 --- Graph
+ 运行模型 --- Session

### Tensor
+ constant: tensorflow.const
此属性为tensorflow的常量

+ Variable: tensorflow.Variable
此属性为变量
var1 = tf.Variable(1, dtype=tf.int64)
var2 = tf.Variable([[1,2],[3,4]])

+ PlaceHolder

+ SparseTensor 稀疏矩阵，非零元素很少的矩阵
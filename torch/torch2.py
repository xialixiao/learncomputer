import torch
#二、pytorch的基本语法
x=torch.zeros([5,3],dtype=torch.long) #创建一个5行3列的全0张量，数据类型为long
print(x) #tensor([[0, 0, 0],
         #        [0, 0, 0], 
         #        [0, 0, 0],
         #        [0, 0, 0],
         #        [0, 0, 0]])
y=torch.rand([5,3]) #创建一个5行3列的随机张量，数据类型为long
#（1）.pytorch的加法操作
#加法运算1
print(x+y)
#tensor([[0.3158, 0.0653, 0.9775],
#        [0.1126, 0.2483, 0.5071],
#        [0.2261, 0.7334, 0.9107],
#        [0.1744, 0.4536, 0.0457],
#        [0.1709, 0.8529, 0.4970]])
#加法操作2
print(torch.add(x,y)) 
#tensor([[0.3158, 0.0653, 0.9775],
#        [0.1126, 0.2483, 0.5071],
#        [0.2261, 0.7334, 0.9107],
#        [0.1744, 0.4536, 0.0457],
#        [0.1709, 0.8529, 0.4970]])
#加法操作3
result=torch.empty([5,3]) #创建一个5行3列的空张量
torch.add(x,y,out=result) #将加法结果存储在result中
print(result) #tensor([[0.3158, 0.0653, 0.9775],
              #        [0.1126, 0.2483, 0.5071],
              #        [0.2261, 0.7334, 0.9107],
              #        [0.1744, 0.4536, 0.0457],
              #        [0.1709, 0.8529, 0.4970]])
#加法操作4
y.add_(x) #将x加到y上，结果存储在y中
print(y) #tensor([[0.3158, 0.0653, 0.9775],
         #        [0.1126, 0.2483, 0.5071],
         #        [0.2261, 0.7334, 0.9107],
         #        [0.1744, 0.4536, 0.0457],
         #        [0.1709, 0.8529, 0.4970]])
#注意：所有in-place操作函数都有一个下划线的后缀。比如x.copy_(y)将y的内容复制到x中，x.t_()将x转置。使用in-place操作会改变原始张量的内容，因此需要谨慎使用。
#（2）张量操作
print(x[:,1]) #索引操作，获取x的第2列
#tensor([0, 0, 0, 0, 0])
print(x[0,:]) #索引操作，获取x的第1行
#tensor([0, 0, 0])
print(x[0,0]) #索引操作，获取x的第1行第1列的元素
#tensor(0)
#（2.1）获取张量元素
x=torch.randn(1)#创建一个包含一个元素的随机张量，randn函数生成一个标准正态分布的随机数
print(x) #tensor([0.4334])
#item()方法可以获取张量中的单个元素的值，并返回一个Python数值类型
print(x.item()) #0.4333690106868744
#（2.2）张量的形状
x=torch.randn(4,4) #创建一个4行4列的随机张量
#view()方法可以改变张量的形状，但不改变其数据内容。它返回一个新的张量，具有相同的数据但不同的形状。
y=x.view(16) #将x的形状改变为16行1列的张量
z=x.view(-1,8) #将x的形状改变为2行8列的张量，-1表示自动计算该维度的大小
print(x.size()) #torch.Size([4, 4])
print(y.size()) #torch.Size([16])
print(z.size()) #torch.Size([2, 8])
#(3)Torch Tensor和Numpy array 互换
#Torch Tensor和Numpy array共享底层的内存空间，因此改变其中一个的值，另一个也会随之被改变。
a=torch.ones(5) #创建一个包含5个元素的全1张量
print(a) #tensor([1., 1., 1., 1., 1.])
#（3.1）将Torch Tensor转换为Numpy array
b=a.numpy() #将a转换为Numpy array
print(b) #[1. 1. 1. 1. 1.]
#（3.2）将Numpy array转换为Torch Tensor
import numpy as np
a=np.ones(5) #创建一个包含5个元素的全1的Numpy array
print(a) #[1. 1. 1. 1. 1.]
b=torch.from_numpy(a) #将a转换为Torch Tensor
print(b) #tensor([1., 1., 1., 1., 1.], dtype=torch.float64)
np.add(a,1,out=a) #将a中的每个元素加1，结果存储在a中
print(a) #[2. 2. 2. 2. 2.]
#注意：所有CPU上的Tensors，除了CharTensor之外，都支持与NumPy数组共享内存。也就是说，如果你将一个Torch Tensor转换为NumPy数组，或者将一个NumPy数组转换为Torch Tensor，那么它们将共享相同的内存空间。改变其中一个的值会影响另一个的值。
#(3.3)squeeze函数:squeeze函数可以去掉张量中所有维度为1的维度，返回一个新的张量。
x=torch.randn(1,2,1,28,1)#创建一个形状为(1,2,1,28,1)的随机张量
#使用squeeze函数去掉所有维度为1的维度
x.squeeze().shape #得到一个形状为(2,28)的张量
#torch.Size([2, 28])
#使用squeeze函数去掉第0维度
x.squeeze(dim=0).shape #，得到一个形状为(2,1,28,1)的张量
#使用squeeze加参数，如果不为1，则不变
x.squeeze(dim=1).shape #得到一个形状为(1,2,1,28,1)的张量
#torch.Size([1, 2, 1, 28, 1])
#既可以是函数，也可以是方法
torch.squeeze(x,-1).shape #得到一个形状为(1,2,1,28)的张量
#(3.4)unsqueeze函数:unsqueeze函数可以在指定位置插入一个维度为1的维度，返回一个新的张量。
x=torch.randn(2,28) #创建一个形状为(2,28)的随机张量
#使用unsqueeze函数在第0维度插入一个维度为1的维度
x.unsqueeze(dim=0).shape #得到一个形状为(1,2,28)的张量
#torch.Size([1, 2, 28])
#使用unsqueeze函数在第2维度插入一个维度为1的维度
x.unsqueeze(dim=2).shape #得到一个形状为(2,28,1)的张量
#torch.Size([2, 28, 1])
#既可以是函数，也可以是方法
torch.unsqueeze(x,0).shape #得到一个形状为(1,2,28)的张量
#torch.Size([1, 2, 28])
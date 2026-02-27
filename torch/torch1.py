import torch
#一、torch 入门
#(1).创建tensor张量
#Tensor张量：张量的概念类似于Numpy中的ndarray，是一种多维数组。张量可以在GPU上进行计算，这使得它非常适合深度学习任务。
x=torch.tensor([2.5,3.5])
print(x)  #tensor([2.5000, 3.5000])
print(x.dtype)  #torch.float32  他的默认数据类型是float32
print(x.shape)  #torch.Size([2]) 他的形状是2维的
#empty函数：创建一个未初始化的张量，张量中的值是随机的，取决于内存中的状态。
x=torch.empty(5,3) #创建一个5行3列的空张量
print(x)  #tensor([[1.4013e-45, 0.0000e+00, 0.0000e+00],
          #        [0.0000e+00, 0.0000e+00, 0.0000e+00],
          #        [0.0000e+00, 0.0000e+00, 0.0000e+00],
          #        [0.0000e+00, 0.0000e+00, 0.0000e+00],
          #        [0.0000e+00, 0.0000e+00, 0.0000e+00]])
#zeros函数：创建一个全0的张量，指定形状和数据类型。
x=torch.zeros(5,3,dtype=torch.long) #创建一个5行3列的全0张量，数据类型为long
print(x)  #tensor([[0, 0, 0],
          #        [0, 0, 0],
          #        [0, 0, 0],
          #        [0, 0, 0],
          #        [0, 0, 0]])

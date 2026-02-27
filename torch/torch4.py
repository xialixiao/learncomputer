#四、导入Imports
#(1)一般操作
#（1.1）根包
import torch
#(1.2)数据集表示和加载
from torch.utils.data import Dataset, DataLoader
#(2)Torchscript相关和JIT编译相关
torch.jit.trace()#使用你的模块和一些示例输入来跟踪模块的执行，并生成一个TorchScript模块。
torch.jit.script()#将你的模块转换为TorchScript模块，支持更复杂的控制流和Python特性。
@script #装饰器，用于将函数或类转换为TorchScript模块。
#(3)神经网络API
#计算图
import torch.autograd as autograd
#计算图中的张量节点
from torch import Tensor
#神经网络
import torch.nn as nn
#层、激活等
import torch.nn.functional as F
#优化器、例如梯度下降、ADAM等
import torch.optim as optim
#混合前端装饰和跟踪git
from torch.jit import script, trace
#(4)ONNX
torch.onnx.export(model,dummy data,xxx.proto)#将PyTorch模型导出为ONNX格式，其中model是要导出的模型，dummy data是一个示例输入张量，xxx.proto是导出的ONNX文件的路径。
#加载ONNX模型
nodel=onnx.load('alexnet.proto')#加载ONNX模型，其中'alexnet.proto'是要加载的ONNX文件的路径。
#检查模型，IT是否结构良好
onnx.checker.check_model(model)#其中model是要检查的ONNX模型。
#打印一个人类可读的图的表示
onnx.helper.printable_graph(model.graph)#其中model是要打印的ONNX模型。
#（5）Vision模型
#视觉数据集、架构&变换
from torchvision import datasets, models, transforms
#组合转换
import torchvision.transforms as T
#(6)分布式训练
#分布式通信
import torch.distributed as dist
#内存共享进城
import torch.multiprocessing as mp
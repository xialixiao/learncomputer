import torch
#三、Cuda相关
#（1）检查Cuda是否可用
import torch.cuda
torch.cuda.is_available() #检查当前系统是否支持CUDA
#如果系统支持CUDA，torch.cuda.is_available()将返回True，否则返回False。
#（2）获取当前CUDA设备的名称
torch.cuda.device_count() #返回当前系统中可用的CUDA设备数量
#（3）将模型、张量等数据在GPU和内存之间进项转移
device=f'cuda:0' #指定使用第0块GPU
#移动到GPU
tensor_m=torch.tensor([1,2,3]) #创建一个张量
tensor_g=tensor_m.to(device) #将张量移动到GPU上
model_m=torch.nn.Linear(1,1) #创建一个线性模型
model_g=model_m.to(device) #将模型移动到GPU上
#移动回CPU
tensor_m2=tensor_g.to('cpu') #将张量移动回CPU上
model_m2=model_g.to('cpu') #将模型移动回CPU上
#（4）列出GPU设备
device_count=torch.cuda.device_count() #返回当前系统中可用的CUDA设备数量
print("CUDA设备")
for i in range(device_count):
    device_name=torch.cuda.get_device_name(i) #获取第i块GPU的名称
    total_memory=torch.cuda.get_device_properties(i).total_memory #获取第i块GPU的总内存
    print(f"设备{i}: {device_name}, 内存: {total_memory/1e9:.2f} GB") #打印设备信息，内存单位为GB
print('结束')




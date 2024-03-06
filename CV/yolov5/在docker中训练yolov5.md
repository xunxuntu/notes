# 在 docker 中训练 yolov5




## 拉取yolov5 docker

```
# 版本自己选择
# 里面自带yolov5-6.1的全部工程文件
# https://hub.docker.com/r/ultralytics/yolov5/tags
sudo docker pull ultralytics/yolov5:v6.1
```



## 创建容器

```
# 守护式方式创建容器
docker run -itd --network=host --ipc=host --gpus all --name yolov5_docker -v /home/tuc/docker_yolov5:/usr/src/docker_yolov5 ultralytics/yolov5:v6.1
```



## 进入容器并查询相关信息

```
#  登录守护式容器
docker exec -it 容器名称 (或者容器ID)  /bin/bash

# 文件拷贝(将文件拷贝到容器内)(将文件从容器内拷贝出来)
docker cp 需要拷贝的文件或目录 容器名称:容器目录
docker cp 容器名称:容器目录 需要拷贝的文件或目录


# 打印环境变量
echo $LD_LIBRARY_PATH

# 查询本地安装的软件和程序
ls /usr/local/

# 显示NVIDIA CUDA 编译器（nvcc）的版本信息
nvcc -V

# 显示 conda 版本
conda -V

# 显示显卡驱动
nvidia-smi

# 显示python解释器, 演示 torch 可以调用 cuda
python
>>> import torch
>>> torch.cuda.is_available()
True
>>>

# 显示 python 第三方库
 pip list

```





https://blog.csdn.net/zhenz0729/article/details/135113577
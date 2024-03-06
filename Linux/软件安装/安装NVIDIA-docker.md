

# 先安装docker

https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

https://zhuanlan.zhihu.com/p/667743782

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# To install the latest version, run:
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



```
# 查看docker 版本
docker version

# 查看docker运行状态
sudo systemctl status docker

# 执行下面的命令会下载一个Docker测试镜像，并在容器中执行一个“hello-world”样例程序。
sudo docker run hello-world

# 如果你看到类似下方的输出，那么祝贺你，Docker能够正常运行在你的Ubuntu系统中了。
root@RTX4060Ti:/home/simple# sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete
Digest: sha256:d000bc569937abbe195e20322a0bde6b2922d805332fd6d8a68b19f524b7d21d
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

拓展

```
# 设置Docker服务在每次开机时自动启动
sudo systemctl enable docker

# 查看docker运行状态
systemctl status docker

# 启动Docker服务
sudo systemctl start docker
```

https://www.cnblogs.com/Can-daydayup/p/16472375.html





# 再安装 nvidia container toolkit

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt

- 前置条件：你得有一张显卡。
- 查看是否安装好：`docker`
- Nvidia Driver. [NVIDIA驱动官网](https://www.nvidia.cn/Download/index.aspx?lang=cn)。查看是否安装好：`nvidia-smi`
- 接下来安装`nvidia- container-toolkit`。

```
# 注意这是一条命令，直接全部复制即可
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

```
sudo apt-get update

sudo apt-get install -y nvidia-container-toolkit

# 重启一下docker
sudo systemctl restart docker

# 接下来你就可以愉快的使用nvidia-docker了
```





```
# 验证是否安装成功
sudo docker run --rm --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
或者
sudo docker run --gpus all nvidia/cuda:11.5.2-base-ubuntu20.04 nvidia-smi 

# 执行上面的命令，如果显示跟下面类似的内容，说明nvidia-docker2已经安装成功。
root@RTX4060Ti:/home/simple# sudo docker run --rm --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
Unable to find image 'nvidia/cuda:11.6.2-base-ubuntu20.04' locally
11.6.2-base-ubuntu20.04: Pulling from nvidia/cuda
96d54c3075c9: Pull complete
a3d20efe6db8: Pull complete
bfdf8ce43b67: Pull complete
ad14f66bfcf9: Pull complete
1056ff735c59: Pull complete
Digest: sha256:a0dd581afdbf82ea9887dd077aebf9723aba58b51ae89acb4c58b8705b74179b
Status: Downloaded newer image for nvidia/cuda:11.6.2-base-ubuntu20.04
Sun Feb 25 12:51:57 2024
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 Ti     Off |   00000000:01:00.0 Off |                  N/A |
|  0%   23C    P8              1W /  165W |      99MiB /  16380MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
+-----------------------------------------------------------------------------------------+
root@RTX4060Ti:/home/simple# docker images
REPOSITORY    TAG                       IMAGE ID       CREATED        SIZE
nvidia/cuda   11.6.2-base-ubuntu20.04   2098e65daccd   3 months ago   154MB
hello-world   latest                    d2c94e258dcb   9 months ago   13.3kB
root@RTX4060Ti:/home/simple# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
root@RTX4060Ti:/home/simple#
```




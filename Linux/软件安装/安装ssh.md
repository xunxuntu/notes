安装ssh
```
sudo apt update  # 更新包
sudo apt install openssh-server  # 安装openssh-server

# ubuntu重启ssh
service ssh restart

# 检查是否安装上
sudo systemctl status ssh

如果出现“active”是“running”，说明ssh服务启动了。
```



配置允许root远程ssh登录访问

```
sudo vim /etc/ssh/sshd_config

在最后添加 PermitRootLogin yes

# 重启 ssh
service sshd restart
```



拓展

```
# 查看ssh是否启动，有sshd说明已经启动
ps -e |grep ssh

sudo systemctl disable --now ssh  # 禁用服务
sudo systemctl enable --now ssh  # 启用服务
```


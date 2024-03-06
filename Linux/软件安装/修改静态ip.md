## Ubuntu20.04 修改静态ip

### Ubuntu22.04.4配置方法

```
按照老版本的配置方式会出现的问题：
WARNING：gateway4 has been deprecated, use default routes instead... 

解决方法：
按照如下的配置
# Let NetworkManager manage all devices on this system
network:
  ethernets:
    enp4s0:
      dhcp4: no
      addresses: [172.16.210.166/24]
      optional: true
      routes:
        - to: default
          via: 172.16.210.254

  version: 2
  renderer: NetworkManager
  
如果你是在root用户设置的，但是又会出现这个问题：
Permissions for /etc/netplan/01-network-manager-all.yaml  are too open. Netplan configuration should NOT be accessible by others.

原因：
这是由于你开放权限太高导致的。

解决方法：
chmod 0600 01-network-manager-all.yaml 


# https://blog.csdn.net/coward__123/article/details/134285762
# https://blog.csdn.net/yilovexing/article/details/126424086
```



### 老版本的Ubuntu配置方法（大约是22.04.3之前的版本）

```

# 修改配置文件，有可能不叫50-cloud-init.yaml这个名字
sudo vi /etc/netplan/50-cloud-init.yaml
network:
    ethernets:
        ens33:  # 有可能叫eno1
            dhcp4: no
            addresses: [192.168.1.100/24]  # /24 一定要带上
            optional: true
            gateway4: 192.168.1.1
 
    version: 2
    renderer: NetworkManager
    
 # 重启网络配置
 sudo netplan apply
 
 # 查看ip地址
 ip addr
 
# https://blog.csdn.net/Eazon_chan/article/details/110130881
```


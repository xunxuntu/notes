安装ubuntu时，系统让用户创建了一个非root用户，系统启动后使用这个用户，在需要执行超级用户权限的指令时，可以通过sudo来执行。

```
sudo passwd root
# 输入非root用户的密码
# 输入root密码
# 再次输入root密码
 su - root  # 切换到root用户下
 
 
 sudo su
 
```


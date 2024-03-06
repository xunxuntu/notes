# tmux常用命令

## 安装

```
# Ubuntu系统
sudo apt-get install tmux

# CentOS
$ sudo yum install tmux

# Mac
$ brew install tmux
```

## 常用操作指令及快捷键

```
# 查看有所有tmux会话
指  令：tmux ls
快捷键：Ctrl+b s

# 新建tmux窗口
指  令：tmux new -s <session-name>

# 重命名会话
指  令：tmux rename-session -t <old-name> <new-name>
快捷键：Ctrl+b $

# 分离会话
指  令：tmux detach  或者使用  exit(关闭窗口)
快捷键：Ctrl+b d

# 重新连接会话
指  令：tmux attach -t <session-name>  或者使用 tmux at -t <session-name>

#平铺当前窗格（个人很喜欢的快捷键，注意：平铺的是当前选中的窗格）
快捷键：Ctrl+b z (再次 Ctrl+b z 则恢复)

# 杀死会话
指  令：tmux kill-session -t <session-name>

# 切换会话
指  令：tmux switch -t <session-name>

# 划分上下两个窗格
指  令：tmux split
快捷键：Ctrl+b “

# 划分左右两个窗格
指  令：tmux split -h
快捷键：Ctrl+b %

# 光标切换到上方窗格
指  令：tmux select-pane -U
快捷键：Ctrl+b 方向键上

# 光标切换到下方窗格
指  令：tmux select-pane -D
快捷键：Ctrl+b 方向键下

# 光标切换到左边窗格
指  令：tmux select-pane -L
快捷键：Ctrl+b 方向键左

# 光标切换到右边窗格
指  令：tmux select-pane -R
快捷键：Ctrl+b 方向键右
```

## 查看会话历史输出信息

```
tmux a -t mysession

# 然后先按快捷键 ctrl+b ，松开后再按下 [ ，即进入历史输出信息查看模式，可通过键盘上的上下左右键来滚动历史输出信息, 也可以使用鼠标来查看，如果要退出查看模式，按下 q 即可。
```




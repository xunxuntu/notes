

# mv

https://cloud.tencent.com/developer/article/2147337



# lsof

```shell
# 查看端口占用情况
lsof -i:端口号

# lsof -i:8000
COMMAND   PID USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
nodejs  26993 root   10u  IPv4 37999514      0t0  TCP *:8000 (LISTEN)
```



# cp

```shell
# 一次性复制多个文件夹到另一个文件夹中
cp -r folder1 folder2 folder3 destination_folder/ 
```

# find

```shell
find / -name "libmyelin.so.1" 2>/dev/null

find: 这是一个用于在文件系统中搜索文件和目录的命令。它会遍历指定的路径以查找符合条件的文件或目录。

/: 此处表示从根目录开始进行搜索。也就是说，搜索将会从文件系统的最顶层目录开始，逐级深入。

-name "libmyelin.so.1": 这是一个用于指定搜索条件的参数。在这里，它指定了要搜索的文件名为 "libmyelin.so.1" 的文件。

2>/dev/null: 这是用于重定向标准错误输出的部分。在Linux中，标准输出通常是显示在屏幕上的内容，而标准错误通常用于显示错误信息。通过将标准错误重定向到 /dev/null，任何错误消息将会被丢弃，不会在屏幕上显示。
```

```shell
# 查看完整手册
man find

# 根据文件名查找
# 在指定目录及其子目录中查找文件
find /path/to/search -name "filename"

# 根据文件夹名查找
# 根据文件夹的名称查找包含特定文件夹名称的目录
find /path/to/search -type d -name "foldername"

# 组合查找条件
# 在特定目录中查找特定文件夹中的特定文件
find /path/to/search -type d -name "foldername" -exec find {} -type f -name "filename" \;

```

```shell
# 根据文件名查找文件的位置
find /start/search/from -type f -name "filename"

e.g. find /home/user/documents -type f -name "report.pdf"

```

- /start/search/from：将此路径替换为你要开始搜索的目录。搜索将从这个目录开始，并包括其所有子目录。
- type f：这指定了你要查找的是文件而不是目录。
- name "filename"：将 "filename" 替换为你要查找的实际文件名。

# zip

```shell
# 压缩一个文件夹成为ZIP文件
zip -r filename.zip foldername

# 解压到指定的文件夹中
unzip example.zip -d extracted_folder
- example.zip是要解压的zip文件
- extracted_folder是要解压到的目标文件夹
- --d选项指定了解压到的目标目录
```

# wc -l

```shell
# 查看一个txt文件中有多少行
wc -l trainval.txt

# 查看一个文件夹下有多少个文件
ls -l | wc -l
```

# tail

```shell
# 实时查看log.txt中的log
tail -f log.txt
```

# scp

```shell
# 从本地将文件传输到服务器
scp /Users/mac_pc/Desktop/test.png root@192.168.1.1:/root

# 从本地将文件夹传输到服务器
scp -r /Users/mac_pc/Desktop/test root@192.168.1.1:/root

# 将服务器上的文件传输到本地
scp root@192.168.1.1:/data/wwwroot/default/111.png /Users/mac_pc/Desktop

# 将服务器上的文件夹传输到本地
scp -r root@172.16.210.212:/home/tuc/yolov5-6.1/runs/detect/exp7 
```

#  df、du

```shell
# 查看硬盘的总空间
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT

# 查看根目录下硬盘空间
df -h /

# 查看家目录下的硬盘空间
df -h /home

# 查看当前文件夹下的
du -h --max-depth=1

-h: 使用人类可读的格式显示文件夹大小。
--max-depth=1: 限制查看的深度，这里设置为 1，只会显示当前文件夹下的子文件夹的大小，而不会深入到子文件夹的子文件夹。

# 查看当前文件夹下各文件的大小
du -h

# 查看文件夹的大小而不显示子文件夹和文件的细节
du -sh
e.g. du -sh my_yolov5_simplify
e.g. du -sh yolov5-6.1.zip
```

# tree

```
# 只查看当前目录下的文件夹
tree -d

# 查看当前目录下的文件夹和其子文件夹，不查看文件
tree -L 1
```



## Linux命令—查看历史，并显示操作时间

https://blog.csdn.net/ZZQHELLO2018/article/details/105115423

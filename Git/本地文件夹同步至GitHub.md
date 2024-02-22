# 使用Git将本地文件夹同步至github

【参考链接】https://blog.csdn.net/Sarah_LZ/article/details/119601673

## 一、操作过程【初次使用】

### Step 1 创建新仓库

在Github上创建一个Note 作为目标仓库。

### Step 2 初始化仓库

进入需要上传的本地文件夹所在的目录（我的目标文件夹为 E:\Test ），进入 Test  目录下，右键 git bash here ，使用`git init`进行仓库初始化。立即生成 .git 文件夹。

![image-20230519161430248](./assets/image-20230519161430248.png)

### Step 3 添加文件（将文件放入暂存区）

将当前目录下所有需要上传的文件代码等资源添加到缓存区

```
# 添加当前目录下的所有文件到缓存区：
git add .
```

`git add`其他命令

```
添加一个或多个文件到暂存区：：git add [file1] [file2]
添加指定目录到缓存区，包括子目录：git add [dir]
```

使用 **git status** 查看状态

![image-20230519162655511](./assets/image-20230519162655511.png)

### Step 4  提交文件提交到仓库

提交缓存区里面的主要内容到本地仓库, 设定注释信息，-m 后面的是提交说明与备注

```
git commit -m 'first commit'
```

在这一步可能会提醒设定git邮箱和用户名，那么就用一下命令输入你的注册邮箱和用户名；

```
# 配置好注册邮箱和用户名
git config --global user.email "xunxunxun.tu@gmail.com"
git config --global user.name "xunxuntu"
# 生成ssh key （git绑定的邮箱）
ssh-keygen -t rsa -C "xunxunxun.tu@gmail.com"
```

输入密码之后，连按几次 Enter 后成功的现象如下：

![image-20230519164051016](./assets/image-20230519164051016.png)

查看key ，根据上图中显示key生成的路径，复制一下；

```
# linux 下查看命令，Windows下则手动去 C:\Users\Simple\.ssh\id_rsa.pub 中复制
cat /Users/.../.ssh/id_rsa.pub
```

git上配置ssh key；

1. 点击个人头像进入 settings
2. 点击ssh and GPG keys
3. 新建一个ssh key

![image-20230519164721188](./assets/image-20230519164721188.png)

![image-20230519165255844](./assets/image-20230519165255844.png)

下图这样就成功了；

![image-20230519165346909](./assets/image-20230519165346909.png)

### Step 5 绑定远程仓库

在github仓库中获取ssh地址，复制。

![image-20230519170249547](./assets/image-20230519170249547.png)

绑定本地文件夹与远程仓库；

```
命令： git remote add <远端名称> <仓库路径>
远端名称， 默认是origin， 取决于远端服务器设置
仓库路径， 从远端服务器获取此url

git remote add origin https://github.com/xunxuntu/Test.git
```

`git remote` 查看远程仓库

```
git remote
```

![image-20230519170635358](./assets/image-20230519170635358.png)

再次 `commit` ；

![image-20230519171418253](./assets/image-20230519171418253.png)



### Step 6 推送到远程仓库

提交本地仓库到远程仓库,push；

```
git push -u origin master
因为第一次提交 所以要加一个 -u
```

若git的版本是 2.39.x 版本会出现下面的错误，并且一直卡在这里；

![image-20230519172649843](./assets/image-20230519172649843.png)

此时参考下面链接进行修正；我选择的是方法一：添加普通凭据；

https://blog.csdn.net/hkl_Forever/article/details/128510014

但是，此时又会出现下面的错误；

![image-20230519172830782](./assets/image-20230519172830782.png)

参考这个链接完成修正：https://blog.csdn.net/qq_41646249/article/details/119777084

再次进行 `git push -u origin master` 命令。

注意，这时候要关闭梯子，不然就报错，如下图。

![image-20230519200300867](./assets/image-20230519200300867.png)

这个不关闭梯子的解决方法，未尝试：https://blog.csdn.net/weixin_45683454/article/details/127219982

===========>>>>>>>> 至此，完全成功。

## 二、更新本地文件到GitHub

【已绑定仓库，不是首次将代码上传GitHub】将在本地更新后的代码上传到GitHub

【参考链接】https://blog.csdn.net/qq_46417852/article/details/127511616

https://blog.51cto.com/u_16113862/6279475

### 0、进入到目标文件夹

### 1、更改本地文件

### 2、在本地文件夹下右键git bash here

### 3、输入pwd确认位置

### 4、输入git add .

### 5、输入git commit -m 'update'

### 6、输入git push

### 7、打开GitHub查看是否成功

===========>>>>>>>> 至此，完全成功。

## 三、操作过程【二次使用】在新文件夹里链接新仓库

0、在目标文件夹下 `git init`

1、`git init`

2、`git add .`

3、`git commit -m 'first commit'`

4、`git remote add origin https://github.com/xunxuntu/Note.git`

5、`git branch -M main` // 将 master 改为 main

// 奇怪每次都要重新带上token

6、`git remote set-url origin https://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@github.com/xunxuntu/Note.git`

7、`git push -u origin main`

===========>>>>>>>> 至此，完全成功。

## github token:

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


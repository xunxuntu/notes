# Conda 环境迁移



https://zhuanlan.zhihu.com/p/87344422



在 **不同的平台和操作系统之间** 复现项目环境

**导出 `environment.yml` 文件：**

```
 conda env export > environment.yml
```

> 注意：如果当前路径已经有了 environment.yml 文件，conda 会重写这个文件

**重现环境：**

```
 conda env create -f environment.yml
```


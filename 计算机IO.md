# 学习资料
- [大话存储：存储系统底层架构原理极限剖析]

- 多路IO复用理解?
    - 传统bio模型, 一个连接建立成功就阻塞线程等待数据写入.这样浪费多个线程和等待时间.
    nio把等待的过程交给了操作系统epoll函数,epoll监听到连接可读可写后通知应用程序,就是这个样子.

- 零copy?
    - 理解了标准IO,直接IO,映射IO就会懂得零copy.

# reference
- [磁盘IO：缓存IO与直接IO](https://www.cnblogs.com/youngerchina/p/5624462.html)
- [IO多路复用详解](https://littlewhitejing.github.io/2018/04/24/os-1/)
- [我读过的最好的epoll讲解](https://zhuanlan.zhihu.com/p/36764771)
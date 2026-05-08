新版本的d2l包中没有`train_ch3()`, 降版本重新安装后可以正常运行
```shell
pip uninstall d2l
pip install d2l=0.17.0
```
> 最初按照书中说的安装0.17.6版本遇到了一些依赖兼容问题(numpy)，故直接安装了最新版本的d2l(1.0.3), 降级后暂未发现问题
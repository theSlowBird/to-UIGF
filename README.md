# Excel&JSON-to-UIGF
原神的祈愿分析，将非小酋导出的Excel格式文件、Genshin Wish Export的json格式文件合并，并转为UIGF的json格式以导入支持UIGF格式的抽卡分析软件中使用。

苦于找到的工具都已经过时，所以自己写了一个。由于不同的抽卡分析软件的支持的UIGF版本不同，目前只保证Hoyo.Gacha能导入成功。

## 使用方法
1. 修改`hparams.py`中的参数
2. 运行`to-UIGF.py`
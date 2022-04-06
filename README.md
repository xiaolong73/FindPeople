## 基于Yolov3和行人重识别的特定行人检索
##### Yolov3SPP + ReID

###文件目录结构
```text
├──── data: 用于存放要检测的图片或者视频
  │    ├── samples: 用于存放要检测的图片或者视频
  │ 
  ├── query: 用于存放要寻找的人的图片
  │ 
  ├── Yolov3SPP: 行人检测网络
  |
  ├── ReID: 行人重识别网络
  │  
  ├── search.py:将行人检测模型和行人重识别的网络结合，是该项目的main函数
```

#### 1. 行人检测部分
行人检测算法用的是YOloV3SPP

#### 2. 行人重识别部分
行人重识别算法用的是Reid-Strong-Baseline

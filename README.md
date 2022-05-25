## 基于Yolov3和行人重识别的特定行人检索
##### 主要网络结构： [Yolov3SPP](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/tree/master/pytorch_object_detection/yolov3_spp) + [ReID](https://github.com/michuanhaohao/reid-strong-baseline)

### 文件目录结构
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
行人检测算法用的是[Yolov3SPP](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/tree/master/pytorch_object_detection/yolov3_spp)

#### 2. 行人重识别部分
行人重识别算法用的是[Reid-Strong-Baseline](https://github.com/michuanhaohao/reid-strong-baseline)


### 如何运行
1. 将`market1501`数据集下载并解压放入到`/FindPeople/ReID/data`中;
2. 将`pascal voc2007`和`pascal voc2012`数据集下载并解压放入到`/FindPeople/Yolov3SPP/make_yolo_dataset`中;
   1. 在`/FindPeople/Yolov3SPP/make_yolo_dataset`中依次运行`python3 extra_person_voc_2007.py`,
   `python3 extra_person_voc_2012.py`,`python3 voc_label`.运行结束后生成这3个文件
      ```text
      2007_train.txt 
      2007_test.txt
      2012_train.txt
      ```
   2. 运行`merge_move.sh`:将`train.txt` 移动到`data`目录下，并改为`my_train_data.txt`,将`2007_test.txt`移动到`data`下并修改名字为`my_val_data.txt`
至此，数据集的准备工作已经完成。
3. 进入到`/FindPeople/Yolov3/`中运行`train.py`. 具体细节请看[Yolov3SPP](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/tree/master/pytorch_object_detection/yolov3_spp)
4. 进入到`/FindPeople/ReID/tools`中运行`train.py`. 具体细节请看[Reid-Strong-Baseline](https://github.com/michuanhaohao/reid-strong-baseline)
5. 将要检测的行人图片以market1501的命名格式放入到`/FindPeople/query`中，视频或者图片放入到`/FindPeople/data/samples`中
6. 运行`/FindPeople/search.py`.
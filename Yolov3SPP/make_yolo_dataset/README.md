### 提取VOC2007和VOC2012行人数据集

#### 步骤：
1. 下载VOC2007和VOC2012数据集并解压
2. 依次运行`python3 extra_person_voc_2007.py`,
`python3 extra_person_voc_2012.py`,`python3 voc_label`.运行结束后生成这3个文件
```text
2007_train.txt 
2007_test.txt
2012_train.txt
```
合并训练集文本`cat 2007_train.txt 2012_train.txt > train.txt`
3. 运行`merge_move.sh`:将`train.txt` 移动到`data`目录下，并改为`my_train_data.txt`,将`2007_test.txt`移动到`data`下并修改名字为`my_val_data.txt`
至此，数据集的准备工作已经完成。
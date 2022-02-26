#!/bin/bash
cat 2007_train.txt 2012_train.txt > train.txt
mv train.txt ../data/my_train_data.txt
mv 2007_test.txt ../data/my_val_data.txt
rm 20* 
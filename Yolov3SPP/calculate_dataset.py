"""
该脚本功能：
根据yolov3-spp.cfg创建my_yolov3.cfg文件修改其中的predictor filters以及yolo classes参数(这两个参数是根据类别数改变的)
"""
import os


classes_label = "./data/my_data_label.names"
cfg_path = "./cfg/yolov3-spp.cfg"


assert os.path.exists(classes_label), "classes_label not exist!"
assert os.path.exists(cfg_path), "cfg_path not exist!"


def change_and_create_cfg_file(classes_info, save_cfg_path="./cfg/my_yolov3.cfg"):
    # create my_yolov3.cfg file changed predictor filters and yolo classes param.
    # this operation only deal with yolov3-spp.cfg
    filters_lines = [636, 722, 809]
    classes_lines = [643, 729, 816]
    cfg_lines = open(cfg_path, "r").readlines()

    for i in filters_lines:
        assert "filters" in cfg_lines[i-1], "filters param is not in line:{}".format(i-1)
        output_num = (5 + len(classes_info)) * 3
        cfg_lines[i-1] = "filters={}\n".format(output_num)

    for i in classes_lines:
        assert "classes" in cfg_lines[i-1], "classes param is not in line:{}".format(i-1)
        cfg_lines[i-1] = "classes={}\n".format(len(classes_info))

    with open(save_cfg_path, "w") as w:
        w.writelines(cfg_lines)


def main():
    classes_info = [line.strip() for line in open(classes_label, "r").readlines() if len(line.strip()) > 0]

    # 根据yolov3-spp.cfg创建my_yolov3.cfg文件修改其中的predictor filters以及yolo classes参数(这两个参数是根据类别数改变的)
    change_and_create_cfg_file(classes_info)


if __name__ == '__main__':
    main()
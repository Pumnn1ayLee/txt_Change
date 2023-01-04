# txt_Change

need_path:是你需要转化的文件夹目录
nano_path:是你需要转化输出的文件夹目录

该代码尝试将像素点坐标进行归一化处理并转化成Yolov5格式的坐标
即例如将：
6.0 492.0 22.0 452.0 174.0 512.0 56.0 512.0 ship 2
转换成:
0 x_center y_center w h

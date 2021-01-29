# 这是什么？
利用OCR、OpenCV识别、提取视频字幕


# 做了什么
从视频提取硬字幕要做以下事情：

## 1、视频切割
把视频切成若干张包含字幕的静态图片（默认每秒1张）。应在考虑调用成本的前提下尽量细切，保证字幕都切到。

## 2、图片OCR
京东OCR能返回识别的文字、对应坐标和可信度，筛选可信度。

## 3、去重
去重有两个目的：

一是防止结果重复

二是能把固定位置的文字收敛（比如台标），避免字幕定位错误。

## 4、字幕定位
每张图可能识别出若干组文字（每组都有位置信息），在获得所有切图的OCR结果后，我们需要确定哪些是字幕的内容。

这里有两个假设：
1. 字幕的纵向位置基本不变
2. 字幕是整个视频中同一位置不同内容文字量最大的部分

有这两个假设之后：
1. 把top相近的识别结果分成一组
2. 去重后字幕量最大的就是字幕组


# 使用指南
## 环境
Python 3.x，Python 2.x 的许多语法和 3.x 不一样，无法使用

OpenCV，pip install opencv-python

## 获取代码
方法一：git clone https://github.com/if1y/jd-video-subtitle-recoginze.git

方法二：右上角 - clone or download - download zip

## 申请京东OCR
https://neuhub.jd.com/ai/api/ocr/general

在京东AI开放平台注册，创建通用文字识别应用得到 APP_KEY 、 SECRET_KEY ，就可以用了。

每天免费调用50000次，QPS是2。

## 配置
修改 config.py 文件在 'APP_KEY' 、 'SECRET_KEY' 后填写自己的 APP_KEY 、 SECRET_KEY

参数说明：

split_duration 默认1 视频切片频率，字幕密度低的情况下可以调至2，提高效率

jpg_quality 默认40 改变图片质量，在保证字幕清晰的情况下减小质量可以提高网络效率，但太小可能频繁触发QPS限制

probability 默认0.66 OCR返回的可信度的下限，可信度低于此下限的识别结果会被废弃，根据需要可适当放宽

## 执行
创建 video 文件夹，把视频文件放进去。

执行 index.py

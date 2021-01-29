# -*- coding: UTF-8 -*-

import cv2
import os
import config


def main(video_name, video_suffix):
    conf = config.get_config(video_name, video_suffix)
    video_path = conf['video_path']
    image_dir = conf['image_dir']
    jpg_quality = conf['jpg_quality']

    if not(os.path.exists(image_dir)):
        os.mkdir(image_dir)

    cv = cv2.VideoCapture(video_path)  # 读入视频文件
    current_frame = 1
    saved_frames = 1
    
    if cv.isOpened():  # 判断是否正常打开
        retval, frame = cv.read()
    else:
        cv.release()
        print("Video open error")
        return False

    duration = int(cv.get(5) * conf['split_duration'])  # 间隔频率 = 帧率 * 切片时间间隔(四舍五入)
    frame_count = int(cv.get(cv2.CAP_PROP_FRAME_COUNT))

    while retval:   # 循环读取视频帧
        retval, frame = cv.read()

        if current_frame % duration == 0:  # 每 duration 帧进行存储操作
            cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])[1].\
                tofile(image_dir + str(current_frame).zfill(6) + '.jpg')
            print(("Now: frame %d, saved: %d frame(s), process: %d%%" %
                   (current_frame, saved_frames, (current_frame * 100) // frame_count)).ljust(60, ' '), end='\r')
            saved_frames += 1

        current_frame += 1
        cv2.waitKey(1)

    print(("Now: frame %d, saved: %d frame(s), process: %d%%" %
           (current_frame, saved_frames, (current_frame * 100) // frame_count)).ljust(60, ' '), end='\r')
    cv.release()
    print("\nSaved: %d frame(s)" % saved_frames)
    return True

# -*- coding: UTF-8 -*-


def get_config(video_name, video_suffix):
    return {
        'APP_KEY': '282ec2d6c6754b27f010f4d8ee241629',  # 修改为你的 APP_KEY
        'SECRET_KEY': 'aed9fafcd6a77e8ed2ab3786055bb120',  # 修改为你的 SECRET_KEY
        'video_path': 'video\\%s%s' % (video_name, video_suffix),
        'image_dir': 'video_frames\\%s\\' % video_name,
        'output_dir': 'output\\',
        'split_duration': 1,  # 切片间隔，每 split_duration 秒输出一帧
        'jpg_quality': 40,  # 图片输出质量，0~100
        'probability': 0.66  # OCR可信度下限
    }

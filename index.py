# -*- coding: UTF-8 -*-

import os
import time
import getframe
import getsubtitle


def main():
    if not(os.path.exists("video")):
        os.mkdir("video")

    if not(os.path.exists("video_frames")):
        os.mkdir("video_frames")

    if not(os.path.exists("output")):
        os.mkdir("output")

    video_name = ""
    video_suffix = ""

    while True:
        os.system("cls")
        print("----------Select Video----------")
        video_list = os.listdir("video")

        if len(video_list) < 1:
            print("Nothing found\n\n")
            print("Process finished")
            input()
            return

        for video in video_list:
            print("%d.%s" % (video_list.index(video) + 1, video))

        try:
            index = int(input("\nInput index: "))
        except ValueError:
            continue

        if 0 < index <= len(video_list):
            video_name = video_list[index - 1][: video_list[index - 1].rfind(".")]
            video_suffix = video_list[index - 1][video_list[index - 1].rfind("."):]
            break

    start = time.time()
    print("\n----------Video Division----------")
    print("Start video division")

    if not getframe.main(video_name, video_suffix):
        print("Video division FAILED!")
        print("Process finished")
        input()
        return

    print("Video division finished")
    print("Time: %.2fs\n" % (time.time() - start))

    start2 = time.time()
    print("----------Subtitle Analysis----------")
    print("Start subtitle analysis")

    if not getsubtitle.main(video_name, video_suffix):
        print("\nSubtitle analysis FAILED!")
    else:
        print("\nSubtitle analysis finished")

    print("Time: %.2fs\n" % (time.time() - start2))

    print("Process finished")
    print("Time: %.2fs" % (time.time() - start))
    input()
    return


main()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import os
from PIL import Image
 
# """
# 将视频转为音频
# :param file_name: 传入视频文件的路径
# :return:
# """
def video2mp3(file_name):
    outfile_name = file_name.split('.')[0] + '.mp3'
    cmd = 'ffmpeg -i ' + file_name + ' -f mp3 ' + outfile_name
    subprocess.call(cmd, shell=True)
    return

# """
# 视频添加音频
# :param file_name: 传入视频文件的路径
# :param mp3_file: 传入音频文件的路径
# :return:
# """
def video_add_mp3(file_name, mp3_file):
    outfile_name = file_name.split('.')[0] + '-f.mp4'
    subprocess.call('ffmpeg -i ' + file_name + ' -i ' + mp3_file + ' -strict -2 -f mp4 ' + outfile_name, shell=True)
    return

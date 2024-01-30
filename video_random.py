#!/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import os.path
import hashlib
import random
import time

current_path_base = file_path_base = os.path.dirname(os.path.abspath(__file__))
target_folder = "飞书20240129-221111/2024.1.29男孩女孩成长启蒙书1/音频+素材1/素材"
target_folder_children = ["开头（结尾）","开业（结尾）","内容","翻书","视频集","细节","合书"]

audio_target_folder = "%s/飞书20240129-221111/2024.1.29男孩女孩成长启蒙书1/音频+素材1/音频/2023-11-03 154534.mov"%current_path_base


create_num = 5
speed = "0.75"

for video_need in range(0,create_num):
    video_list = []
    for target_folder_child in target_folder_children:
        file_list_dir_path = "%s/%s/%s"%(current_path_base,target_folder,target_folder_child)
        try:
            file_list_dir=os.listdir(file_list_dir_path)
        except Exception as e:
            file_list_dir = None
        if not file_list_dir:
            continue
        random_int = random.randint(0, len(file_list_dir)-1)
        # print("%s/%s"%(random_int,len(file_list_dir)),file_list_dir)
        video_list_item_path = "\"%s/%s\""%(file_list_dir_path,file_list_dir[random_int])
        video_list.append(video_list_item_path)
    print(video_list)

    current_video_name = "video_%s"%(int(time.time()))
    cmd_i_video = ""
    cmd_va = ""
    cmd_va_num = 0
    for video_item in video_list:
        cmd_i_video = "%s -i %s"%(cmd_i_video,video_item)
        cmd_va = "%s[%s:v:0][%s:a:0]"%(cmd_va,cmd_va_num,cmd_va_num)
        cmd_va_num+=1
    cmd = "ffmpeg%s -an -filter_complex \"%sconcat=n=%s:v=1:a=1[outv][outa]\" -map \"[outv]\" -map \"[outa]\" %s.mp4"%(cmd_i_video,cmd_va,cmd_va_num,current_video_name)
    print(cmd)
    os.system(cmd)
    cmd1 = "ffmpeg -i %s.mp4 -an -r 30 -filter:v \"setpts=%s*PTS\" -c:a copy speed_%s.mp4"%(current_video_name,speed,current_video_name)
    print(cmd1)
    os.system(cmd1)
    cmd2 = "ffmpeg -i speed_%s.mp4 -i \"%s\" -c:v copy -map 0:v:0 -map 1:a:0 speed_audio_%s.mp4"%(current_video_name,audio_target_folder,current_video_name)
    print(cmd2)
    os.system(cmd2)
# coding=gbk
import ctypes, sys
import os
import time
import ffmpeg
import requests
import re
import json
import shutil
import subprocess

def admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if admin():#����Աִ��
    print("************************************************************")
    print("************************************************************")
    print("����ĿΪ��Դ��Ŀ��δ����������������ҵ��;")
    print("���ߣ�Li Jiashu")
    print("��Ŀ����GitHub��Դ���ֿ�����:https://github.com/cescofz/bilibili-analysis")
    print("ffmpeg�ϳ�����Ƶ���ܿ�����")
    print("************************************************************")
    print("************************************************************")
    # current_directory = os.getcwd()
    # print(current_directory)
    # ffmpeg_lib = f"{current_directory}" + "\\" + "ffmpeg\\bin"
    # path = f"setx PATH" + ' "' + "%PATH%;" + ffmpeg_lib + '" '
    # system_path_str = os.environ["Path"]
    # if ffmpeg_lib in system_path_str:
    #     pass
    #     print("����ffmpeg��������")
    # else:
    #     os.system(path)
    #     print("�����ffmpeg��������")
    print("**********************")
    print("**********************")
    print("********0���˳�*******")
    print("********1����ʼ*******")
    print("**********************")
    print("**********************")
    a = int(input("����:"))
    if a == 1:
        def my_match(text, pattern):
            match = re.search(pattern, text)
            print(match.group(1))
            print()
            return json.loads(match.group(1))
        def download_video(old_video_url, video_url, audio_url, video_name):
            headers.update({"Referer": old_video_url})
            print("��ʼ������Ƶ,�ٶȺ������йأ�%s" % video_name)
            video_content = requests.get(video_url, headers=headers)
            print('%s��Ƶ��С��' % video_name, video_content.headers['content-length'])
            audio_content = requests.get(audio_url, headers=headers)
            print('%s��Ƶ��С��' % video_name, audio_content.headers['content-length'])
            received_video = 0
            with open('%s_video.mp4' % video_name, 'ab') as output:
                while int(video_content.headers['content-length']) > received_video:
                    headers['Range'] = 'bytes=' + str(received_video) + '-'
                    response = requests.get(video_url, headers=headers)
                    output.write(response.content)
                    received_video += len(response.content)
            audio_content = requests.get(audio_url, headers=headers)
            received_audio = 0
            # video_path = current_directory+"\\"+video_name+"_video.mp4"
            # audio_path = current_directory+"\\"+video_name+"_audio.mp3"
            with open('%s_audio.mp4' % video_name, 'ab') as output:
                while int(audio_content.headers['content-length']) > received_audio:
                    headers['Range'] = 'bytes=' + str(received_audio) + '-'
                    response = requests.get(audio_url, headers=headers)
                    output.write(response.content)
                    received_audio += len(response.content)
            #ִ��FFMPEG����
            # ffmpeg_commend = f"ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a aac -strict experimental �ϳ�{video_name}.mp4"
            # os.system(ffmpeg_commend)
            # output_video = f"�ϳ� {video_name}.mp4"
            # ffmpeg.input(video_path).audio_path.addinput(ffmpeg.input(audio_path)).output(output_video).run()
            #FFMPEG����
            # current_directory_file = os.listdir()
            # for file_name in current_directory_file:
            #     if file_name == f"�ϳ�{video_name}.mp4":
            #         del_video_commend = video_name+"_video.mp4"
            #         del_audio_commend = video_name+"_audio.mp3"
            #         os.remove(del_video_commend)
            #         os.remove(del_audio_commend)
    else:
        exit()
    while True:
        if __name__ == '__main__':
            url = str(input("������Ƶ��ַ��"))
            headers = {
                "Referer": "https://www.bilibili.com",
                "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }
            res = requests.get(url, headers=headers)
            print(res.text)
            playinfo = my_match(res.text, '__playinfo__=(.*?)</script><script>')
            initial_state = my_match(res.text, r'__INITIAL_STATE__=(.*?);\(function\(\)')
            video_url = playinfo['data']['dash']['video'][0]['baseUrl']
            audio_url = playinfo['data']['dash']['audio'][0]['baseUrl']
            video_name = initial_state['videoData']['title']
            print('��Ƶ����Ϊ��', video_name)
            print('��Ƶ��ַΪ��', video_url)
            print('��Ƶ��ַΪ��', audio_url)
            download_video(url, video_url, audio_url, video_name)
            print("��ɣ�")
else:
    # ���»�ȡ����ԱȨ��ִ��
	ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)


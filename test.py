import ctypes, sys
import os
import requests
import re
import json
def admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if admin():#管理员执行
    current_directory = os.path.dirname(__file__)
    ffmpeg_lib = f"{current_directory}" + "\\" + "ffmpeg\\bin"
    path = f"setx PATH" + ' "' + "%PATH%;" + ffmpeg_lib + '" '
    system_path_str = os.environ["Path"]
    if ffmpeg_lib in system_path_str:
        pass
        print("已有ffmpeg环境变量")
    else:
        os.system(path)
        print("已添加ffmpeg环境变量")
    print("**********************")
    print("**********************")
    print("********0、退出*******")
    print("********1、开始*******")
    print("**********************")
    print("**********************")
    a = int(input("输入:"))
    if a == 1:
        def my_match(text, pattern):
            match = re.search(pattern, text)
            print(match.group(1))
            print()
            return json.loads(match.group(1))
        def download_video(old_video_url, video_url, audio_url, video_name):
            headers.update({"Referer": old_video_url})
            print("开始下载视频,速度和网速有关：%s" % video_name)
            video_content = requests.get(video_url, headers=headers)
            print('%s视频大小：' % video_name, video_content.headers['content-length'])
            audio_content = requests.get(audio_url, headers=headers)
            print('%s音频大小：' % video_name, audio_content.headers['content-length'])
            received_video = 0
            with open('%s_video.mp4' % video_name, 'ab') as output:
                while int(video_content.headers['content-length']) > received_video:
                    headers['Range'] = 'bytes=' + str(received_video) + '-'
                    response = requests.get(video_url, headers=headers)
                    output.write(response.content)
                    received_video += len(response.content)
            audio_content = requests.get(audio_url, headers=headers)
            received_audio = 0
            video_path = current_directory+"\\"+video_name+"_video.mp4"
            audio_path = current_directory+"\\"+video_name+"_audio.mp3"
            with open('%s_audio.mp3' % video_name, 'ab') as output:
                while int(audio_content.headers['content-length']) > received_audio:
                    headers['Range'] = 'bytes=' + str(received_audio) + '-'
                    response = requests.get(audio_url, headers=headers)
                    output.write(response.content)
                    received_audio += len(response.content)
            ffmpeg_commend = f"ffmpeg -i {video_path} -i {audio_path} -c:v copy -c:a aac -strict experimental 合成{video_name}.mp4"
            os.system(ffmpeg_commend)
            del_video_commend = video_name+"_video.mp4"
            del_audio_commend = video_name+"_audio.mp3"
            os.remove(del_video_commend)
            os.remove(del_audio_commend)
    else:
        exit()
    while True:
        if __name__ == '__main__':
            url = str(input("键入视频网址："))
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
            print('视频名字为：', video_name)
            print('视频地址为：', video_url)
            print('音频地址为：', audio_url)
            download_video(url, video_url, audio_url, video_name)
            print("完成！")
else:
    # 重新获取管理员权限执行
	ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)


import requests

url1 = 'https://v3-webf.douyinvod.com/b6ba3f2cfd9a129fa7ff0421850ab6a2/6767dae8/video/tos/cn/tos-cn-ve-15c000-ce/ogrAFCiNRWBBeqwpDa20iGZEfyeQRzEAqdIINr/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1940&bt=1940&cs=0&ds=4&ft=hJILWM6xxoucL.H5PN12lMg4-iGNbLAr1f1U_4jUG94JNv7TGW&mime_type=video_mp4&qs=0&rc=O2U4O2RoPDU2OWY7Ozc0NkBpajxxNmw5cjd0dzMzbGkzNEBeNGMtNmI0Xl4xMzEuY14wYSMvNl9hMmRjMGBgLS1kLWJzcw%3D%3D&btag=80000e00008000&dy_q=1734848689&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2024122214244966C7AC459ED2EEF32DE4'
url2 = 'https://v26-web.douyinvod.com/8fdd5ff530d6ab83cbe5c0ffe07261d4/6767dae8/video/tos/cn/tos-cn-ve-15c000-ce/ogrAFCiNRWBBeqwpDa20iGZEfyeQRzEAqdIINr/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1940&bt=1940&cs=0&ds=4&ft=hJILWM6xxoucL.H5PN12lMg4-iGNbLAr1f1U_4jUG94JNv7TGW&mime_type=video_mp4&qs=0&rc=O2U4O2RoPDU2OWY7Ozc0NkBpajxxNmw5cjd0dzMzbGkzNEBeNGMtNmI0Xl4xMzEuY14wYSMvNl9hMmRjMGBgLS1kLWJzcw%3D%3D&btag=80000e00008000&dy_q=1734848689&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2024122214244966C7AC459ED2EEF32DE4'
url3 = 'https://www.douyin.com/aweme/v1/play/?video_id=v1e00fgi0000ctcq34fog65id3bn992g&line=0&file_id=33a1f418486c46a3a279ee9a08f57ba8&sign=ecadbd882f4eab00a9984c4dbf8833a5&is_play_url=1&source=PackSourceEnum_PUBLISH'
url = 'https://v3-webf.douyinvod.com/505fb361739fdb4499fe486623a18e1b/6767d877/video/tos/cn/tos-cn-ve-15c000-ce/oov73icEAhAkiOigKDPxJZMZx6L2IGRXyBGQD/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=776&bt=776&cs=2&ds=3&ft=hJILWM6xxoucL.H5PN12lMg4-iGNbL4EVf1U_4jUG94JNv7TGW&mime_type=video_mp4&qs=15&rc=Ojo7ZjNpNjY4aDNpOGllOUBpMzZ1ZnQ5cjU0dzMzbGkzNEA1NTIzLi1fXmIxYTExNTVhYSMyMTVkMmRrbWZgLS1kLWJzcw%3D%3D&btag=c0000e00008000&cquery=101r_100B_100x_100z_100o&dy_q=1734848064&feature_id=0b1897f6f4d4a76c1fe37e67bccd4222&l=202412221414247ABA37D2CA2BED0113C7&__vid=7450111499760127289'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'referer': 'https://www.douyin.com/'
}

with open('test1.mp4', mode='wb') as file:
    response = requests.get(url1, headers=headers)
    file.write(response.content)

with open('test2.mp4', mode='wb') as file:
    response = requests.get(url2, headers=headers)
    file.write(response.content)

with open('test3.mp4', mode='wb') as file:
    response = requests.get(url, headers=headers)
    file.write(response.content)

'''
0
: 
"https://v3-webf.douyinvod.com/b6ba3f2cfd9a129fa7ff0421850ab6a2/6767dae8/video/tos/cn/tos-cn-ve-15c000-ce/ogrAFCiNRWBBeqwpDa20iGZEfyeQRzEAqdIINr/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1940&bt=1940&cs=0&ds=4&ft=hJILWM6xxoucL.H5PN12lMg4-iGNbLAr1f1U_4jUG94JNv7TGW&mime_type=video_mp4&qs=0&rc=O2U4O2RoPDU2OWY7Ozc0NkBpajxxNmw5cjd0dzMzbGkzNEBeNGMtNmI0Xl4xMzEuY14wYSMvNl9hMmRjMGBgLS1kLWJzcw%3D%3D&btag=80000e00008000&dy_q=1734848689&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2024122214244966C7AC459ED2EEF32DE4"
1
: 
"https://v26-web.douyinvod.com/8fdd5ff530d6ab83cbe5c0ffe07261d4/6767dae8/video/tos/cn/tos-cn-ve-15c000-ce/ogrAFCiNRWBBeqwpDa20iGZEfyeQRzEAqdIINr/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1940&bt=1940&cs=0&ds=4&ft=hJILWM6xxoucL.H5PN12lMg4-iGNbLAr1f1U_4jUG94JNv7TGW&mime_type=video_mp4&qs=0&rc=O2U4O2RoPDU2OWY7Ozc0NkBpajxxNmw5cjd0dzMzbGkzNEBeNGMtNmI0Xl4xMzEuY14wYSMvNl9hMmRjMGBgLS1kLWJzcw%3D%3D&btag=80000e00008000&dy_q=1734848689&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2024122214244966C7AC459ED2EEF32DE4"
2
: 
"https://www.douyin.com/aweme/v1/play/?video_id=v1e00fgi0000ctcq34fog65id3bn992g&line=0&file_id=33a1f418486c46a3a279ee9a08f57ba8&sign=ecadbd882f4eab00a9984c4dbf8833a5&is_play_url=1&source=PackSourceEnum_PUBLISH"
width
: 
1080
'''
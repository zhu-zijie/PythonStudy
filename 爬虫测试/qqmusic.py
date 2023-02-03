'''
qq音乐
2022.05.07
by不相交直线
'''

# -*- coding: utf-8 -*-
import json
import requests
import re
import execjs

# 请求头
headers = {
    'cookie': 'pgv_pvid=2327409999; RK=RB0V1aVE8j; ptcz=d712618ae01282f0f43c38751fbf333d118fb2a9a9a7627c825386e5c3cdae43; fqm_pvqid=536434c1-2ab2-44b1-87b0-a7d9c95f4f50; ts_uid=6715541618; tmeLoginType=2; psrf_access_token_expiresAt=1659617280; euin=oK4PoKozowvk; fqm_sessionid=7267668e-691d-49d3-9c7b-792c8509752a; pgv_info=ssid=s9648679293; ts_refer=www.baidu.com/; ts_last=y.qq.com/n/ryqq/player',
    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

def show(text):
    # 正则预加载
    resp_compile = re.compile('callback\((.*)\)', re.S)
    response = re.findall(resp_compile, text)[0]
    # 保存在data文件夹里
    # with open('data.json','w', encoding='utf-8') as f:
    #     f.write(response)
    response_json = json.loads(response)
    lists = response_json['data']['song']['list']
    t_ple = '{:<10}{:<10}{:<10}'
    print(t_ple.format('序号', '歌手', '歌名'))
    num = 1
    song_list = []
    for list in lists:
        albummid = list['albummid']
        songmid = list['songmid']
        songname = list['songname']
        singer = list['singer'][0]['name']
        song = {
            "num": num,
            "songmid": songmid,
            "songname": songname,
            "singer": singer,
            "albummid": albummid
        }
        print(t_ple.format(num, singer, songname))
        song_list.append(song)
        num += 1
    return song_list


def get_sign(data):
    with open('get_sign.js', mode='r', encoding='utf-8') as f:
        text = f.read()

    js_data = execjs.compile(text)
    sign = js_data.call('get_sign', data)
    return sign

def download(list):
    url = 'https://u.y.qq.com/cgi-bin/musics.fcg?_=1651994036293&sign='
    song_num = int(input("请输入下载的序号："))
    for song in list:
        if(song['num'] == song_num):
            data1 = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2672884775,"g_tk_new_20200303":419396559,"g_tk":419396559},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["2672884775"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["2672884775"]}},"req_3":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8510399644","songmid":["'+song['songmid']+'"],"songtype":[0],"uin":"2672884775","loginflag":1,"platform":"20"}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["'+song['songmid']+'"]}},"req_5":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"100806793","biz_sub_type":0}]}},"req_6":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"'+song['albummid']+'"}},"req_7":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"5305349816","songmid":["'+song['songmid']+'"],"songtype":[0],"uin":"2672884775","loginflag":1,"platform":"20"}}}'
            data = get_sign(data1)
            url = url+data
            print(url)
            resp = requests.post(url, data=data)
            print(resp.text)

            '''
            sign解密有点问题
            '''

            # with open('song/'+song['songname']+'-'+song['singer']+'.mp3', mode='wb') as file:
            #     file.write(resp_song.content)
            #     print(song['songname']+'-'+song['singer']+" 下载完成！")
            # break

def main(url):
    # 发送请求
    resp = requests.get(url).text
    # 展示歌曲信息
    song_list = show(resp)
    # 下载歌曲
    download(song_list)

if __name__ == '__main__':
    key = input("请输入你要下载的歌曲：")
    # p为页码，n为返回的数据条数
    url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?w={key}&n=20'
    main(url)

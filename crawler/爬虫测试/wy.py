import json
import requests
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import tkinter as tk
from tkinter import simpledialog, messagebox

# 代码逻辑
'''
加密代码
function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
}();

'''
# 分析
'''
分析：
评论：params和encSecKey是两个参数，需要通过get_params和get_encSecKey方法获取
var bVj1x = window.asrsea(JSON.stringify(i6c), bse8W(["流泪", "强"]), bse8W(RR7K.md), bse8W(["爱心", "女孩", "惊恐", "大笑"]));
    params: bVj1x.encText,
    encSecKey: bVj1x.encSecKey

bse8W(["流泪", "强"]) = '010001'
JSON.stringify(i6c) = '{"rid":"R_SO_4_2638631898","threadId":"R_SO_4_2638631898","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'
bse8W(RR7K.md) = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
bse8W(["爱心", "女孩", "惊恐", "大笑"]) = '0CoJUm6Qyw8W8jud'
JSON.stringify(i6c) = '{"rid":"R_SO_4_2638631898","threadId":"R_SO_4_2638631898","pageNo":"1","pageSize":"20","cursor":"-1","offset":"0","orderType":"1","csrf_token":""}'

歌曲搜索：
csrf_token: 5d2041a48d11e68f70e0c675c7286a39

https://music.163.com/weapi/cloudsearch/get/web?csrf_token=5d2041a48d11e68f70e0c675c7286a39
var bVj3x = window.asrsea(JSON.stringify(i1x), bse1x(["流泪", "强"]), bse1x(RR1x.md), bse1x(["爱心", "女孩", "惊恐", "大笑"]));
e1x.data = j1x.cr2x({
        params: bVj3x.encText,
        encSecKey: bVj3x.encSecKey
            })

歌曲信息：
https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=da1db1553a7e3c98b6ef016e39c89d32

歌词：
https://music.163.com/weapi/song/lyric?csrf_token=da1db1553a7e3c98b6ef016e39c89d32
'''


def get_encSecKey():
    """
    :return:
    """
    # 固定i得到的encSecKey
    encSecKey = 'ab77b55c56b84e2e6a6bf1142b337d64205a51b4149806f9e7e340f09ac366cf339303ed095a0db9a6434a030fa7d87defcad67c6d8781c85a0bd74a8bb943c353bb60bd5ba33f7c4cf314bd6624e9089aabd500b98e016f259b4fca0aabf4860464b3afc0d4f5c54f9835a256d15811116ff03d8feb70ac604a19e77d6008a6'
    return encSecKey


def aes_encrypt(text, key):
    """AES CBC mode encryption"""
    # Convert to bytes
    text = text.encode('utf-8')
    key = key.encode('utf-8')
    iv = b'0102030405060708'
    # Create cipher and encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(text, AES.block_size))
    # Encode as base64
    return base64.b64encode(encrypted).decode('utf-8')


def show_message(message):
    """
    显示信息对话框。

    :param message: 要显示的消息内容，类型为字符串。
    """
    messagebox.showinfo("Message", message)


class App:
    def __init__(self, root):
        self.song_list = None
        self.singer_name = None
        self.root = root
        self.root.title("Music App")
        self.root.geometry("400x300")
        self.center_window()

        self.second = '010001'
        self.third = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.fourth = '0CoJUm6Qyw8W8jud'
        self.i = '5r7Fojvz1584CFQ0'
        self.headers = {
            'cookie': 'NMTID=00OTlmM7WjvWABVNETAsBcsWXtWtOwAAAGTP5y3uQ; _iuqxldmzr_=32; _ntes_nnid=4e58a15dbc3498ba3ade6ad5a351af88,1731939055981; _ntes_nuid=4e58a15dbc3498ba3ade6ad5a351af88; WEVNSM=1.0.0; WNMCID=qqfphp.1731939056826.01.0; WM_TID=xx%2B0BkKMJGpEUUFBFAOSDg6%2Fk%2FSmLzkp; __snaker__id=gX6pszJu4bCZinGf; WM_NI=8VCJh5Q0ntfYBN15vjHy4TzZu7PsqJ8shMZo3mbDBj4yr7UCYb8IboqDSHvRerT3%2BqDv9Efd%2Fo4M0hwD7pkSMv3%2FB3E9SlmvM%2BVuVe8LxGtum%2BhnbE7eQbkozVH4FAtFMnI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaeb5398aaa89a2b179b4b88fb7c54e938f8e86c760ab9dadb9b864878aad8ec12af0fea7c3b92afc8a8dabeb3f93f0a295e5538292ffd6f5628ca7fcb5f952b7e9a094f442fcada8aed965f1b3aea5c162f8a7bed8d8499bbef8aae165b39c9da9f55aa7ae9cd4aa7b88aaf7a6e570edb1fcaeb364b59cf991ea598faafdd0c13987e79d8df07e8ff59a96d56ffc94b8a8f77faff5a88fe14ff5bb9f83ea65ba8a88d5c54bb89a838fcc37e2a3; gdxidpyhxdE=VSVQYK%5CWspkTeyrorKhgc0ORDKqZWB6RiqCdtpSjM0W8E6rLoaJ8a7oylwa%5CY5eTdShPHx3%5CE64Ij1R430LjEYR1iYa5tupQbAO%2BD%5Cp4%2BarCYtIIeLEYSktei7LnhlhZCzrIDSmHuHJQejaljRdg%5CTDX41WttgpqgZMOJyXnXpy6zflG%3A1732183160987; MUSIC_U=0069D42FC33EAD921DFC0A1686473FBFF135EF88B0884952FAFDFED0475851B08CED83FF92359E23DFC7FA3FB3E9334A45A0D0A1DAEAB43E66AD79B508B4948BE003BE4F84545CB545E9776D1A4307930987AE4397C96B1CF578FB4C9052273B33748B7850AAB472ED91E3105EFF3E3A1C9BB47271E3013082F1C4DEE3DE3F69BC3C2BF80334BD65CE7F3ECFC309B7F888D6BFD9CC91881629A652F35C316A2D6C372F50DDBD7FCB8EF7E7B043DDA598CB0E66DEE77E0592D6F1B84288AA3696B4222D4FC5DBF44286FBC3F92ABDE239A7E23316E49B4826700A47BFC72285EECC15955D479A498783E6F1386DDA0295DE13573EA24759FECDA215641257E1C20F6AC00CF4D76740A932727224FFC33E17A4BBB918DBC928F87BBCB804C9081AD91A963A37C2A91BEE991F12A5196DF12C; __csrf=da1db1553a7e3c98b6ef016e39c89d32; JSESSIONID-WYYY=T9pH%2B0KvkyjZcuq7AJDcaZu3cXYZ1XYXMymxmoWrkAuQvsW0%5CyozWE0cNZvmVDTB26p4mOjD9NcjmaDkS3SqPAGUln%2BiYqoop5HVwEKkl5%2FwErzRmrYHl4SaSs5QighDIFxi5PD%2BZVZv1%2BGtrIJNZy7N5%2BjRbG9IKU4stT%5CcqMBNSQtR%3A1732184150177',
            'referer': 'https://music.163.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_main_menu()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_main_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="请输入歌手的姓名：").pack(pady=10)
        self.singer_entry = tk.Entry(self.main_frame)
        self.singer_entry.pack(pady=10)
        tk.Button(self.main_frame, text="确定", command=self.get_music_list).pack(pady=10)

    def get_music_list(self):
        self.singer_name = self.singer_entry.get()
        self.song_list = self.fetch_music_list(self.singer_name)
        self.create_choice_menu()

    def create_choice_menu(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="请输入歌曲id（0.结束任务！）：").pack(pady=10)
        self.song_id_entry = tk.Entry(self.main_frame)
        self.song_id_entry.pack(pady=10)
        tk.Button(self.main_frame, text="确定", command=self.handle_song_choice).pack(pady=10)

    def handle_song_choice(self):
        # 获取用户输入的歌曲ID
        song_id = int(self.song_id_entry.get())
        # 如果输入的ID为0，表示结束任务
        if song_id == 0:
            show_message("感谢您的使用！")
            self.root.quit()
        else:
            # 遍历歌曲列表，查找与输入ID匹配的歌曲
            for song in self.song_list:
                if song['id'] == song_id:
                    # 如果找到匹配的歌曲，创建操作菜单
                    self.create_action_menu(song)
                    return
            # 如果没有找到匹配的歌曲，显示错误信息并重新显示选择菜单
            show_message("您输入的歌曲id有误！")
            self.create_choice_menu()

    def create_action_menu(self, song):
        # 清空 main_frame 中的所有子控件
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # 在 main_frame 中创建一个标签，显示歌曲名称
        tk.Label(self.main_frame, text=f"歌曲名：{song['name']}").pack(pady=10)

        # 定义一个字典，包含操作选项
        options = {0: "取消任务", 1: "下载歌曲", 2: "显示热评", 3: "下载歌词"}

        # 创建一个 IntVar 实例，用于跟踪单选按钮的选择
        self.choice_var = tk.IntVar()

        # 遍历 options 字典，为每个选项创建一个单选按钮
        for key, value in options.items():
            tk.Radiobutton(self.main_frame, text=value, variable=self.choice_var, value=key).pack(anchor=tk.W)

        # 创建一个按钮，点击后调用 handle_action_choice 方法，并传递 song 参数
        tk.Button(self.main_frame, text="确定", command=lambda: self.handle_action_choice(song)).pack(pady=10)

    def handle_action_choice(self, song):
        # 获取用户选择的操作
        choice = self.choice_var.get()
        # 如果选择为0，返回到歌曲选择菜单
        if choice == 0:
            self.create_choice_menu()
        # 如果选择为1，下载歌曲
        elif choice == 1:
            self.download_music(song['id'], song['name'], self.singer_name)
            self.create_action_menu(song)
        # 如果选择为2，获取热评
        elif choice == 2:
            self.get_comments(song['id'])
            self.create_action_menu(song)
        # 如果选择为3，下载歌词
        elif choice == 3:
            self.get_lyric(song['id'], song['name'], self.singer_name)
            self.create_action_menu(song)
        # 如果输入有误，显示错误信息并重新显��操作菜单
        else:
            show_message("输入有误！")
            self.create_action_menu(song)

    def get_params(self, data):
        """
        对传入的数据进行两次AES加密，返回加密后的文本。

        :param data: 需要加密的数据，类型为字符串。
        :return: 返回加密后的文本，类型为字符串。
        """
        # 使用第四个密钥进行第一次AES加密
        encText = aes_encrypt(data, self.fourth)
        # 使用随机生成的密钥进行第二次AES加密
        encText = aes_encrypt(encText, self.i)
        return encText

    def get_data(self, data):
        """
        对传入的数据进行加密，并返回包含加密参数的字典。

        :param data: 需要加密的数据，类型为字典。
        :return: 包含加密参数的字典，类型为字典。
        """
        # 将字典数据转换为JSON字符串
        first = json.dumps(data)
        # 获取固定的encSecKey
        encSecKey = get_encSecKey()
        # 对JSON字符串进行两次AES加密，获取加密后的参数
        params = self.get_params(first)
        # 构造包含加密参数的字典
        datas = {
            'params': params,
            'encSecKey': encSecKey
        }
        # 返回包含加密参数的字典
        return datas

    def fetch_music_list(self, singer):
        """
        Fetches a list of songs for a given singer from the NetEase Cloud Music API.

        :param singer: The name of the singer to search for, type: str
        :return: A list of dictionaries, each containing the song name and song id, type: list
        """
        # URL for the NetEase Cloud Music search API
        url = 'https://music.163.com/weapi/cloudsearch/get/web'

        # Data payload for the POST request, including the singer's name and other parameters
        music_data = {
            "csrf_token": "da1db1553a7e3c98b6ef016e39c89d32",
            "hlposttag": "</span>",
            "hlpretag": "<span class=\"s-fc7\">",
            "limit": "30",
            "offset": "0",
            "s": f"{singer}",
            "total": "true",
            "type": "1"
        }

        # Encrypt the data payload
        data = self.get_data(music_data)

        # Send the POST request to the API
        resp = self.send_request(url, data)

        # Parse the JSON response to extract the list of songs
        songs = resp.json()['result']['songs']

        # Initialize an empty list to store the song details
        song_list = []

        # Iterate over the list of songs and extract the song id and name
        for song in songs:
            id = song['id']
            name = song['name']
            print(f"歌曲名：{name}，歌曲id：{id}")  # Print the song name and id
            song_list.append(dict(name=name, id=id))  # Append the song details to the list

        # Return the list of songs
        return song_list

    def send_request(self, url, data):
        """
        :param url:
        :param data:
        :return:
        """
        resp = requests.post(url, data=data, headers=self.headers)
        return resp

    def get_comments(self, song_id):
        """
        :param song_id:
        """
        url = 'https://music.163.com/weapi/comment/resource/comments/get'
        comment_data = {
            "rid": f"R_SO_4_{song_id}",
            "threadId": f"R_SO_4_{song_id}",
            "pageNo": "1",
            "pageSize": "20",
            "cursor": "-1",
            "offset": "0",
            "orderType": "1",
            "csrf_token": ""
        }
        data = self.get_data(comment_data)

        resp = requests.post(url, data=data)
        comments = resp.json()['data']['hotComments']
        num = 1  # 初始化
        comments_text = ""
        for comment in comments:
            comments_text += f"********************************* 第{num}条热评！*********************************\n"
            comments_text += f"{comment['user']['nickname']}: {comment['content']}\n\n"
            num += 1
        show_message(comments_text)
        self.create_choice_menu()

    def download_music(self, song_id, song_name, singer_name):
        """
        :param song_id:
        :param song_name:
        :param singer_name:
        """
        url = "https://music.163.com/weapi/song/enhance/player/url/v1"
        song_detail_data = {
            "csrf_token": "da1db1553a7e3c98b6ef016e39c89d32",
            "encodeType": "aac",
            "ids": f"[{song_id}]",
            "level": "standard"
        }
        data = self.get_data(song_detail_data)
        resp = self.send_request(url, data)
        download_url = resp.json()['data'][0]['url']
        with open(f'data/{singer_name}-{song_name}.mp3', mode='wb') as f:
            f.write(requests.get(download_url).content)
        show_message("歌曲下载完成！")
        self.create_choice_menu()

    def get_lyric(self, song_id, song_name, singer_name):
        """
        :param song_id:
        :param song_name:
        :param singer_name:
        """
        url = 'https://music.163.com/weapi/song/lyric'
        lyric_data = {
            "csrf_token": "da1db1553a7e3c98b6ef016e39c89d32",
            "id": song_id,
            "lv": -1,
            "tv": -1
        }
        data = self.get_data(lyric_data)
        resp = self.send_request(url, data)
        lyric = resp.json()['lrc']['lyric']
        with open(f'data/{singer_name}-{song_name}.lrc', mode='w', encoding='utf-8') as f:
            f.write(lyric)
        show_message("歌词下载完成！")
        self.create_choice_menu()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()

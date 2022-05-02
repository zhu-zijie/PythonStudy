import requests
import re


class alipanso(object):
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def get_html(self):
        response_html = requests.get(self.url, headers=self.headers, params=self.params)

        return response_html.content.decode()

    def parse_response_html(self, page):
        response_data = self.get_html()
        url_name = re.findall('<a href="(.*?)".*\W*.*>\W*?(.*)\W*</a>', response_data)
        name_download_url = []
        n = 1
        flag = 1
        for i in url_name:
            if page == 1 and flag <= 3:
                flag += 1
                continue
            download_url = 'https://www.upyunso.com/' + i[0]
            name = i[1]
            name_download_url.append(f'{n}.' + name + '  ' + download_url)
            n += 1

        return name_download_url


if __name__ == '__main__':

    word = input('请输入要搜索的资源名称：')
    choose = '1.全部文件\n''2.视频\n''3.图片\n''4.文档\n''5.音频\n''6.压缩文件\n''7.其他'

    print('请选择文件类型：')

    print(choose)

    num = input('请选择选项前的序号：')
    line = input('请选择线路1或者线路2，输入1或2：')
    format = {
        '1': 'all',
        '2': 'video',
        '3': 'image',
        '4': 'doc',
        '5': 'audio',
        '6': 'zip',
        '7': 'others'
    }

    url = 'https://www.upyunso.com/search.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    }

    for i in range(1, 10):

        params = {
            'page': f'{i}',
            'keyword': word,
            'search_folder_or_file': '0',
            'is_search_folder_content': '0',
            'is_search_path_title': '0',
            'category': format[num],
            'file_extension': 'all',
            'search_model': line
        }
        sosuo = alipanso(url, headers=headers, params=params)

        ziyuan = sosuo.parse_response_html(i)
        if ziyuan:
            print(f'第{i}页内容：')
            print(ziyuan)
        else:
            print('没有找到任何相关资源，请重新搜索')
            break
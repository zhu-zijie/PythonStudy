import execjs
import requests

def getValue(id):
    # 加载JavaScript文件
    with open('wangyiyun.js', mode='r') as file:
        js_code = file.read()

    # 编译JavaScript代码
    ctx = execjs.compile(js_code)

    # 调用JavaScript函数并传递参数
    return ctx.call('processData', id)

if __name__ == '__main__':
    url = 'https://music.163.com/weapi/comment/resource/comments/get'
    id = 2638631898
    data = getValue(id)
    data['params'] = data.pop('encText')


    headers = {
        'cookie': 'NMTID=00OTlmM7WjvWABVNETAsBcsWXtWtOwAAAGTP5y3uQ; JSESSIONID-WYYY=WE5bZZPZeC%5Ctum6ABVFYPMNv%2FpHI0%2Bb6SyBmMCvu8bA1fR2AJaEY%5CCahXO273wBz5O5HZWTZJ8%5CZNJsQMgb%2FxlyB%2FoAVOeWWsWcUCXB9u%2FcZWcEipVN3nR8%2FnCUVQExHQrDeb%5CRvdwspCkgTlK8ozMW%5CgMsME20QCJ2wVNXOjRq%5CmwcB%3A1731940855961; _iuqxldmzr_=32; _ntes_nnid=4e58a15dbc3498ba3ade6ad5a351af88,1731939055981; _ntes_nuid=4e58a15dbc3498ba3ade6ad5a351af88; WEVNSM=1.0.0; WNMCID=qqfphp.1731939056826.01.0; WM_NI=8Cs7p6jY6QfrWfs3d%2BwAH5eP0heJuDuEUOS2la%2FeFqfDGkSSjCy1THsbcw3V4g4qyTMJqHgsTr3yL%2BBnYa1R7j9ZHzGROFKiQBnoEJmjTtJNIW7J0xqwaARn9lBuX9RlMnk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccce6f89eaa5abc74092a88fa3d84a938a9b83db54f4aee198b644ae95fe88b72af0fea7c3b92afc9dbdd8f33eaa87fab2e57a95babdd4e721b59f88d6e85cf4b8ababf850b79b9bb0d23ab0bfe186c57ba69c898cd259aa9db7d2d744b1bead98b25ef8b9fc92fc608f96bfa9e67998aefd9acf2182b29782b45af5b6f7bbcb72858e81a7ca63939ea290c842afb69c95c9468b89f9abb374b3a9afa2d166fbb48e96db3392b4838fea37e2a3; WM_TID=xx%2B0BkKMJGpEUUFBFAOSDg6%2Fk%2FSmLzkp; __snaker__id=gX6pszJu4bCZinGf; gdxidpyhxdE=0scPa5q37zgWGjDAnHwH%5C0SoWsDqWHDkvjh0YoL4BnfV%2FMT9YohhjOf3L9uPi3eBPC1sTA4WT5LMARl3CaoIYJ%2FfxyYJQ8XOdZMwQ2vRq917bB%5CXm0gI03eRMB15hKbSubzMh%5Ch5Opl%5CNN5wvqj5Pga18hDDNiB6e63JzPIJhq9q7Sv7%3A1731939975489',
        'referer': 'https://music.163.com/song?id=2638631898',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    resp = requests.post(url, headers=headers, data=data)

    print(resp.text)

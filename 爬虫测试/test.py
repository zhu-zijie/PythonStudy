import requests
import re
url = "https://www.douyin.com/video/6952079436124638472"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'cookie': 'passport_csrf_token=1b9858131eae47287fec106116aa624e; passport_csrf_token_default=1b9858131eae47287fec106116aa624e; d_ticket=47b5d5dcfdbbacac4c8120dcec8d33113a511; n_mh=FAKXF62TqrHxsiZxcAxXtZhonM3Bl6wBODVhl-Gf818; passport_auth_status=1b15765097ab3e300b499bc5ee64c79d,; passport_auth_status_ss=1b15765097ab3e300b499bc5ee64c79d,; sso_auth_status=0078d8b15aa67d87ed15b03497b99fbc; sso_auth_status_ss=0078d8b15aa67d87ed15b03497b99fbc; sso_uid_tt=ce3289c9eb6d395637ed02730653927a; sso_uid_tt_ss=ce3289c9eb6d395637ed02730653927a; toutiao_sso_user=2e9d4ca784e19df0a322a6b2cafca2c8; toutiao_sso_user_ss=2e9d4ca784e19df0a322a6b2cafca2c8; sid_ucp_sso_v1=1.0.0-KDhhYWI5YTJjNWFiYWQ4NGRmZGQwZDE0MzgwYWVmNTkyNzZmYWIzOGIKHQjhoajN6wIQ1fnlkgYY7zEgDDCn3v_WBTgCQPEHGgJsZiIgMmU5ZDRjYTc4NGUxOWRmMGEzMjJhNmIyY2FmY2EyYzg; ssid_ucp_sso_v1=1.0.0-KDhhYWI5YTJjNWFiYWQ4NGRmZGQwZDE0MzgwYWVmNTkyNzZmYWIzOGIKHQjhoajN6wIQ1fnlkgYY7zEgDDCn3v_WBTgCQPEHGgJsZiIgMmU5ZDRjYTc4NGUxOWRmMGEzMjJhNmIyY2FmY2EyYzg; odin_tt=6411b2d225991aa4bac86cc4adcb4331f99df1ed1e4788ee8f65f66df241b7d536abb7e948e652c7bfdede6d7f97cd14; sid_guard=2e9d4ca784e19df0a322a6b2cafca2c8|1650031830|5184000|Tue,+14-Jun-2022+14:10:30+GMT; uid_tt=ce3289c9eb6d395637ed02730653927a; uid_tt_ss=ce3289c9eb6d395637ed02730653927a; sid_tt=2e9d4ca784e19df0a322a6b2cafca2c8; sessionid=2e9d4ca784e19df0a322a6b2cafca2c8; sessionid_ss=2e9d4ca784e19df0a322a6b2cafca2c8; sid_ucp_v1=1.0.0-KDEwNDg5YTg2NDc0ODU2ZDFkMDg0NzRhODEzYTgyZDZhMGUxNTFlYmUKHQjhoajN6wIQ1vnlkgYY7zEgDDCn3v_WBTgCQPEHGgJscSIgMmU5ZDRjYTc4NGUxOWRmMGEzMjJhNmIyY2FmY2EyYzg; ssid_ucp_v1=1.0.0-KDEwNDg5YTg2NDc0ODU2ZDFkMDg0NzRhODEzYTgyZDZhMGUxNTFlYmUKHQjhoajN6wIQ1vnlkgYY7zEgDDCn3v_WBTgCQPEHGgJscSIgMmU5ZDRjYTc4NGUxOWRmMGEzMjJhNmIyY2FmY2EyYzg; ttwid=1|3FF--EPW6rxtcrYR07nZkDnrp16qPNLQOURlFCDqOaU|1650193351|c5e9e99224b9b59165ac3b605503528f89d0d965d545bf012c6e6a6a45bb6605; __ac_nonce=0626e824d00fae7405370; __ac_signature=_02B4Z6wo00f01AP-7agAAIDAg.wX6G7A4WgD3ukAAGKXxyucIasC4g6G3vzCs-z4Pmdgns8aeQyis1zo9fApFAkwzjeOSRwtocIZ6GhvFvtOALwEMapHRs8mMVh18rDxShS8y3t.U0xJ9mse91; douyin.com; strategyABtestKey=1651409488.884; _tea_utm_cache_2285=undefined; s_v_web_id=verify_l2naku6c_z1WOJRjC_vn7d_43yM_8nvZ_6DtYWVpUi0qf; _tea_utm_cache_1300=undefined; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAW-R4E6nwK-AviEC0NTamQFnqbdGCfg7iVBdsLFHUI9E/1651420800000/0/0/1651410166302; msToken=oZ5Cg_PfZTEqYNb64tzuQ6Cl8QuOowPdpixDtyKpXtvjzTjQstV9W_5F6a5bApIZeKckmC1cGO-WRhgnros29DPLgTcO084Y6Z89dOnkJe6F9n4QG-F8VrEdXm4BMNuS8g==; tt_scid=fwAjpDNmBG2HSsmuWNyCnTWgTMwIwCMzUod4zPcwo.siRUeCh4XoIsDZXb.Pk29D4981; home_can_add_dy_2_desktop=1; pwa_guide_count=2; THEME_STAY_TIME=299792; IS_HIDE_THEME_CHANGE=1; _dd_s=logs=1&id=0b5f3081-7212-43fe-afcd-f7791453dcdd&created=1651409491825&expire=1651410788081; msToken=9cxqRlf4mpAJ_jRP7WWigy2CQDCzzADJsxMACQRBIHOo17lxWDm9UdytKOyBLT0NRFjXghw6cUulivhMZ2qdLUlRqC7bdHmk44qUTYgfN1gR3L8c2zNpfYmalznU6imY5g=='
}
resp = requests.get(url, headers = headers)
resp = requests.utils.unquote(resp.text)
print(resp)

# # 解析数据
title = re.findall('<title data-react-helmet="true">(.*?)</title>', resp, re.S)[0]
src = re.findall('"playAddr":\[{"src":"(.*?)"}', resp, re.S)[0].replace('//', 'https://')
new_title = re.sub(r'[\/?*:;|#]', "_", title)
print(new_title)
print(src)
# resp1 = requests.get(src)
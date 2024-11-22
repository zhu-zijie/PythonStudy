import requests

url = 'https://www-hj.douyin.com/aweme/v1/web/aweme/post'

data = {
    'device_platform': 'webapp',
    'aid': 6383,
    'channel': 'channel_pc_web',
    'tag_id':'',
    'share_aweme_id':'',
    'live_insert_type':'',
    'count': 10,
    'refresh_index': 2,
    'video_type_select': 1,
    'aweme_pc_rec_raw_data': '{"videoPrefer":{"fsn":[],"like":[],"halfMin":["7429571970855633444","61294237130"],"min":[]},"seo_info":"https://www.douyin.com/","is_client":false,"ff_danmaku_status":1,"danmaku_switch_status":1,"is_dash_user":1,"is_auto_play":0,"is_full_screen":0,"is_full_webscreen":0,"is_mute":1,"is_speed":1,"is_visible":1,"related_recommend":1}',
    'globalwid':'',
    'pull_type': 2,
    'min_window': 0,
    'free_right': 0,
    'view_count': 8,
    'plug_block': 0,
    'ug_source':'',
    'creative_id':'',
    'pc_client_type': 1,
    'pc_libra_divert': 'Windows',
    'version_code': 170400,
    'version_name': '17.4.0',
    'cookie_enabled': 'true',
    'screen_width': 1680,
    'screen_height': 1050,
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Chrome',
    'browser_version': '131.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '131.0.0.0',
    'os_name': 'Windows',
    'os_version': 10,
    'cpu_core_num': 16,
    'device_memory': 8,
    'platform': 'PC',
    'downlink': 10,
    'effective_type': '4g',
    'round_trip_time': 150,
    'webid': 7405909213782197775,
    'msToken': '8FzvuhWv2oo8EmVmjaRDoDV8YAWsZaFlYSZYUAlllFrF1_5XFp8H0-1s9yoa2m_wByBKuEkvQKeGVlPg40co_WZKMyk0JKuLo51oyMQU_tnX31y-fd5osJvg7eVsvPAM7BYbkuHxSEw70TsoruFiqkXELhLsI3n6GQvNtwjPl1gC0TiZkE-Maw==',
    'a_bogus': 'mXsfgzSjEqQcadFbYObXCRcltlylNB8yv1ixSHpTyOOCb1McKYP8hNcbcxzojlbw/WBiioI7adF/YdVcMtUwZKnpumpDugzjmU/9V7XLhqi2PzJsEqmgezDzow0t8Qsol/cfN1URIs0j6dQlVNChAp-7z/XN-mRmMr-4V/utT9KmUW8jk92na5Spuhv8',
    'verifyFp': 'verify_m2pxikzw_CLtBmoLO_otvm_45lE_9taR_VGsjgqEx23md',
    'fp': 'verify_m2pxikzw_CLtBmoLO_otvm_45lE_9taR_VGsjgqEx23md',
}
headers = {
    'referer': 'https://www.douyin.com/?recommend=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Cookie': 'ttwid=1%7CG7tEL5_g8GuqeqpU3gWYBQuWTQhe4j6vMBqpfN_u1DI%7C1724322633%7C4e84962658535632e9cd563e75fd7f954eb75275030b777282d80a923ed4edc1; UIFID_TEMP=973a3fd64dcc46a3490fd9b60d4a8e663b34df4ccc4bbcf97643172fb712d8b001e228ff1dd4f29aa8506b2ea69feb62a4b23c65e16b754164defc6a895193c5ade21005a6a4b7b546c1f2d38b64ba32c961d76d4e6af06557093d2edc00898f4257ae8f12d6f838302e1e6a391ce89e; fpk1=U2FsdGVkX1+81Q80ywf65lkNBugiYLdy/1OPoCoybBzNlTjxEsC/E6UhlXVVZkCDz9nesNJLZmR4a4/rXkCJTg==; fpk2=362d7fe3d8b2581bffa359f0eeda7106; bd_ticket_guard_client_web_domain=2; SEARCH_RESULT_LIST_TYPE=%22single%22; UIFID=973a3fd64dcc46a3490fd9b60d4a8e663b34df4ccc4bbcf97643172fb712d8b01cffdb5846708d13a3b812e21ae3a47825ae3e91307e0e5ee6a99a1e3a06725ef85a3575f4d628707df0a65bde4eda5b7d5fdb167882c45d539987e845898352d5684636ba419bbaee1687298e4ac3d620c8d7301591f524f348997af87b564def50aebfa02b43ee277fd40ac3dbe55c3c8e6bd8882f5a57c28f64224c6459cd; hevc_supported=true; s_v_web_id=verify_m2pxikzw_CLtBmoLO_otvm_45lE_9taR_VGsjgqEx23md; passport_csrf_token=642a66edd1854b3b8d7596e52f614408; passport_csrf_token_default=642a66edd1854b3b8d7596e52f614408; xgplayer_user_id=452913920516; passport_mfa_token=CjX%2BM0UcjdpH4vez4Atm3PyDNV3UsHGL%2FBwTpSmjE1mxjzu5jn0tFBb7bgW5bC0p53LlCwYWShpKCjxIFpyPTnYfq3Msxb4Q%2F0DBvfqgKY7YyMQI3yf7rps9dnMwLrvpmePcnkYORg8RKbaa0F6olAaBU%2FE6BrkQnePfDRj2sdFsIAIiAQNfue55; d_ticket=19a42c8b48323e9a73d43752a8161cbd57215; passport_assist_user=CjwUvoglbhPqh-EZMTHrYd9cmmMW8eGQZqkNQmYhiQ0PgWpjoUOtTQh0GxJ_37us6CbDOUakNiPQAbBxL7AaSgo8VR1ml04bovL2Gu8Rkj-pnjMraRJoHReiYqZ3v4Lgi00vxPXPtoYpsQWvDQdVOc2KUYra8OyjQZBS4Qr-ENzi3w0Yia_WVCABIgED2933sw%3D%3D; n_mh=qogyIz1IMic5UHATYbxdbx6ZI5do3HFw90ZV0HdgRwI; sso_uid_tt=4a1a9fa694013540708ec93d0fdc4c01; sso_uid_tt_ss=4a1a9fa694013540708ec93d0fdc4c01; toutiao_sso_user=8aedbbfb83d14a14c5ab21a5435714cd; toutiao_sso_user_ss=8aedbbfb83d14a14c5ab21a5435714cd; sid_ucp_sso_v1=1.0.0-KDJhNTlhZjgzMTE4NWU3ODBhYmNiZWQ1ZTNkNzY4ZmQ0NDMwN2FlYmUKHwj59Ov5sgIQrt_yuAYY7zEgDDDW-_nRBTgGQPQHSAYaAmhsIiA4YWVkYmJmYjgzZDE0YTE0YzVhYjIxYTU0MzU3MTRjZA; ssid_ucp_sso_v1=1.0.0-KDJhNTlhZjgzMTE4NWU3ODBhYmNiZWQ1ZTNkNzY4ZmQ0NDMwN2FlYmUKHwj59Ov5sgIQrt_yuAYY7zEgDDDW-_nRBTgGQPQHSAYaAmhsIiA4YWVkYmJmYjgzZDE0YTE0YzVhYjIxYTU0MzU3MTRjZA; passport_auth_status=9acb9f26c20295c6de760be9e7186a9a%2C; passport_auth_status_ss=9acb9f26c20295c6de760be9e7186a9a%2C; uid_tt=dd66c77f27c41145d22ab8d1714cc243; uid_tt_ss=dd66c77f27c41145d22ab8d1714cc243; sid_tt=7c93127f3ce62edced7fa4f96524ebfa; sessionid=7c93127f3ce62edced7fa4f96524ebfa; sessionid_ss=7c93127f3ce62edced7fa4f96524ebfa; is_staff_user=false; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=5d0852a266d1b87dc222f3223080f3c4; __security_server_data_status=1; store-region=cn-xj; store-region-src=uid; MONITOR_WEB_ID=2d7e696b-660e-4aa1-85fc-abc85265a8c0; dy_swidth=1680; dy_sheight=1050; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1680%2C%5C%22screen_height%5C%22%3A1050%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; is_dash_user=1; publish_badge_show_info=%220%2C0%2C0%2C1732191000036%22; sid_guard=7c93127f3ce62edced7fa4f96524ebfa%7C1732191000%7C5184000%7CMon%2C+20-Jan-2025+12%3A10%3A00+GMT; sid_ucp_v1=1.0.0-KDFlOWI3ZDI4MTE1M2MzYzk5ZmY1YmY0N2JkZTcxOGJhMWU5YzgzMGIKGQj59Ov5sgIQmMb8uQYY7zEgDDgGQPQHSAQaAmxmIiA3YzkzMTI3ZjNjZTYyZWRjZWQ3ZmE0Zjk2NTI0ZWJmYQ; ssid_ucp_v1=1.0.0-KDFlOWI3ZDI4MTE1M2MzYzk5ZmY1YmY0N2JkZTcxOGJhMWU5YzgzMGIKGQj59Ov5sgIQmMb8uQYY7zEgDDgGQPQHSAQaAmxmIiA3YzkzMTI3ZjNjZTYyZWRjZWQ3ZmE0Zjk2NTI0ZWJmYQ; __live_version__=%221.1.2.5449%22; live_use_vvc=%22false%22; h265ErrorNum=-1; live_can_add_dy_2_desktop=%221%22; download_guide=%223%2F20241121%2F0%22; pwa2=%220%7C0%7C3%7C0%22; __ac_nonce=067407888009489ce401d; __ac_signature=_02B4Z6wo00f01v7UwaAAAIDCyfAF.VURFMr-9MUAANkC43; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; csrf_session_id=9f1661d09cedc291c4b0e25b3cedd4f5; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAa0XlhbtznRwjYnpJ8m1OVT5vlBznd4lwbJck5YF2ILE%2F1732291200000%2F0%2F1732278412508%2F0%22; strategyABtestKey=%221732278413.153%22; biz_trace_id=553903c0; XIGUA_PARAMS_INFO=%7B%7D; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCT3pFRllIMS9BR3pwbmFIN3V4VDc5RkdMbjQ1cmU4WGNXN2ZUVzRVdDkwZFBPZW9OTXNPd0ZiWFBDSktrRVF4R3ZJQkJoZGd5MWNCVFZEMlVtV2RWMlU9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; passport_fe_beating_status=true; volume_info=%7B%22isUserMute%22%3Atrue%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; odin_tt=9d203255153edb28a3720f5492f329a4c04949a922bb18a8bd15b5a9fc14cc08c8159f01d5609ca93f7719e624525de4; xg_device_score=7.701734858542043; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; IsDouyinActive=true'
}
resp = requests.get(url, headers=headers, params=data)
print(resp.json())

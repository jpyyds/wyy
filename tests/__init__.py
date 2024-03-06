print('实名上网cwz')
print('输入wyy.Getrequest()即可下载')
def Getrequest():
    import requests
    import os

    if not os.path.exists('music'):
        os.mkdir('music')
    import re
    link = 'https://music.163.com/discover/toplist'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 '
                      'Safari/537.36 Edg/122.0.0.0'}
    response = requests.get(url=link, headers=headers)
    html_data = response.text

    info_list = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>', html_data)

    print(info_list)
    for info in info_list:
        mid = info[0]
        music_name = info[1]
        music_url = 'http://music.163.com/song/media/outer/url?id=' + mid
        print(music_name, music_url)
        music_data = requests.get(music_url).content
        with open(f'music/{music_name}.mp3', mode='wb') as f:
            f.write(music_data)

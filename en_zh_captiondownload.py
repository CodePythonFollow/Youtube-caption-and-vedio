import requests
import random
from lxml import etree


class Youtube_language():

    def __init__(self, v_id):
        self.v_id = v_id

    
    # 获取双语字幕的加密参数
    def get_key(self):
        url = "https://zhuwei.me/v1/site/gettts?url=" + self.v_id + "&lan=e&action=test&r=" + str(random.random())

        response = requests.get(url)

        html = etree.HTML(response.text)

        urls = html.xpath('//div[@class="panel-body"]/a')

        for url in urls:
            title = url.xpath('./text()') 
            if "双语字幕" in title[0] and "中文" in title[0]:
                key = url.xpath('./@onclick')
        
        if key:
            self.get_url(key)

    
    # 获取下载链接
    def get_url(self, key):
        url = "https://zhuwei.me/v1/site/tts2srt?url=" + key[0].split("'")[1]
        response = requests.get(url)
        html = etree.HTML(response.text)
        srt_title = html.xpath('//a[@id ="downloadsrt"]/@download')
        srt_link = html.xpath('//a[@id ="downloadsrt"]/@href')

        self.save(srt_title, srt_link)

    
    # 保存srt字幕
    def save(self, srt_title, srt_link):
        if '.srt' in srt_link[0]:
            response = requests.get(srt_link[0])
            with open(srt_title[0], 'wt', encoding='utf-8') as fi:
                fi.write(response.text)
            print(srt_title[0] + '保存完成')
    

    # 运行命令
    def run(self):
        self.get_key()


if __name__ == "__main__":
    language = Youtube_language(v_id='')
    language.run()


import os, re
from multiprocessing import Process, Pool   
from en_zh_captiondownload import Youtube_language
from youtube_caption_deal import Deal_caption                                

def download_page(data):
    print(data)
    os.system(r"you-get " + r'https://www.youtube.com' + data)
    print(f'download page {data} success'.format(data))
    
    
def download_all_page():
    pool = Pool(processes=5)

    for data in datas:
        # p = Process(target=download_page, args=(data, ))
        pool.apply_async(download_page, args=(data,))
    pool.close()
    pool.join()


# 爬取字幕
def get_caption(datas):
    for data in datas:
        try:
            k_id= re.findall(r'watch.v=(.*?)&list', data)[0]
            Youtube_language(k_id).run()
        except Exception as e:
            print(e)
            continue

# 处理字幕文件
def deal_caption():
    dir_name = './'
    list_dir = os.listdir(dir_name)
    
    for file in list_dir:
        if '.srt' in file: 
            deal_caption = Deal_caption() 
            deal_caption.replace_srt(dir_name + file)
            print(f'{file}下载完成')

        
if __name__ == '__main__':
    # 传入数据，可以写成链接
    datas = [
        '/watch?v=xFciV6Ew5r4&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=1',
        '/watch?v=xqcTfplzr7c&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=2',
        '/watch?v=DjEuROpsvp4&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=3',
        '/watch?v=YJC6ldI3hWk&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=4',
        '/watch?v=NDFbXIiqT4o&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=5',
        '/watch?v=U2ZN104hIcc&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=6',
        '/watch?v=N5vscPTWKOk&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=7',
        '/watch?v=06I63_p-2A4&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=8',
        '/watch?v=-nh9rCzPJ20&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=9'
    ]

    # 下载所有视频
    download_all_page()

    # 删除默认下载的srt文件
    dir_files = os.listdir('./')
    for file in dir_files:
        if '.srt' in file and '.mp4' not in file:    
            os.remove(file)

    # caption_download
    get_caption(datas)

    # deal_caption 
    deal_caption()



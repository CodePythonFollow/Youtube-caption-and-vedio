import os, re
from multiprocessing import Process, Pool   
from en_zh import Youtube_language                                 

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

        
if __name__ == '__main__':
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
    download_all_page()
    get_caption(datas)



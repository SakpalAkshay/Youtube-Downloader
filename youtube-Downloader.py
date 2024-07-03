from pytube import YouTube
print("Youtube Downloader")
yt = YouTube('https://www.youtube.com/watch?v=zWWniuV8juI&ab_channel=FOXSoccer')
print(yt.title)
print(yt.thumbnail_url)

import requests
import shutil

def download_image(url, file_name):
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image successfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')
print("Running Image download")
# Call the function
download_image(yt.thumbnail_url, 'download.jpg')
